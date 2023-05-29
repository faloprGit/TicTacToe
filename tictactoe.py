# Made By falopr
from tkinter import *

player_turn = 1


def call_funcs(n1, plyr_turn):
    verification_win()
    btn_pressed(n1, plyr_turn)


def btn_pressed(n1, plyr_turn):
    if plyr_turn == 1:
        if n1.get() == '':
            n1.set('O')
            global player_turn
            player_turn += 1
    else:
        if n1.get() == '':
            n1.set('X')
            player_turn -= 1


def adwins(var1):
    if var1 == 1:
        string_var10.set('Desactivated')
        global active_wins
        active_wins -= 1
    else:
        string_var10.set('Activated')
        active_wins += 1


window = Tk()
window.geometry('300x350')
window.resizable(False, False)
window.title('Tic Tac Toe')

string_var0 = StringVar()
string_var1 = StringVar()
string_var2 = StringVar()
string_var3 = StringVar()
string_var4 = StringVar()
string_var5 = StringVar()
string_var6 = StringVar()
string_var7 = StringVar()
string_var8 = StringVar()
string_var9 = StringVar()
string_var10 = StringVar(window, 'Activated')


def verification_win():
    if ((string_var1.get() and string_var2.get()) and string_var3.get()) == 'O':
        string_var0.set('Player 1 Won !')
    elif ((string_var4.get() and string_var5.get()) and string_var6.get()) == 'O':
        string_var0.set('Player 1 Won !')
    elif ((string_var7.get() and string_var8.get()) and string_var9.get()) == 'O':
        string_var0.set('Player 1 Won !')
    elif ((string_var1.get() and string_var4.get()) and string_var7.get()) == 'O':
        string_var0.set('Player 1 Won !')
    elif ((string_var2.get() and string_var5.get()) and string_var8.get()) == 'O':
        string_var0.set('Player 1 Won !')
    elif ((string_var3.get() and string_var6.get()) and string_var9.get()) == 'O':
        string_var0.set('Player 1 Won !')
    elif ((string_var1.get() and string_var5.get()) and string_var9.get()) == 'O':
        string_var0.set('Player 1 Won !')
    elif ((string_var3.get() and string_var5.get()) and string_var7.get()) == 'O':
        string_var0.set('Player 1 Won !')
    elif ((string_var1.get() and string_var2.get()) and string_var3.get()) == 'X':
        string_var0.set('Player 2 Won !')
    elif ((string_var4.get() and string_var5.get()) and string_var6.get()) == 'X':
        string_var0.set('Player 2 Won !')
    elif ((string_var7.get() and string_var8.get()) and string_var9.get()) == 'X':
        string_var0.set('Player 2 Won !')
    elif ((string_var1.get() and string_var4.get()) and string_var7.get()) == 'X':
        string_var0.set('Player 2 Won !')
    elif ((string_var2.get() and string_var5.get()) and string_var8.get()) == 'X':
        string_var0.set('Player 2 Won !')
    elif ((string_var3.get() and string_var6.get()) and string_var9.get()) == 'X':
        string_var0.set('Player 2 Won !')
    elif ((string_var1.get() and string_var5.get()) and string_var9.get()) == 'X':
        string_var0.set('Player 2 Won !')
    elif ((string_var3.get() and string_var5.get()) and string_var7.get()) == 'X':
        string_var0.set('Player 2 Won !')


def clear_ttt():
    string_var1.set('')
    string_var2.set('')
    string_var3.set('')
    string_var4.set('')
    string_var5.set('')
    string_var6.set('')
    string_var7.set('')
    string_var8.set('')
    string_var9.set('')
    string_var0.set('')


frame1 = Frame(window, width=200, height=200)
frame1.pack(expand=True)

frame3 = Frame(window)
frame3.pack()

frame2 = Frame(window)
frame2.pack(side=BOTTOM)


lbl1 = Label(frame2, text='Player 1 = O')
lbl1.pack(side=LEFT, padx=10)

lbl2 = Label(frame2, text='Player 2 = X')
lbl2.pack(side=RIGHT, padx=10)

lbl3 = Label(window, textvariable=string_var0)
lbl3.pack(side=TOP, pady=10)

btn1 = Button(frame1, width=6, height=3, textvariable=string_var1,
              command=lambda: call_funcs(string_var1, player_turn))
btn1.grid(row=0, column=0)

btn2 = Button(frame1, width=6, height=3, textvariable=string_var2,
              command=lambda: call_funcs(string_var2, player_turn))
btn2.grid(row=0, column=1)

btn3 = Button(frame1, width=6, height=3, textvariable=string_var3,
              command=lambda: call_funcs(string_var3, player_turn))
btn3.grid(row=0, column=2)

btn4 = Button(frame1, width=6, height=3, textvariable=string_var4,
              command=lambda: call_funcs(string_var4, player_turn))
btn4.grid(row=1, column=0)

btn5 = Button(frame1, width=6, height=3, textvariable=string_var5,
              command=lambda: call_funcs(string_var5, player_turn))
btn5.grid(row=1, column=1)

btn6 = Button(frame1, width=6, height=3, textvariable=string_var6,
              command=lambda: call_funcs(string_var6, player_turn))
btn6.grid(row=1, column=2)

btn7 = Button(frame1, width=6, height=3, textvariable=string_var7,
              command=lambda: call_funcs(string_var7, player_turn))
btn7.grid(row=2, column=0)

btn8 = Button(frame1, width=6, height=3, textvariable=string_var8,
              command=lambda: call_funcs(string_var8, player_turn))
btn8.grid(row=2, column=1)

btn9 = Button(frame1, width=6, height=3, textvariable=string_var9,
              command=lambda: call_funcs(string_var9, player_turn))
btn9.grid(row=2, column=2)

btn_clear = Button(frame3, width=4, height=1, text='Clear',
                   command=lambda: clear_ttt())
btn_clear.pack(pady=3)

btn_wins = Button(frame3, width=20, height=1, text='Active/Desactive Wins',
                  command=lambda: adwins(active_wins))
btn_wins.pack()

lbl4 = Label(frame3, textvariable=string_var10)
lbl4.pack()

window.mainloop()
