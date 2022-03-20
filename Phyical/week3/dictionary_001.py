# dictionary

# 리스트와 비슷하나 순서를 따지지 않는다.
# 키와 값이 pair로 원소가 된다.

#            k   :  V
# fruits = {'apple':'사과', 'watermelon':'수박'}
# print(fruits['watermelon'])
# print(fruits)
# fruits['kiwi'] = '키우' # 삽입
# fruits['banana'] = '바나나' # 삽입
# print(fruits)
# fruits['kiwi'] = '키위' # 수정
# print(fruits)
#
# empty = {}
# print(type(fruits), type(empty)) # result-><class 'dict'>


# List -> dict / dict()함수

# test1 = [['python', '3'], ['english', 2], ['dance', 1]]
# print(test1[1]) # result->['english', 2]
# print(test1[1][0]) # result->english
#
# test2 = ['ad', 'cd', 'ef'] # 원소 내부를 짝수로 맞춰야함 ['adx', 'cd', 'ef'] -> 오류 발생
# print(test2[1][0]) # result->c
# print(dict(test2)) # result->{'a': 'd', 'c': 'd', 'e': 'f'}

# dict.update() 결합함수
fruits = {'apple':'사과', 'watermelon':'수박'}
fruits['banana'] = '바나나'

others = {'strawberry':'딸기', 'kiwi':'키위', 'banana':'버내너'}
fruits.update(others)
print(fruits) # result->{'apple': '사과', 'watermelon': '수박', 'banana': '버내너', 'strawberry': '딸기', 'kiwi': '키위'}
              # 결합 하면서 'banana' key가 중복되어 value값 '바나나' 를 '버내너' 로 덮어씌움

# del 삭제
del fruits['apple']
print(fruits) # 'apple' 키로 {'apple':'사과'} 원소 삭제
fruits.clear() # 원소 전체 삭제 함수
# del fruits # dict자체를 삭제시킴
print(fruits) # result->{}
