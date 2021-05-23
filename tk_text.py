#coding:utf -8

import FolderClass as Fclass
import tk_init as tki 
import logging
import tk_listbox

global Displayed

def save_text(event):
	try:
		lbxSelection = tki.Listbox.curselection()
		lbxSelection = Displayed
		curFile = Fclass.Folder.get_folder_in_foldList(lbxSelection)

		logging.info('TXT - Saving text from "%s"'%curFile.name)

		curFile.content =tki.Text.get(1.0, index2=tki.tk.END)
		with open(curFile.path, encoding='utf-8', mode='w') as ofi:
			ofi.write(curFile.content)

		tki.pop_alert('Saving text from "%s"'%curFile.name)

	except Exception as exception:
		logging.error('TXT - Saving {} FAILED:\n {}'.format(curFile.name, exception))



