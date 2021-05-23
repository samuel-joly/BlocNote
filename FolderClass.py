#coding:utf-8
import os
from FileClass import File
import logging
import shutil

class Folder:
	total_folder = 0
	foldList = []
	mainFold = ''
	# Unwanted Files for mainFold in main.pyw
	unwanted_Files = ['tk_listbox.py',	'.git',			'.gitignore',	'Bloc Note.pyw',
					'FolderClass.py',	'icon.ico',	'blocNote.pyw',		'__pycache__',
					'tk_init.py', 		'FileClass.py',	'tk_text.py',
					'desktop.ini']


	def __init__(self, dirEntry):
		self._path = dirEntry.path
		self._contentList = []*len(os.listdir(dirEntry.path))

		self.dirEntry = dirEntry
		self.name = dirEntry.name
		self.lbx_name = ""
		

		
		if self.name != os.path.split(os.getcwd())[1]:
			Folder.total_folder += 1
			Folder.foldList.append(self)
		else:
			Folder.mainFold = self

		logging.info('FOLD - __init__ %s'%self)
		self.update_lbx_name()
		self.update_contentList()
		

	def __repr__(self):
			folderLen = len(self.contentList)
			return '"{}" with {} file(s) inside.'.format(self.name, folderLen)

	"""--------------------Folder Instance method -----------------------"""

	def update_contentList(self):
		logging.info('FOLD - update_contentList({})'.format(self.name))
		self.contentList = []
		try:
			for content in os.scandir(self.path):
				if content.name not in Folder.unwanted_Files:
					if content.is_dir():
						newFold = Folder(content)
						self.contentList.append(newFold)
						Folder.foldList.append(newFold)
						logging.info('FOLD - Add <{}> to {} contentList'.\
								format(newFold.name, self.name))

					elif content.is_file():
						newFile = File(content)
						self.contentList.append(newFile)
						Folder.foldList.append(newFile)
						logging.info('FOLD - Add <{}> to {} contentList'.\
								format(newFile.name, self.name))

		except Exception as exception:
			logging.error('FOLD - update_contentList({}) FAILED.'.format(type(exception).__name__))

	def update_lbx_name(self):
		logging.info('FOLD - update_lbx_name({}).'.format(self.name))

		try:
			parentFolder = os.path.dirname(self.path)
			parentFolder = Folder.get_folder_in_foldList(os.path.split(parentFolder)[-1])

			if parentFolder != None:
				while parentFolder != None:
					self.lbx_name += '   '
					parentFolder = Folder.get_folder_in_foldList(os.path.split(\
											os.path.dirname(parentFolder.path))[-1])
				self.lbx_name += self.name
				logging.info('FOLD - lbx_name -> %s'%(self.lbx_name))

			else:
				self.lbx_name = self.name
				logging.info('FOLD - lbx_name -> %s'%(self.lbx_name))

					
		except Exception as exception:
			logging.error('FOLD - update_lbx_name({}) FAILED:\n{}'.format(self.name, exception))

	def get_folder_in_foldList(searched_folderName):
		logging.info('FOLD - get_folder_in_foldList({})'.format(searched_folderName))

		try :
			if Folder.is_in_foldList(searched_folderName):
				for folder in Folder.foldList:
					if folder.name == searched_folderName \
					or folder.lbx_name == searched_folderName:
						logging.info('FOLD - Return <%s>' % folder)
						return folder
			else:
				return None

		except Exception as exception:
			logging.error('FOLD - get_folder_in_foldList({}) FAILED.'.\
					format(type(exception).__name__, searched_folderName))

	def is_in_foldList(searched_folderName):
		logging.info('FOLD - Folder.is_in_foldList({})'.format(searched_folderName))
		try:
			for folder in Folder.foldList:
				if folder.lbx_name == searched_folderName or folder.name == searched_folderName:
					logging.info("FOLD - YES")
					return True

			logging.info("FOLD - NO")
			return False

		except Exception as exception:
			logging.error("FOLD - Folder.is_in_foldList({}):\n{}".\
					format(searched_folderName,exception))

	def add_file(self, fileName):
		try:
			logging.info('FOLD - Adding file "%s" to %s'%(fileName, self.name))
			filePath = os.path.join(self.path,fileName)
			ofi = open(filePath, mode='w+', encoding='utf-8')
			ofi.close()
			self.update_contentList()

		except Exception as exception:
			logging.error('FOLD - Adding file "%s" to %s FAILED:\n %s'\
						%(fileName, self.name, exception))
	
	def add_folder(self, folderName):
		try:
			logging.info('FOLD - Adding folder "%s" to %s'%(folderName, self.name))
			folderPath = os.path.join(self.path,folderName)
			os.makedirs(folderPath)
			self.update_contentList()
		except Exception as exception:
			logging.error('FOLD - Adding folder "%s" to %s FAILED:\n %s'\
						%(fileName, self.name, exception))

	def delete_content(self, content):
		try:
			logging.info('FOLD - Deleting content "%s" to %s'%(content.name, self.name))
			if content.dirEntry.is_dir():
				shutil.rmtree(content.path)
			elif content.dirEntry.is_file():
				os.remove(content.path)

			self.update_contentList()

		except Exception as exception:
			logging.error('FOLD - Deleting file "%s" to %s FAILED:\n %s'\
						%(content.name, self.name, exception))
	"""-------------------- Folder Attribute property ----------------------"""


	def _get_Folder_path(self):
		try:
			return self._path
		except:
			logging.error('FOLD - Get path FAILED.\n')

	def _set_Folder_path(self, newPath):
		try:
			self._path = newPath
		except:
			logging.error('FOLD - Set newPath  FAILED.\n')


	def _get_Folder_contentList(self):
		try:
			return self._contentList
		except:
			logging.error('FOLD - Get contentList FAILED.\n')

	def _set_Folder_contentList(self, newContentList):
		try :
			self._contentList = newContentList
		except:
			logging.error('FOLD - Set contentList FAILED.\n')


	path = property(_get_Folder_path, _set_Folder_path)
	contentList = property(_get_Folder_contentList, _set_Folder_contentList)