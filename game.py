import tkinter as tk
from tkinter import PhotoImage
from tkinter.constants import CENTER

#從PIL套件載入Image及ImageTK二個模組
from PIL import ImageTk,Image
win = tk.Tk()
width=600
height=400
# print(10//3)
#f-string
# print(f'寬度={width},高度={height}')
# 設定視窗標題
win.title("皇阿瑪數位學院")
# 設定視窗圖示
win.iconbitmap('dog.ico')
#取得螢幕寬度
s_width=win.winfo_screenwidth()
#取得螢幕高度
s_height=win.winfo_screenheight()
# print(s_height)
#設定x與y座標
x=(s_width-width)//2
y=(s_height-height)//2
# 設定視窗大小
win.geometry(f'{width}x{height}+{x}+{y}')

# 設定縮放功能
win.resizable(0, 0)
#將應用程式視窗設為最上層,不會被其它程式蓋過去
win.attributes('-topmost',1)
#設定視窗背景色
win.config(bg='#FF8EFF')
#利用Image模組的open方法去載入外部影像
img=Image.open('bg.jpg')
#利用ImageTK模組將載入進來的相片轉成TKinter的相片格式
photo=ImageTk.PhotoImage(img)
#建立畫布
canvas=tk.Canvas(win,width=width,height=height)
#為畫面建立影像
#anchor 設定相片的註冊點 east(東,右) w(左) s(下) n(上)
canvas.create_image(0,0,anchor='nw',image=photo)
canvas.place(x=0,y=0)
# 設定視窗最小寬高
# win.minsize(width=400,height=200)
# 設定視窗最大寬高
# win.maxsize(width=800,height=600)


win.mainloop()

# #函式
# def say_hello():
#     print('我是function函式')
#
# class Person:
#     def __init__(self):
#         self.name="皇阿瑪數位學院"
#     #方法
#     def set_name(self,name_):
#         self.name=name_
#     #方法
#     def show_name(self):
#         print(self.name)
# p1=Person()
# say_hello()
# p1.show_name()
# p2=Person()
# p2.set_name('hello kitty')
# p2.show_name()
