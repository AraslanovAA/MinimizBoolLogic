import functools
import tkinter as tk
from tkinter.ttk import Combobox


root = tk.Tk()
root.state('zoomed')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
canvas_upload_image = tk.Canvas(root, width=screen_width, height=screen_height)
canvas_upload_image.place(x=0, y=0)

x_delete_coordinate = 0
y_delete_coordinate = 0

tp = []
equal_number_inputs = []
entry = {}
btn = {}
column = 0
coord_btnX = 0
coord_btnY = 100
names_btn = ['AND', 'OR', 'XOR', 'NOT', 'IMPL', 'AND-NOT', 'OR-NOT']
select_element = 'AND'
selection = False
count_inputs = 2
entry_input = {}
entry_output = {}
all_count_input = 0
all_count_output = 0
count_elements = 0
counter = 0
border = []
elements = []
block_areas = []
startX = []
add_element = False
names_inputs = []
names_outputs = []
coordinats_elements = []
cursor = True
selected_element = False
select_one = True
draw_elements = {}
mas_connect = []
connect_counter = 0
values_inputs = []
values_outputs = []
values_outputs_res = []
next_way = False
coordinats_output_line = []
names_inputs_temp = []
mlist = []




def change_combobox(event):
    global cursor
    global selection
    global select_element
    if combobox.get() == 'AND-OR-NOT':
        btnAND.config(state='normal')
        btnOR.config(state='normal')
        btnNOT.config(state='normal')
        btnXOR.config(state='disabled')
        btnANDNOT.config(state='disabled')
        btnORNOT.config(state='disabled')
        btnIMPL.config(state='disabled')
        select_element = 'AND'

    if combobox.get() == 'AND-NOT':
        btnAND.config(state='disabled')
        btnOR.config(state='disabled')
        btnNOT.config(state='disabled')
        btnXOR.config(state='disabled')
        btnANDNOT.config(state='normal')
        btnORNOT.config(state='disabled')
        btnIMPL.config(state='disabled')
        select_element = 'AND-NOT'

    if combobox.get() == 'OR-NOT':
        btnAND.config(state='disabled')
        btnOR.config(state='disabled')
        btnNOT.config(state='disabled')
        btnXOR.config(state='disabled')
        btnANDNOT.config(state='disabled')
        btnORNOT.config(state='normal')
        btnIMPL.config(state='disabled')
        select_element = 'OR-NOT'

    if combobox.get() == 'NOT-IMPL':
        btnAND.config(state='disabled')
        btnOR.config(state='disabled')
        btnNOT.config(state='normal')
        btnXOR.config(state='disabled')
        btnANDNOT.config(state='disabled')
        btnORNOT.config(state='disabled')
        btnIMPL.config(state='normal')
        select_element = 'NOT'

    if combobox.get() == 'XOR-IMPL':
        btnAND.config(state='disabled')
        btnOR.config(state='disabled')
        btnNOT.config(state='disabled')
        btnXOR.config(state='normal')
        btnANDNOT.config(state='disabled')
        btnORNOT.config(state='disabled')
        btnIMPL.config(state='normal')
        select_element = 'XOR'

    selection - False
    cursor - True


def return_view(temp):
    if temp == False:
        temp = 0
    else:
        temp = 1
    return temp

def emul():
    global oordinats_output_line
    global connect_counter
    global names_inputs
    global names_outputs
    global mas_connect
    global values_outputs
    global values_inputs
    global values_outputs_res
    global entry_output
    global next_way
    global names_inputs_temp

    goto_next = True
    tp.clear()
    names_inputs.clear()
    names_outputs.clear()
    mas_connect.clear()
    values_inputs.clear()
    values_outputs.clear()
    values_outputs_res.clear()
    connect_counter = 0

    i = 0
    while i < all_count_input:
        names_inputs.append(entry_input[i].get().upper())
        i = i + 1
    i = 0
    while i < all_count_input:
        if names_inputs[i] == '':
            info_build_lbl_input.config(text="    Введены не все имена входов")
            goto_next = False
        else:
            info_build_lbl_input.config(text="")
            goto_next = True
        i = i + 1
    names_outputs.clear()
    i = 0
    while i < all_count_output:
        names_outputs.append(entry_output[i].get().upper())
        i = i + 1
    i = 0
    while i < all_count_output:
        if names_outputs[i] == '':
            info_build_lbl_output.config(text="    Введены не все имена выходов")
            goto_next = False
        else:
            info_build_lbl_output.config(text="")
            goto_next = True
        i = i + 1
    # Проверка нет ли одинаковых имен выходов
    i = 0
    while i < len(names_outputs):
        current_name_output = names_outputs[i]
        j = 0
        while j < len(names_outputs):
            if (i != j):
                if ((current_name_output == names_outputs[j]) & (names_outputs[j] != '')):
                    info_build_lbl_output.config(text="    Имена выходов повторяются")
                    goto_next = False
                    break
            j = j + 1
        i = i + 1
    # Проверка AA != (AA0 or AA1)



    # Проверка AA0 and AA1
    b = 0
    c = 0
    while b < len(names_inputs):
        string = names_inputs[b][2:]
        string2 = names_inputs[b][:2]
        if (string == '1') | (string == '0'):
            values_inputs.append([])
            values_inputs[c].append(names_inputs[b])
            values_inputs[c].append(string2)
            values_inputs[c].append(string)
            c = c + 1
        b = b + 1
    print("values_inputs", values_inputs)

    i = 0
    while i < len(values_inputs):
        j = 0
        while j < len(values_inputs):
            if (i != j):
                if (values_inputs[i][1] == values_inputs[j][1]):
                    if (values_inputs[i][2] != values_inputs[j][2]):
                        print("фиаско, они не равны")
                        goto_next = False
                        break
            j = j + 1
        i = i + 1


    if goto_next == True:
        i = 0
        while i < len(names_inputs):
            j = 0
            while j < len(names_outputs):
                if names_inputs[i] == names_outputs[j]:
                    mas_connect.append([])
                    mas_connect[connect_counter].append(i)
                    mas_connect[connect_counter].append(j)
                    connect_counter = connect_counter + 1
                j = j + 1
            i = i + 1
        print("names_inputs ", names_inputs)
        print("names_outputs ", names_outputs)
        print("mas_connect = ", mas_connect)
        i = 0
        k = 0
        y = 0
        x = 0
        while x < len(elements):
            tp.append([])
            p = 0
            while p < elements[x][1]:
                string = names_inputs[y][2:]
                if (string == '1') | (string == '0'):
                    tp[x].append(1)
                else:
                    tp[x].append(0)
                y = y + 1
                p = p + 1
            x = x + 1

        while i < len(elements):
            values_outputs.append([])
            j = 0
            sum = 0
            n = 0
            while n < len(tp[i]):
                sum = sum + tp[i][n]
                n = n + 1
            if sum == elements[i][1]:
                while j < elements[i][1]:
                    string = names_inputs[k][2:]
                    if (string == '1') | (string == '0'):
                        if elements[i][0] == 'AND':
                            if j == 0:
                                operand1 = int(string)
                            else:
                                operand2 = int(string)
                                result = operand1 & operand2
                                operand1 = result
                                values_outputs[i].append(result)
                        if elements[i][0] == 'OR':
                            if j == 0:
                                operand1 = int(string)
                            else:
                                operand2 = int(string)
                                result = operand1 | operand2
                                operand1 = result
                                values_outputs[i].append(result)
                        if elements[i][0] == 'NOT':
                            operand1 = int(string)
                            result = not operand1
                            result = return_view(result)
                            values_outputs[i].append(result)
                        if elements[i][0] == 'XOR':
                            if j == 0:
                                operand1 = int(string)
                            else:
                                operand2 = int(string)
                                result = operand1 ^ operand2
                                operand1 = result
                                values_outputs[i].append(result)
                        if elements[i][0] == 'AND-NOT':
                            if j == 0:
                                operand1 = int(string)
                            else:
                                operand2 = int(string)
                                result = not (operand1 & operand2)
                                operand1 = result
                                result = return_view(result)
                                values_outputs[i].append(result)
                        if elements[i][0] == 'OR-NOT':
                            if j == 0:
                                operand1 = int(string)
                            else:
                                operand2 = int(string)
                                result = not (operand1 | operand2)
                                operand1 = result
                                result = return_view(result)
                                values_outputs[i].append(result)
                        if elements[i][0] == 'IMPL':
                            if j == 0:
                                operand1 = int(string)
                            else:
                                operand2 = int(string)
                                result = (operand1 & operand2) | (not operand1)
                                operand1 = result
                                result = return_view(result)
                                values_outputs[i].append(result)
                    else:
                        break
                    k = k + 1
                    j = j + 1
            else:
                k = k + elements[i][1]
                values_outputs[i].append(-1)
            i = i + 1
        i = 0
        while i < len(values_outputs):
            temp = len(values_outputs[i]) - 1
            values_outputs_res.append(values_outputs[i][temp])
            i = i + 1

        i = 0
        while i < len(values_outputs_res):
            if values_outputs_res[i] != -1:
                names_outputs[i] = names_outputs[i] + str(values_outputs_res[i])
                next_way = True
            i = i + 1

        i = 0
        while i < all_count_output:
            if values_outputs_res[i] != -1:
                string = values_outputs_res[i]
                canvas.create_rectangle(coordinats_output_line[i][0] + 10, coordinats_output_line[i][1] - 45,
                                        coordinats_output_line[i][0] + 20, coordinats_output_line[i][1] - 15,
                                        fill='white', outline='white')
                if string == 0:
                    canvas.create_text(coordinats_output_line[i][0] + 15, coordinats_output_line[i][1] - 30, text=string,
                                       fill='red')
                if string == 1:
                    canvas.create_text(coordinats_output_line[i][0] + 15, coordinats_output_line[i][1] - 30, text=string,
                                       fill='green')
            i = i + 1

        i = 0
        while i < len(names_inputs):
            j = 0
            while j < len(names_outputs):
                if len(names_inputs[i]) == 2:
                    if names_inputs[i] == names_outputs[j][:-1]:
                        if values_outputs_res[j] != -1:
                            names_inputs[i] = names_inputs[i] + str(values_outputs_res[j])
                            entry_input[i].delete(0, tk.END)
                            entry_input[i].insert(0, names_inputs[i].lower())
                            string = values_outputs_res[j]
                            if string == 0:
                                canvas.create_text(coordinats_output_line[j][0] + 15, coordinats_output_line[j][1] - 30,
                                                   text=string, fill='red')
                            if string == 1:
                                canvas.create_text(coordinats_output_line[j][0] + 15, coordinats_output_line[j][1] - 30,
                                                   text=string, fill='green')
                j = j + 1
            i = i + 1

        print("values_outputs = ", values_outputs)
        print("values_outputs_res = ", values_outputs_res)


def read_entry(event):
    l = len(elements)
    i = 0
    while (i < l):
        emul()
        i = i + 1
    print("len(elements) = ", l)

def read_entry2(event):
        emul()



def check_table(event):
    global names_inputs
    global names_outputs
    j = 0
    while (j < len(mlist)):
        mlist.clear()
        j = j + 1
    i = 0
    while (i < len(elements)):
        mlist.append([])
        mlist[i].append(elements[i][0])

        i = i + 1
    print(mlist)
    print(names_inputs)
    print(names_outputs)


def select_default(event):
    global selection
    global cursor
    cursor = True
    selection = False


def delete_element(event):
    global x_delete_coordinate
    global y_delete_coordinate
    global selection
    global cursor
    global counter
    global coordinats_elements
    global elements
    if len(elements) != 0:
        if (selection == False) & (cursor == True):
            # удалить визально и удалить все связи, следующие из удаляемого элемента
            i = 0
            x = x_delete_coordinate
            y = y_delete_coordinate

            if ((x != 0) & (y != 0)):
                while i < counter:
                    if ((x > coordinats_elements[i][0]) & (y > coordinats_elements[i][1]) & (
                            x < coordinats_elements[i][2]) & (y < coordinats_elements[i][3])):
                        entry_output[i].destroy()
                        k = elements[i][1]
                        j = equal_number_inputs[i][1]
                        l = 0
                        h = 0
                        while h < len(block_areas):
                            if ((block_areas[h][0] < x) & (block_areas[h][1] < y) & (block_areas[h][2] > x) & (block_areas[h][3] > y)):
                                canvas.create_rectangle(coordinats_elements[h][0]-25, coordinats_elements[h][1], coordinats_elements[h][2]+29, coordinats_elements[h][3], fill='white', outline='white')
                                block_areas[h].clear()
                                block_areas.remove([])
                                break
                            h = h + 1
                        while (l < k):
                            entry_input[j].destroy()
                            l = l + 1
                            j = j + 1
                    i = i + 1
    print(block_areas)



def on_entry_input_count_click(event):
    if len(entry_count_input.get()) > 0:
        st1 = entry_count_input.get()
        st1 = st1[:-1]
        entry_count_input.delete(0, tk.END)
        entry_count_input.insert(0, st1)
        if (entry_count_input.get() == ''):
            print("пустая строка")
        else:
            print("отслеживает")


def on_entry_input_click(event, param):
    if len(entry_input[param].get()) >= 3:
        st = entry_input[param].get()
        st = st[:-3]
        entry_input[param].delete(0, tk.END)
        entry_input[param].insert(0, st)


def on_entry_output_click(event, param):
    if len(entry_output[param].get()) >= 3:
        st = entry_output[param].get()
        st = st[:-3]
        entry_output[param].delete(0, tk.END)
        entry_output[param].insert(0, st)


def select_element(event, param):
    global select_element
    global selection
    global count_inputs
    selection = True
    if param == 0:
        select_element = 'AND'
    if param == 1:
        select_element = 'OR'
    if param == 2:
        select_element = 'NOT'
    if param == 3:
        select_element = 'XOR'
    if param == 4:
        select_element = 'AND-NOT'
    if param == 5:
        select_element = 'OR-NOT'
    if param == 6:
        select_element = 'IMPL'


def click_on_canvas(event, param1, param2):
    global coordinats_output_line
    global all_count_output
    global counter
    global count_elements
    global my_variable
    global select_element
    global all_count_input
    global width
    global height
    global count_inputs
    global equal_number_inputs
    global add_element
    global selected_element
    global x_delete_coordinate
    global y_delete_coordinate
    if (selection == False) & (cursor == True):
        count_inputs = int(entry_count_input.get())
        getx = canvas.canvasx(event.x)
        gety = canvas.canvasy(event.y)
        if selected_element == False:
            i = 0
            if len(coordinats_elements) != 0:
                while i < len(coordinats_elements):
                    if ((coordinats_elements[i][0] < getx) & (coordinats_elements[i][1] < gety) & (
                            coordinats_elements[i][2] > getx) & (
                            coordinats_elements[i][3] > gety)):
                        canvas.itemconfig(draw_elements[i], fill='green', outline='green')
                        x_delete_coordinate = canvas.canvasx(event.x)
                        y_delete_coordinate = canvas.canvasy(event.y)
                        selected_element = True
                    i = i + 1
        else:
            i = 0
            if len(coordinats_elements) != 0:
                while i < len(coordinats_elements):
                    if ((coordinats_elements[i][0] < getx) & (coordinats_elements[i][1] < gety) & (
                            coordinats_elements[i][2] > getx) & (
                            coordinats_elements[i][3] > gety)):
                        canvas.itemconfig(draw_elements[i], fill='white', outline='black')
                        x_delete_coordinate = 0
                        y_delete_coordinate = 0
                        selected_element = False
                    i = i + 1
    if selection == True:
        bool = False
        entry_count_input.update()
        count_inputs = int(entry_count_input.get())
        getx = canvas.canvasx(event.x)
        gety = canvas.canvasy(event.y)
        if gety < 103:
            bool = True
        else:
            if (getx < 98) | (getx > screen_width - 300):
                bool = True
            xt = 98
            j = 0
            while j < screen_width - 230:
                k = 0
                while k < 5:
                    if getx == xt + k:
                        bool = True
                    k = k + 1
                xt = xt + 110
                j = j + 1
        if bool == False:
            count_elements = count_elements + 1
            deltaX = 50
            deltaY = 25 * (count_inputs + 1)
            k = 0
            minX_which_less = 0
            while k < len(border):
                if getx < border[k]:
                    minX_which_less = border[k] - 110
                    break
                k = k + 1
            blocking = False
            ch = gety
            while ch < 10 + deltaY + gety:
                if blocking == False:
                    h = 0
                    check = False
                    if len(block_areas) != 0:
                        while h < len(block_areas):
                            if ((block_areas[h][0] < getx) & (block_areas[h][1] < ch) & (block_areas[h][2] > getx) & (
                                    block_areas[h][3] > ch)):
                                blocking = True
                                add_element = False
                                check = True
                            h = h + 1
                    else:
                        block_areas.append([])
                        if count_inputs == 1:
                            ks = 55
                        if count_inputs == 2:
                            ks = 90
                        if count_inputs == 3:
                            ks = 110
                        if count_inputs == 4:
                            ks = 130
                        if count_inputs == 5:
                            ks = 160
                        if count_inputs == 6:
                            ks = 190
                        if count_inputs == 7:
                            ks = 220
                        if count_inputs == 8:
                            ks = 240
                        block_areas[counter].append(minX_which_less)
                        block_areas[counter].append(ch - ks)
                        block_areas[counter].append(minX_which_less + 110)
                        block_areas[counter].append(ch + ks)
                        check = True
                        add_element = True
                    if check == False:
                        block_areas.append([])
                        if count_inputs == 1:
                            ks = 55
                        if count_inputs == 2:
                            ks = 90
                        if count_inputs == 3:
                            ks = 110
                        if count_inputs == 4:
                            ks = 130
                        if count_inputs == 5:
                            ks = 160
                        if count_inputs == 6:
                            ks = 190
                        if count_inputs == 7:
                            ks = 220
                        if count_inputs == 8:
                            ks = 240
                        block_areas[counter].append(minX_which_less)
                        block_areas[counter].append(ch - ks)
                        block_areas[counter].append(minX_which_less + 110)
                        block_areas[counter].append(ch + ks)
                        add_element = True
                    if add_element == True:
                        t = 0
                        while t < len(border):
                            if getx < border[t + 1]:
                                getx = startX[t]
                                break
                            t = t + 1
                        #сanvas.create_rectangle(minX_which_less, ch - 10, minX_which_less + 110, ch + deltaY + 10, outline='black')
                        draw_elements[counter] = canvas.create_rectangle(getx, ch, getx + deltaX, ch + deltaY,
                                                                         outline="black")
                        coordinats_elements.append([])
                        coordinats_elements[counter].append(getx)
                        coordinats_elements[counter].append(ch)
                        coordinats_elements[counter].append(getx + deltaX)
                        coordinats_elements[counter].append(ch + deltaY)
                        canvas.create_line(getx + 50, ch + deltaY / 2 + 1, getx + 80, ch + deltaY / 2 + 1,
                                           fill="black")
                        coordinats_output_line.append([])
                        coordinats_output_line[counter].append(getx + 50)
                        coordinats_output_line[counter].append(ch + deltaY / 2 + 1)
                        entry_output[all_count_output] = tk.Entry(root, bg="white", fg="black")
                        entry_output[all_count_output].bind('<Key>',
                                                            functools.partial(on_entry_output_click,
                                                                              param=all_count_output))
                        entry_output[all_count_output].place(x=getx + 255, y=ch + deltaY / 2 + 1 + 30, width=23,
                                                             height=20)
                        all_count_output = all_count_output + 1
                        i = 0
                        x = getx
                        y = ch
                        canvas.create_text(getx + 25, ch + 25, text=select_element, fill="black")
                        canvas.create_text(getx + 25, ch + 50, text=counter, fill="black")
                        elements.append([])
                        elements[counter].append(select_element)
                        elements[counter].append(count_inputs)
                        elements[counter].append(counter)
                        equal_number_inputs.append([])
                        equal_number_inputs[counter].append(counter)
                        equal_number_inputs[counter].append(all_count_input)
                        counter = counter + 1
                        # print("elements", elements)





                        while i < count_inputs:
                            canvas.create_line(x - 25, y + 25, x, y + 25, fill="black")
                            entry_input[all_count_input] = tk.Entry(root, bg="white", fg="black")
                            entry_input[all_count_input].config(text='')
                            entry_input[all_count_input].bind('<Key>',
                                                              functools.partial(on_entry_input_click,
                                                                                param=all_count_input))
                            entry_input[all_count_input].place(x=178 + x, y=y + 55, width=23, height=20)
                            all_count_input = all_count_input + 1
                            y = y + 25
                            i = i + 1
                        # print(block_areas)
                ch = ch + 1


coord_btnY = 0
coord_btnX = 400
'''i = 0
while i < 7:
    btn[i] = tk.Button(root, text=names_btn[i])
    btn[i].bind('<Button-1>', functools.partial(select_element, param=i))
    btn[i].bind('<Button-3>', functools.partial(select_element, param=i))
    btn[i].place(x=coord_btnX, y=coord_btnY)
    coord_btnX = coord_btnX + 70
    i = i + 1'''

btnAND = tk.Button(root, text='AND', bg='white', fg='black')
btnAND.place(x=10, y=100)
btnAND.config(width=7, height=4)
btnAND.bind('<Button-1>', functools.partial(select_element, param=0))

btnOR = tk.Button(root, text='OR', bg='white', fg='black')
btnOR.place(x=70, y=100)
btnOR.config(width=7, height=4)
btnOR.bind('<Button-1>', functools.partial(select_element, param=1))

btnNOT = tk.Button(root, text='NOT', bg='white', fg='black')
btnNOT.place(x=130, y=100)
btnNOT.config(width=7, height=4)
btnNOT.bind('<Button-1>', functools.partial(select_element, param=2))

btnXOR = tk.Button(root, text='XOR', bg='white', fg='black')
btnXOR.place(x=10, y=180)
btnXOR.config(width=7, height=4)
btnXOR.bind('<Button-1>', functools.partial(select_element, param=3))
btnXOR.config(state='disabled')

btnANDNOT = tk.Button(root, text='AND-NOT', bg='white', fg='black')
btnANDNOT.place(x=70, y=180)
btnANDNOT.config(width=7, height=4)
btnANDNOT.bind('<Button-1>', functools.partial(select_element, param=4))
btnANDNOT.config(state='disabled')

btnORNOT = tk.Button(root, text='OR-NOT', bg='white', fg='black')
btnORNOT.place(x=130, y=180)
btnORNOT.config(width=7, height=4)
btnORNOT.bind('<Button-1>', functools.partial(select_element, param=5))
btnORNOT.config(state='disabled')

btnIMPL = tk.Button(root, text='IMPL', bg='white', fg='black')
btnIMPL.place(x=10, y=260)
btnIMPL.config(width=7, height=4)
btnIMPL.bind('<Button-1>', functools.partial(select_element, param=6))
btnIMPL.config(state='disabled')

combobox = Combobox(root, values=[u"AND-OR-NOT", u"AND-NOT", u"OR-NOT", u"NOT-IMPL", u"XOR-IMPL"],
                    height=3, state='readonly')
combobox.bind("<<ComboboxSelected>>", functools.partial(change_combobox))
combobox.set(u"AND-OR-NOT")
combobox.place(x=10, y=10)

canvas = tk.Canvas(root, bg='white', width=screen_width, height=screen_height,
                   scrollregion=(0, 0, screen_width, screen_height))
# hbar=tk.Scrollbar(root, orient=tk.HORIZONTAL)
# hbar.pack(side=tk.BOTTOM,fill=tk.X)
# hbar.config(command=canvas.xview)
vbar = tk.Scrollbar(root, orient=tk.VERTICAL)
vbar.pack(side=tk.RIGHT, fill=tk.Y)
vbar.config(command=canvas.yview)
canvas.config(width=screen_width, height=screen_height)
# canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.place(x=200, y=50)
canvas.bind('<Button-1>', functools.partial(click_on_canvas, param1=selection, param2=select_element))

entry_count_input = tk.Entry(root, width=1, font="Helvetica 18 bold")
entry_count_input.bind('<Key>', functools.partial(on_entry_input_count_click))
entry_count_input.place(x=175, y=500)
entry_count_input.insert(tk.END, '2')
entry_count_input.update()

i = 0
x1 = 100
y1 = 100
y2 = screen_height
canvas.create_line(98, 100, screen_width - 223, 100, fill="black", width=5)
while i < screen_width - 230:
    canvas.create_line(x1, y1, x1, y2, fill="black", width=5)
    border.append(x1)
    x1 = x1 + 110
    i = i + 110

i = 0
xs = 128
while i < len(border):
    startX.append(xs)
    xs = xs + 110
    i = i + 1
# print(startX)
# print(border)

info_build_lbl_input = tk.Label(root, text="")
info_build_lbl_input.config(fg="red")
info_build_lbl_input.place(x=-10, y=700)

info_build_lbl_output = tk.Label(root, text="")
info_build_lbl_output.config(fg="red")
info_build_lbl_output.place(x=-10, y=750)


btn_def = tk.Button(root, text="Курсор", width=11, height=3, bg='white', fg='black')
btn_def.place(x=10, y=560)
btn_def.bind('<Button-1>', select_default)
btn_build = tk.Button(root, text="Шаг", width=11, height=3, bg='white', fg='black')
btn_build.bind('<Button-1>', read_entry2)
btn_build.place(x=105, y=560)

btn_build = tk.Button(root, text="Эмуляция", width=11, height=3, bg='white', fg='black')
btn_build.bind('<Button-1>', read_entry)
btn_build.place(x=105, y=630)

lbl_count_input = tk.Label(root, text="Число входов:", font='Arial 18', bg='white', fg='black')
lbl_count_input.place(x=5, y=500)
root.bind('<Return>', delete_element)
lbl_canon = tk.Label(root, text='уравнение', fg='black', bg='white', font='Arial 20')
lbl_canon.place(x=screen_width / 2, y=80)

btn_check_table = tk.Button(root, text="Проверить", width=11, height=3, bg='white', fg='black')
btn_check_table.place(x=10, y=630)
btn_check_table.bind('<Button-1>', check_table)

root.mainloop()
