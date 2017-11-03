from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired

class PanelForms(FlaskForm):
	"""docstring for PanelForms"""
	def __init__(self, arg):
		super(PanelForms, self).__init__()
		self.arg = arg
		
class UFileForms(FlaskForm):
	"""docstring for UFileFormsFlaskForm"""
	def __init__(self, arg):
		super(UFileForms,FlaskForms,self).__init__()
		self.arg = arg
		
		