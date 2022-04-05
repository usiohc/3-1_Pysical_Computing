# list comprehension (line 줄이기)


# numbers = []
# for k in range(0, 10, 2):
#     numbers.append(k * k)
# print(numbers)

# 리스트이름 = [ 표현식 for 반복할 변수명 in 순환(range함수 또는 list등)]
# numbers = [k * k for k in range(0, 10, 2)]
# print(numbers)
#
# # 시네마 키오스크 v0.3
# # 리스트 컴프리헨션 적용
# # ages = []
# price = 0
# kids = 0
# mids = 0
# adults = 0
# humans = int(input('몇 분이 오셨죠? '))
#
# ages = [int(input('나이는? ')) for i in range(humans)]
# # for i in range(humans):
# #     ages.append(int(input('나이는? ')))
# for age in ages:
#     if 0 <= age < 8:
#         price += 5000
#         kids += 1
#     elif 8 <= age < 19:
#         price += 9000
#         mids += 1
#     elif age >= 19:
#         price += 11000
#         adults += 1
#     else:
#         print('정확한 나이를 입력해주세요!')
#
# print("=" * 50)
# print('총 인원 : {0}명 (어린이 : {1}, 청소년 : {2}, 성인 : {3})'.format(humans, kids, mids, adults))
# print('총 금액 : {0}원'.format(price))

# n = [x for x in range(1, 11) if x % 3 == 0]
# print(n) # result->[3, 6, 9]

# n = []
# for x in range(1, 11):
#     if x % 3 == 0:
#         n.append(x)
# print(n) # result->[3, 6, 9]

# artists = ['악뮤', '빅뱅', '볼사', '릴러말즈']
# copy_artists = [artist for artist in artists if artist != '빅뱅']
# print(artists)
# print(copy_artists) # result->['악뮤', '볼사', '릴러말즈']

import random
# # 주사위
# dice = random.randint(1, 6)
# print(dice)

lotto = []
while(len(lotto) < 6):
    lotto.append(random.randint(1, 45))
    # 리스트 중복 원소 제거 -> set()했다가 list()하면 끝
    lotto = list(set(lotto)) # set함수는 중복을 허용하지 않음


print(sorted(lotto)) # result->[20, 22, 27, 37, 38, 42]
for l in sorted(lotto):
    print(l, end=' ')

