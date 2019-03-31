import Recognize
#берём на вход список с таблицей истинности
import truthTable


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
    print(SDNF)
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
    print(SKNF)
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
    maxparams = SNF[0].__len__()
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
    if(AllPermut[AllPermut.__len__()-1][0] != []):
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
                    sendfunc += " and ( " + SNF[each[0]][each[1]] +" )"
                    flag2 = True
                    firststep = False
                else:
                    sendfunc += ") or ( ( " + SNF[each[0]][each[1]] + " ) "
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
                    sendfunc += " or ( " + SNF[each[0]][each[1]] +" )"
                    flag1 = True
                else:
                    sendfunc += ") and ( (" + SNF[each[0]][each[1]] +" )"
                prev = each[0]
            if(flag1 == True):
                sendfunc += ")"
            else:
                sendfunc += " )"


        TableForCheck = truthTable.Recognizer(sendfunc)
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
    return ResultList

def MinimizationSNF(SNF,dis):
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
            print(i)
            FullResult.append(result)
    else:
        return SNF
    #print(FullResult)
    for testforminimiz in range(FullResult.__len__()):
        A = CheckForMinimiz(FullResult[testforminimiz],dis)
        if (A != []):
            FullResult[testforminimiz] = MinimizationSNF(FullResult[testforminimiz],dis)
    return FullResult

Table = [[0,0,0,1],[1,0,1,1],[1,0,0,1]]
print(MinimizationSNF(CreateSDNF(Table), True))





