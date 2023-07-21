#!/usr/bin/env python
import sys
from setuptools import setup, find_packages

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
setup_requires = ['pytest-runner>=2.0,<3.0'] if needs_pytest else []

setup(
    name='NearPy',
    version='1.0.7',
    author='Ole Krause-Sparmann, Roman Sergienko',
    author_email='ole@pixelogik.de',
    packages=find_packages(exclude=["tests.*"]),
    url='https://github.com/riskmethods/mlops-nearpy-rm',
    license='LICENSE.txt',
    description='Framework for fast approximated nearest neighbour search.',
    keywords='nearpy approximate nearest neighbour',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy==1.25.1",
        "scipy==1.11.1",
        "bitarray==2.7.5",
        "future==0.18.3",
    ],
    setup_requires=setup_requires,
    tests_require=[
        "pytest==7.3.2",
        "redis==4.6.0",
        "mockredispy==2.9.3",
        "mongomock==4.1.2",
    ]
)
