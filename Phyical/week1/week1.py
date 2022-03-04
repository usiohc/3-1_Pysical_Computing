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
