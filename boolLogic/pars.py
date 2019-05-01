import random

import Recognize

global ListOfLists
ListOfLists = []
global UsedElementsOfList
UsedElementsOfList = 0


def ParserToListOfLists(sFunc, numInList):
    global  UsedElementsOfList
    resultList = ['-', '-', '-']

    i_start = 0
    i_finish = i_start
    if(sFunc[i_start] == '-'):
        resultList[0] = '-'
        #дальше 2 варианта, там скобка либо там операнд
        i_start+=1
        i_finish = i_start
        if (sFunc[i_start] == '('):
            openskobka = 1
            while (openskobka != 0):
                i_finish += 1
                if (sFunc[i_finish] == '('):
                    openskobka += 1
                if (sFunc[i_finish] == ')'):
                    openskobka -= 1
            # i_start и i_finish обозначают границы операнда(скобки)
            resultList[1] = '#' + str(UsedElementsOfList)
            UsedElementsOfList += 1
            ParserToListOfLists(sFunc[(i_start + 1):i_finish], UsedElementsOfList - 1)
            resultList.pop()
        else:
            resultList[1]= sFunc[i_start]
            resultList.pop()
    else:
        if (sFunc[i_start] == '('):
            # перед нами скобка, наша цель найти закрывающую её скобку
            openskobka = 1
            while(openskobka != 0):
                i_finish +=1
                if(sFunc[i_finish] == '('):
                    openskobka +=1
                if(sFunc[i_finish] == ')'):
                    openskobka -=1
            #i_start и i_finish обозначают границы операнда(скобки)
            resultList[1] = '#' + str(UsedElementsOfList)
            UsedElementsOfList += 1
            ParserToListOfLists(sFunc[(i_start+1):i_finish], UsedElementsOfList - 1)
        else:
            resultList[1] = sFunc[i_start]
            # перед нами операнд
        i_finish += 1# независимо операнд или скобка была ранее теперь указывает на операцию
        resultList[0] = sFunc[i_finish]
        i_start = i_finish + 1

        #repeat
        i_finish = i_start
        if (sFunc[i_start] == '('):
            # перед нами скобка, наша цель найти закрывающую её скобку
            openskobka = 1
            while (openskobka != 0):
                i_finish += 1
                if (sFunc[i_finish] == '('):
                    openskobka += 1
                if (sFunc[i_finish] == ')'):
                    openskobka -= 1
            # i_start и i_finish обозначают границы операнда(скобки)
            resultList[2] = '#' + str(UsedElementsOfList)
            UsedElementsOfList += 1
            ParserToListOfLists(sFunc[(i_start + 1):i_finish], UsedElementsOfList - 1)
        else:
            resultList[2] = sFunc[i_start]
            # перед нами операнд
        #repeat
        '''код может сломаться если в функции будет присутствовать запись вида (A+B+C)
            при верном выполнении функции i_finish должно равняться длине строки-1'''
    ListOfLists[numInList] = resultList

def AddNum(seeingPos, line):
    global ListOfLists
    ListOfLists[seeingPos].insert(0,str(line))
    if('#' in ListOfLists[seeingPos][2]):
        AddNum(int(ListOfLists[seeingPos][2][1:]),line+1)
    if(ListOfLists[seeingPos].__len__() == 4):
        if ('#' in ListOfLists[seeingPos][3]):
            AddNum(int(ListOfLists[seeingPos][3][1:]), line + 1)
def AddPostNum():
    global  ListOfLists
    for i in range(ListOfLists.__len__()):
        ListOfLists[i].append(i)
def ReverseLines():
    global ListOfLists
    maximLine = 0
    for i in range(ListOfLists.__len__()):
        if(int(ListOfLists[i][0]) > maximLine):
            maximLine = int(ListOfLists[i][0])
    for i in range(ListOfLists.__len__()):
        ListOfLists[i][0] = str(maximLine - int(ListOfLists[i][0]))
def SortLines():
    global ListOfLists
    for i in range(ListOfLists.__len__()-1):
        for j in range(i+1,ListOfLists.__len__()):
            if(int(ListOfLists[i][0]) > int(ListOfLists[j][0])):
                ListOfLists[i],ListOfLists[j] = ListOfLists[j], ListOfLists[i]
def RebuiltLinks():
    global  ListOfLists
    for i in range(ListOfLists.__len__()):
        for j in range(ListOfLists[i].__len__()-1):
            if('#' in ListOfLists[i][j]): #тогда надо найти какой сейчас номер имеет тот список на который ссылка
                flag = False
                for k in range(ListOfLists.__len__()):
                    if ((int(ListOfLists[i][j][1:]) == ListOfLists[k][ListOfLists[k].__len__()-1]) and (flag == False)):
                        ListOfLists[i][j] = '#' + str(k)
                        flag = True
def Retranslate():
    AddNum(0,0)#добавили номера обратных слоёв
    AddPostNum()
    ReverseLines()
    SortLines()
    RebuiltLinks()
    for i in ListOfLists:
        i.pop()
def StartParse(sFunc = "A+(-(A*B))"):
    Sygnal = {
        '-': 1,
        '*': 4,
        '+': 5,
        '^': 6,  # xor
        '|': 7,
        '/': 8,
        '>': 9  # импликация
    }
    numOperations = 0
    global ListOfLists
    ListOfLists = []
    for i in range(sFunc.__len__()):
        if (sFunc[i] in Sygnal):
            numOperations += 1
    for i in range(numOperations):
        ListOfLists.append([])
    global UsedElementsOfList
    UsedElementsOfList = 0
    UsedElementsOfList = UsedElementsOfList + 1
    ParserToListOfLists(sFunc, UsedElementsOfList - 1)
    Retranslate()
    return ListOfLists
#StartParse("(((-D)/C)>((-D)/C))>(((-D)/C)*(-(B+(-A))))")

global strFunction
strFunction = ""
hardFalseDict = {
        1 : [0,1,1,'|'],#результат, операнды подбора, функция
        2 : [1,0,0,'/'],
        3 : [0,1,0,'>'],
        4 : [1,1,1,'*'],
        5 : [0,0,0,'+']
    }
hardTrueDict = {
        1 : [1,1,0,"((X)>(X))|((-(X))+(Y))"],
        2 : [0,0,1,"((X)^(X))/((-(X))*(Y))"],
        3 : [1,1,1, "((X)>(X))>((X)*(Y))"],
        4 : [0,0,0, "((X)^(X))^((X)+(Y))"],
        5 : [1,1,1,"((X)>(X))*((X)*(Y))"],
        6 : [1,0,1,"((X)^(X))+(-((Y)>(X)))"]
    }
global resinput
resinput = []
global lUsedNames
lUsedNames= []
def TakeNames(res):
    paramNames = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
    }
    global lUsedNames
    num = -1
    for i in range(lUsedNames.__len__()):
        if( lUsedNames[i] == 0):
            num = i
    if(num == -1):
        num = random.randint(0,3)

    lUsedNames[num] +=1
    if(resinput[num] == res):
        return paramNames[num]
    else:
        return "-" + paramNames[num]


def GenerateElement(resElem, hard,currentLine,maxLine  = 2):
    global strFunction
    resStr = ""
    if(currentLine < maxLine):
        if(hard == False):
            numOper = random.randint(1,5)
            if(currentLine//2 == 1):
                resStr = "(" + GenerateElement(hardFalseDict[numOper][1],False,currentLine+1,maxLine) + ")" + hardFalseDict[numOper][3] + "(" + GenerateElement(hardFalseDict[numOper][2],True,currentLine+1,maxLine) + ")"
            else:
                resStr = "(" + GenerateElement(hardFalseDict[numOper][1], False, currentLine + 1,maxLine) + ")" + \
                         hardFalseDict[numOper][3] + "(" + GenerateElement(hardFalseDict[numOper][2], False,
                                                                           currentLine + 1,maxLine) + ")"

            if (resElem != hardFalseDict[numOper][0]):
                resStr = "-(" + resStr + ")"
            return resStr
        if(hard == True):
            numOper = random.randint(1, 6)
            str1 = GenerateElement(hardTrueDict[numOper][1],False,currentLine+1,maxLine)
            str2 = GenerateElement(hardTrueDict[numOper][2], False, currentLine + 1,maxLine)
            resStr0 =  hardTrueDict[numOper][3]
            for i in resStr0:
                resStr += i
            while resStr.find("X") > 0:
                i = resStr.find("X")
                resStr = resStr[:i] + str1 + resStr[i + len("X"):]
            while resStr.find("Y") > 0:
                i = resStr.find("Y")
                resStr = resStr[:i] + str2 + resStr[i + len("Y"):]
            if (resElem != hardTrueDict[numOper][0]):
                resStr = "-(" + resStr + ")"
            return resStr

    if(currentLine >= maxLine):
        return TakeNames(resElem)
    return ""

def Recognizer(Function,task):#возвращает таблицу истинности введённой функции, парсит в список
    OPNames = Recognize.vocabulary(Function,task)
    if(OPNames[0] == -1):
        return OPNames
    A = OPNames.pop()
    A = A[2:len(A)-2]
    table =[]
    table = A.split('], [')
    TrTable = []
    row = []
    for i in table:
        row = i.split(', ')
        TrTable.append(row)
    return TrTable
def CheckCorrect(sFunc, num):
    trTable = Recognizer(sFunc, "task1")
    numTrue = 0
    guessedInput = []
    for i in trTable:
        if(i[4] == str(num)):
            numTrue+=1
            guessedInput.append(i)
    if(numTrue == 1):
        return [True, guessedInput]
    else:
        return [False,guessedInput]

def CutListOfLists(extraList):
    n = extraList.__len__()
    currentEl = 0
    i = currentEl +1
    flag0 = True
    flag1 = True
    while(flag0 == True):
        flag1 = True
        while((currentEl < (n-1)) and (flag1 == True)):#незабыть увеличивать current и i
            i = currentEl + 1
            while((i < n)and (flag1 == True)):
                if(extraList[currentEl].__len__() == extraList[i].__len__()):
                    flag = True
                    for j in range(1,extraList[currentEl].__len__()):
                        if(extraList[currentEl][j] != extraList[i][j]):
                            flag = False
                    if(flag == True):
                        extraList.pop(i)
                        for k in extraList:
                            if(k[2].__len__()>1):
                                if(int(k[2][1:]) == i):
                                    k[2] = "#" + str(currentEl)
                                if(int(k[2][1:]) > i):
                                    k[2] = "#" + str(int(k[2][1:])-1)
                            if(k.__len__() == 4):
                                if (k[3].__len__() > 1):
                                    if (int(k[3][1:]) == i):
                                        k[3] = "#" + str(currentEl)
                                    if (int(k[3][1:]) > i):
                                        k[3] = "#" + str(int(k[3][1:]) - 1)
                            flag1 = False
                        # вот тут кароч ситуация когда надо удлаять i-ый элемент из списка списков
                        currentEl = -1
                        i = 0# после возвращаем всё на начало
                        n = extraList.__len__()
                i+=1
            currentEl+=1
        if(currentEl == n-1):
            flag0 = False
    return extraList


def CreatesFunc(maxLines=2):
    print("StartProgi")
    lFuncParams = []
    for i in range(5):
        lFuncParams.append(random.randint(0,1))
    if(lFuncParams[1] == 1):
        hardParam = True
    else:
        hardParam = False
    global lUsedNames
    lUsedNames.clear()
    for i in range(4):
        lUsedNames.append(0)
    global resinput
    resFunc = lFuncParams[4]
    lFuncParams.pop()
    resinput = lFuncParams
    generatedFunc = GenerateElement(resFunc,hardParam,0,maxLines)

    subStrOld = "(A)"
    subStrNew = "A"
    lenStrOld = len(subStrOld)
    while generatedFunc.find(subStrOld) > 0:
        i = generatedFunc.find(subStrOld)
        generatedFunc = generatedFunc[:i] + subStrNew + generatedFunc[i + lenStrOld:]

    subStrOld = "(B)"
    subStrNew = "B"
    lenStrOld = len(subStrOld)
    while generatedFunc.find(subStrOld) > 0:
        i = generatedFunc.find(subStrOld)
        generatedFunc = generatedFunc[:i] + subStrNew + generatedFunc[i + lenStrOld:]

    subStrOld = "(C)"
    subStrNew = "C"
    lenStrOld = len(subStrOld)
    while generatedFunc.find(subStrOld) > 0:
        i = generatedFunc.find(subStrOld)
        generatedFunc = generatedFunc[:i] + subStrNew + generatedFunc[i + lenStrOld:]

    subStrOld = "(D)"
    subStrNew = "D"
    lenStrOld = len(subStrOld)
    while generatedFunc.find(subStrOld) > 0:
        i = generatedFunc.find(subStrOld)
        generatedFunc = generatedFunc[:i] + subStrNew + generatedFunc[i + lenStrOld:]

    print(generatedFunc)
    lCheck = CheckCorrect(generatedFunc,resFunc)
    if(lCheck[0] == True):
        #print(generatedFunc)
        LL = CutListOfLists(StartParse(generatedFunc))
        if(LL.__len__() > 6):
            A = [LL,lCheck[1]]
            return A#возвращает список списков как [0] параметр списка и входные значения для единственновозможного получения заданного числа и само число [1]
        else:
            return CreatesFunc()
    else:
        return  CreatesFunc()

#CreatesFunc()

#StartParse("(A*B)+(B>(A+B))")
#print(ListOfLists)
