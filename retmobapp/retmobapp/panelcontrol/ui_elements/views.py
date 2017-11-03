# -*- coding: utf-8 -*-
"""Panel views."""
from flask import Blueprint, render_template, request

blueprint = Blueprint('ui-elements', __name__, url_prefix='/ui-elements', static_folder='../static')

@blueprint.route('/')
def ui_elements():
	"""UI-ELEMENTS MEMBER"""
	return render_template('panelcontrol/ui-elements.html')

