#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='iPeenCrawler',
      version='1.0',
      description='test fork from enginebai',
      author='enginebai',
      author_email='liho.chen@pentium.network',
      packages=['iPeenCrawler'],
      install_requires=[    # 依赖列表
        'requests',
        'beautifulsoup4']
     )
