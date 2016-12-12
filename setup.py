#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-fastcgi-server',
    version='0.1',
    description="Package for deploying django projects via FastCGI for django version 1.9 or higher.",
    author='NetAngels team',
    author_email='info@netangels.ru',
    packages=find_packages(),
    keywords="django fastcgi",
    url="https://github.com/NetAngels/django-fastcgi",
    download_url='https://github.com/NetAngels/django-fastcgi/tarball/0.1',  # I'll explain this in a second
)
