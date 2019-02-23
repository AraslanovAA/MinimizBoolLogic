
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
                print("значит формируем значение")
                flag = False
                for k in OpNames:#если такого имени в списке нет, добавляем
                    if k == name:
                        flag = True
                if flag == False:
                    OpNames.append(name)
                return letter-1
            else:
                print("ебашим дальше")
                name = name + Func[letter]
        else:
            print("тут гг, формируем значение")
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



def vocabulary(Func):
    if Func.find('#') > 0:
        print("зарпещённный символ: " + str(Func.find('#')+1))# todo:передать сообщение на экран
        return -1
    if Func.find('%') > 0:
        print("зарпещённный символ: " + str(Func.find('#') + 1))  # todo:передать сообщение на экран
        return -1
    subStrOld = 'xor'#преобразовнаие xor
    subStrNew = '%'
    lenStrOld = len(subStrOld)
    while Func.find(subStrOld) > 0:
        i = Func.find(subStrOld)
        Func = Func[:i] + subStrNew + Func[i + lenStrOld:]

    subStrOld = 'imp'#преобразовнаие импликации
    subStrNew = '#'
    lenStrOld = len(subStrOld)
    while Func.find(subStrOld) > 0:
        i = Func.find(subStrOld)
        Func = Func[:i] + subStrNew + Func[i + lenStrOld:]

    subStrOld = ' '  # удаление пробелов
    subStrNew = ''
    lenStrOld = len(subStrOld)
    while Func.find(subStrOld) > 0:
        i = Func.find(subStrOld)
        Func = Func[:i] + subStrNew + Func[i + lenStrOld:]

    letter =0
    L = len(Func)
    X='X0'
    openskobka = 0
    recognized = False
    # пиздец сука говнокод нахуй switch case бы блять
    Sygnal = {
        '-' : 1,
        '(' : 2,
        ')' : 3,
        '+' : 4,
        '*' : 5,
        '%' : 6,#xor
        '|' : 7,
        '/' : 8,
        '#' : 9#импликация
    }
    while(letter < L):
        recognized = False
        if ((X == 'X0') and (recognized == False)):
            print("обрабатываемый символ:" +Func[letter])
            recognized = True
            print("X0")
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
                print("встречен символ")#добавить сюда функцию по распознованию операндов
                X='X3'

        if ((X == 'X1') and (recognized == False)):
            print("обрабатываемый символ:" + Func[letter])
            recognized = True
            print("X1")
            if Func[letter] in Sygnal:
                if (Sygnal[Func[letter]] == 2):
                    X='X2'
                else:
                    print('некорректное выражение, символ: ' + str(letter + 1))# todo:передать сообщение на экран
                    return -1
            else:
                print("встречен символ")  # добавить сюда функцию по распознованию операндов
                X='X3'
        if ((X == 'X2') and (recognized == False)):
            print("обрабатываемый символ:" + Func[letter])
            recognized = True
            print("X2")
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
                print("встречен символ")  # добавить сюда функцию по распознованию операндов
                X='X3'
        if ((X == 'X3') and (recognized == False)):
            print("обрабатываемый символ:" + Func[letter])
            recognized = True
            print("X3")
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
                print("встречен символ")  # добавить сюда функцию по распознованию операндов
                X='X3'
        if ((X == 'X4') and (recognized == False)):
            print("обрабатываемый символ:" + Func[letter])
            recognized = True
            print("X4")
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
                print("встречен символ")  # добавить сюда функцию по распознованию операндов
                X='X3'
        if ((X == 'X5') and (recognized == False)):
            print("обрабатываемый символ:" + Func[letter])
            if(openskobka <0):
                print("Обработка ошибки: перевес закрывающих скобок символ: " +str(letter+1))# todo:передать сообщение на экран
                return -1
            recognized = True
            print("X5")
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