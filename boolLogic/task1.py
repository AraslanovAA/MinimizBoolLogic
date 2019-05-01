import functools
from tkinter import messagebox
import pars
import tkinter as tk
elements = []
layers = []
operations = []
inputs_elements = []
coordinats_outputs = []
coordinats_inputs = []
equal_coord_elem = []
str1 = ''
count_inputs_len = []
number_inputs = []
inputs_coordinatsX = []
inputs_coordinatsY = []
outputs_coordinatsX = []
outputs_coordinatsY = []
counter_elem = 0
ss = ''

def read_entry(event):
    global str1
    str1 = entry.get()
    print(str1)


def read_valueA(event):
    s = entryA.get()
    if len(s) > 0:
        entryA.delete('0', tk.END)

def read_valueB(event):
    s = entryB.get()
    if len(s) > 0:
        entryB.delete('0', tk.END)

def read_valueC(event):
    s = entryC.get()
    if len(s) > 0:
        entryC.delete('0', tk.END)

def read_valueD(event):
    s = entryD.get()
    if len(s) > 0:
        entryD.delete('0', tk.END)
def CheckInput():#Антон добавил для реализации сравнения
    resCheck = pars.Recognizer(InputFunction.get(),"task1")
    if( resCheck[0] == -1):
        #print(resCheck[1])
        messagebox.showinfo("Error", resCheck[1])
        return -1
    else:
        numTNum = 0#количество строк имеющих 0/1 в соответствие с заданием
        rememberPos = []#запоминаем строку соответствующую заданию
        for i in resCheck:
            if(int(i[4]) == int(klist[1][0][4])):
                numTNum+=1
                rememberPos = i
        if(numTNum !=1):
            #print("Функция неверна0")
            messagebox.showinfo("Задание 1", "Функция неверна")
            return -1
        flag = True
        for i in range(4):
            if(int(rememberPos[i]) !=int(klist[1][0][i])):
                flag = False
        if (flag == False):
            #print("Функция неверна1")
            messagebox.showinfo("Задание 1", "Функция неверна")
            return -1
        #print("Красавчик хуле")
        messagebox.showinfo("Задание 1", "Функция введена верно")
        entry.config(state=tk.DISABLED)
        lbltemp.destroy()
        butn.config(state=tk.DISABLED)
        return 0
        print(resCheck)
    return 0
def emulation(event):
    A = entryA.get()
    B = entryB.get()
    C = entryC.get()
    D = entryD.get()
    if ((A != '1') & (A != '0') | (B != '1') & (B != '0') | (C != '1') & (C != '0') | (D != '1') & (D != '0')):
        ex = 1
    else:
        if ((A == str(klist[1][0][0])) & (B == str(klist[1][0][1])) & (C == str(klist[1][0][2])) & (D == str(klist[1][0][3]))):
            l = len(elements)
            x = coordinats_outputs[l - 1][0]
            y = coordinats_outputs[l - 1][1] - 15
            canvas.create_rectangle(x - 5, y - 15, x + 5, y + 5, fill='white', outline='white')
            canvas.create_text(x, y, text=str(klist[1][0][4]))
        else:
            l = len(elements)
            if (klist[1][0][4] == '1'):
                x = coordinats_outputs[l-1][0]
                y = coordinats_outputs[l-1][1] - 15
                canvas.create_rectangle(x - 5, y - 15, x + 5, y + 5, fill='white', outline='white')
                canvas.create_text(x, y, text='0')
              #  messagebox.showinfo("Error", '0')
            else:
                x = coordinats_outputs[l-1][0]
                y = coordinats_outputs[l-1][1] - 15
                canvas.create_rectangle(x - 5, y - 15, x + 5, y + 5, fill='white', outline='white')
                canvas.create_text(x, y, text='1')
             #   messagebox.showinfo("Error", '1')

root = tk.Tk()
root.state('zoomed')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


canvas = tk.Canvas(root, bg='white', width=screen_width + 10, height=screen_height + 10,scrollregion=(0,0,10000,10000))
hbar=tk.Scrollbar(root,orient=tk.HORIZONTAL)
hbar.pack(side=tk.BOTTOM, fill=tk.X)
hbar.config(command=canvas.xview)
vbar=tk.Scrollbar(root,orient=tk.VERTICAL)
vbar.pack(side=tk.RIGHT,fill=tk.Y)
vbar.config(command=canvas.yview)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

entry = tk.Entry(root , width=45, font="Helvetica 18 bold", bg='white')
entry.place(x=50, y=25)
butn = tk.Button(root, text='ОК', width=11, height=2)
butn.place(x=670, y=20)
lblA = tk.Label(root, width=2, font="Helvetica 18 bold", text='A=', bg='white')
lblA.place(x=820, y=20)
entryA = tk.Entry(root, width=1, font="Helvetica 18 bold")
entryA.bind('<Key>', read_valueA)
entryA.place(x=860, y=20)
entryA.insert(tk.END, '0')
entryA.update()
lblB = tk.Label(root, width=2, font="Helvetica 18 bold", text='B=',bg='white')
lblB.place(x=890, y=20)
entryB = tk.Entry(root, width=1, font="Helvetica 18 bold")
entryB.bind('<Key>', read_valueB)
entryB.place(x=930, y=20)
entryB.insert(tk.END, '0')
entryB.update()
lblC = tk.Label(root, width=2, font="Helvetica 18 bold", text='C=', bg='white')
lblC.place(x=960, y=20)
entryC = tk.Entry(root, width=1, font="Helvetica 18 bold")
entryC.bind('<Key>', read_valueC)
entryC.place(x=1000, y=20)
entryC.insert(tk.END, '0')
entryC.update()
lblD = tk.Label(root, width=2, font="Helvetica 18 bold", text='D=', bg='white')
lblD.place(x=1030, y=20)
entryD = tk.Entry(root, width=1, font="Helvetica 18 bold")
entryD.bind('<Key>', read_valueD)
entryD.place(x=1070, y=20)
entryD.insert(tk.END, '0')
entryD.update()

btn_emul = tk.Button(root, text='Проверить', width=11, height=2)
btn_emul.bind('<Button-1>', emulation)
btn_emul.place(x=1100, y=16)

lbltemp = tk.Label(root, text='Введите функцию: ', bg='white')
lbltemp.place(x=300, y=2)


canvas.place(x=0, y=0)

#Антон добавли для реализации сравнения
butn.configure(command = CheckInput)
global InputFunction
InputFunction = tk.StringVar()
entry.configure(textvariable = InputFunction)
#

 #mlist = [[0,'+','A','B','C'], [0,'|','A','C'],[1,'-','#1'],[1,'^','#0','#1'],[2,'/','#3','#2']]
#mlist = pars.StartParse("((-A)|(C/B))+(B>(A+B))")
global klist
klist = []
klist = pars.CreatesFunc(2)
print(klist[1])
'''Информация для Дениса:
    Запрашиваем генерацию функции через pars.CreatesFunc()
    В klist[0] - список списков который рисуешь
    klist[1] - необходимая инфа для задания 4 цифры - входные параметры и 5-ая - реузультат функции при таких параметрах'''
if(klist!= None):
    mlist = []
    mlist = klist[0]

    ss = klist[1][0][4]
    lblTarget = tk.Label(root, text='Цель = ' + ss, font="Helvetica 18 bold", bg='white')
    lblTarget.place(x=1200, y=20)
    i = 0
    while i < len(mlist):
        elements.append(mlist[i])
        i = i + 1
    i = 0
    while i < len(mlist):
        layers.append(elements[i][0])
        i = i + 1
    i = 0
    while i < len(mlist):
        operations.append(elements[i][1])
        i = i + 1
    i = 0
    while i < len(mlist):
        inputs_elements.append([])
        k = 2
        while k < len(elements[i]):
            inputs_elements[i].append(elements[i][k])
            k = k + 1
        i = i + 1

    x_start = 100
    y_start = 100
    i = 0
    h = 0
    prev_layer = -1
    while i < len(mlist):
        current_layer = layers[i]
        if current_layer != prev_layer:
            y_start = 100
        count_inputs = len(inputs_elements[i])
        x1 = int(layers[i]) * 150 + x_start
        y1 = y_start
        x2 = int(layers[i]) * 150 + 50 + x_start
        y2 = 30 * count_inputs + 30 + y_start
        canvas.create_rectangle(x1, y1, x2, y2)
        canvas.create_text(x1 + 25, y1 + 50, text=counter_elem)
        counter_elem = counter_elem + 1
        if elements[i][1] == '*':
            oper = 'AND'
        if elements[i][1] == '+':
            oper = 'OR'
        if elements[i][1] == '-':
            oper = 'NOT'
        if elements[i][1] == '^':
            oper = 'XOR'
        if elements[i][1] == '/':
            oper = 'PIRS'
        if elements[i][1] == '|':
            oper = 'SHEF'
        if elements[i][1] == '>':
            oper = 'IMPL'
        canvas.create_text(x1 + 20, y1 + 20, text=oper)
        canvas.create_line(x2, y1 + (y2 - y1) / 2 + 1, x2 + 25, y1 + (y2 - y1) / 2 + 1)
        if oper == 'NOT':
            canvas.create_oval(x2 - 5, y1 + 25, x2 + 6, y2 - 24, fill='white')
        outputs_coordinatsX.append(x2 + 25)
        outputs_coordinatsY.append(y1 + (y2 - y1)/2 + 1)
        coordinats_outputs.append([])
        coordinats_outputs[i].append(x2 + 25)
        coordinats_outputs[i].append(y1 + (y2 - y1)/2 + 1)
        j = 0
        deltaY = 30
        while j < count_inputs:
            canvas.create_line(x1 - 25, y1 + deltaY, x1, y1 + deltaY)
            coordinats_inputs.append([])
            coordinats_inputs[h].append(x1 - 25)
            coordinats_inputs[h].append(y1 + deltaY)
            coordinats_inputs[h].append(i)
            number_inputs.append(j)
            inputs_coordinatsX.append(x1 - 25)
            inputs_coordinatsY.append(y1 + deltaY)

            if (inputs_elements[i][j][0] != '#'):
                canvas.create_text(x1 - 20, y1 + deltaY - 10, text=inputs_elements[i][j])
            if (inputs_elements[i][j][0] == '#'):
                number = inputs_elements[i][j]
                number = number[1:]
            h = h + 1
            deltaY = deltaY + 30
            j = j + 1
        i = i + 1
        y_start = y2 + 50
        prev_layer = current_layer

    i = 0
    while i < len(inputs_elements):
        l = len(inputs_elements[i])
        count_inputs_len.append(l)
        i = i + 1
    print(count_inputs_len)
    print(number_inputs)


    i = 0
    while i < len(mlist):
        j = 0
        while j < len(inputs_elements[i]):
            if inputs_elements[i][j][0] == '#':
                temp = inputs_elements[i][j]
                first_element = int(temp[1:]) # НОМЕР ПЕРВОГО ЭЛЕМЕНТА
                second_element = i  # НОМЕР ВТОРОГО ЭЛЕМЕНТА
                numer_input_element = j  # НОМЕР ВХОДА ЭЛЕМЕНТА
                k = 0
                count1 = 0
                count2 = 0
                while k < len(count_inputs_len):
                    l = 0
                    while l < count_inputs_len[k]:
                        if (k == second_element) and (numer_input_element == number_inputs[count1]):
                            second_dotX = inputs_coordinatsX[count1]
                            second_dotY = inputs_coordinatsY[count1]
                            first_dotX = outputs_coordinatsX[first_element]
                            first_dotY = outputs_coordinatsY[first_element]
                            line = canvas.create_line(first_dotX, first_dotY, second_dotX, second_dotY, fill='black')
                            break
                        count1 = count1 + 1
                        count2 = count2 + 1
                        l = l + 1
                    k = k + 1
            j = j + 1
        i = i + 1

    root.mainloop()
