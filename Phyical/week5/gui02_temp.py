# 화씨 섭씨 변환 프로그램

import tkinter as tk


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


def c2f():
    try:
        c = float(en_input.get())
        f = (c * 9/5) + 32 # 32!.0!이 포인트
        lbl_temp.configure(text='섭씨 {0}도는 화씨 {1}도 입니다.'.format(c, round(f, 4)))
    except ValueError as e:
        lbl_temp.configure(text='숫자만 입력해주세요\n {0}'.format(e))
        en_input.delete(0, 'end')

    # lbl_temp.configure(text=round(c, 4))
    # print('버튼 클릭됨' + f)
    # print(1 + f) # TypeError


w = tk.Tk()
w.title('두 번째 GUI 프로그램')
w.geometry('300x100')

# 선언
en_input = tk.Entry(w)
btn_f2c = tk.Button(w, text='화씨->섭씨', command=f2c)
btn_c2f = tk.Button(w, text='섭씨->화씨', command=c2f)
# command 함수에 인수로 던져두는 함수 -> 콜백함수
lbl_temp = tk.Label(w, text='온도변환 프로그램')

# 폼 화면에 출력
en_input.pack()
btn_f2c.pack()
btn_c2f.pack()
lbl_temp.pack()

# 마우스커서 focus
en_input.focus()

w.mainloop()