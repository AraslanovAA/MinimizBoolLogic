
global OpNames#список с именами параметров
OpNames = []
def recognizeOperands(letter,Func,Sygnal,N=4):
    #N - ограничение на количесвто символов имени параметра
    i = 0
    name  =Func[letter]
    endrecognize = False
    while((endrecognize == False) and (i < N)):
        i+=1
        letter+=1
        if (letter < len(Func)):
            if Func[letter] in Sygnal:
                endrecognize = True#хмм
                flag = False
                for k in OpNames:#если такого имени в списке нет, добавляем
                    if k == name:
                        flag = True
                if flag == False:
                    OpNames.append(name)
                return letter-1
            else:
                name = name + Func[letter]
        else:
            endrecognize= True
            flag = False
            for k in OpNames:  # если такого имени в списке нет, добавляем
                if k == name:
                    flag = True
            if flag == False:
                OpNames.append(name)
            return letter - 1#тут конец обработки функции в принципе
    if (i == N):
        print("превышено допустимое количесвто символов в имени параметра: " + str(letter+1-i))# todo:передать сообщение на экран
        return -1


'''
существование полных форм записей и коротких:
внимание: операнды чувствительны к регистру
разрешается использование следующих логических операторов:
not	:	'-'
or	:	'+'
and	:	'*'
xor	:	'%'
sheff	:	'|'
pirs	:	'/'
imp	:	'#' наверно чуть логичнее было бы импользовать > ?'''
#короткие имена разрешено писать слитно, имспользуя длинные имена необходимо ставить пробелы
def vocabulary(Func):
    ShortNames ={
        'not': '-',
        'or': '+',
        'and': '*',
        'xor': '%',
        'sheff': '|',
        'pirs' : '/',
        'imp' : '#'
    }
    LFunc =[]
    LFunc = list(Func)
    for i in LFunc:
        if i == '(':
            i = ' ( '
        if i == ')':
            i =' ) '
    Func = ""  # собираем строку обратно
    for Item in LFunc:
        Func = Func + Item
    LFunc.clear()
    LFunc = Func.split(' ')
    print(LFunc)
    while '' in LFunc:
        LFunc.pop(LFunc.index(''))
    for ItemIndex in range(len(LFunc)):#заменяем длинные имена на короткие
        if LFunc[ItemIndex] in ShortNames:
            LFunc[ItemIndex] = ShortNames[LFunc[ItemIndex]]

    print(LFunc)
    Func =""#собираем строку обратно
    for Item in LFunc:
        Func = Func + Item

    letter =0
    L = len(Func)
    X='X0'
    openskobka = 0
    recognized = False
    # пиздец сука говнокод нахуй switch case бы блять
    Sygnal = {
        '-': 1,
        '(': 2,
        ')': 3,
        '+': 4,
        '*': 5,
        '%': 6,  # xor
        '|': 7,
        '/': 8,
        '#': 9  # импликация
    }
    while(letter < L):
        recognized = False
        if ((X == 'X0') and (recognized == False)):
            recognized = True
            if Func[letter] in Sygnal:
                if (Sygnal[Func[letter]] == 1):
                    X = 'X1'
                else:
                    if(Sygnal[Func[letter]] == 2):
                        X = 'X2'
                    else:
                        print('некорректное выражение, символ: ' + str(letter+1))# todo:передать сообщение на экран
                        return -1
            else:
                X='X3'

        if ((X == 'X1') and (recognized == False)):
            recognized = True
            if Func[letter] in Sygnal:
                if (Sygnal[Func[letter]] == 2):
                    X='X2'
                else:
                    print('некорректное выражение, символ: ' + str(letter + 1))# todo:передать сообщение на экран
                    return -1
            else:
                X='X3'
        if ((X == 'X2') and (recognized == False)):
            recognized = True
            if Func[letter] in Sygnal:
                if (Sygnal[Func[letter]] == 1):
                    X='X1'
                else:
                    if (Sygnal[Func[letter]] == 2):
                        X = 'X2'
                    else:
                        print('некорректное выражение, символ: ' + str(letter + 1))# todo:передать сообщение на экран
                        return -1
            else:
                X='X3'
        if ((X == 'X3') and (recognized == False)):
            recognized = True
            if Func[letter] in Sygnal:
                if (Sygnal[Func[letter]] == 3):
                    X = 'X5'
                else:
                    if ((Sygnal[Func[letter]] >=4) and (Sygnal[Func[letter]] <=9)):
                        X='X4'
                    else:
                        print('некорректное выражение, символ: ' + str(letter + 1))# todo:передать сообщение на экран
                        return -1
            else:
                X='X3'
        if ((X == 'X4') and (recognized == False)):
            recognized = True
            if Func[letter] in Sygnal:
                if (Sygnal[Func[letter]] == 1):
                    X='X1'
                else:
                    if (Sygnal[Func[letter]] == 2):
                        X='X2'
                    else:
                        print('некорректное выражение, символ: ' + str(letter + 1))# todo:передать сообщение на экран
                        return -1
            else:
                X='X3'
        if ((X == 'X5') and (recognized == False)):
            if(openskobka <0):
                print("Обработка ошибки: перевес закрывающих скобок символ: " +str(letter+1))# todo:передать сообщение на экран
                return -1
            recognized = True
            if Func[letter] in Sygnal:
                if (Sygnal[Func[letter]] == 3):
                    X= 'X5'
                else:
                    if ((Sygnal[Func[letter]] >=4) and(Sygnal[Func[letter]] <=9)):
                        X='X4'
                    else:
                        print('некорректное выражение, символ: ' + str(letter + 1))# todo:передать сообщение на экран
                        return -1
            else:
                print("Ошибка! заркывающая скобка - операнд")# todo:передать сообщение на экран
                return -1

        if(X=='X2'):#счётчик скобок
            openskobka+=1
        if (X == 'X5'):
            openskobka -=1

        if (X=='X3'):
            letter = recognizeOperands(letter,Func,Sygnal)
            if letter == -1:
                return -1
        letter += 1

    if (openskobka < 0):
        print("Обработка ошибки: перевес закрывающих скобок символ: " + str(letter + 1))
        return -1
    if openskobka != 0:
        print("Обработка ошибки: перевес открывающих скобок в выражении")
        return -1
    print("Твоя функция записана верно")
    print(Func)
    print(OpNames)

vocabulary(input())