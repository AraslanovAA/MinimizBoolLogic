from truths import Truths
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
                return [0,letter-1]
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
            return [0,letter - 1]#тут конец обработки функции в принципе
    if (i == N):
        return [-1,"превышено допустимое количесвто символов в имени параметра: " + str(letter+1-i)]

def vocabulary(Func, task):
    for i in Func:
        if i == "\\":
            return [-1,"\?"]
    global OpNames
    OpNames.clear()
    '''существование полных форм записей и коротких:
    короткие имена разрешено писать слитно, имспользуя длинные имена необходимо ставить пробелы
    внимание: операнды чувствительны к регистру
    разрешается использование следующих логических операторов:'''
    ShortNames ={
        'not': '-',
        'or': '+',
        'and': '*',
        'xor': '^',
        'sheff': '|',
        'pirs' : '/',
        'imp' : '>' #наверно чуть логичнее было бы импользовать > ?
    }
    LFunc =[]
    LFunc = list(Func)
    for i in range(LFunc.__len__()):
        if LFunc[i] == '(':
            LFunc[i] = ' ( '
        if LFunc[i] == ')':
            LFunc[i] = ' ) '
    Func = ""  # собираем строку обратно
    for Item in LFunc:
        Func = Func + Item
    LFunc.clear()
    LFunc = Func.split(' ')
    while '' in LFunc:
        LFunc.pop(LFunc.index(''))
    for ItemIndex in range(len(LFunc)):#заменяем длинные имена на короткие
        if LFunc[ItemIndex] in ShortNames:
            LFunc[ItemIndex] = ShortNames[LFunc[ItemIndex]]

    Func =""#собираем строку обратно
    for Item in LFunc:
        Func = Func + Item

    letter =0
    L = len(Func)
    X='X0'
    openskobka = 0
    recognized = False
    global Sygnal
    Sygnal = {
        '-': 1,
        '(': 2,
        ')': 3,
        '*': 4,
        '+': 5,
        '^': 6,  # xor
        '|': 7,
        '/': 8,
        '>': 9  # импликация
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
                        return [-1,'некорректное выражение, символ: ' + str(letter+1)]
            else:
                X='X3'

        if ((X == 'X1') and (recognized == False)):
            recognized = True
            if Func[letter] in Sygnal:
                if (Sygnal[Func[letter]] == 2):
                    X='X2'
                else:
                    return [-1,'некорректное выражение, символ: ' + str(letter + 1)]
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
                        return [-1,'некорректное выражение, символ: ' + str(letter + 1)]
            else:
                X='X3'
        if ((X == 'X3') and (recognized == False)):
            recognized = True
            if Func[letter] in Sygnal:
                if (Sygnal[Func[letter]] == 3):
                    X = 'X5'
                else:
                    if (Sygnal[Func[letter]] >=4):
                        X='X4'
                    else:
                        return [-1,'некорректное выражение, символ: ' + str(letter + 1)]
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
                        return [-1,'некорректное выражение, символ: ' + str(letter + 1)]
            else:
                X='X3'
        if ((X == 'X5') and (recognized == False)):
            if(openskobka <0):
                return [-1,"Обработка ошибки: перевес закрывающих скобок символ: " +str(letter+1)]
            recognized = True
            if Func[letter] in Sygnal:
                if (Sygnal[Func[letter]] == 3):
                    X= 'X5'
                else:
                    if (Sygnal[Func[letter]] >=4):
                        X='X4'
                    else:
                        return [-1,'некорректное выражение, символ: ' + str(letter + 1)]
            else:
                return [-1,"Ошибка! заркывающая скобка - операнд"]

        if(X=='X2'):#счётчик скобок
            openskobka+=1
        if (X == 'X5'):
            openskobka -=1

        if (X=='X3'):
            if Func[letter].isdigit():
                if Func[letter] == '0' or Func[letter] == '1':#если 0 или 1 используется в качестве операнда
                    c = 0
                    #print("встречени 0/1")
                else:
                    return [-1,"Обработка ошибки операн не может начинаться с 0/1"]
            else:
                letter = recognizeOperands(letter,Func,Sygnal)
                if letter[0] == -1:
                    return [-1,letter[1]]
                else:
                    letter = letter[1]
        letter += 1

    if ((X !='X3') and (X!='X5')):
        return [-1,"обработка ошибки: функция недописана"]
    if (openskobka < 0):
        return [-1,"Обработка ошибки: перевес закрывающих скобок символ: " + str(letter + 1)]
    if openskobka != 0:
        return [-1,"Обработка ошибки: перевес открывающих скобок в выражении"]
   # print("Твоя функция записана верно")
    if (task == "task1"):
        paramNames = ['A','B','C','D']
    if(task == "task2"):
        paramNames = ['A', 'B', 'C']
    if(task == "1"):
        paramNames = ['N2']
    if(task == "2"):
        paramNames = ['N1']
    if(task == "3"):
        paramNames = ['N1', 'N2']
    if(task == "4"):
        paramNames = ['N0']
    if(task == "5"):
        paramNames = ['N0','N2']
    if(task == "6"):
        paramNames = ['N0','N1']
    if(task == "7"):
        paramNames = ['N0','N1','N2']
    if(OpNames.__len__() != paramNames.__len__()):
        return [-1,"Ошибка количества операндов"]
    for i in paramNames:
        if((i in OpNames) == False):
            return [-1,"Встречены не заявленные операнды"]
    if(task == "task1"):
        OpNames = ['A','B','C','D']#чтобы порядок следования операндов не сломался
    if(task == "task2"):
        OpNames = ['A', 'B', 'C']
    if(task == "1"):
        OpNames = ['N2']
    if(task == "2"):
        OpNames = ['N1']
    if(task == "3"):
        OpNames = ['N1','N2']
    if(task == "4"):
        OpNames = ['N0']
    if(task == "5"):
        OpNames = ['N0','N2']
    if(task == "6"):
        OpNames = ['N0','N1']
    if(task == "7"):
        OpNames = ['N0','N1','N2']
    OpNames.append(str(Truths(OpNames, [transform(Func, Sygnal)])))
    return OpNames
    #return str(Truths(OpNames,[transform(Func, Sygnal)]))



def SearcArgs(Func, i,Sygnal):
    '''функция на вход принимает строку функции и индекс логического выражения
        на выходе индексы границ правого и левого операнда указанного логического выражения'''
    #сначала напишем обработчик поиска левого аргумента
    Result = []
    k = i
    numCloseBrackets = 0
    flag = False
    while flag == False:
        if k != 0:
            k-=1
            if Func[k] in Sygnal:
                if Sygnal[Func[k]] == 3:
                    numCloseBrackets+=1
                if Sygnal[Func[k]] == 2:
                    if numCloseBrackets ==0:#если встретили открывающую скобку, первой то операнд уже считан
                        Result.append(k+1)
                        Result.append(i-1)
                        flag=True
                    else:
                        numCloseBrackets-=1
                if ((Sygnal[Func[k]]>=5) and(numCloseBrackets ==0)):#если скобки парно закрыты и встречен следущий управляющий символ, то формируем левый операнд
                    Result.append(k+1)
                    Result.append(i-1)
                    flag=True
        else:#если дошли до конца функции, то все с 0 символа до i-1 искомый операнд
            Result.append(0)
            Result.append(i-1)#в теории можно и без этого обойтись, но может быть загвоздка в будущем
            flag = True

    #теперь обрабатываем операнд справа
    k = i
    numCloseBrackets = 0
    flag = False
    while flag == False:
        if k != len(Func)-1:
            k += 1
            if Func[k] in Sygnal:
                # если встретили одну из скобок
                # если встретили A4-9
                if Sygnal[Func[k]] == 3:
                    if numCloseBrackets ==0:#если встретили закрывающую скобку, первой то операнд уже считан
                        Result.append(i+1)
                        Result.append(k-1)
                        flag=True
                    else:
                        numCloseBrackets += 1
                if Sygnal[Func[k]] == 2:
                    numCloseBrackets -= 1
                if ((Sygnal[Func[k]] >= 5) and (#умножение разрешено очевидно
                        numCloseBrackets == 0)):  # если скобки парно закрыты и встречен следущий управляющий символ, то формируем левый операнд
                    Result.append(i + 1)
                    Result.append(k - 1)
                    flag = True
        else:  # если дошли до конца функции, то все с i+1 до конца FUnc
            Result.append(i+1)
            Result.append(len(Func)-1)
            flag = True
    return Result

def substitution(Func):
    '''функция заменяет короткие имена на логические выражения воспринимаемы питоном'''
    flag = False
    while flag == False:
        flag = True
        for i in range(len(Func)):
            if ((Func[i] == '+') or (Func[i] == '*') or (Func[i] == '-')):
                flag =False
            if (Func[i] == '+'):
                Func = Func[:i] + ' or ' + Func[(i+1):]
            if (Func[i] == '*'):
                Func = Func[:i] + ' and ' + Func[(i+1):]
            if (Func[i] == '-'):
                Func = Func[:i] + ' not ' + Func[(i+1):]
    return Func


def transform(Func, Sygnal):
    '''функция получает на вход проверенную функцию, преобразует все логические выражения в базис и или не, затем
    вызывает функцию substitution  и после должна передать получившееся выражение для создания таблицы истинности'''
    argsindex =[]
    LeftArg =""
    RightArg=""
    flag = False
    moved = True
    while flag == False:
        flag=True
        for i in range(len(Func)):
            moved = True
            if Func[i] in Sygnal:
                if(Sygnal[Func[i]]>=6):
                    flag=False
                if moved == True:
                    if(Sygnal[Func[i]] == 6):
                        argsindex = SearcArgs(Func,i,Sygnal)
                        LeftArg =Func[argsindex[0] : argsindex[1]+1]#интересный факт: вырезать подстроку из строки
                        RightArg=Func[argsindex[2] : argsindex[3]+1]#левая координата указывает на индекс правая на индекс+1
                        Func = Func[:argsindex[0]] + '(-' +LeftArg +'*'+RightArg + '+' + LeftArg +'*-' + RightArg +')'+ Func[(argsindex[3]+1):]
                        moved = False
                if moved == True:
                    if (Sygnal[Func[i]] == 7):
                        argsindex = SearcArgs(Func, i, Sygnal)
                        LeftArg = Func[argsindex[0]: argsindex[1] + 1]
                        RightArg = Func[argsindex[2]: argsindex[3] + 1]
                        Func = Func[:argsindex[0]] + '(-' + LeftArg + '+-' + RightArg + ')' + Func[(argsindex[3] + 1):]
                        moved = False
                if moved == True:
                    if (Sygnal[Func[i]] == 8):
                        argsindex = SearcArgs(Func, i, Sygnal)
                        LeftArg = Func[argsindex[0]: argsindex[1] + 1]
                        RightArg = Func[argsindex[2]: argsindex[3] + 1]
                        Func = Func[:argsindex[0]] + '(-' + LeftArg + '*-' + RightArg + ')' + Func[(argsindex[3] + 1):]
                        moved = False
                if moved == True:
                    if (Sygnal[Func[i]] == 9):
                        argsindex = SearcArgs(Func, i, Sygnal)
                        LeftArg = Func[argsindex[0]: argsindex[1] + 1]
                        RightArg = Func[argsindex[2]: argsindex[3] + 1]
                        Func = Func[:argsindex[0]] + '(-' + LeftArg + '+' + RightArg + ')' + Func[(argsindex[3] + 1):]
                        moved = False
    return substitution(Func)

#print(vocabulary(""))