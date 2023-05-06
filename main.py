from tkinter import *
import random
import csv

is_run = False

def str2int(s):
    ret = 0
    while s:
        d = int(s[-1]) - int('0')
        ret = ret * 10 + d
        s = s[:-1]
    return ret

def Run(list, bias):
    global is_run
    is_run = True
    Running(list, bias)

def Running(list, bias):
    result = random.choices(list, k=1) #使用random库中的choices函数进行随机
    var.set(result) #将随机结果传给TK窗口，并在窗口中显示随机的结果
    if is_run:
        window.after(50, Running, list, bias)
    else:
        result = random.choices(list, weights=bias, k=1) #使用random库中的choices函数进行随机
        var.set(result) #将随机结果传给TK窗口，并在窗口中显示随机的结果

def Stop():
    global is_run
    is_run = False

if __name__ == '__main__': #主程序
    stu_list = []
    csv_reader = csv.reader(open("同学名单.csv"))
    for row in csv_reader:
        stu_list.append(row)
    len = stu_list.__len__()

    bias = [1 for i in range(len)]
    csv_reader = csv.reader(open("cache.csv"))
    for row in csv_reader:
        bias[str2int(row[0]) - 1] = str2int(row[1])

    window = Tk() #初始化TK窗口
    window.geometry('720x480+250+150') #设定窗口大小
    window.resizable(0,0) #将窗口设置为不可拉伸
    window.title('抽签程序')

    var = StringVar() #初始化一个字符串变量，用于滚动显示抽奖结果

    noteLable = Label(font=("微软雅黑", 20), text="请抽签：")
    noteLable.place(anchor=CENTER, x=240, y=100)

    resultLable = Label(font=("微软雅黑", 40, "bold"), textvariable=var) #设置一个显示抽奖结果的文本框
    resultLable.place(anchor=CENTER,x=360,y=200)

    startBt = Button(font=("微软雅黑", 20), text="开始", command=lambda: Run(list=stu_list, bias=bias))
    confirmBt = Button(font=("微软雅黑", 20), text="确定", command=lambda: Stop())
    startBt.place(anchor=CENTER, x=240, y=320)
    confirmBt.place(anchor=CENTER, x=480, y=320)

    window.mainloop()