import importlib
import bjoern
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


if not hasattr(bjoern._bjoern, 'features'):
    has_statsd = False
    has_statsd_tags = False
else:
    has_statsd = bjoern._bjoern.features.get('has_statsd')
    has_statsd_tags = bjoern._bjoern.features.get('has_statsd_tags')


def feature_help_msg(msg, flag):
    if flag:
        return msg
    return '{}. {}'.format(msg, 'Ignored since bjoern is not compiled with this feature')


def arg_help_formatter(prog):
    return ArgumentDefaultsHelpFormatter(prog=prog, indent_increment=2, max_help_position=70, width=140)


def main():
    parser = ArgumentParser(prog='bjoern-cli', formatter_class=arg_help_formatter)
    parser.add_argument('--host', default='0.0.0.0', help='Host name or the IP address to bind with', metavar='host')
    parser.add_argument('--port', default=8787, type=int, help='Port number to bind with', metavar='port')
    parser.add_argument('--module', required=True, help='Importable python module that exposes the WSGI app', metavar='module')
    parser.add_argument('--app', default='app', help='Name of the app as exposed by the module', metavar='app')

    parser.add_argument('--statsd-enable', action='store_true', help=feature_help_msg('Expose metrics to statsd', has_statsd))
    parser.add_argument('--statsd-host', default='127.0.0.1', help=feature_help_msg('Address of the Statsd collector', has_statsd), metavar='host')
    parser.add_argument('--statsd-port', default=8125, type=int, help=feature_help_msg('Port of the Statsd collector', has_statsd), metavar='port')
    parser.add_argument('--statsd-ns', default='bjoern', help=feature_help_msg('Statsd metrics namespace', has_statsd), metavar='namespace')
    parser.add_argument('--statsd-tags', default=[], help=feature_help_msg('Comma separated list of tags to expose with metrics', has_statsd_tags), metavar='tags')

    args = parser.parse_args()

    try:
        mod = importlib.import_module(args.module)
    except ImportError:
        raise ImportError('Failed to find module {}'.format(args.module))

    try:
        app = getattr(mod, args.app)
    except AttributeError:
        raise ImportError('Failed to find app {app} in module {mod}. Is {mod}.{app} importable?'.format(app=args.app, mod=args.module))

    if not callable(app):
        raise TypeError('{mod}.{app} must be callable'.format(app=args.app, mod=args.module))

    statsd_args = dict()
    if args.statsd_enable:
        if has_statsd:
            statsd_args = {
                'enable': True,
                'host': args.statsd_host,
                'port': args.statsd_port,
                'ns': args.statsd_ns
            }

        if args.statsd_tags and has_statsd_tags:
            statsd_args['tags'] = args.statsd_tags

    server_args = dict()
    if statsd_args:
        server_args['statsd'] = statsd_args

    bjoern.listen(app, args.host, args.port)
    bjoern.run(**server_args)
