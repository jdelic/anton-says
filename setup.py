from setuptools import setup, find_packages
from distutils.command.install import INSTALL_SCHEMES
from pip.req import parse_requirements

import time
_version = "1.0.dev%s" % int(time.time())
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

setup(
    name='jdelic.irc.anton.says',
    data_files=[('', ['README.md']), ],
    version=_version,
    packages=_packages,
    install_requires=[
        'irc.anton',
    ],
    entry_points={
        'anton.external.modules': ['anton_says = anton_says',]
    },
)
