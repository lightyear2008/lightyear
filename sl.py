#0:空(已翻) 1-9:雷数显示(已翻) '?':未翻 '!':标记 'b':雷
import pgzrun
import random
import time

size_wide = 9
b_num = 8

WIDTH = 500
HEIGHT = 500

#二维列表及布雷
l1 = []
for n in range(size_wide**2):
    l1.append('?')
for n in range(b_num):
    l1[n] = 'b'
random.shuffle(l1)
l = []
for n in range(size_wide):
    l.append(l1[n*size_wide:(n+1)*size_wide])
del l1
for n in l:
    print(n)

#Actor二维列表
l_acts = []
for n in range(size_wide):
    l1 = []
    for i in range(size_wide):
        l1.append(Actor('cover.png'))
    l_acts.append(l1)
    del l1

#pos判断函数，参数(pos元组,格子的xy坐标，返回1或0)0032326464 0164329664 1032646496
#((y+1)*32,(x+1)*32)  ((y+2)*32,(x+2)*32)
def judge_pos(pos,x,y):
    if pos[0]>(y+1)*32 and pos[0]<(y+2)*32 and pos[1]>(x+1)*32 and pos[1]<(x+2)*32:
        return True
    return False

#设置显示数字函数,参数(x坐标,y坐标,显示的数字)
def give_num(x,y,num):
    if num == 0:
        l_acts[x][y].image = 'uncover.png'
    images = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png']
    for n in range(1,9):
        if num == n:
            l_acts[x][y].image = images[n-1]

#九宫格搜索函数,参数(x,y),返回应显示的数字0-8
def search(x,y):
    num = 0
    if x-1 >= 0:#上
        if l[x-1][y] == 'b' or l[x-1][y] == '!b':
            num += 1
    if x+1 < size_wide:#下
        if l[x+1][y] == 'b' or l[x+1][y] == '!b':
            num += 1
    if y-1 >= 0:#左
        if l[x][y-1] == 'b' or l[x][y-1] == '!b':
            num += 1
    if y+1 < size_wide:#右
        if l[x][y+1] == 'b' or l[x][y+1] == '!b':
            num += 1
    if y-1 >= 0 and x-1 >= 0:#左上
        if l[x-1][y-1] == 'b' or l[x-1][y-1] == '!b':
            num += 1
    if y+1 < size_wide and x-1 >= 0:#右上
        if l[x-1][y+1] == 'b' or l[x-1][y+1] == '!b':
            num += 1
    if y-1 >= 0 and x+1 < size_wide:#左下
        if l[x+1][y-1] == 'b' or l[x+1][y-1] == '!b':
            num += 1
    if y+1 < size_wide and x+1 < size_wide:#右下
        if l[x+1][y+1] == 'b' or l[x+1][y+1] == '!b':
            num += 1
    return num

#自动打开格子函数
def open(x,y):
    print('open')
    if l[x][y] == '?':
        give_num(x,y,search(x,y))
        if search(x,y) == 0:
            l[x][y] = 0
    if search(x,y) != 0:
        l[x][y] = search(x,y)
        return None

    if x-1 >= 0 and l[x-1][y] == '?':#上
        if search(x-1,y) == 0:
            open(x-1,y)
            l_acts[x-1][y].image = 'uncover.png'
            l[x-1][y] = 0
        else:
            give_num(x-1,y,search(x-1,y))
            l[x-1][y] = search(x-1,y)

    if x+1 < size_wide and l[x+1][y] == '?':#下
        if search(x+1,y) == 0:
            open(x+1,y)
            l_acts[x+1][y].image = 'uncover.png'
            l[x+1][y] = 0
        else:
            give_num(x+1,y,search(x+1,y))
            l[x+1][y] = search(x+1,y)

    if y-1 >= 0 and l[x][y-1] == '?':#左
        if search(x,y-1) == 0:
            open(x,y-1)
            l_acts[x][y-1].image = 'uncover.png'
            l[x][y-1] = 0
        else:
            give_num(x,y-1,search(x,y-1))
            l[x][y-1] = search(x,y-1)

    if y+1 < size_wide and l[x][y+1] == '?':#右
        if search(x,y+1) == 0:
            open(x,y+1)
            l_acts[x][y+1].image = 'uncover.png'
            l[x][y+1] = 0
        else:
            give_num(x,y+1,search(x,y+1))
            l[x][y+1] = search(x,y+1)

    if x-1 >= 0 and y-1 >= 0 and l[x-1][y-1] == '?':#左上
        if search(x-1,y-1) == 0:
            open(x-1,y-1)
            l_acts[x-1][y-1].image = 'uncover.png'
            l[x-1][y-1] = 0
        else:
            give_num(x-1,y-1,search(x-1,y-1))
            l[x-1][y-1] = search(x-1,y-1)

    if x-1 >= 0 and y+1 < size_wide and l[x-1][y+1] == '?':#右上
        if search(x-1,y+1) == 0:
            open(x-1,y+1)
            l_acts[x-1][y+1].image = 'uncover.png'
            l[x-1][y+1] = 0
        else:
            give_num(x-1,y+1,search(x-1,y+1))
            l[x-1][y+1] = search(x-1,y+1)

    if x+1 < size_wide and y-1 >= 0 and l[x+1][y-1] == '?':#左下
        if search(x+1,y-1) == 0:
            open(x+1,y-1)
            l_acts[x+1][y-1].image = 'uncover.png'
            l[x+1][y-1] = 0
        else:
            give_num(x+1,y-1,search(x+1,y-1))
            l[x+1][y-1] = search(x+1,y-1)

    if x+1 < size_wide and y+1 < size_wide and l[x+1][y+1] == '?':#右下
        if search(x+1,y+1) == 0:
            open(x+1,y+1)
            l_acts[x+1][y+1].image = 'uncover.png'
            l[x+1][y+1] = 0
        else:
            give_num(x+1,y+1,search(x+1,y+1))
            l[x+1][y+1] = search(x+1,y+1)

#库自带函数部分
background = Actor('background.png')

def draw():
    background.draw()
    acts_pos = [50,50]
    for n in l_acts:
        for i in n:
            i.draw()
            i.pos = (acts_pos[0],acts_pos[1])
            acts_pos[0] += 32
        acts_pos[1] += 32
        acts_pos[0] = 50

def on_mouse_down(pos,button):
    print(button,pos)
    for x in range(size_wide):
        for y in range(size_wide):
            if judge_pos(pos,x,y) and button == mouse.LEFT:#左键点击
                if l[x][y] == 'b':
                    print('end')
                    exit()
                if l[x][y] == '?':
                    open(x,y)
                    for n in l:
                        print(n)
                    print(search(x,y))
            if judge_pos(pos,x,y) and button == mouse.RIGHT:#右键点击
                if l[x][y] == '?':
                    l_acts[x][y].image = 'flag.png'
                    l[x][y] = '!'
                elif l[x][y] == 'b':
                    l_acts[x][y].image = 'flag.png'
                    l[x][y] = '!b'
                elif l[x][y] == '!':
                    l_acts[x][y].image = 'cover.png'
                    l[x][y] = '?'
                elif l[x][y] == '!b':
                    l_acts[x][y].image = 'cover.png'
                    l[x][y] = 'b'

def update():
    pass

pgzrun.go()