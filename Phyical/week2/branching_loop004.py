# 시네마 키오스크 v0.2
ages = []
price = 0
kids = 0
mids = 0
adults = 0
humans = int(input('몇 분이 오셨죠? '))
for i in range(humans):
    ages.append(int(input('나이는? ')))
for age in ages:
    if 0 <= age < 8:
        price += 5000
        kids += 1
    elif 8 <= age < 19:
        price += 9000
        mids += 1
    elif age >= 19:
        price += 11000
        adults += 1
    else:
        print('정확한 나이를 입력해주세요!')

print("=" * 50)

# print('총 인원 : ' + str(humans) +'명 (어린이 : ' + str(kids) + ', 청소년 : ' + str(mids) + ', 성인 : ' + str(adults) + ')')
# print('총 금액 : ' + str(price) + '원')

# .format() -> 함수타입 자동변경 / +필요 X / {i} i번째로 locate 가능
print('총 인원 : {0}명 (어린이 : {1}, 청소년 : {2}, 성인 : {3})'.format(humans, kids, mids, adults))
# print('총 금액 : {0}원'.format(price))

print('총 금액 : %d원' % price) # C언어 스타일 출력
