# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-30 14:01:47
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-06 23:14:56


from distutils.core import setup
from setuptools import find_packages

setup(
    name='digAgeExtractor',
    version='0.3.0',
    description='digAgeExtractor',
    author='Lingzhe Teng',
    author_email='zwein27@gmail.com',
    url='https://github.com/usc-isi-i2/dig-age-extractor',
    download_url='https://github.com/usc-isi-i2/dig-age-extractor',
    packages=find_packages(),
    keywords=['age', 'extractor'],
    install_requires=['digExtractor',
                      'digCrfTokenizer', 'digDictionaryExtractor']
)
