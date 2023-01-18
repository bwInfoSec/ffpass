#!/usr/bin/env python3

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ffpass-next",
    version="0.1.1",
    author="Stefan Machmeier",
    license="MIT",
    author_email="stefan-machmeier@outlook.com",
    description="Import and Export passwords for Firefox",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/bwInfoSec/ffpass",
    packages=["ffpass"],
    install_requires=["pyasn1", "pycryptodome"],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["ffpass = ffpass:main"]},
    classifiers=["Topic :: Utilities", "Topic :: Security :: Cryptography"],
)
