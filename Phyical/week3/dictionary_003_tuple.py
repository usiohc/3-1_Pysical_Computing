# 안주 추천 프로그램 v0.3

# import  random
# alcohol_foods = {'맥주':'치킨',
#                  '와인':'치즈',
#                  '고량주':'짬뽕',
#                  '소주':'골뱅이소면'}
#
# while True:
#     alchol = input('주문하실 술(맥주/와인/소주/고량주/아무거나/결제)은? ')
#     if alchol == '결제':
#         break
#     if alchol in alcohol_foods.keys():
#         print('{0}에 어울리는 안주는 {1}입니다.'.format(alchol, alcohol_foods[alchol]))
#     elif alchol == '아무거나':
#         print(random.choice(list(alcohol_foods)))
#     else:
#         print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alchol))

# alcohol_foods = {'맥주':'치킨',
#                  '와인':'치즈',
#                  '고량주':'짬뽕',
#                  '소주':'골뱅이소면'}
#
# # copy()
# # copy_alcohol = alcohol_foods # 같은 주소를 참조하는 복사
# copy_alcohol = alcohol_foods.copy()
# copy_alcohol['소주'] = '두부김치'
# print(alcohol_foods)
# print(copy_alcohol)


# tuple / 읽기 전용 list
# immutable 불변, 상수의 리스트라고 할 수 있다.
# 튜플의 원소를 정의한 후에는 추가, 삭제, 수정 불가

# empty = ()
# numbers = (1, -9, 7)
# print(type(empty)) # result-><class 'tuple'>
# print(numbers[1])
# # numbers[0] = 5 # result->TypeError: 'tuple' object does not support item assignment

# subjects = ('python', 'c++', 'english') # packing
# # for subject in subjects:
# #     print(subject)
# kim, han, tom = subjects # unpacking, 인수의 개수가 같아야함
# print(kim, han, tom)

a = input()
b = input()
# t = b
# b = a
# a = t
a, b = (b, a) # packing과 unpacking을 동시에 수행
print(a, b)