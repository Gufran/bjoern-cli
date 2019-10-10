from setuptools import setup, find_packages

with open('README.md', 'r') as desc:
    long_description = desc.read()

setup(
        name='bjoern-cli',
        author='Mohammad Gufran',
        license='MIT',
        url='https://github.com/Gufran/bjoern-cli',
        description='A convenient command line wrapper around bjoern web server',
        long_description=long_description,
        version='0.0.1',
        packages=find_packages(),
        install_requires=['bjoern'],
        entry_points={
            'console_scripts': [
                'bjoern-cli=bjoerncli.main:main'
            ]
        },
        classifiers=['Development Status :: 4 - Beta',
                     'License :: OSI Approved :: MIT License',
                     'Environment :: Console',
                     'Environment :: Web Environment',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 3',
                     'Topic :: Internet :: WWW/HTTP :: WSGI :: Server'],
)
