from __future__ import print_function
from setuptools import setup, find_packages
import io
import os
import sys
import whwn

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='We Have We Need',
    version=whwn.__version__,
    url='http://github.com/wehaveweneed/wehaveweneed',
    tests_require=['pytest']
    install_requires=['Django==1.5.2'],
    cmdclass={'test': PyTest},
    description='Inventory Management System',
    long_description=long_description,
    pacakages=['whwn'],
    include_package_data=True,
    platforms='any',
    test_suite='whwn.test.test_whwn',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 2 - Pre-Alpha',
        'Natural English :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Healthcare Industry',
        'Operating System :: OS Independent',
        'Topic :: Communications :: Chat',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    extras_require={
        'testing': ['pytest'],
    }
)
