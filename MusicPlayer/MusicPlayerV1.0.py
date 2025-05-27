import os
import time
import threading
import tkinter
from tkinter import messagebox
import pygame
import random

def file_deal():#筛选可播放文件
    list_origin = os.listdir(os.getcwd())
    print(os.listdir(os.getcwd()))
    list = []
    for n in list_origin:
        if n[-4:] == '.mp3':
            list.append(n)
    del list_origin
    if len(list) == 0:#没有可播放文件时报错
        messagebox.showerror('error','There is nothing can be play in the file')
        exit()
    random.shuffle(list)
    print(list)
    return list

class Window:
    def __init__(self):
        self.if_pause = 'unpaused'
        self.list = file_deal()
        self.num = 0

        self.root = tkinter.Tk()
        self.root.title('music player')
        self.root.geometry('350x150')
        self.root.resizable(False, False)
        self.bu_pause = tkinter.Button(self.root,command = self.pause,text = '▶',font = ('Arial',15),height = 2,width = 10)#播放暂停按钮
        self.bu_pause.place(x = 5,y = 5)
        self.bu_next = tkinter.Button(self.root,command = self.next,text = 'next',width = 7,height = 2)
        self.bu_next.place(x = 130,y = 5)
        self.la_now = tkinter.Label(self.root,text = 'now playing:'+self.list[0],font = ('Arial',15))
        self.la_now.place(x = 5,y = 70)
        self.la_version = tkinter.Label(self.root,text = 'Music Player V1.0   created by lightyear in 2025.5',font = ('Arial',10))
        self.la_version.place(x = 5,y = 130)

        self.run_thread()

    def pause(self):
        print('self_pause run',self.if_pause)
        if self.if_pause == 'paused':
            pygame.mixer.music.unpause()
            self.if_pause = 'unpaused'
            self.bu_pause.config(text = '⏸')
        elif self.if_pause == 'unpaused':
            pygame.mixer.music.pause()
            self.if_pause = 'paused'
            self.bu_pause.config(text = '▶')

    def next(self):
        pygame.mixer.music.stop()
        self.num += 1
        if self.num >= len(self.list):
            self.num = 0
        pygame.mixer.music.load(self.list[self.num])
        pygame.mixer.music.play()
        self.if_pause = 'unpaused'
        self.bu_pause.config(text='⏸')

    def play_thread(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.list[0])
        pygame.mixer.music.play()
        self.bu_pause.config(text='⏸')
        while True:
            time.sleep(0.5)
            try:
                self.la_now.config(text = 'now playing:'+self.list[self.num])
            except:
                print('shut down')
                exit()
            if pygame.mixer.music.get_busy() == 0 and self.if_pause == 'unpaused':
                self.num += 1
                if self.num >= len(self.list):
                    self.num = 0
                pygame.mixer.music.load(self.list[self.num])
                self.la_now.config(text = 'now playing:'+self.list[self.num])
                pygame.mixer.music.play()
                self.if_pause = 'unpaused'
                self.bu_pause.config(text='⏸')

    def run_thread(self):
        thread = threading.Thread(target = self.play_thread)
        thread.start()

if __name__ == '__main__':
    main = Window()
    main.root.mainloop()
