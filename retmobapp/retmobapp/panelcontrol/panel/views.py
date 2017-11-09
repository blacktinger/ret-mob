# -*- coding: utf-8 -*-
"""Panel views."""
from flask import Blueprint, render_template, request,Flask,current_app
from werkzeug.utils import secure_filename
import os
from forms import PanelForms,UFileForms
from flask import jsonify
from flask_wtf.csrf import CSRFProtect

blueprint = Blueprint('panel', __name__, url_prefix='/panel', static_folder='../static')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + '/retmobapp/static/uploads'



@blueprint.route('/')
def panel():
    """List members."""
    form = PanelForms(request.form)
    return render_template('panelcontrol/encheader.html',form=form)

# def allowed_file(self,filename):
#     ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
#     return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           
@blueprint.route('/upload', methods=['POST'])
def upload():
    print "a===============",os.getcwd()
    ufile = UFileForms(request)
    return ufile.validate()
    # if request.method == 'POST':
    #     file = request.files['kartik-input-705']
    #     print file
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         print os.path.join(app.config['UPLOAD_FOLDER'], filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         #上传成功
    #         return jsonify({'ok':True})
    return abort(403)



