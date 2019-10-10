# bjoern-cli

bjoern-cli is a command line wrapper to serve a Python WSGI app with [bjoern][] server.
It exists because the only way to serve an app with [bjoern][] is to import it in your code and configure the entrypoint to launch the server. This way to serve bjoern ties your application code to a webserver implementation and upgrading or changing the server becomes a change in application code.

With `bjoern-cli` you can configure your application to expose the WSGI app object and serve it from command line. It also provides a convenient wrappers to selectively use features that are compiled in bjoern and ignore those that aren't.

## Installation

If you ship your app in a docker container then the recommended way is to install `bjoern-cli` in the container context separate from the application. This makes it easier to upgrade the server or simply swap it out for something inferior.
Alternatively you can also use it as an app dependency. If that is what you want to do — and you really shouldn't be doing it like this — add `bjoern-cli` in your `setup.py` or `requirements.txt` file. If you are using the pathetically slow, pain in the ass tool then put it in `Pipenv` file.

```shell script
pip install bjoern-cli
```


## Usage

Assuming that your application `api` is exposed by module `my_app.web`, you can start the server with

```shell script
bjoern-cli --module my_app.web --app api
```

Following command line parameters are available:

```
  --host host            Host name or the IP address to bind with (default: 0.0.0.0)
  --port port            Port number to bind with (default: 8787)
  --module module        Importable python module that exposes the WSGI app (default: None)
  --app app              Name of the app as exposed by the module (default: app)
  --statsd-enable        Expose metrics to statsd (default: False)
  --statsd-host host     Address of the Statsd collector (default: 127.0.0.1)
  --statsd-port port     Port of the Statsd collector (default: 8125)
  --statsd-ns namespace  Statsd metrics namespace (default: bjoern)
  --statsd-tags tags     Comma separated list of tags to expose with metrics (default: [])
```

Features than can be selectively compiled into bjoern are appropriately indicated in the argument description. If a feature is not available its parameter description is followed by `"Ignored since bjoern is not compiled with this feature"`.


[bjoern]: https://github.com/jonashaag/bjoern
