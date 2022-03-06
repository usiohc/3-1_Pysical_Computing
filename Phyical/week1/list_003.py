# 리스트 003

# # 리스트 복사
# my_utube = ['악뮤', '볼사', '코노', '언더독', '홍수웅', '빅뱅']
# ur_utube = my_utube
# print(ur_utube)
#
# ur_utube = my_utube[0:5]
# print(ur_utube)
#
# ur_utube = my_utube
# del ur_utube[-1] # or [5]
# print(ur_utube)
#
# ur_utube.append('태양')
# print(ur_utube)
# print(my_utube)
# print(id(my_utube), id(ur_utube))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# a = [2, 3, 1, 5]
# # b = a # 공유, 주소값이 같음 b에 추가 제거 해도 a에도 동일한 입력
# # b = a[0:] # 슬리이싱, 0번째 index부터 끝까지
# # b = a.copy() # 공유하지 않는 복사
# b = list(a) # 공유하지 않는 복사
# print(b)
# b[-2] = 4
# print(b)
# print(a)
# print(id(a), id(b)) # id(), 해당 변수의 주소값 함수


my_utube = ['악뮤', '볼사', '코노', '언더독', '홍수웅', '빅뱅']
# friends = my_utube[2:5]
# friends = my_utube[-4:-1]
# friends = my_utube[2:-1]
# friends = my_utube[-4:5]
friends = my_utube[2:len(my_utube)-1]
print(friends) # result ->['코노', '언더독', '홍수웅']

ur_friends = ['릴러말즈', '슈퍼비']
print(friends)

friends.extend(ur_friends) # 병합
print(friends) # result ->['코노', '언더독', '홍수웅', '릴러말즈', '슈퍼비']