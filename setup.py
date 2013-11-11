import io
import os
import sys
import whwn
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))

with open('README.md') as readme:
    long_description = readme.read()

with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n') if (line and not 
                                                     line.startswith('--'))
    ]

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
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    description='Inventory Management System',
    long_description=long_description,
    install_requires=install_requires,
    packages=['whwn'],
    include_package_data=True,
    test_suite='whwn.test.test_whwn',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
    extras_require={
        'testing': ['pytest'],
    }
)
