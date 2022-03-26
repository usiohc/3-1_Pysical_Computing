# exception handling (cont.)

# def midterm():
#     score = int(input('1에서 10사이의 정수 입력 : '))
#     if score < 0 or score > 10:
#         raise Exception("중간고사 점수 입력 범위를 벗어났습니다. {0}".format(score))
#     else:
#         print('{0}점 입니다.'.format(score))
#
# try:
#     midterm()
# except Exception as e:
#     print('예외 발생 : {0}'.format(e))


# try:
#     print(5/2)
#     b = int(input())
#     a = [1, 2, 3]
#     print(a[1])
#     raise Exception('내가 만든 예외')
# except ZeroDivisionError as err: # 오류 이유를 err 변수로
#     print('분모에 0이 올 수 없습니다. : {0}'.format(err))
# except IndexError as err:
#     print('인덱스 범위를 벗어났습니다. : {0}'.format(err))
# except Exception as err: # 맨 마지막에 작성
#     print('무언가 에러가 발생했습니다. : {0}'.format(err))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 안주 추천 프로그램 v0.6

import random
alcohol_foods = {}

with open('alcohols.txt', 'r') as fp1:
    with open('foods.txt') as fp2:
        alcohols = fp1.readlines() # 리스트 변수 alcohols
        foods = fp2.readlines()
        for k in range(len(alcohols)):
            alcohol_foods[alcohols[k].strip('\n')] = foods[k][0:-1] # '~~\n' 에서 \n 제거, strip와 [0:-1]

while True:
    alchol = input('주문하실 술('+ '/'.join([alcohol.rstrip('\n') for alcohol in alcohols]) +'/아무거나/결제)은? ')
    if alchol == '결제':
        break
    if alchol in alcohol_foods.keys():
        print('{0}에 어울리는 안주는 {1}입니다.'.format(alchol, alcohol_foods[alchol]))
    elif alchol == '아무거나':
        any = random.choice(list(alcohol_foods))
        print('{0}을/를 추천합니다. 안주는 {1}입니다.'.format(any, alcohol_foods[any]))
    else:
        print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alchol))
