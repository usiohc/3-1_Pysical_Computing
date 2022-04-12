# take 3
import tkinter as tk
from tkinter import ttk

# 다음
def click_next():
    global idx
    idx += 1
    if idx > len(photos)-1:
        idx = 0
    # 경로지정
    p = tk.PhotoImage(file=photos[idx])
    # commit
    lbl_photo.configure(image=p)
    # push
    lbl_photo.image = p

# 이전
def click_prev():
    global idx
    idx -= 1
    if idx < 0:
        idx = len(photos)-1
    # 경로지정
    p = tk.PhotoImage(file=photos[idx])
    # commit
    lbl_photo.configure(image=p)
    # push
    lbl_photo.image = p


# 전역변수 선언
photos = ['michael.PNG', 'franklin.PNG', 'trevor.PNG']
idx = 0


# 폼 선언
w = tk.Tk()
w.title('포토뷰어 v0.1')
w.geometry('500x600')


# 이미지 준비
p = tk.PhotoImage(file=photos[0])
lbl_photo = ttk.Label(w, image=p)
btn_next = ttk.Button(w, text='다음 -->', command=click_next)
btn_prev = ttk.Button(w, text='<-- 이전', command=click_prev)


# 화면 출력
lbl_photo.grid(row=0, column=0, columnspan=2)
btn_next.grid(row=1, column=1, sticky=tk.EW)
btn_prev.grid(row=1, column=0, sticky=tk.EW)


# 실행
w.mainloop()




# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# # take 3
# import tkinter as tk
# from tkinter import ttk
#
#
# def popup():
#     if selected.get() == 0:
#         lbl_display.configure(image=p1)
#     elif selected.get() == 1:
#         lbl_display.configure(image=p2)
#     else:
#         lbl_display.configure(image=p3)
#
#
# w = tk.Tk()
# w.title('체크버튼 실습')
# w.geometry('500x600')
#
# # 이미지 준비
# p1 = tk.PhotoImage(file='michael.PNG')
# p2 = tk.PhotoImage(file='franklin.PNG')
# p3 = tk.PhotoImage(file='trevor.PNG')
#
#
# # 버튼 이미지 선언
# selected = tk.IntVar()  # variable = 연결되어있는 변수
# rb_1 = ttk.Radiobutton(w, text='마이클', command=popup, variable=selected, value=0)
# rb_2 = ttk.Radiobutton(w, text='프랭클린', command=popup, variable=selected, value=1)
# rb_3 = ttk.Radiobutton(w, text='트레버', command=popup, variable=selected, value=2)
# lbl_display = ttk.Label(w, text='선택할 플레이어는?')
# lbl_display.configure(image=p1)
#
#
# #화면에 출력
# rb_1.grid(row=0, column=0)
# rb_2.grid(row=0, column=1)
# rb_3.grid(row=0, column=2)
# lbl_display.grid(row=1, column=0, columnspan=3)
#
# w.mainloop()
