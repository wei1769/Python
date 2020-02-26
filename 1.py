#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests


res = requests.get('https://resource.hle.com.tw/Books/BooksResource/03_基礎化學(三)課本_第1章 氣體(108f814086).pdf')

print (res)
