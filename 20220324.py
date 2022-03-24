#1
letters = 'python'
print(letters[0])
print(letters[2])

#2
string = 'PYTHON'
reversed_str = ''
for i in string:
    reversed_str = i + reversed_str

print(f'Original String: {string}')
print(f'Reversed String: {reversed_str}')

#3
a = "http://sharebook.kr"
last = a.rfind('kr')
print(last)



#4
file_name = "2020_보고서.xlsx"
if file_name.endswith("xlsx"):
     print("It ends with xlsx")
else:
     print("It doesn't end with xlsx")

#5
file_name = "2020_보고서.xlsx"
if file_name.startswith("2020"):
     print("It starts with 2020")
else:
    print("It doesn't start with 2020")

#6
score =int(input("점수를 입력하세요 : "))
if (score>=81) & (score<=100):
   print("A")
elif score>=61:
    print("B")
elif score>=41:
    print("C")
elif score>=21:
    print("D")
else:
    print("E")

#7
cook = ["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소시지","라면","팥빙수","김치전"]
print(len(cook))

#8
warn_investment_list = ["Microsoft","Google","Naver","Kakao","SAMSUNG","LG"]
list = input("종목을 입력하세요 : ")
if list in warn_investment_list:
    print("투자 경고 종목입니다")
else:a
    print("투자 경고 종목이 아닙니다")

#9
list = [100,200,300]
for i in list:
    print(f'{int(i)+10}')

#10
list = ["sk하이닉스","삼성전자","LG전자"]
for i in list:
    print(len(i))
