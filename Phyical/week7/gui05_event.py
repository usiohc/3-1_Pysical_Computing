# 화씨 섭씨 변환 프로그램

import tkinter as tk

                   # 이외 방법은 람다함수 사용
def f2c_enter(_):  # _ = 매개변수 넣어야 하는데 필요 없음
    f2c()

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


w = tk.Tk()
w.title('두 번째 GUI 프로그램')
w.geometry('300x100')

# 선언
en_input = tk.Entry(w)
btn_f2c = tk.Button(w, text='화씨->섭씨', command=f2c)
# command 함수에 인수로 던져두는 함수 -> 콜백함수
lbl_temp = tk.Label(w, text='온도변환 프로그램')

# 키이벤트
en_input.bind('<Return>', f2c_enter)

# 폼 화면에 출력
en_input.pack()
btn_f2c.pack()
lbl_temp.pack()

# 마우스커서 focus
en_input.focus()

w.mainloop()