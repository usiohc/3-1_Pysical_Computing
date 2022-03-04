# 리스트
# 리스트는 특정 순서가 있는 항목의 모음
# 대괄호 [ ] 쉼표 기호를 사용함

# empty_list = []
# print(type(empty_list)) # result-><class 'list'>
# type() -> 자료형의 타입 출력
# print(type(5))
# print(type(5.7))
# print(type('python'))

# empty_lists = list()
# subjects = ['english', 'python', 'java']
# print(empty_lists) # result->[]
# print(subjects)# result->['english', 'python', 'java']
# print(type(empty_lists)) # result-><class 'list'>
# print(type(subjects)) # result-><class 'list'>

# 리스트 인덱싱
# 정방향 인덱싱 0, 1, 2, ...
# 역방향 인덱싱 뒤에서 부터 -1, -2, -3, ...
subjects = ['english', 'python', 'java']
# print(subjects[1])
# print(subjects[-2])

# 리스트 추가(append()), 삽입(insert())
print(subjects[-2])
subjects.append('C++')
print(subjects)
print(subjects[2])
print(subjects[-2])
subjects.insert(2, 'math') # 2번에 자리에 추가
print(subjects)
print(subjects[2])

# 리스트 원소 수정
subjects[3] = 'assembly'
print(subjects)

# 리스트 원소 삭제
# delete pop remove
# del subjects[-1]
del subjects[4]
print(subjects)

# subjects.pop() # 맨 뒤의 원소 삭제
subjects.pop(1)
print(subjects)

subjects.append('math')
print(subjects)
subjects.remove('math') # 직접 value 값을 지정해서 삭제
                        # 중복 원소 일때 맨 앞의 원소만 삭제
print(subjects)
