# module

# built in module 내장(표준)모듈
# import math
# import random
from math import *
import random as rd

print(ceil(3.1)) # 올림
print(floor(4.9)) # 내림
print(sqrt(16)) # 제곱근 floot 타입으로 리턴
print(rd.randint(1, 6))


# 사용자 정의 모듈
# 1)
# import my_math

# print(my_math.power(2, 10))
# print(my_math.factorial_loop(5))
# print(my_math.square(5))

# 2)
# from  my_math import fibo_recursion, power
# # from 모듈이름 import 가져오고 싶은 함수 또는 변수
# # 모듈 이름을 생략하고 함수를 사용한다.
# print(fibo_recursion(7))
# print(power(2, 10))
# # print(my_math.square(5)) # 오류발생

# 3)
# import my_math as mm
# print(mm.fibo_recursion(6))
# print(mm.power(2, 10))
# # print(my_math.power(2, 10)) # 오류발생


