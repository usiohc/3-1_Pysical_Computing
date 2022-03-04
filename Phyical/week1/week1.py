# 1주차 자료형 (Data Types)
# 문자열 (String)
# print("Hello " + "파이썬")
# print("Hello " - "파이썬") # TypeError: unsupported operand type(s) for -: 'str' and 'str' / -는 지원하지 않음
# print("Hello " * "파이썬") # TypeError: unsupported operand type(s) for *: 'str' and 'str' / *는 지원하지 않음
# print("Hello " * 5) # 곱셈은 지원

# 숫자형 (정수, 실수)
# 정수
# print(1+'2') #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(2**8) #2의 8승 (제곱연산)
# print(pow(2, 8)) #pow = 제곱함수
# 실수
# print(1.2+1.4) # 실수는 부동 소수점 방식을 쓰기 때문 미세한 오차 발생
# print(5.1-2.9)
# print(1.5*2.0)
# print(10.0/2.5)

#변수
# name = '파이썬'
# name = 123

# 변수는 문자, 숫자, 언더스코를 사용할 수 있다. _ 제외한 특수기호 사용 불가
# 단 숫자로 시작되는 변수명은 사용 불가.
# 변수는 대소문자를 구분함
# 예약어 if, for 등등 변수명으로 사용 불가
# 7_name = True # Bool type SyntaxError: invalid decimal literal
# _Name = True
# name = False
# print(_Name)
# print(name)
# for = True # SyntaxError: invalid syntax

# 자료형 (cont.)
# 문자열 함수

# words = 'Life is too short, You need Python'

# temp = words.title() # 각 단어의 첫 글자를 대문자로
# result -> Life Is Too Short, You Need Python

# temp = words.lower() # 모두 소문자로
# result -> life is too short, you need python

# temp = words.upper() # 모두 대문자로
# result -> LIFE IS TOO SHORT, YOU NEED PYTHON
# print(temp)

# # strip()
# # 연속되는 ()만 지울 수 있음.
# # lstrip rstrip 을 지원하지만 중앙의 strip은 불가능
# trim1 = 'python'
# trim2 = '$$$python$ $'
# trim3 = '$$ $python$ $'
# # print(trim1)
# # print(trim2) # result ->$$$python$ $
# # print(trim2.strip('$')) # result ->python$ <-(space)
# # print(trim3.strip('$')) # result -> $python$ <-(space)
#
# # 줄바꿈, py는 println이 print와 같음 줄바꿈 제거는 다음과 같음
# print(trim1, end='') # , end=''
# print(trim1, end='')

# str()
# print (1 + "hi")
# TypeError 발생 int + str
# print(str(1) + "hi") # result ->1hi

# int()
# a = '1'
# b = 2
# # print(a + b) # TypeError
# print(int(a) + b) # result ->3

# input() -> scanf()와 같음
# name = input('이름을 입력하세요 : ') #result ->이름을 입력하세요 : 에서 대기상태
# # print('안녕 ' + name)
# print('안녕', name) # 쉼표는 띄어쓰기 한칸이 추가됨

# 섭씨 화씨 변환
# celsius = input('섭씨 온도 : ') # TypeError 'str' and 'int'
#input() -> 키보드로 입력 받기 때문에 str 타입으로 문자열 변수로 선언된것
celsius = input('섭씨 온도 : ') # 40입력 result -> 섭씨 온도 : 40(\n) 104.0
fahrenheit = (int(celsius) * 9/5) + 32
print(fahrenheit)