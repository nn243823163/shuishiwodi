#coding:utf-8
from Tkinter import *
import ttk
from PIL import Image, ImageTk
from packs_need.spyword import spywords
import random
import tkMessageBox
from tkSimpleDialog import askinteger

str_note = '''游戏规则：
1、游戏有卧底和平民两种身份；
2、平民得到同一词语，卧底得到与之相关的另一词语；
3、每人每轮用一句话描述自己的词语，既不能被卧底察觉，也要给同伴暗示；
4、每轮描述完毕，在场的所有人投票，选出怀疑谁是卧底的人，得票最多的人出局，
     若出现平局，平局的人进行描述，大家再投票选出一个卧底；
5、若有卧底撑到最后一轮（场上剩两人），则卧底获胜，反正平民获胜。

'''

#####定义全局变量#####

num = 0

# 卧底玩家
spy = 0

# 随机产生词语 定义词语列表 计算玩家票数的列表 统计死亡玩家的列表
list_rand = ()
word = []
cnt = []
dead = []

sameVote = 0
spyWin = 0

#####定义回调函数#####

def givewords():
    global num,word,cnt,dead,spy,sameVote,spyWin,list_rand
    list_rand = random.sample(spywords, 1)[0]
    num = int(number_chose.get())
    spy = random.randint(0, num - 1)
    print 'zongrenshu',num
    # 给三个列表赋值
    for i in range(0, num):
        word.append('a')
        cnt.append(0)
        dead.append(num + 2)
    # 给玩家词语 其中print是调试用的,sanmeVote是出现相同票数的标志，spyWin是卧底胜利的判决条件
    for i in range(0, num):
        if (i == spy):
            word[i] = str(list_rand[1])
        else:
            word[i] = str(list_rand[0])
        print (word[i])
        tkMessageBox.showinfo('请依次看单词',"第%d玩家的词语是：%s"%(i+1,word[i]))


def startgame():
    # player_choice['values'] = range(1,num+1)

    for i_lun in range(0,num-2):

            for i_ren in range(0,num):
                cnt[i_ren] = 0
                if i_ren not in dead:
                    tkMessageBox.showinfo('请发言','请%d玩家发言'%(i_ren+1))

            tkMessageBox.showinfo('开始投票','开始投票')

            for i_ren in range(0,num):
                if i_ren not in dead:
                    res = askinteger('请%d玩家投票'%(i_ren+1), "%d玩家您觉得卧底是："%(i_ren+1), initialvalue=0)
                    print res
                    cnt[res-1] = cnt[res-1]+1

            print cnt

            dead[i_lun] = cnt.index(max(cnt))
            if dead[i_lun] == spy:
                tkMessageBox.showinfo('卧底%d玩家被投出，游戏结束'%(dead[i_lun]+1),'卧底%d玩家被投出，游戏结束'%(dead[i_lun]+1))
                spyWin = 0
                break
            else:
                tkMessageBox.showinfo('%d玩家被冤死'%(dead[i_lun]+1),'%d玩家被冤死'%(dead[i_lun]+1))
                spyWin = 1
            print cnt

            tkMessageBox.showinfo('投票结束,进入下一轮','投票结束,进入下一轮')

    if spyWin:
        tkMessageBox.showinfo('卧底玩家%d获胜'%(spy+1),'卧底玩家%d获胜'%(spy+1))


def overgame():
    root.quit()



    print '单词是'

max_number = 8  #设置最大游戏人数

root = Tk()
root.title('谁是卧底')

frame1 = Frame(root,width=800,bg='green')
frame1.pack(fill=X)

load = Image.open('pic.jpg')
render= ImageTk.PhotoImage(load)
img = Label(frame1,image = render)
img.pack()

text1 = Label(frame1,text = "谁是卧底")
text1.pack()

tex2 = Label(frame1,text = str_note,justify = LEFT,anchor = 'w',bg = 'gray')
tex2.pack(fill = X)


frame2 = Frame(root,width=800,bg='red')
frame2.pack(fill = X)

number_chose = ttk.Combobox(frame2)
number_chose.config(width = 20 )
number_chose['values'] = (3,4,5,6,7,8)
number_chose.set('选择玩家个数')
number_chose.grid(row = 0 ,column=0)

button1 = Button(frame2,width = 20 ,text = '分配单词',command = givewords)
button1.grid(row = 0 ,column = 1)

button2 = Button(frame2,width = 20 ,text = '开始游戏',command  = startgame)
button2.grid(row = 0 ,column = 2)

#
# player_choice = ttk.Combobox(frame2)
# player_choice.config(width = 10)
# player_choice.grid(row = 0,column = 3)
# player_choice.set('选择玩家号码')
#
# button3 = Button(frame2,text = '投票',command  = givetickets)
# button3.grid(row = 0 ,column = 4)

button4 = Button(frame2,width = 20 ,text = '结束游戏',command  = overgame)
button4.grid(row = 0 ,column = 3)



root.mainloop()