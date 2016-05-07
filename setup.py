"""setuptools based setup file for playingcards module
"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name='playingcards',
    version='1.0.0',
    description='Implements Card and Stack classes for manipulating playing cards in card games',
    url='https://github.com/ccdale/playingcards',
    author='Christopher Allison',
    author_email='chris.allison@hotmail.com',
    license='MIT',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Game Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      ],
    keywords='playingcards games development',
    packages=find_packages(exclude=['docs', 'tests']),
    extras_require={
      'test': ['py.test'],
      },
    # data_files= [('', ['img'])],
    package_data={
      'playingcards': ['img'],
      }
    )
