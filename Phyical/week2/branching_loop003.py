# 반복문 cont.
# for 변수 in range(변수 시작값, 끝값, 증감값)

# 짝수 출력
# for n in range(2, 11, 2):
#     print(n)

# for n in range(1, 11):
#     if n % 2 == 0:
#         print(n)

# 증감 step 에 감소식
# for n in range(10, 1, -2):
#     print(n)

# 문자열의 문자 출력
# words = 'I love python'
# for word in words:
#     print(word, end='')


# # 리스트 원소 출력
# words = ['I', 'love', 'python']
# for word in words:
#     print(word)
# # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 위의 방법이 더 안전, 파이썬스럽다
# # for i in range(0 ,3, 1):
# for i in range(3):
#     print(words[i])

# words = ['I', 'love', 'python']
# for i in range(len(words)):
#     print(words[i], end=' ')


# 극장 매표 관리 프로그램 v0.1
ages = []
price = 0
humans = int(input('몇 분이 오셨죠? '))
for i in range(humans):
    ages.append(int(input('나이는? ')))
for age in ages:
    if 0 <= age < 8:
        price += 5000
    elif 8 <= age < 19:
        price += 9000
    elif age >= 19:
        price += 11000
    else:
        print('정확한 나이를 입력해주세요!')
print('총 금액은 ' + str(price) + '원 입니다.')




