#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
head ='https://resource.hle.com.tw/Books/BooksResource/'
end  = ').pdf'
name ='02_選修物理(上)互動式教學講義_CH1(108f'
number = 100000
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
print (url)
