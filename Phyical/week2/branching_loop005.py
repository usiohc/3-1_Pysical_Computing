# while

# r = list(range(1, 6))
# print(r)

# for k in range(1, 6, 1):
#     print(k, end=' ')

# k = 1
# while k <= 5:
#     print(k, end=' ')
#     k += 1 # 증감식을 따로 표현하지 않으면 k = 1에서 무한 loop 발생


# FizzBuzz Test

# n = 1
# while n < 101:
#     output = n
#     if(n % 3 == 0) and (n % 5 == 0): # 3과 5의 공배수
#         print('FizzBuzz')
#     elif n % 3 == 0:
#         print('Fizz')
#     elif n % 5 == 0:
#         print('Buzz')
#     else:
#         print(n)
#     n += 1

# for n in range(1, 101):
#     output = n
#     if(n % 3 == 0) and (n % 5 == 0): # 3과 5의 공배수
#         print('FizzBuzz')
#     elif n % 3 == 0:
#         print('Fizz')
#     elif n % 5 == 0:
#         print('Buzz')
#     else:
#         print(n)

# while True:
#     answer = input('런던, 파리, 서울 중 영국의 수도는?')
#     if answer == '런던':
#         print('정답입니다.')
#         break
#     elif answer == '파리':
#         print('파리는 프랑스의 수도 입니다.')
#     elif answer == '서울':
#         print('서울은 대한민국의 수도 입니다.')
#     else:
#         print('보기에서 골라주세요.')

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue # 반복문으로 다시 복귀
    print(count) # 3 출력 X