from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
from Texteditor import file_menu
from Texteditor import edit_menu
from Texteditor import format_menu
from Texteditor import help_menu

class mu:
	def __init__(self,root,text):
		self.root=root
		self.text=text
		menubar = Menu(self.root)
		file_menu.main(self.root, self.text, menubar)
		edit_menu.main(self.root, self.text, menubar)
		format_menu.main(self.root, self.text, menubar)
		help_menu.main(self.root, self.text, menubar)


