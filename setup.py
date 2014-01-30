# -*- coding: utf-8 -*-
"""Setup file for django-unfriendly."""

from setuptools import setup, find_packages
import unfriendly
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.rst')

setup(
    name = "django-unfriendly",
    version = unfriendly.__version__,
    description = 'The unfriendliest urls in town! Django app that obfuscates urls and allows your application to natively execute the original view.',
    long_description = README,
    url = 'http://github.com/tomatohater/django-unfriendly',
    author = 'Drew Engelson',
    author_email = 'drew@engelson.net',
    license='LGPLv3',
    zip_safe = False,
    packages = find_packages(),
    include_package_data = True,
    package_data = {},
    install_requires = [
        'pycrypto>=2.0.1',
    ],
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
