# -*- coding: utf-8 -*-
"""Tasks models."""
import datetime as dt

from retmobapp.database import Column, Model, SurrogatePK, db, reference_col, relationship
from retmobapp.extensions import bcrypt


class FileMap(SurrogatePK, Model):
	"""docstring for Tasks"""
	__tablename__ = 'filemap'
	file_url = Column(db.String(128), nullable=False)
	auth_key = Column(db.String(30), nullable=False)
	file_orig_name = Column(db.String(128), nullable=False)

	# def __init__(self, arg):
	# 	super(Tasks, self).__init__()
	# 	pass
	def __init__(self, file_url, auth_key , file_orig_name,**kwargs):
		"""Create instance."""
		db.Model.__init__(self, file_url=file_url, auth_key=auth_key, file_orig_name=file_orig_name, **kwargs)
        # super(Tasks, self).__init__()
