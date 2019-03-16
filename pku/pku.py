# encoding=utf8 
import time
import threading

import remind
import rw

def maxNum(filename):
    f = open(filename, encoding='utf8')
    count = 0
    maxnum = 0
  
    while True:
        line = f.readline()
        if not line:
            break

        line = line.strip()
        if count > 0:
            num = int(line[line.rfind('【') + 1:-1]) 
            if num > maxnum:
                maxnum = num
                
        count = count + 1
    print(maxnum)            
    f.close()

filename1 = '2020.txt'
filename2 = '2020-2.txt'

def getTime(list0):
    dict0 = {}
    for a in list0:
        arr = a.split(' ')
        dict0[arr[0]] = int(arr[6])
    return dict0

def remindMe(list0, dict0, dict2):
    while True:
        t = int(time.time())
        maxnum = 0
        dict1 = {}
        
        for key in dict2:
            t2 = t - dict2[key]
            if t2 >= 250 and t2 <= 3000:
                if maxnum < t2:
                    maxnum = t2
                dict1[key] = t2
                
        t1 = 3000 - maxnum
        if t1 > 0:
            for key in dict1:
                dict1[key] = dict1[key] + t1
 #           time.sleep(t1)
        remind.remind(dict1, list0, dict0)
        time.sleep(2)

def show(filename1, filename2):
    list0, dict0 = rw.loadData(filename1)
    list2 = rw.loadInfo(filename2)
    dict2 = getTime(list2)
    t = threading.Thread(target=remindMe,args=(list0, dict0, dict2))
    t.setDaemon(True) ## thread1,它做为程序主线程的守护线程,当主线程退出时,thread1线程也会退出,由thread1启动的其它子线程会同时退出,不管是否执行完任务
    t.start()
    layer = 0
    uplayerBeginline = 0
    sameLayer = False
    while True:
        count = 0
        count2 = 0
        list3 = [0]
        begin = False
        
        for a in list0:
            c = a.count('	')
            a = a.strip()
            
            if begin and c < layer:
                uplayerBeginline = list3[0]
                break
            if c < layer - 1:
                sameLayer = False
            if c == layer - 1 and sameLayer == False:
                list3[0] = count
                sameLayer = True
            if c == layer and count >= uplayerBeginline:
                begin = True
                if count2 == 0:
                    print('b.\t返回上一层')
                    print('a.\t增加内容')
                    print('d.\t删除内容')
                    print('m.\t修改内容')
                    print('e.\t退出')
                    print('-------------------')
                count2 = count2 + 1                      
                print(str(count2) + '.\t' + a[:a.find('【')])
                list3.append(count)
 
            count = count + 1
                
        
        #print(list3)
        list2 = rw.updateInfo(list3, list2)
        rw.writeFile(filename2, list2)
        num = input("请输入：")
        if num == 'e':
            return
        elif num == 'b':
            num = 0
            layer = layer - 1
        else:
            num = int(num)
            if num == -1:
                break
            layer = layer + 1
        uplayerBeginline = list3[num]
        
    return list3    

show(filename1, filename2)
