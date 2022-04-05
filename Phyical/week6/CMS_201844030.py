import random
import tkinter as tk

alcohol_foods = {'맥주': ['치킨', 20000],
                 '와인': ['치즈', 5000],
                 '고량주': ['짬뽕', 8000],
                 '소주': ['골뱅이소면', 9000]}
tlist = []

def fw():
    with open('bill.txt', 'w') as fp:
        for t in tlist:
            fp.writelines(t + '\n')

# output = lbl_output 출력 변수
# temp = tlist[] 요소로 받기 위한 변수

def af():
    alchol = en_input.get()

    if alchol == '결제':
        temp = '감사합니다. 다음 또 방문 부탁 드려요~'
        lbl_output.configure(text=temp)
        tlist.append(temp)
        fw()
    elif alchol in alcohol_foods.keys():
        output = '{0}에 어울리는 안주는 {1}입니다.'.format(alchol, alcohol_foods[alchol][0])
        lbl_output.configure(text=output)
        temp = alchol + ' 입력 : {0}에 어울리는 안주는 {1}입니다. 안주가격은 {2}원'.format(alchol, alcohol_foods[alchol][0],
                                                                       alcohol_foods[alchol][1])
        tlist.append(temp)
    elif alchol == '아무거나':
        any = random.choice(list(alcohol_foods))
        output = '{0}에 어울리는 안주는 {1}~~'.format(any, alcohol_foods[any][0])
        lbl_output.configure(text=output)
        temp = alchol + ' 입력 : {0}을/를 추천합니다. 안주는 {1}~~ 안주가격은 {2}원'.format(any, alcohol_foods[any][0],
                                                                         alcohol_foods[any][1])
        tlist.append(temp)
    else:
        output = '{0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alchol)
        lbl_output.configure(text=output)
        temp = alchol + ' 입력 : ' + output
        tlist.append(temp)

w = tk.Tk()
w.title('3학년 A반')
w.geometry('500x100')

# 선언
lbl_menu = tk.Label(w, text='주문하실 술(맥주/와인/소주/고량주/아무거나/결제)은?')
lbl_output = tk.Label(w, text='주문 내역')
en_input = tk.Entry(w)
btn_check = tk.Button(w, text='확인', command=af)

# 폼 화면에 출력
lbl_menu.pack()
lbl_output.pack()
en_input.pack()
btn_check.pack()

# 마우스커서 focus
en_input.focus()

w.mainloop()
