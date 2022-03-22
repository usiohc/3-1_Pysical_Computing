# 함수 (Function cont.)

# 5! = 5 * 4 * 3 * 2 * 1
#    = 120

# 팩토리얼 함수 예제
# def factorial_loop(n):
#     """
#     팩토리얼 by 반복문
#     """
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result
# print(factorial_loop(5))

# 재귀함수
# def factorial_recursion(n):
#     """
#     팩토리얼 by 재귀
#     f(n) = n * n-1 * n-2 * n-3 * ... * 1
#     f(5) = 5 * 4!
#          = 5 * f(n-1)
#     ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#     실제 동작
#     f(3) = 3 * f(2)
#          = 3 * 2 * f(1)
#          = 3 * 2 * 1 * f(0)
#          = 3 * 2 * 1 * 1
#     """
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_recursion(n-1)
# print(factorial_recursion(5))


def fibo_recursion(n):
    """
    피보나치 수열
    f(1) = 1
    f(2) = 1
    f(n) = f(n-1) + f(n-2)
    f(3) = f(2) + f(1)
         = 1 + 1
    f(4) = f(3) + f(2)
    """
