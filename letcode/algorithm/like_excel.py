# coding:utf-8
import math

#arr:需要循环加字母的数组
#level：需要加的层级
def cycle_letter(arr,level):
    tempArr = []
    letterArr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',\
              'Q','R','S','T','U','V','W','X','Y','Z']
    arrNum = len(arr)
    if(level==0 or arrNum==0):
        return letterArr
    for index in range(arrNum):
        for letter in letterArr:
            tempArr.append(arr[index]+letter)
    return tempArr

#arr:需要生成的Excel列名称数目
def reduce_excel_col_name(num):
    tempVal = 1
    level = 1
    while(tempVal):
        tempVal = num/(math.pow(26, level))
        if(tempVal>1):
            level += 1
        else:
            break

    excelArr = []
    tempArr = []
    for index in range(level):
        tempArr = cycle_letter(tempArr,index)
        for numIndex in range(len(tempArr)):
            if(len(excelArr)<num):
                excelArr.append(tempArr[numIndex])
            else:
                return excelArr
    return excelArr

print(reduce_excel_col_name(27))