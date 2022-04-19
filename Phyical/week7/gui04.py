
# take 2
import tkinter as tk
from  tkinter import messagebox
from tkinter import ttk
# 디자인의 차이, ttk는 플랫한느낌


def popup():
    # 체크가 해재 되었을때
    if checked.get() == False:
        lbl_display.configure(text='체크버튼 OFF')
        messagebox.showinfo('언체크됨', '체크버튼 OFF')
    elif checked.get() == True:
        lbl_display.configure(text='체크버튼 ON')
        messagebox.showinfo('체크됨', '체크버튼 ON')
    else:
        messagebox.showerror('오류', '실행될 일 없음')

w = tk.Tk()
w.title('체크버튼 실습')
w.geometry('300x100')

# 선언
# IntVar(), 정수형 변수 객체 지정
# 레퍼 변수 클래스 / 객체여서 위if문에서 .get()을 사용 할 수가 있는거임
# checked = tk.IntVar() 논리형 변수 객체 지정
# print(type(checked))  # result-><class 'tkinter.IntVar'>
# 체크 값만 받기 떄문에 True, False로 받음
checked = tk.BooleanVar() # <class 'tkinter.BooleanVar'>
#    checked = 0, .get() 오류 발생 / AttributeError: 'int' object has no attribute 'get'
#    int 객체는 get이라는 attribute를 가지고있지않음
#    checked = 0 # 기본 정수, get()함수 등을 사용할 수 없다.

cb_on_off = tk.Checkbutton(w, text='출석체크', variable=checked, command=popup)
lbl_display = tk.Label(w, text='')

# 디자인의 차이, ttk는 플랫한느낌
btn_btndumy = ttk.Button(w, text='더미버튼')


cb_on_off.pack()
lbl_display.pack()

w.mainloop()

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# # take 2
# import tkinter as tk
# from  tkinter import messagebox
#
# def popup():
#     # info, warning, error 아이콘 이미지가 다름
#     #                   "제목,    본문내용"
#     # messagebox.showinfo("쿨릭", "버튼이 눌렸습니다.")
#     # messagebox.showwarning("쿨릭", "버튼이 눌렸습니다.")
#     # messagebox.showerror("쿨릭", "버튼이 눌렸습니다.")
#
#     messagebox.askokcancel("쿨릭", "버튼이 눌렸습니다.")
#
#
#
# # 이미지 배치
#
# w = tk.Tk()
# w.title()
# # w.geometry('300x100')
#
# # 이미지 준비
# p1 = tk.PhotoImage(file='michael.PNG')
# p2 = tk.PhotoImage(file='franklin.PNG')
# p3 = tk.PhotoImage(file='trevor.PNG')
#
# # 레이블 및 버튼에 사용할 이미지 바인딩
# lbl_disp1 = tk.Label(w, image=p1)
# lbl_disp2 = tk.Label(w, image=p2)
# btn_disp3 = tk.Button(w, image=p3, command=popup)
#
# # 위젯 배치
# lbl_disp1.pack(side='left')  # side = 배치 위치
# lbl_disp2.pack(side='left')
# btn_disp3.pack()  # 마지막 pack()는 생략하면 자동으로
#
#
# w.mainloop()
#

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# take 1

# import tkinter as tk
#
# # 이미지 배치
#
# w = tk.Tk()
# w.title()
# # w.geometry('300x100')
#
# # 이미지 준비
# p1 = tk.PhotoImage(file='michael.PNG')
# p2 = tk.PhotoImage(file='franklin.PNG')
# p3 = tk.PhotoImage(file='trevor.PNG')
#
# # 레이블 및 버튼에 사용할 이미지 바인딩
# lbl_disp1 = tk.Label(w, image=p1)
# lbl_disp2 = tk.Label(w, image=p2)
# btn_disp3 = tk.Button(w, image=p3)
#
# # 위젯 배치
# lbl_disp1.pack(side='left')  # side = 배치 위치
# lbl_disp2.pack(side='left')
# btn_disp3.pack()  # 마지막 pack()는 생략하면 자동으로
#
#
# w.mainloop()