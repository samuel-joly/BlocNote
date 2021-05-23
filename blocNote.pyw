#coding: utf-8

import os
import FolderClass 
import FileClass
import tk_init as tki
import logging

logging.basicConfig(level = logging.DEBUG,\
		format=' %(asctime)s - %(levelname)s - %(message)s',datefmt='%H:%M:%S')


"""----------Init Current Working Directory folder-----------"""

for content in os.scandir(os.path.split(os.getcwd())[0]):
	if content.name == os.path.split(os.getcwd())[1]:
		mainFold = FolderClass.Folder(content)


for content in mainFold.contentList:
	if content.dirEntry.is_dir():
		tki.Listbox.insert(tki.tk.END, content.lbx_name)
		tki.Listbox.itemconfig(tki.tk.END, foreground='blue')
	elif content.dirEntry.is_file():
		tki.Listbox.insert(tki.tk.END, content.lbx_name)
		tki.Listbox.itemconfig(tki.tk.END, foreground='red')


"""--------------------Tkinter----------------------------"""


tki.app.mainloop()