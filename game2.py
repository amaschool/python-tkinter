import tkinter as tk
from tkinter import PhotoImage
from tkinter.constants import CENTER
from tkinter import messagebox


#從PIL套件載入Image及ImageTK二個模組
from PIL import ImageTk,Image
win = tk.Tk()
width=800
height=600
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
img=Image.open('bg.jpg').resize((width,height))
#利用ImageTK模組將載入進來的相片轉成TKinter的相片格式
photo=ImageTk.PhotoImage(img)
btn_photo=ImageTk.PhotoImage(Image.open('home.png').resize((60,60)))
canvas=tk.Canvas(win,width=width,height=height)
#建立按鈕
#text,width,height,bg,activebackground,fg,activeforeground,font,padx,pady,cursor,image
#寬度單位為字元,高度單度為行數
#padx內距,水平,單位 px
#command 參數,可以設定行為
#亘告按鈕按下去要呼叫的函式
#state 初始狀態
def btn_click():
    messagebox.showinfo("按鈕行為測試","您按到我了")

btn1=tk.Button(win,text='按我',
               # width=5,
               # height=1,
               padx=20,
               pady=5,
               font=('Microsoft Jhenghei',30,'bold'),
               cursor='hand2',
               bg='#131563',
               fg='#fff',
               activebackground='#1E4E27',
               activeforeground='#D83ED9',
               command=btn_click,
               image=btn_photo,
               compound='left',
               state=tk.DISABLED
               )
#建立畫布
#為畫面建立影像
#anchor 設定相片的註冊點 east(東,右) w(左) s(下) n(上)
canvas.create_image(0,0,anchor='nw',image=photo)
#使用相對座標relx(0~1) ,rely
btn1.place(relx=0.5,rely=0.5,anchor='center')
canvas.place(x=0,y=0)
# 設定視窗最小寬高
# win.minsize(width=400,height=200)
# 設定視窗最大寬高
# win.maxsize(width=800,height=600)


win.mainloop()


