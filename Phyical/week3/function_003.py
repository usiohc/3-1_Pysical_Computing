# 함수 (Function cont.)

# fibonacci
# 재귀함수는 성능 상의 문제 발생 (오버헤드)
# 해결 방법 중 하나가 메모화

# def fibo_recursion(n):
#     """
#     피보나치 수열
#     f(n) = f(n-1) + f(n-2)
#     f(1) = 1
#     f(2) = 1
#     f(n) = f(n-1) + f(n-2)
#     f(3) = f(2) + f(1)
#          = 1 + 1 = 2
#     f(4) = f(3) + f(2)
#          = 3
#     """
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibo_recursion(n-1) + fibo_recursion(n-2)
#
# for k in range(1, 11):
#     print('피보나치 {0} : {1}'.format(k, fibo_recursion(k)))

# 함수의 매개변수로 함수 전달하기
# def print_hi(hi):
#     for k in range(5):
#         hi()
#
# def hi():
#     print('hello~')
# # hi()
# print_hi(hi)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# map(함수, 순환가능한 자료구조)
# 리스트, 딕셔너리, 문자열, 범위 range
def square(n):
    return n*n
# for k in range(1, 6):
#     print(square(k))

# print(map(square, [1, 2, 3, 4, 5])) # 맵 주소가 출력, 제네레이터
# print(list(map(square, [1, 2, 3, 4, 5]))) # result->[1, 4, 9, 16, 25]
# 위 아래 코드는 같음 map()
# result = []
# for k in range(1, 6):
#     result.append(square(k))
# print(result) # result->[1, 4, 9, 16, 25]

# filter(함수, 순환가능한 자료구조) / map()와 비슷
def odd(n):
    return n % 2 == 1
print(list(filter(odd, [1, 2, 3, 4, 5]))) # result->[1, 3, 5] / [T, F, T, F, T] 결과값이 True인 것만 리스트에 추가

# 람다함수, 제네레이터