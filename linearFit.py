#coding: UTF-8
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs


def inputData():
    #print("input x,y:")
    i = 0
    inData = [[], []]
    while True:
        #temp1, temp2 = (input("请输入X和Y的值").split())
        #print("请输入X和Y的值")
        temp1 = input("请输入X的值:")
        if not (str.isalpha(temp1) or temp1 == ''):
            temp2 = input("请输入Y的值:")
            if str.isalpha(temp2) or temp2 == '':
                break
            i = i + 1
            inData[0].append(eval(temp1))
            inData[1].append(eval(temp2))
        else:
            break
    print("输入了%d组数据" % i)
    return inData


while 1:
    inData = inputData()
    print(inData)
    flag = input('Right?')
    if flag == 'y':
        break

slope, intercept, rValue, pValue, stdErr = scs.linregress(inData[0], inData[1])#回归计算
#print(slope,intercept,rValue)
print("斜率:%f\n 截距:%f\n 相关系数r:%f" % (slope, intercept, rValue))
fitx = np.asarray(inData[0])#将list转化为narray方便计算
fity = fitx * slope + intercept
print("绘图参数:")
picTitle = input("标题:")
xLab = input("X轴标签:")
yLab = input("Y轴标签:")
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号，unicode符号
plt.scatter(inData[0], inData[1], color='w', edgecolors='r', marker='o')#绘制空心散点
plt.plot(fitx, fity, color='steelblue', linestyle='-')#绘制拟合曲线
plt.grid()
plt.title(picTitle)
plt.xlabel(xLab)
plt.ylabel(yLab)
plt.legend(["Fit line", "Data"])
plt.show()
