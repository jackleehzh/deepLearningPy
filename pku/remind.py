import time
#早上记忆控制程序
list11 =   [[[0, 7], [30, 32]]
          , [[7, 14], [39, 41]]
          , [[14, 21], [48, 50]]
          , [[21, 28], [50, 52]]
          , [[32, 39], [66, 68]]
          , [[41, 48], [71, 73]]
          , [[52, 59], [73, 75]]
          , [[59, 66], [88, 90]]
          , [[28, 30], [-1, -1]]
          , [[68, 71], [-1, -1]]
          , [[77, 88], [-1, -1]]
          ]

def printNewLine():
    #print('\n\n\n\n\n\n\n\n\n\n')
    pass
def test(n):
    for m in range(90):
        for i in range(11):
            if i != 9 and i != 4 and i != 10:
                if(m == list11[i][0][0]):
                    printNewLine()
                    print('开始第 ' + str(n + i) + ' 轮学习，时间 ' + str(list11[i][0][1] - list11[i][0][0]) + ' 分钟！')
                    break
                elif m == list11[i][1][0]:
                    printNewLine()
                    print('开始第 ' + str(n + i) + ' 轮复习，时间 ' + str(list11[i][1][1] - list11[i][1][0]) + ' 分钟！')
                    break
            elif m == list11[4][0][0]:
                printNewLine()
                print('休息一下吧！时间 ' + str(list11[4][0][1] - list11[4][0][0]) + ' 分钟！')
                break
            elif m == list11[9][0][0]:
                printNewLine()
                print('休息一下吧！时间 ' + str(list11[9][0][1] - list11[9][0][0]) + ' 分钟！')
                break
            elif i == 10 and m == list11[10][0][0]:
                printNewLine()
                print('总结一下吧! 时间 ' + str(list11[10][0][1] - list11[10][0][0]) + ' 分钟！')

def remind2(n, m):
    for i in range(11):
        if i != 9 and i != 4 and i != 10:
            if(m == list11[i][0][0]):
                printNewLine()
                print('开始第 ' + str(n + i) + ' 轮学习，时间 ' + str(list11[i][0][1] - list11[i][0][0]) + ' 分钟！')
                break
            elif m == list11[i][1][0]:
                printNewLine()
                print('开始第 ' + str(n + i) + ' 轮复习，时间 ' + str(list11[i][1][1] - list11[i][1][0]) + ' 分钟！')
                break
        elif m == list11[4][0][0]:
            printNewLine()
            print('休息一下吧！时间 ' + str(list11[4][0][1] - list11[4][0][0]) + ' 分钟！')
            break
        elif m == list11[9][0][0]:
            printNewLine()
            print('休息一下吧！时间 ' + str(list11[9][0][1] - list11[9][0][0]) + ' 分钟！')
            break
        elif i == 10 and m == list11[10][0][0]:
            printNewLine()
            print('总结一下吧! 时间 ' + str(list11[10][0][1] - list11[10][0][0]) + ' 分钟！')

def remind(dict1, list0, dict0):
   
    for key in dict1:
        i = dict0[key]
        s = list0[i]
        print(s)
        

#test(0)
#printNewLine()
#print('休息5分钟！')
#time.sleep(5)
#test(8)
