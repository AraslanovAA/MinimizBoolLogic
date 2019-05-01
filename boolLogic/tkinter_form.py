import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import logic

class AutoScrollbar(ttk.Scrollbar):
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
            ttk.Scrollbar.set(self, lo, hi)

    def pack(self, **kw):
        raise tk.TclError('Cannot use pack with this widget')

    def place(self, **kw):
        raise tk.TclError('Cannot use place with this widget')


class Zoom_Advanced(ttk.Frame):
    def __init__(self, mainframe, path):
        ttk.Frame.__init__(self, master=mainframe)
        self.master.title('попытка сделать курсач')
        vbar = AutoScrollbar(self.master, orient='vertical')
        hbar = AutoScrollbar(self.master, orient='horizontal')
        vbar.grid(row=0, column=1, sticky='ns')
        hbar.grid(row=1, column=0, sticky='we')
        self.canvas = tk.Canvas(self.master, highlightthickness=0,
                                xscrollcommand=hbar.set, yscrollcommand=vbar.set, bg='white')
        self.canvas.grid(row=0, column=0, sticky='nswe')
        self.canvas.update()
        vbar.configure(command=self.scroll_y)
        hbar.configure(command=self.scroll_x)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.canvas.bind('<Configure>', self.show_image)
        self.canvas.bind('<ButtonPress-1>', self.move_from)
        self.canvas.bind('<B1-Motion>', self.move_to)
        self.canvas.bind('<MouseWheel>', self.wheel)
        self.canvas.bind('<Button-5>', self.wheel)
        self.canvas.bind('<Button-4>', self.wheel)
        self.image = Image.open(path)
        self.width, self.height = self.image.size
        self.imscale = 1.0
        self.delta = 1.2

        dx = 50
        current_x = 75
        maxY = 0
        elements_on_layer = []
        temp_layer = 0
        i = 0
        inversion = False
        while i < len(logic.mlist):
            if (logic.elements[i][0] == temp_layer):
                elements_on_layer.append(logic.elements[i])
            i = i + 1
        j = 0
        k = 0
        t = 0
        i1 = 0
        i2 = 0
        operation = ''
        while j <= logic.max_layers:
            beginX = 85
            beginY = 50
            i = 0
            while i < logic.list_elements[j]:

                if logic.elements[t][0] == '+':
                    operation = ' 1'

                if logic.elements[t][0] == '*':
                    operation = ' &'

                if logic.elements[t][0] == '-':
                    operation = ' 1'
                    inversion = True

                if logic.elements[t][0] == '^':
                    operation = '=1'

                if logic.elements[t][0] == '|':
                    operation = ' &'
                    inversion = True

                if logic.elements[t][0] == '/':
                    operation = ' 1'
                    inversion = True

                if logic.elements[t][0] == 'i':
                    operation = ' >'

                size_element = logic.count_inputs[k] * 15 + 15
                self.canvas.create_rectangle(beginX + logic.layers[k] * 100, beginY,
                                            beginX + logic.layers[k] * 100 + 30, beginY + size_element, outline='black', width="2")

                self.canvas.create_text(beginX + logic.layers[k] * 100 + 10, beginY + 10, text=operation, fill="black",width="2") # операция
                beginY = beginY + size_element + 20
                if beginY > maxY:
                    maxY = beginY
                self.canvas.create_line(beginX + logic.layers[k] * 100 + 30, beginY - 20 - size_element / 2,
                                        beginX + logic.layers[k] * 100 + 30 + 10, beginY - 20 - size_element / 2, fill="black",width="2")

                logic.outputs_coordinatsX.append(beginX + logic.layers[k] * 100 + 30 + 10)
                logic.outputs_coordinatsY.append(beginY - 20 - size_element / 2)

                if inversion:
                    self.canvas.create_oval(beginX + logic.layers[k] * 100 + 30 - 5,
                                            beginY - 20 - size_element / 2 + 1 - 5,
                                            beginX + logic.layers[k] * 100 + 30 + 5,
                                            beginY - 20 - size_element / 2 + 1 + 5, fill="white",outline='black')
                    inversion = False
                operand_output = logic.output_elements[i1]
                line2 = self.canvas.create_text(beginX + logic.layers[k] * 100 + 36, beginY - 30 - size_element / 2,
                                        text=operand_output, fill="black",width="2")
                if operand_output == '0':
                    self.canvas.itemconfig(line2, fill='red')
                if operand_output == '1':
                    self.canvas.itemconfig(line2, fill='green')
                l = 0
                Y = beginY
                c = 1

                while c < len(logic.elements[i2]):
                    while l < logic.count_inputs[k]:
                        operand_input = logic.elements[i2][c]
                        line1 =self.canvas.create_text(beginX + logic.layers[k] * 100 - 5, Y - size_element - 12, text = operand_input, fill="black", width="2")
                        if operand_input == '0':
                            self.canvas.itemconfig(line1, fill='red')
                        if operand_input == '1':
                            self.canvas.itemconfig(line1, fill='green')

                        self.canvas.create_line(beginX + logic.layers[k] * 100, Y - size_element - 5,
                                                beginX + logic.layers[k] * 100 - 10, Y - size_element - 5, fill="black",width="2")

                        logic.number_inputs.append(l)
                        logic.number_outputs.append(-1)
                        logic.inputs_coordinatsX.append(beginX + logic.layers[k] * 100 - 10)
                        logic.inputs_coordinatsY.append(Y - size_element - 5)

                        Y = Y + 15
                        l = l + 1
                        c = c + 1
                t = t + 1
                i = i + 1
                k = k + 1
                i1 = i1 + 1
                i2 = i2 + 1
            j = j + 1
        i = 0
        line = 0
        while i < len(logic.mlist2):
            j = 0
            while j < len(logic.elements_for_wire[i]):
                if logic.elements_for_wire[i][j][0] == '#':
                    temp = logic.elements_for_wire[i][j]
                    first_element = int(temp[1:])
                    second_element = i
                    numer_input_element = j
                    k = 0
                    count1 = 0
                    count2 = 0
                    while k < len(logic.count_inputs):
                        l = 0
                        while l < logic.count_inputs[k]:
                            if (k == second_element) and (numer_input_element == logic.number_inputs[count1]):
                                second_dotX = logic.inputs_coordinatsX[count1]
                                second_dotY = logic.inputs_coordinatsY[count1]

                                #first_dotX = logic.outputs_coordinatsX[count2]
                                #first_dotY = logic.outputs_coordinatsY[count2]

                                first_dotX = logic.outputs_coordinatsX[first_element]
                                first_dotY = logic.outputs_coordinatsY[first_element]


                                line = self.canvas.create_line(first_dotX, first_dotY, second_dotX, second_dotY,fill='black')

                                #oval = self.canvas.create_oval(first_dotX,first_dotY, first_dotX, first_dotY)
                                #hdc = win32gui.GetWindowDC(win32gui.GetDesktopWindow())
                                #c = int(win32gui.GetPixel(hdc, round(first_dotX), round(first_dotY)))
                                #r = win32con.GetRValue(c);
                                #g = win32con.GetGValue(c);
                                #b = win32con.GetBValue(c);
                                #print(r,g,b)
                                break
                            count1 = count1 + 1
                            count2 = count2 + 1
                            l = l + 1
                        k = k + 1
                j = j + 1
            i = i + 1

        #self.canvas.create_line(0, 0, logic.max_layers * 100 + 176, 0, fill="yellow", width="6")
       #self.canvas.create_line(0, maxY, logic.max_layers * 100 + 176, maxY, fill="yellow", width="6")


        self.canvas.create_rectangle(0,0,logic.max_layers * 100 + 176,maxY+100,outline="gray", width="6")


        #while current_x < 126 + logic.max_layers * 100:
           # self.canvas.create_line(current_x, 0, current_x, maxY+100, fill="#1A243B")
           # current_x = current_x + dx

        print("number_inputs = ", logic.number_inputs)
        print("number_outputs = ", logic.number_outputs)
        print("outputs_coordinatsX = ",logic.outputs_coordinatsX)
        print("outputs_coordinatsY = ", logic.outputs_coordinatsY)
        print("inputs_coordinatsX = ", logic.inputs_coordinatsX)
        print("inputs_coordinatsY = ", logic.inputs_coordinatsY)
        print("output_elements = ", logic.output_elements)
        print('number_inputs', logic.number_inputs)

        self.container = self.canvas.create_rectangle(0, 0, 500, 500, width=0)


        self.show_image()
        function = 'A V B ^ C'
        temp = str(logic.output_elements[len(logic.output_elements)-1])
        temp2 = "F = "+temp
        self.canvas.create_text(logic.layers[0]+100,maxY,text=temp2)



    def scroll_y(self, *args, **kwargs):
        self.canvas.yview(*args, **kwargs)
        self.show_image()

    def scroll_x(self, *args, **kwargs):
        self.canvas.xview(*args, **kwargs)
        self.show_image()

    def move_from(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def move_to(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.show_image()

    def wheel(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        bbox = self.canvas.bbox(self.container)  # get image area
        if bbox[0] < x < bbox[2] and bbox[1] < y < bbox[3]:
            pass
        else:
            return
        scale = 1.0
        if event.num == 5 or event.delta == -120:
            i = min(self.width, self.height)
            if int(i * self.imscale) < 600: return
            self.imscale /= self.delta
            scale /= self.delta
        if event.num == 4 or event.delta == 120:
            i = min(self.canvas.winfo_width(), self.canvas.winfo_height())
            if i < self.imscale: return
            self.imscale *= self.delta
            scale *= self.delta
        self.canvas.scale('all', x, y, scale, scale)
        self.show_image()

    def show_image(self, event=None):
        bbox1 = self.canvas.bbox(self.container)
        bbox1 = (bbox1[0] + 1, bbox1[1] + 1, bbox1[2] - 1, bbox1[3] - 1)
        bbox2 = (self.canvas.canvasx(0),
                 self.canvas.canvasy(0),
                 self.canvas.canvasx(self.canvas.winfo_width()),
                 self.canvas.canvasy(self.canvas.winfo_height()))
        bbox = [min(bbox1[0], bbox2[0]), min(bbox1[1], bbox2[1]),
                max(bbox1[2], bbox2[2]), max(bbox1[3], bbox2[3])]
        if bbox[0] == bbox2[0] and bbox[2] == bbox2[2]:
            bbox[0] = bbox1[0]
            bbox[2] = bbox1[2]
        if bbox[1] == bbox2[1] and bbox[3] == bbox2[3]:
            bbox[1] = bbox1[1]
            bbox[3] = bbox1[3]
        self.canvas.configure(scrollregion=bbox)
        x1 = max(bbox2[0] - bbox1[0], 0)
        y1 = max(bbox2[1] - bbox1[1], 0)
        x2 = min(bbox2[2], bbox1[2]) - bbox1[0]
        y2 = min(bbox2[3], bbox1[3]) - bbox1[1]
        if int(x2 - x1) > 0 and int(y2 - y1) > 0:
            x = min(int(x2 / self.imscale), self.width)
            y = min(int(y2 / self.imscale), self.height)
            image = self.image.crop((int(x1 / self.imscale), int(y1 / self.imscale), x, y))
            imagetk = ImageTk.PhotoImage(image.resize((int(x2 - x1), int(y2 - y1))))
            imageid = self.canvas.create_image(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]),
                                               anchor='nw', image=imagetk)
            self.canvas.lower(imageid)
            self.canvas.imagetk = imagetk


#path = 'back_ground.jpg'
path = 'back_white.jpg'
root = tk.Tk()
root.state('zoomed')
app = Zoom_Advanced(root, path=path)

root.mainloop()
