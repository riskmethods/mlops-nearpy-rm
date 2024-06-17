#!/usr/bin/env python
import sys
from setuptools import setup, find_packages

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
setup_requires = ['pytest-runner>=2.0,<3.0'] if needs_pytest else []

setup(
    name='NearPy',
    version='1.0.13',
    author='Ole Krause-Sparmann, Roman Sergienko',
    author_email='ole@pixelogik.de',
    packages=find_packages(exclude=["tests.*"]),
    url='https://github.com/riskmethods/mlops-nearpy-rm',
    license='LICENSE.txt',
    description='Framework for fast approximated nearest neighbour search.',
    keywords='nearpy approximate nearest neighbour',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy==2.0.0",
        "scipy==1.13.0",
        "bitarray==2.9.2",
        "future==1.0.0",
    ],
    setup_requires=setup_requires,
    tests_require=[
        "pytest==8.1.1",
        "redis==4.6.0",
        "mockredispy==2.9.3",
        "mongomock==4.1.2",
    ]
)
