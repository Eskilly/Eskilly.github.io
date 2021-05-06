#-*-utf-8-*-
from tkinter import *
import math as i
π=i.pi
e=i.e
sqrt=i.sqrt
sin=i.sin
cos=i.cos
tan=i.tan
class Clcl:
	def __init__(self):
		reset=True
		def buttonCallBack(event):
		    global reset
		    num=event.widget['text']
		    if num=='C':
		        label['text']="0"
		        return 
		    if num in "=":
		        try:
		        	label['text']=str(round(eval(label['text']),4))
		        	reset=True
		        except:
		        	label["text"]="格式错误"
		        return 
		    if num =="Del":
		        a=label["text"]
		        a=a[:-1]
		        label["text"]=a
		        return
		  
		    s=label['text']
		    if s=='0' or reset==True:
		        s=""
		        reset=False
		    label['text']=s+num
		#主窗口
		root=Tk()
		root.title("计算器")
		#显示栏1
		menubar=Menu(root)
		menubar.add_command(label='退出',command= root.destroy)
		root["menu"]=menubar
		label=Label(root,text="0",background="white",anchor="e")
		label['width']=35
		label['height']=5
		label.grid(row=1,columnspan=4,sticky=W)
		#钮
		showText="123/456*789-0.C+"
		for i in range(4):
		    for j in range(4):
		        b=Button(root,text=showText[i*4+j],width=7)
		        b.grid(row=i+2,column=j)
		        b.bind("<Button-1>",buttonCallBack)
		showText="()"
		for i in range(2):
		    b=Button(root,text=showText[i],width=7)
		    b.grid(row=6,column=2+i)
		    b.bind("<Button-1>",buttonCallBack)
		b=Button(root,text="=")
		b.grid(row=6,columnspan=2,sticky="we")
		b.bind("<Button-1>",buttonCallBack)
		showText=["sin","cos","tan","e"]
		for i in range(4):
		    b=Button(root,text=showText[i],width=7)
		    b.grid(row=7, column=i)
		    b.bind("<Button-1>",buttonCallBack)
		showText=["π","sqrt","abs","%"]
		for i in range(4):
		    b=Button(root,text=showText[i],width=7)
		    b.grid(row=8,column=i)
		    b.bind("<Button-1>",buttonCallBack) 
		b=Button(root,text="Del" )
		b.grid(row=9,columnspan=4,sticky="we")
		b.bind("<Button-1>",buttonCallBack) 
		
		
		root.mainloop()

	