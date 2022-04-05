# 별찍기

import tkinter as tk


def star():
    n = int(en_input.get())
    texts = ''
    for line in range(1, n + 1):
        for space in range(n - line, 0, -1):
            texts = texts + '0'
        for stars in range(1, 2 * line):
            texts = texts + '*'
        texts = texts + '\n'
    lbl_temp.configure(text=texts)

def easystar():
    n = int(en_input.get())
    star = '*'
    texts = ''
    for i in range(1, n*2 , 2):
        texts = texts + '{0:^{1}}'.format(star*i, n) + '\n'
    lbl_temp.configure(text=texts)


w = tk.Tk()
w.title('별 찍기 프로그램')
w.geometry('300x200')

# 선언
en_input = tk.Entry(w)
btn_star = tk.Button(w, text='별 찍기', command=easystar)
lbl_temp = tk.Label(w, text='별 찍기 프로그램')

# 폼 화면에 출력
en_input.pack()
btn_star.pack()
lbl_temp.pack()

# 마우스커서 focus
en_input.focus()

w.mainloop()








