#!/usr/bin/env python
from setuptools import setup, find_packages
from fake import __version__

setup(
    name="fake",
    version=__version__,
    description="Make Python's Fabric act like Ruby's Capistrano",
    author="Brian Muller",
    author_email="bamuller@gmail.com",
    license="MIT",
    url="http://github.com/bmuller/fake",
    packages=find_packages(),
    requires=["Fabric3"],
    install_requires=['Fabric3>=1.12']
)
