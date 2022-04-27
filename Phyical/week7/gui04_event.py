# 화씨 섭씨 변환 프로그램
# radiobutton 활용

import tkinter as tk
from tkinter import ttk


def rb_check_result_enter(_):
    rb_check_result()

def rb_check_result():
    rb_check()

def rb_check():
    if selected.get() == 0:
        f2c()
        pass
    elif selected.get() == 1:
        c2f()
        pass


#                    # 이외 방법은 람다함수 사용
# def f2c_enter(_):  # _ = 매개변수 넣어야 하는데 필요 없음
#     f2c()

def f2c():
    # pass
    # (32°F − 32) × 5 / 9 = 0°C
    try:
        f = float(en_input.get())
        c = (f - 32.0) * (5.0/9.0) # 32!.0!이 포인트
        lbl_temp.configure(text='화씨 {0}도는 섭씨 {1}도 입니다.'.format(f, round(c, 4)))
    except ValueError as e:
        lbl_temp.configure(text='숫자만 입력해주세요\n {0}'.format(e))
        en_input.delete(0, 'end')

# def c2f_enter(_):  # _ = 매개변수 넣어야 하는데 필요 없음
#     c2f()

def c2f():
    try:
        c = float(en_input.get())
        f = (c * 9/5) + 32 # 32!.0!이 포인트
        lbl_temp.configure(text='섭씨 {0}도는 화씨 {1}도 입니다.'.format(c, round(f, 4)))
    except ValueError as e:
        lbl_temp.configure(text='숫자만 입력해주세요\n {0}'.format(e))
        en_input.delete(0, 'end')


w = tk.Tk()
w.title('두 번째 GUI 프로그램')
w.geometry('400x200')

# 선언
selected = tk.IntVar() # <class 'tkinter.BooleanVar'>
rb_f2c = ttk.Radiobutton(w, text='화씨->섭씨', variable=selected, value=0)
rb_c2f = ttk.Radiobutton(w, text='섭씨->화씨', variable=selected, value=1)


en_input = tk.Entry(w)
btn_result = tk.Button(w, text='결과', command=rb_check_result)
# command 함수에 인수로 던져두는 함수 -> 콜백함수
lbl_temp = tk.Label(w, text='온도변환 프로그램')

# 키이벤트
# en_input.bind('<Return>', rb_check_result_enter)
# 라디오버튼 클릭하면 en_input에서 포커스가 벗어남
w.bind('<Return>', rb_check_result_enter)

# 폼 화면에 출력
en_input.pack()
rb_f2c.pack()
rb_c2f.pack()
btn_result.pack()
lbl_temp.pack()

# 마우스커서 focus
en_input.focus()

w.mainloop()