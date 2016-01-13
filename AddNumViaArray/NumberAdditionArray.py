from numpy.distutils.system_info import numarray_info

__author__ = 'Anup'

numberList=[1,1,1,1]

def addOne(n=1):
    reversedTempList=[]
    listLen=len(numberList)
    carry=0;
    isFirst=True
    for i in range(listLen-1,-1,-1):
        if isFirst:
            isFirst=False
            temp=numberList[i]+n+carry
        else:
            temp=numberList[i]+carry
        carry=0
        if temp>9:
            carry=1
            reversedTempList.insert(0,temp%10)
        else:
            reversedTempList.insert(0,temp)

    if carry==1:
        reversedTempList.insert(0,1)
    print reversedTempList


#n should be from 0 to 9 i.e one digit only
addOne(9)