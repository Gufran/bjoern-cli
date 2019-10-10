from setuptools import setup, find_packages

bjoern_repo_link = 'git+https://github.com/jonashaag/bjoern.git'
bjoern_commit_hash = 'eac53bf44cd9443897a26da93029f1fa6a898128'

with open('README.md', 'r') as desc:
    long_description = desc.read()

setup(
        name='bjoern-cli',
        author='Mohammad Gufran',
        license='MIT',
        url='https://github.com/Gufran/bjoern-cli',
        description='A convenient command line wrapper around bjoern web server',
        long_description=long_description,
        long_description_content_type="text/markdown",
        version='0.0.1',
        packages=find_packages(),
        install_requires=['bjoern @ {}@{}'.format(bjoern_repo_link, bjoern_commit_hash)],
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
