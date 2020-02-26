#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
head ='https://resource.hle.com.tw/Books/BooksResource/'
end  = ').pdf'
name ='03_基礎化學(三)課本_第1章 氣體(108f81'
number = 4080

urll = head + name + str(number) + end
res = requests.get(urll)
#res = requests.get('https://resource.hle.com.tw/Books/BooksResource/03_基礎化學(三)課本_第1章 氣體(108f814086).pdf')
#res1 = requests.get('https://resource.hle.com.tw/Books/BooksResource/03_基礎化學(三)課本_第1章 氣體(108f814086).pdf')

pp = "aa"
pp = res.status_code
if pp == 200 :
    print ("aa")
else :
    print (pp)
