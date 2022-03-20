# dictionary (cont.)

# fruits = {'apple':'사과',
#           'watermelon':'수박',
#           'strawberry':'딸기',
#           'kiwi':'키위',
#           'banana':'바나나'}
#
# for k in fruits: # 키값만 출력
#     print(k)

# for k, v in fruits.items():
#     print(k, '\t', v)

# keys()
# print(fruits.keys()) # result->dict_keys(['apple', 'watermelon', 'strawberry', 'kiwi', 'banana'])
# values()
# print(fruits.values()) # result->dict_values(['사과', '수박', '딸기', '키위', '바나나'])
# items()
# print(fruits.items()) # result->dict_items([('apple', '사과'), ('watermelon', '수박'), ('strawberry', '딸기'), ('kiwi', '키위'), ('banana', '바나나')])


# # 음식 추천 프로그램 v0.1
# alcohol_foods = {'맥주':'치킨',
#                  '와인':'치즈',
#                  '고량주':'짬뽕',
#                  '소주':'골뱅이소면'}
#
# alchol = input('주문하실 술(맥주/와인/소주/고량주)은? ')
#
# if alchol in alcohol_foods.keys():
#     print('{0}에 어울리는 안주는 {1}입니다.'.format(alchol, alcohol_foods[alchol]))

#
# # 음식 추천 프로그램 v0.2
# alcohol_foods = {'맥주':'치킨',
#                  '와인':'치즈',
#                  '고량주':'짬뽕',
#                  '소주':'골뱅이소면'}
#
# while True:
#     alchol = input('주문하실 술(맥주/와인/소주/고량주/결제)은? ')
#     if alchol == '결제':
#         break
#     if alchol in alcohol_foods.keys():
#         print('{0}에 어울리는 안주는 {1}입니다.'.format(alchol, alcohol_foods[alchol]))
#     else:
#         print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alchol))


# 음식 추천 프로그램 v0.3
# import random
# star = ['테란', '저그', '프로토스']
# print(random.choice(star))

import  random
alcohol_foods = {'맥주':'치킨',
                 '와인':'치즈',
                 '고량주':'짬뽕',
                 '소주':'골뱅이소면'}

while True:
    alchol = input('주문하실 술(맥주/와인/소주/고량주/아무거나/결제)은? ')
    if alchol == '결제':
        break
    if alchol in alcohol_foods.keys():
        print('{0}에 어울리는 안주는 {1}입니다.'.format(alchol, alcohol_foods[alchol]))
    elif alchol == '아무거나':
        print(random.choice(alcohol_foods)) # 오류발생, choice()함수는 List에서 사용가능함 dict에서 불가능
    else:
        print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alchol))
