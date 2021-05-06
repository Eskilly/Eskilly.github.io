from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
from tkinter import messagebox
from Texteditor import menumain
import os
import down
import jisuanqi



 
window = Tk()
frame = Frame(window)
frame.pack()
w = Label(frame,text="输入")
w.pack()
bar=Notebook(frame)
def op():#打开文件
	name=askopenfilename()
	if name==():
		name=""
	nm=os.path.basename(name)
	tb=Frame(bar)
	bar.add(tb,text=nm)
	bar.pack(fill=X)
	try:
		with open(name,"r",encoding="utf-8") as f:
			date=f.read()
		name_input.insert(INSERT,date)
	except:
		pass

def clc():
	jisuanqi.Clcl()

def player():
	import playerfile
	try:
		playerfile.Player()
	except:
		return

def clear():
	name_input.delete(1.0, END)

def download():
	from ttf import yiyun

def paint():
	#画布
	from ttf import drawing

def pro():
	menumain.mu(window,name_input)
	
#运行器
window.geometry('500x500')
#文本框
name_input = ScrolledText(window,state='normal',width='200',height='10',wrap='word', pady=2, padx=3, undo=True)		# width宽 height高
name_input.pack()
name_input.focus_set()
menubar=Menu(window)
menubar.add_command(label='退出',command= window.destroy)
openmenu=Menu(menubar,tearoff=False)

openmenu.add_command(label='打开',command= op)

openmenu.add_command(label='音乐',command=player)
openmenu.add_command(label='歌曲信息',command=download)
menubar.add_cascade(label='文件',menu=openmenu)
menubar.add_command(label='画布',command=paint)
menubar.add_command(label='清空',command=clear)
menubar.add_command(label='文本编辑',command=pro)
menubar.add_command(label='计算器',command=clc)

window["menu"]=menubar 


#警示弹窗
def print_name():
	try:
		exec(name_input.get('1.0',END))
	except:
		messagebox.showinfo("警告！", "错误，点击继续。")	
		
Button(window,text='运行turtle',command=print_name).pack(side="left")




window.mainloop()

