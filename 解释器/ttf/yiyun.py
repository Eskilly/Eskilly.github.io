from json import *
import requests as rq
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

inform={
		        "音乐":"song",
		        "歌词":"lyric",
		        "评论":"comments",
		        "详情":"detail",
		        "歌手":"artist",
		        "专辑":"album",
		        "歌单":"playlist",
		        "mv":"mv",
		        "主播电台":"djradio",
		        "单曲DJ":"dj",
		        "dj详情":"detail_dj",
		        "搜索关键字":""
		        }
headers = {
		        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
		        }
def downld():
	id=d.get()
	type=inform[com.get()]
	if type!="":
		url="https://api.imjad.cn/cloudmusic/?type="+type+"&id="+id
	else:
		url="http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={}&type=1&offset=0&total=true&limit=20".format(id)
	wb=rq.get(url,headers=headers)
	wbs=wb.content.decode("utf-8")
	data=loads(wbs)
	#data=dumps(data,indent=9,separators=(",",": "))
	text="信息:\n"+str(data)
	lb.insert(INSERT,text)
def down():
	ul=num.get()
	w=rq.get(ul,headers =headers)
	ws=w.content
	print(ws)
	
	
root=Tk()
root.geometry("300x300")
Label(root,text="输入关键字或id:",width=15).grid(row=0,column=0,sticky=E)
d=Entry(root,width=20)
d.grid(row=0,column=1,sticky=W)
Label(root,text="目标类型:").grid(row=1,column=0,sticky=E)
xVariable = StringVar()     # #创建变量，便于取值
 
com = ttk.Combobox(root, textvariable=xVariable)     # #创建下拉菜单
com.grid(row=1,column=1,sticky=W)     # #将下拉菜单绑定到窗体
com["value"] = tuple(inform.keys())    # #给下拉菜单设定值
com.current(2)    # #设定下拉菜单的默认值为第3个，即山东
 
 
com.bind("<<ComboboxSelected>>")     # #给下拉菜单绑定事件
Button(root,text="开始",command=downld).grid(row=2,column=1,sticky=W)
lb=scrolledtext.ScrolledText(root,bg="white")
lb.grid(columnspan=9,sticky=W+N)
root.mainloop()