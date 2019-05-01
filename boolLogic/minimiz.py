import Recognize
import pars


def CreateSDNF(TruthTable1):
    TrueComponents = []
    # ищем строки где целевая функция принимает знаение единицы
    for i in TruthTable1:
        if(i[i.__len__() - 1] == 1):
            TrueComponents.append(i)
    SDNF = []
    row = []
    for i in TrueComponents:
        for j in range(0,i.__len__()-1):
            if(i[j] == 0):
                row.append("not N" + str(j))
            if(i[j] == 1):
                row.append("N" + str(j))
        SDNF.append(row)
        row = []
    #в row храним обработанной каждую строку, добавляем в SDNF, N символизиурет имя
    #сами имена хранятся в TruthTable1[0][0:len-2]
    return SDNF #[[*]+[*]]

#берём на вход список с таблицей истинности
def CreateSKNF(TruthTable1):
    TrueComponents = []
    # ищем строки где целевая функция принимает знаение единицы
    for i in TruthTable1:
        if(i[i.__len__() - 1] == 0):
            TrueComponents.append(i)
    SKNF = []
    row = []
    for i in TrueComponents:
        for j in range(0,i.__len__()-1):
            if(i[j] == 0):
                row.append("N" + str(j))
            if(i[j] == 1):
                row.append("not N" + str(j))
        SKNF.append(row)
        row = []
    #в row храним обработанной каждую строку, добавляем в SDNF, N символизиурет имя
    return SKNF #[[+]*[+]]


def Recognizer(Function):
    A = Recognize.vocabulary(Function).pop()
    #A = Recognize.vocabulary(Function)
    A = A[2:len(A)-2]
    table =[]
    table = A.split('], [')
    TrTable = []
    row = []
    for i in table:
        row = i.split(', ')
        TrTable.append(row)
    return TrTable

def StrReverse(s):
    return s[::-1]
def BinaryView(n, numparams):#numparams обепечивает постоянную разрядность сетки
    wroteparams = 0
    B = ""
    if (n != 0):
        A = bin(n)
        i = n.bit_length()
        i=i+1
        while(i!=1):
            B += A[i]
            wroteparams +=1
            i-=1
        while(wroteparams != numparams):
            wroteparams+=1
            B+="0"
        B = StrReverse(B)
        return B
    else:
        while (wroteparams != numparams):
            wroteparams += 1
            B += "0"
        return B

def ShowAllPermutations(SNF):
    '''по итогу функция найдёт все повторения и обхединит всё в список списков, где первый список - повторения второй номера строк с повторениями'''
    maxparams = SNF[0].__len__()#todo:в теории SNF мб равен []
    #необходимо сделать все возможные выборки от 1 до maxparams-1
    AllPermut = []
    #зациклить это для каждого списка
    for row in range(0,SNF.__len__()-1):
        i = 0
        while(i < 2 ** maxparams -1):#2 ** maparams -1 найти все перестановки сразу
            whichparams = BinaryView(i,maxparams)
            CompareParams =[]
            number = 0
            for letter in whichparams:
                if(letter  == "1"):
                    CompareParams.append(number)
                number+=1
            for nextrow in range(row+1,SNF.__len__()):
                flag = True
                for j in CompareParams:
                    if(SNF[row][int(j)] != SNF[nextrow][int(j)]):
                        flag = False
                    if SNF[row][int(j)] == "none":
                        flag = False #появилось здесь так как списки могу тбыть не мнимальны после 1 минимизации, а при минимизации параметр ставится на none
                if((flag == True) and (CompareParams != [])):#при прохождении условия будут отобраны все группы с одинаковыми именами
                    truecmp = []
                    truecmp.append(CompareParams)
                    truecmp.append([row,nextrow])
                    AllPermut.append(truecmp)
            i+=1
    #ALlPermut - собрал все повторяющиеся параметры
    '''находим все параметры смежные повторяющимся, проверяем равенство суммы 1 или умножения 0 используя truths
    в случае успеха - удаляем'''
    #то есть модернизиурем AllPermut так, чтобы одним и тем же повторяющимся параметрам ставились в соответствие все списки
    ModernPermut =[]
    for i in range(AllPermut.__len__()-1):
        lists =[]
        if(AllPermut[i][0] !=[]):
            for k in AllPermut[i][1]:
                lists.append(k)#сохранили нjмера списков с обозреваемыми повторениями

            for j in range(i+1,AllPermut.__len__()):#сравниваем обозреваемые параметры и доавляем номера спписков
                #надо сравнить списки по значению
                if(AllPermut[i][0].__len__() == AllPermut[j][0].__len__()):
                    #сравниваем списки по значению
                    flag1 = True
                    for Npar in range(AllPermut[i][0].__len__()):
                        if(AllPermut[i][0][Npar] != AllPermut[j][0][Npar]):
                            flag1 = False
                    if(flag1 == True):
                        #добавляем номера списков
                        for x in AllPermut[j][1]:
                            flag2 = False
                            for k in lists:
                                if( k == x):
                                    flag2 = True
                            if (flag2 == False):
                                lists.append(x)
                        #если записали, сохранили, то надо бы убрать список из рассмотрения
                        AllPermut[j][0] = []
            #перебрали все списки и если возможно, то AllPermut схлопнется

            ModernPermut.append([AllPermut[i][0],lists])
    if(AllPermut[AllPermut.__len__()-1][0] != []):#todo:по идее может не существовать и 0 элемента
        ModernPermut.append(AllPermut[AllPermut.__len__()-1])

    return ModernPermut

def CheckForMinimiz(SNF, dis):
    '''функция возвращает индексы параметров смежных с теми, что можно удалить'''
    ResultList = []
    ModernPermut = ShowAllPermutations(SNF)
    for i in ModernPermut:
        #1. запомниаем номера параметров которые пытаемся хотим удалить
        #каждому элементу deleteparams должно соответствовать номер элемента в списке списков и номер списка списков
        listdeletparams = []
        for numinsnf in i[1]:#номера спискa в списке списков(списков)
            for elemname in range(SNF[numinsnf].__len__()):#если элемента нет, то добавляем
                flag0 = False
                for numini in i[0]:
                    if(numini == elemname):
                        flag0 = True#элемент из снф совпадает с повторяющимся - значит не удаляем
                if(flag0 == False):
                    listdeletparams.append([numinsnf, elemname])
        #2. собираем функцию для отправки на таблице истинности
        sendfunc = ""
        if(dis == True):
            #доказываем, что сумма параметров == 1
            flag2 = False
            firststep = True
            prev = -1
            sendfunc +="( 1 "
            for each in listdeletparams:
                if ((each[0] == prev ) or (firststep == True)):#если из 1 списка, то умножение
                    if(SNF[each[0]][each[1]]!='none'):
                        sendfunc += " and ( " + SNF[each[0]][each[1]] +" )"
                    else:
                        sendfunc += " and ( " + "1" + " )"
                    flag2 = True
                    firststep = False
                else:
                    if (SNF[each[0]][each[1]] != 'none'):
                        sendfunc += ") or ( ( " + SNF[each[0]][each[1]] + " ) "
                    else:
                        sendfunc += ") or ( ( " + "0" + " ) "
                    flag2 = False
                prev = each[0]
            if (flag2 == True):
                sendfunc += " ) "
            else:
                sendfunc +=" ) "
        else:
            # доказываем, что произведение параметров =0
            prev = -1
            sendfunc += "( 0 "
            firststep = True
            flag1 = False
            for each in listdeletparams:
                if ((each[0] == prev) or (firststep == True)):  # если из 1 списка, то умножение
                    if (SNF[each[0]][each[1]] != 'none'):
                        sendfunc += " or ( " + SNF[each[0]][each[1]] +" )"
                    else:
                        sendfunc += " or ( " + "0" + " )"
                    flag1 = True
                else:
                    if (SNF[each[0]][each[1]] != 'none'):
                        sendfunc += ") and ( (" + SNF[each[0]][each[1]] +" )"
                    else:
                        sendfunc += ") and ( (" + "1" + " )"
                prev = each[0]
            if(flag1 == True):
                sendfunc += ")"
            else:
                sendfunc += " )"

        import pars
        UsedN = [0,0,0]
        if(sendfunc.find('N0')>0):
            UsedN[0] = 1
        if (sendfunc.find('N1') > 0):
            UsedN[1] = 1
        if (sendfunc.find('N2') > 0):
            UsedN[2] = 1
        shifrator = 4*UsedN[0] + 2*UsedN[1] + UsedN[2]
        izbavlyaemsyaOtNone = True
        if(shifrator == 0):
            izbavlyaemsyaOtNone = False
        if(izbavlyaemsyaOtNone == True):
            TableForCheck = pars.Recognizer(sendfunc,str(shifrator))
            #3. првоеряем эквивалентна ли замена
            flagEcviv = True
            for everylist in range(TableForCheck.__len__()):
                A = TableForCheck[everylist].pop()
                if(dis == True):
                    if (A == "0"):
                        flagEcviv = False
                else:
                    if(A == "1"):
                        flagEcviv = False
            if(flagEcviv == True):
                ResultList.append(i)#добавление всех вариантов удаления
        else:
            #ResultList.append(i)
            temp=0
    return ResultList

def MinimizationSNF(SNF,dis):
    '''говно внутри'''#todo: единственная ошибка скрывается там
    Varieties = []
    Varieties = CheckForMinimiz(SNF,dis)
    FullResult = []
    if (Varieties != []):
        for i in Varieties:
            result = []
            for k in SNF:
                preresult = []
                for j in k:
                    preresult.append(j)
                result.append(preresult)
            #закрываем лишние элементы(мнимизируем)
            for num in i[1]:
                for numname in range(SNF[num].__len__()):
                    flag = False
                    for truename in i[0]:

                        if truename == numname:
                            flag = True#как раз то имя которое мы не трогаем
                    if flag == False:
                        result[num][numname] = "none"

            FullResult.append(result)
    else:
        return SNF
    #print(FullResult)
    for testforminimiz in range(FullResult.__len__()):
        A = CheckForMinimiz(FullResult[testforminimiz],dis)
        if (A != []):
            FullResult[testforminimiz] = MinimizationSNF(FullResult[testforminimiz],dis)
    return FullResult


global ParsedJaggedArr
ParsedJaggedArr = []
def RecParsReclist(res):
    '''рекурсивно парсит jagged arr в список постоянной глубины'''
    global ParsedJaggedArr
    A = 1
    for i in range(res.__len__()):
        if( isinstance(res[i], list)):
            A = RecParsReclist(res[i])
        else:
            return -2
    if A == -2:
        temp =0
        #вот тут мы понимаем, что нашли то самое место где нада парсить, в коце видимо нао вернут ьвсё чт оугодно, только не -2
        ParsedJaggedArr.append(res)
    return 0
def SecondStepMinimiz(res):
    '''возвращает функции без повторяющихся операций'''
    global ParsedJaggedArr
    RecParsReclist(res)
    for i in range(ParsedJaggedArr.__len__()):
        newList = []
        newList.append(ParsedJaggedArr[i][0])
        for j in range(ParsedJaggedArr[i].__len__()):
            flag = False
            for k in range(newList.__len__()):
                if ((newList[k][0] == ParsedJaggedArr[i][j][0]) and (newList[k][1] == ParsedJaggedArr[i][j][1]) and (
                        newList[k][2] == ParsedJaggedArr[i][j][2])):
                    flag = True
            if flag == False:
                newList.append(ParsedJaggedArr[i][j])
        ParsedJaggedArr[i] = newList
    return ParsedJaggedArr
def ThirdStepOfMinimiz(secondMin):
    '''подсчитываем количество входов'''

    for i in secondMin:
        notOp = [0, 0, 0]
        for j in i:
            for k in j:
                if k == "not N0":
                    notOp[0]=1
                if k == "not N1":
                    notOp[1] = 1
                if k == "not N2":
                    notOp[2] = 1
        #посчитали какие отрицания у нас имеются соответственно их входы считаем единожды
        CT = 0
        for j in i :
            noneNum = 0
            for el in j:
                if el == 'none':
                    noneNum+=1
            if noneNum == 0:
                CT+=4
            if noneNum == 1:
                CT+=2
        CT += 2*(i.__len__() -1)
        for eachM in notOp:
            if eachM == 1:
                CT+=1
        i.append(CT)
    return secondMin

def CheckTrTable(Table, secMin,dis):
    correctList = []
    if (dis == True):
        for  i in secMin:
            UsedN = [0, 0, 0]
            func = ""
            for listsk in i:
                func +="( "
                for oper in listsk:
                    if oper != 'none':
                        func+=oper + " * "
                func += " 1 ) + "
            func = func[:-2]
            if (func.find('N0') > 0):
                UsedN[0] = 1
            if (func.find('N1') > 0):
                UsedN[1] = 1
            if (func.find('N2') > 0):
                UsedN[2] = 1
            shifrator = 4 * UsedN[0] + 2 * UsedN[1] + UsedN[2]
            retTable = pars.Recognizer(func, str(shifrator))
            flag = True
            for row in Table:
                combination = ""
                CT = 0
                if UsedN[0] == 1:
                    combination +=str(row[0])
                if UsedN[1] == 1:
                    combination+=str(row[1])
                if UsedN[2] == 1:
                    combination+=str(row[2])
                for retRows in retTable:
                    checkcomb = ""
                    last = ""
                    for el in retRows:
                        checkcomb += el
                    last = checkcomb[-1:]
                    checkcomb = checkcomb[:-1]

                    if(checkcomb == combination):
                        if (row[3] != int(last)):
                            flag = False
            if flag == True:
                correctList.append(i)
    return correctList
def TakeMinANDORNOT(Table):
    res = MinimizationSNF(CreateSDNF(Table), True)#todo: добавить выбор сднф скнф
    secodMinimiz = SecondStepMinimiz(res)
    secodMinimiz = CheckTrTable(Table,secodMinimiz,True)
    thirdMinimiz = ThirdStepOfMinimiz(secodMinimiz)
    minimum = thirdMinimiz[0][-1]
    for i in thirdMinimiz:
        if(i[-1] < minimum):
            minimum = i[-1]
    print("SNF RES:")
    for i in thirdMinimiz:
        if i[-1] == minimum:
            print(i)
    return minimum


#Table = [[0,0,0,1],[0,0,1,1],[0,1,0,0],[0,1,1,1],[1,0,0,1],[1,0,1,1],[1,1,0,0],[1,1,1,0]]#прмиер для эквивалентности
#Table = [[0,0,0,0],[0,0,1,0],[0,1,0,0],[0,1,1,0],[1,0,0,0],[1,0,1,1],[1,1,0,1],[1,1,1,1]]
#Table = [[0,0,0,0],[0,0,1,0],[0,1,0,0],[0,1,1,1],[1,0,0,0],[1,0,1,1],[1,1,0,1],[1,1,1,1]]
#TakeMinANDORNOT(Table)



