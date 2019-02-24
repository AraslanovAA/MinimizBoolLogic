import math

import Recognize

global SDNF
SDNF = []
'''
def createSDNF(Lresults):
    i = 0
    N = int(math.log2(Lresults.__len__()))
    while(i < Lresults.__len__()):
        if(Lresults[i] ==1):

        i+=1
'''
def Recognizer():
    A = Recognize.vocabulary('A+B')
    #обработка ошибок длины строки
    A = A[2:len(A)-2]
    table =[]
    table = A.split('], [')
    for i in table:
        print(i)
def InputTable(Lresults):
    print(Lresults)
    while '' in Lresults:
        Lresults.pop(Lresults.index(''))
    while ' ' in Lresults:
        Lresults.pop(Lresults.index(' '))

    for i in Lresults:
        if(((i=='0') or (i=='1')) == False):
            print("Один из элементов списка говно")
            return -1#один из элементов списка говно подкрутить printerr?
    if Lresults.__len__() > 1:
        if not(math.log2(Lresults.__len__()).is_integer()):
            print("ты наверно забыл про 2^n")
            return -1#количество входных параметров нарушено
    else:
        print("so less")
        return -1#тут либо 1 входной либо 0, но как так?!
    #BinaryTest(int(math.log2(Lresults.__len__())))

def BinaryTest(N):
    print("start BinaryTest")
    print(N)
    A = bin(N)
    print(A)
    i = N.bit_length()
    i=i+1
    while(i!=1):
        print(A[i])
        i-=1
#InputTable(list(input()))

Recognizer()
