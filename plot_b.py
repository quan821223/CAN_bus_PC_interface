import matplotlib.pyplot as plt

# 设置三维坐标

b1 = []
z1 = []
v1 = []
x_time = []

b2 = []
z2 = []
x_time1 = []

b3 = []
z3 = []
x_time2 = []

b4 = []
z4 = []
x_time3 = []

b5 = []
z5 = []
x_time4 = []
with open('data/启动/current800rpm.txt', 'r') as f, open('data/启动/speed800rpm.txt', 'r') as f2:# open('data/b0/speed_1.5b0.txt', 'r') as f3:
    #open('data/position4.txt','r')as f4,open('data/position5.txt','r')as f5:
    data = f.read()
    data1 = f2.read()
    #data2 = f3.read()
    #data3 = f4.read()
    #data4 = f5.read()
    lines = data.split('\n')
    lines2 = data1.split('\n')
    #lines3 = data2.split('\n')
    #lines4 = data3.split('\n')
    #lines5 = data4.split('\n')
    for line in lines:
        if len(line) > 1:
            x1, vv1,position,  time = line.split(',')
            b1.append(300)
            z1.append(float(position))
            v1.append(float(vv1))
            x_time.append(float(time))

    for line in lines2:
        if len(line) > 1:
            x2, position1, time1 = line.split(',')
            b2.append(200)
            z3.append(float(x2))
            z2.append(float(position1))
            x_time1.append(float(time1))
    '''
    for line in lines3:
        if len(line) > 1:
            x3, position2, time2 = line.split(',')
            b3.append(100)
            z3.append(float(position2))
            x_time2.append(float(time2))
            
    for line in lines4:
        if len(line) > 1:
            x4, position3, time3 = line.split(',')
            b4.append(100)
            z4.append(float(position3))
            x_time3.append(float(time3))
    for line in lines5:
        if len(line) > 1:
            x5, position4, time4 = line.split(',')
            b5.append(100)
            z5.append(float(position4))
            x_time4.append(float(time4))

'''

Y1 = x_time
Y2 = x_time1
Y3 = x_time2
Y4 = x_time3
Y5 = x_time4

Z1 = z1
Z2 = z2
Z3 = z3
Z4 = z4
Z5 = z5

# 画2d图
plt.figure()
p1 = plt.subplot(211)
p2 = plt.subplot(212)
p1 = p2.twinx()  # 与ax1镜像
#plt.set_ylim=(0,500)
#plt.grid(True)
p1.plot(Y1, Z1, color='r',linewidth=1)#label=r'$b_0= 0.5b$')
p2.plot(Y2, Z2,color='b',linewidth=2.5,label='s')
p2.plot(Y2, Z3,color='k',linewidth=1.5,linestyle='-.',label='ref')
#p1.plot(Y3, Z3, color='#B22222',linestyle='-.', linewidth=2.5,label=r'$b_0= 1.5b$')
#plt.plot(Y4, Z4, 'y', linewidth=2, label='b0 = 3b')
#plt.plot(Y5, Z5, 'pink', linewidth=2, label='b0 = 4b')
p1.set_ylim(-6,6)
p2.set_ylim(0,900)
p2.set_xlim(0,4)
#plt.legend(loc='lower right')
plt.show()