# exception handling
# 오류는 컴파일 전과 후로 나뉨

# 들여쓰기 오류
# for k in range(5):
# print(k)
# ^
# IndentationError: expected an indented block

# 실행중 발생하는 error 런타임 오류
# a = int(input())
# b = int(input())
# print(a + b)
# error 발생
# b = int(input())
# ValueError: invalid literal for int() with base 10: '7ㅇ'
# int형에 string 입력
# base 10, 10진수사용 '7ㅇ'

# 양의 정수 판별
# a = input()
# b = input()
# print(a.isdigit(), b.isdigit())
# if a.isdigit() and b.isdigit(): # 숫자로 바꿀 수 있는 string인지 판별, (양의 정수 = true, 그 외= false) 출력
#     print(int(a)+int(b))
# else:
#     print('입력된 수는 양의 정수가 아닙니다.!')


# try: except:
# try: 예외가 발생할 가능성이 있는 코드
# except: 예외가 발생했을 떄 실행할 코드
# else: 예외가 발생하지 않았을 때 실행할 코드
# finally: 무조건 실행

# 오류 발생 즉시 except로 바로감
# try:
#     a = int(input())
#     b = int(input())
#     print(a+b)
#     print(a/b)
# except:
#     print('입력된 수는 정수가 아닙니다.!')

try:
    c = list()
    c.append('사과')
    a = int(input())
    b = int(input())
    print(a / b)
    print(c[1]) # IndexError: list index out of range
except ZeroDivisionError: # ZeroDivisionError 에러 검출
    print('분모에 0이 올 수 없습니다.!')
except ValueError: # ValueError 에러 검출
    print('입력된 수는 정수가 아닙니다.!')
except IndexError: # IndexError 에러 검출
    print('리스트의 범위를 벗어났습니다.!')
except: # except handling 하지 않은 오류 전부 해당 except 오류문 출력
    print('무언가 에러가 발생했습니다.!')
else: # except가 발생하지 않으면 else문을 출력함
    print('정상적으로 처리되었습니다.!')
finally: # 오류 여부 상관없이 출력
    print('예외 발생 여부 없이 상관없이 항상 실행')