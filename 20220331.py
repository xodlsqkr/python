#1
from random import randrange


price_list = [32100,32150,32000,32500]
for i in range(4):
    print(i, price_list[i])

#2
price_list = [32100,32150,32000,32500]
for i in range(3):
    print(i*10+100, price_list[i+1])

#3
for i in range(2002,2051):
    if i%4==2:
        print(i)

#4
for i in range(0,10):
    a = 0.0
    print(a+0.1*i)

#5
ticker = "btc_krw"
print(ticker.upper())

#6
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

#7
a = "hello world"
print("첫번째 :", a.rstrip("world"))
print("두번째 :", a.lstrip("hello "))

#8
date = "2020-05-01"
print("년 : ", date[0:4])
print("월 : ", date[5:7])
print("일 : ", date[8:10])

#9
상장주식수 = "5,969,782,550"
print(상장주식수.replace(",",""))

#10
a = "hello world"
print("첫번째 :", a.rstrip("world"))
print("두번째 :", a.lstrip("hello "))
