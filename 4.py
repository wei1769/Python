#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests

head ='https://resource.hle.com.tw/Books/BooksResource/'
end  = ').pdf'
name ='01_選修數學甲(下)無敵講義_編輯大意、目次(108f'
number = 800000
url = head + name + str(number) + end
res = requests.get(url)
response = res.status_code
#res = requests.get('https://resource.hle.com.tw/Books/BooksResource/03_基礎化學(三)課本_第1章 氣體(108f814086).pdf')
#res1 = requests.get('https://resource.hle.com.tw/Books/BooksResource/03_基礎化學(三)課本_第1章 氣體(108f814086).pdf')
while response != 200 :
    print(response)
    print(url)
    number = number + 1
    url = head + name + str(number) + end
    res = requests.get(url)
    response = res.status_code
    if number > 1000000:
        break
print (url)
