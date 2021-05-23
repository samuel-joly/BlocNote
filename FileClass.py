#coding:utf-8

import os
import logging
import FolderClass
#logging.disable(logging.INFO)


class File:
	
	total_file = 0
	

	def __init__(self, dirEntry):
		self._path = dirEntry.path
		self._content = ""
		self.dirEntry = dirEntry
		self.name = dirEntry.name
		self.lbx_name = ""

		File.total_file += 1
		logging.info('FILE - __init__ %s'% self.name)

		self.update_lbx_name()
		self.update_content()

	def __repr__(self):
		return 'FILE "{}"'.format(self.name, self.path)

	"""-------------------- File instance method -------------------------"""

	def update_content(self):
		logging.info('FILE - "{}" Update content.'.format(self.name))
		try:
			with open(self.path, "r", encoding='utf-8') as ofi:
				self.content = ofi.read()

		except Exception as exception:
			logging.error('FILE - {} Update content FAILED.\n'.format(exception))

	def update_lbx_name(self):
		logging.info('FILE - update_lbx_name({}).'.format(self.name))

		try:
			parentFolder = os.path.dirname(self.path)
			parentFolder = FolderClass.Folder.get_folder_in_foldList(os.path.split(parentFolder)[1])

			if parentFolder != None:
				while parentFolder != None:
					self.lbx_name += '   '
					parentFolder = FolderClass.Folder.get_folder_in_foldList(os.path.split(\
											os.path.dirname(parentFolder.path))[1])
				self.lbx_name += self.name
				logging.info('FILE - lbx_name -> %s'%(self.lbx_name))
			else:
				self.lbx_name = self.name
				logging.info('FILE - lbx_name -> %s'%(self.lbx_name))

					
		except Exception as exception:
			logging.error('FOLD - update_lbx_name({}) FAILED:\n{}'.format(self.name, exception))
	
	"""-------------------- File Attribute property ----------------------"""
	
	def _get_File_path(self):

		try:
			return self._path
		except:
			logging.error('FILE - Get path FAILED.')

	def _set_File_path(self, newPath):

		try:
			self._path = newPath
		except:
			logging.error('FILE - Set newPath  FAILED.')



	def _get_File_content(self):
		try:
			return self._content
		except:
			logging.error('FILE - Get content FAILED.')

	def _set_File_content(self, newContent):
		try :
			self._content = newContent
		except:
			logging.error('FILE - Set content FAILED.')

	




	path = property(_get_File_path, _set_File_path)
	content = property(_get_File_content, _set_File_content)