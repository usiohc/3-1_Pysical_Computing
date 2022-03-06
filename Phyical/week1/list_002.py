# # 리스트 002
#
# # 리스트 원소 삭제 (계속)
# subjects = ['english', 'python', 'java']
# print(subjects)
# # print(subjects.remove('python')) # result ->None / 삭제는 했으나 해당 값을 리턴하지는 않음
# print(subjects.pop(1)) # result ->python / 삭제하려는 원소 값을 리턴 후 삭제
# print(subjects)
#
# # 리스트의 위치 출력
# print(subjects.index('java'))
#
# # 리스트 원소의 값 세기
# subjects.append('java')
# subjects.append('java')
# print(subjects)
# print(subjects.count('java')) # result ->3
# print(subjects.count('english')) # result ->1
#
# # in 키워드
# # bool타입 출력
# print('python' in subjects) # result ->False
# print('java' in subjects) # result ->True
#
# # 리스트 원소의 개수 리턴
# subjects.insert(0, 'python')
# print(len(subjects)) # result ->5
# print(subjects)
#
# # 리스트를 문자열로 바꿔주는 함수 join()
# # subjects_string = ''.join(subjects)
# # print(subjects_string) # result ->pythonenglishjavajavajava
# subjects_string = '/'.join(subjects)
# print(subjects_string) # result ->python/english/java/java/java
#
# # 문자열을 리스트로 바꿔주는 함수 split()
# subjects_lists = subjects_string.split('/') # /를 구분자로 split
# print(subjects_lists) # result ->['python', 'english', 'java', 'java', 'java']
#
# # 리스트 원소 정렬 sort()
# print(subjects)
# subjects.sort() # 기본값은 알파벳 오름차순 정렬 (사전순)
# print(subjects)
# subjects.sort(reverse=True) # 내림차순 정렬 (사전순)
# print(subjects)


list_a = [2, 3, 1]
list_copy = sorted(list_a)
print(list_a)
print(list_copy)

list_copy = sorted(list_a, reverse=True)
print(list_copy)

# 단, 문자열과 숫자의 비교가 불가능
# list_b = [2, 3, 1, 'sort', 'python']
# list_bCopy = sorted(list_b) # result -> TypeError 'str' and 'int'


