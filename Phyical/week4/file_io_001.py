# file io

# 파일 객체 = open(파일 경로, 읽기 모드)
# w: 쓰기모드, r: 읽기모드, a: 이어쓰기모드
# 피알을 닫을 때 파일객체.close()

# 파일 쓰기
# fp = open('war_flower.txt', 'w')
# print('고니', file=fp) # 실제 쓰기
# print('정마담', file=fp) # 실제 쓰기
# print('아귀', file=fp) # 실제 쓰기
# fp.write('너부리')
# fp.close()

# 파일 읽기
# fp = open('war_flower.txt', 'r')
# lines = fp.readlines() # 파일을 1행 단위의 리스트 원소로 리턴
# print(lines)
# for line in lines:
#     # print(line.rstrip('\n'))
#     # print(line[0:-1]) # 제일 마지막 문자를 안읽어서 너부리 -> 너부로 출력함
#     print(line, end='')
# # for line in fp:
# #     print(line, end='')
# fp.close()


# with
# 파일을 열면 항상 close를 해줘야함
# 하지만 with는 자동적으로 처리할 수 있게 해줌
# with open(파일 경로, 읽기 모드) as 파일객체:
#   with 블록을 벗어나는 순간 열린 파일객체가 자동으로 close
with open('war_flower.txt') as fp:
    lines = fp.readlines() # 파일을 1행 단위의 리스트 원소로 리턴
    for line in lines:
        print(line[0:-1])
        # print(line, end='')

