# 조건문 cont.

# age = int(input('나이는? '))
# price = 0
# if 0 <= age < 8:
#     price = 5000
# elif 8 <= age < 19:
#     price = 9000
# elif age >= 19:
#     price = 11000
# else:
#     print('정확한 나이를 입력해주세요!')
#
# print('요금은 ' +  str(price) + '원 입니다.')


# options = ['콜라', '치즈토핑', '버섯', '치즈크러스터']
# if '버섯' in options:
#     print('버섯 추가합니다.')
# if '페퍼로니' in options:
#     print('페퍼로니를 추가합니다.')
# if '치즈토핑' in options:
#     print('치즈토핑을 추가합니다.')
#
# print('\n피자 주문이 완료 됐습니다.')


# 빈복문
for i in range(5): # range = i값이 0부터 5전까지(4) 반복, i = 0, i = 1 ... i = 4
    print(i, end=' ') # result->0 1 2 3 4
print()
for i in range(2, 5): # 0은 시작 값, 5는 (끝값) + 1 , 끝값 = 4
    print(i, end=' ') # result->2 3 4
print()
for k in range(1, 6, 2): # 1은 시작 값, 6는 (끝값) + 1 , 2는 증감 연산
    print(k, end=' ') # result->1 3 5
print()
print(k) # result ->5 증감 연산을 하지 않고 반복문 탈출
