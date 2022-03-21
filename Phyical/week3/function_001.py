# 함수(Function)
# 한 가지 작업을 수행하도록 디자인된 코드블럭 or 코드의 집합

# def test(name):
#     # print("{0} hi".format(name))
#     print("hi " + name)
#     # return # result -> None
#     return '이름을 출력함'
#
# test('파이썬') # Function call
# print(test('C++')) # return # result->None

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# def minus(a, b):
#     # document string
#     """ 두 수의 차를 구하는 함수 """
#     return a - b
#
#
# print(minus(5, 3))
# # help(minus) # """ 설명 주석 출력 document string
# # print(minus.__doc__)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 가변 매개변수
# def print_even(times, *values): # 가변 매개변수는 항상 맨 뒤, 1개만 사용할 수 있음
#     for value in values:
#         print(times * value)
#
# print_even(2, -9, 11, 7) # result-> -18 22 14
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 기본 매개변수
def print_default(value, times=3): # 기본 매개변수는 항상 맨 뒤, times = 3 으로 default 값 선언
    print(times * value)

print_default(5, 2) # default = 3이지만 2로 다시 선언 result-> 10
