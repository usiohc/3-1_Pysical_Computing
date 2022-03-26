# graphic user interface

from tkinter import *

w = Tk() # 윈도우 객체 생성
w.title('레이블 실습') # 제목

# from tkinter import * -> tkinter.Label() -> Label()
# w를 객체로 지정
lbl_1 = Label(w, text='파이썬을')
lbl_2 = Label(w, text='열심히', font=("돋움", 20), fg="red")
lbl_3 = Label(w, text='공부합니다', fg="blue", bg="green", width=20, height=10, anchor=SW)

# label 객체를 시각화
lbl_1.pack()
lbl_2.pack()
lbl_3.pack()

w.mainloop() # 생성된 윈도우 객체 mainloop() 함수 실행


# 찍먹
# import tkinter # 그래픽 모듈 불러오기
#
# win = tkinter.Tk() # 윈도우 객체 생성
#
# win.title('GUI') # 제목
# win.geometry('600x150') # 가로 세로 크기 지정
# win.resizable(width=False, height=False) # 너비 높이 고정
#
# win.mainloop() # 생성된 윈도우 객체 mainloop() 함수 실행




# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 안주 추천 프로그램 v0.7
#
# import random
#
# alcohol_foods = {}
# a = input('술의 종류를 보관하고 있는 파일? ')
# f = input('안주의 종류를 보관하고 있는 파일? ')
#
# try:
#     with open(a) as fp1:
#         with open(f) as fp2:
#             alcohols = fp1.readlines() # 리스트 변수 alcohols
#             foods = fp2.readlines()
#             for k in range(len(alcohols)):
#                 alcohol_foods[alcohols[k].strip('\n')] = foods[k][0:-1] # '~~\n' 에서 \n 제거, strip와 [0:-1]
# except FileNotFoundError:
#     print('파일이 없거나 폴더의 경로가 틀렸습니다.')
# else:
#     while True:
#         alchol = input('주문하실 술('+ '/'.join([alcohol.rstrip('\n') for alcohol in alcohols]) +'/아무거나/결제)은? ')
#         if alchol == '결제':
#             break
#         if alchol in alcohol_foods.keys():
#             print('{0}에 어울리는 안주는 {1}입니다.'.format(alchol, alcohol_foods[alchol]))
#         elif alchol == '아무거나':
#             any = random.choice(list(alcohol_foods))
#             print('{0}을/를 추천합니다. 안주는 {1}입니다.'.format(any, alcohol_foods[any]))
#         else:
#             print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alchol))
# finally:
#     print('다음에 또 만나요~')