# -*- coding: utf-8 -*-
# @Time    : 2018/6/30
# @Author  : Clark Du
# @简介    : 
# @File    : setup.py

from distutils.core import setup, Extension

module1 = Extension('demo',
                    sources=['demo.c'])

setup(name='Demo hello',
      version='1.0',
      description='This is a demo package by Sink',
      ext_modules=[module1])
