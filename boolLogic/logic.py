mlist = [[0,'*','1','0','1'],[0,'*','0','1','1'],[1,'*','#0','#1','0','1'],[2,'-','#2']]
mlist2 = [[0,'*','1','0','1'],[0,'*','0','1','1'],[1,'*','#0','#1','0','1'],[2,'-','#2']]
elements3 = []
elements_for_wire = []
elements = []
elements2 = []
elements_on_layers = []
layers = []
current_line = []
outputs = []
count_inputs = []
count_outputs = []
id_elements = []
output_elements = []
input_elements = []
outputs_coordinatsX = []
outputs_coordinatsY = []
inputs_coordinatsX = []
inputs_coordinatsY = []
number_inputs = []
number_outputs = []
input_variables = []

def layer_selection():
    check = False

    i = 0
    while i < len(mlist):
        elements.append(mlist[i])
        i = i + 1

    i = 0
    while i < len(mlist):
        layers[i] = elements[i][0]
        elements[i].pop(0)
        i = i + 1

    i = 0
    while i < len(mlist):
        outputs.append(mlist[i])
        i = i + 1

    i = 0
    while i < len(mlist):
        output_elements.append(mlist[i])
        i = i + 1

    i = 0
    while i < len(mlist):
        ch = False
        operation = elements[i][0]
        if (operation == '-'):
            j = 1
            k = j
            if elements[i][k][0] == '#':
                    id_elements = int(elements[i][k][1:])
                    elements[i][k] = output_elements[id_elements]
        else:
            j = 2
            k = j - 1
            while k < len(elements[i]):
                if elements[i][k][0] == '#':
                    temp = elements[i][k]
                    t = 0
                    while t < len(mlist):
                        r = 0
                        while r < len(elements[t]):
                            if elements[t][r] == temp:
                                id_elements = int(elements[t][r][1:])
                                elements[t][r] = str(output_elements[id_elements])
                            r = r + 1
                        t = t + 1
                k = k + 1

        if check == False:
            h = 0
            while h < len(mlist):
                output_elements[h] = elements[h][1]
                h = h + 1
                check = True

        x = 0
        while x < len(output_elements):
             if output_elements[x][0] == '#':
                id_elem = int(output_elements[x][1:])
                output_elements[x] = output_elements[id_elem]
             x = x + 1

        while j < len(elements[i]):
            if operation == '+':
                output_elements[i] = int(output_elements[i]) | int(elements[i][j])
            if operation == '*':
                output_elements[i] = int(output_elements[i]) & int(elements[i][j])
            if operation == '-':
                output_elements[i] = not int(elements[i][j])
                output_elements[i] = return_view(int(output_elements[i]))
            if operation == '^':
                output_elements[i] = int(output_elements[i]) ^ int(elements[i][j])
            if operation == '|':
                output_elements[i] = not (int(output_elements[i]) & int(elements[i][j]))
                output_elements[i] = return_view(int(output_elements[i]))
            if operation == '/':
                output_elements[i] = not (int(output_elements[i]) | int(elements[i][j]))
                output_elements[i] = return_view(int(output_elements[i]))
            if operation == 'i':
                output_elements[i] = (int(output_elements[i]) & int(elements[i][j])) | (
                    not int(output_elements[i]))
                output_elements[i] = return_view(int(output_elements[i]))
            j = j + 1

            y = 0
            while y < len(output_elements):
                output_elements[y] = str(output_elements[y])
                y = y + 1
        i = i + 1

def return_view(temp):
    if temp == False:
        temp = 0
    else:
        temp = 1
    return temp


i = 0
while i < len(mlist):
    layers.append(mlist[i])
    i = i + 1

'''i = 0
while i < len(mlist):
    a = []
    for j in mlist[i]:                 #ЗНАМЕНИТЫЙ КОСТЫЛЬ АНТОНА
        a.append(j)
    elements3.append(a)
    elements_for_wire.append(mlist[i])
    i = i + 1
i = 0
while i < len(elements3):
    elements3[i].pop(0)
    i = i + 1'''

layer_selection()
print("mlist2 = ", mlist2)
i = 0
while i < len(mlist2):
    elements_for_wire.append(mlist2[i])
    i = i + 1
print("output_elements = ",output_elements)

i = 0
while i < len(mlist):
    input_elements.append(mlist[i])
    i = i + 1

count_elements_all = len(mlist)
max_layers = 0
i = 0
while i < len(layers):
    if (layers[i] > max_layers):
        max_layers = layers[i]
    i = i + 1

i = 0
while i < len(mlist):
    count_inputs.append(0)
    i = i + 1

i = 0
while i < len(mlist):
    count_outputs.append(0)
    i = i + 1

i = 0
while i < len(mlist):
    j = 1
    while j < len(elements[i]):
        count_inputs[i] = count_inputs[i] + 1
        j = j + 1
    i = i + 1

i = 0
while i < len(mlist):
    j = 1
    while j < len(elements[i]):
        count_outputs[i] = count_outputs[i] + 1
        j = j + 1
    i = i + 1

i = max_layers
list_elements = []
while i >= 0:
    list_elements.append(-1)
    i = i - 1

if (max_layers == 0):
    list_elements[0] = layers.count(0)
else:
    i = 0
    while i <= max_layers:
        list_elements[i] = layers.count(i)
        i = i + 1

i = 0
while i < len(mlist):
    elements_for_wire[i].pop(0)
    elements_for_wire[i].pop(0)
    i = i + 1

print("elements_for_wire = ",elements_for_wire)
print("count_elements_all = ",count_elements_all)
print("max_layers = ",max_layers)
print("count_inputs = ", count_inputs)
print("count_outputs = ", count_outputs)
print("layers = ",layers)
print("list_elements = ", list_elements)





