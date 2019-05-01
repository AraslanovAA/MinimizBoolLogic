
import random
import minimiz
def Zhegalkin(F):
    '''принимает список со значениями функции типа int, возвращает треугольник по которому определяются параметры полнома'''
    triangle = []
    triangle.append(F)
    endFlag = False
    watchingLine = 0
    while(endFlag == False):
        nextline = []
        for i in range(0,triangle[watchingLine].__len__()-1):
            nextline.append(triangle[watchingLine][i] ^ triangle[watchingLine][i+1])
        triangle.append(nextline)
        watchingLine+=1
        if( watchingLine == (F.__len__() -1)):
            endFlag = True
    return triangle

def ZhegalkinNameAnswer(F):
    '''принимает на вход список значений функции во всех точках пространста возвращает полином Жегалкина'''
    triangle = Zhegalkin(F)
    import math
    numParams = math.log2(F.__len__())  # непроверяем на целостность число, так как параметры в функцию приходят он нас самих
    polinomZhegalkina = []
    for i in range(triangle.__len__()):
        if( i == 0):#частный случай
            if(triangle[i][0] == 1):
                polinomZhegalkina.append([1])
        else:
            if(triangle[i][0] == 1):
                name = minimiz.BinaryView(i, numParams)
                listAnswer = []
                for j in range(name.__len__()):
                    if(name[j] == "1"):
                        listAnswer.append("N"+str(j))
                polinomZhegalkina.append(listAnswer)
    return polinomZhegalkina
def CheckHowManyInput(func):
    '''на вход функция в виде стркои - на выход количество входов на схеме'''
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
    CT = 0
    for i in func:
        if i in Sygnal:
            if Sygnal[i] > 3:
                CT += 2
            if Sygnal[i] == 1:
                CT+=1
    return CT
def GenerateFunc():
    FunctionView = {
        0: [4, "(XYX)Y(XYX)"],
        1: [4, "((XYX)YX)YX"],
        2: [3, "(XYX)YX"]
    }
    pirssheff = random.randint(0, 1)
    numfuncview = random.randint(0,2)
    F = FunctionView[numfuncview]
    if(pirssheff == 1):
        op = "|"
    else:
        op = "/"
    while( F[1].find("Y") > 0):
        i = F[1].find("Y")
        F[1] = F[1][:i] + op + F[1][i + 1:]#установили | or /
    if F[0] == 4:
        whichmore = random.randint(0,2)
        if (whichmore == 0):
            elmore = "A"
        if(whichmore == 1):
            elmore = "B"
        if(whichmore == 2):
            elmore = "C"
        i = F[1].find("X")
        F[1] = F[1][:i] + elmore + F[1][i + 1:]
    arrUsed = [0,0,0]
    for i  in range(arrUsed.__len__()):
        k = random.randint(0,2)
        flag =False
        while flag == False:
            if (arrUsed[k] == 0):
                flag = True
            else:
                k+=1
            if( k == 3):
                k = 0
        arrUsed[k] = 1
        if (k == 0):
            elmore = "A"
        if(k == 1):
            elmore = "B"
        if(k == 2):
            elmore = "C"
        i = F[1].find("X")
        F[1] = F[1][:i] + elmore + F[1][i + 1:]

    return [op,F[1]]
def GiveMeListOfLists():
    import pars
    ListOfLists = []
    func = GenerateFunc()#['pirs/sheff', 'func']
    otdaytablicu = pars.Recognizer(func[1],"task2")
    trtable = []
    for i in otdaytablicu:
        trtable.append(int(i[-1]))
    ZhegRes = ZhegalkinNameAnswer(trtable)
    CTZheg = 0
    for i in ZhegRes:
        CTZheg += (i.__len__()-1)*2
    CTZheg += (ZhegRes.__len__()-1)*2
    ListOfLists.append(["Zheg",CTZheg])
    for i in range(otdaytablicu.__len__()):
        for j in range(otdaytablicu[i].__len__()):
            otdaytablicu[i][j] = int(otdaytablicu[i][j])
    ListOfLists.append(["SNF", minimiz.TakeMinANDORNOT(otdaytablicu)])

    if (func[0] == '|'):
        ListOfLists.append(['sheff',CheckHowManyInput(func[1])])
    else:
        ListOfLists.append(['pirs',CheckHowManyInput(func[1])])
    ListOfLists.append(trtable)
    print("ZHEG RES:")
    print(ZhegRes)
    print("Pirs/Sheff RES:")
    print(func[1])
    print(ListOfLists)
    return ListOfLists