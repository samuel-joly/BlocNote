#coding:utf-8

import tkinter as tk
import tk_listbox as Lbx
import tk_text as tkt
from threading import Timer

def pop_alert(text):
	Alert.config(text=text)
	Alert.grid(row=0, column=1, sticky='SW')
	wait = Timer(2, Alert.grid_remove)
	wait.start()

def creation_box(mode):
	NameEntry.delete(0, last=tk.END)
	tk.Label(CreationBox, text='Name:', justify=tk.LEFT).grid(row=0,column=0, sticky='SW')
	NameEntry.grid(row=0,column=1, sticky='SEW')
	CreationBox.grid(row=0, column=1, sticky='SW')
	NameEntry.focus_set()

	if mode == 'File':
		NameEntry.bind('<Return>',Lbx.add_file)
	elif mode =='Folder':
		NameEntry.bind('<Return>',Lbx.add_folder)





app = tk.Tk()
app.title('Bloc Note ~ Aze')
#=================GENERAL WIDGET=================
Background = tk.Frame(app)
Listbox = tk.Listbox(Background)
Text = tk.Text(Background, width = 60, wrap=tk.WORD)
Alert = tk.Message(Background, width=200, bg='white', text="", justify=tk.LEFT)


#=================CREATION BOX=================
CreationBox = tk.Frame(Background, background='light grey')
NameEntry = tk.Entry(CreationBox, width=73)


#=================Right-Click Menu=================
pop_menu = tk.Menu(app,tearoff=0)
pop_menu.add_command(label = 'Add File', command=lambda:creation_box("File"))
pop_menu.add_command(label='Add Folder', command=lambda:creation_box("Folder"))
pop_menu.add_command(label='Delete', command=Lbx.delete_content)


#=================GRID=================
Background.grid(row=0,column=0)
Listbox.grid(row=0, column=0, sticky='NSEW')
Text.grid(row=0,column=1, sticky='NSEW')


#=================BINDING=================
Listbox.bind('<<ListboxSelect>>',Lbx.Listbox_click)
Listbox.bind("<Button-3>", Lbx.do_pop_menu)

app.bind("<Control-KeyPress-w>", lambda command:app.quit())
app.bind("<Control-KeyPress-W>", lambda command:app.quit())

Text.bind("<Control-KeyPress-s>", tkt.save_text)
Text.bind("<Control-KeyPress-S>", tkt.save_text)

