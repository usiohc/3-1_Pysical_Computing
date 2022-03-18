# 조건문
# 조건에 따라 코드 실행 여부를 결정하는 구문

# 비교연산자
# print(5 == 5) # result->True
# print(5 != 5) # result->False
# print(5 > 5)  # result->False
# print(5 >= 5) # result->True

# 논리 연산자 (feat. 비교 연산자)
# x = 5
# print(2>x and x>1) # result->False
# print(2!=x and x>1) # result->True
# print(2>x or x>1) # result->True
# print(2==x or x<1) # result->False
# print(not(2==x)) # result ->True

# if문
# if True: # 음수 양수 모두 True / 0만 False
#     print('항상 실행!')
# else:
#     print('실행 될 일이 없음')


# age = input('나이가 어떻게 되세요? ')
# if int(age) >= 19:

# age = int(input('나이가 어떻게 되세요? '))
# if age >= 19:
#     print('입장 하세요.')
# else:
#     print('입장을 하실 수 없습니다.')


age = int(input('나이가 어떻게 되세요? '))
with_parents = input('보호자와 같이 오셨나요? (네/아니오) ')

if (age >= 15) or (with_parents == '네'): # 괄호를 사용해주는게 좀 더 좋은 코드
    print("15세 이상 관람가 입장가능.")
else:
    print("입장을 하실 수 없습니다.!")


