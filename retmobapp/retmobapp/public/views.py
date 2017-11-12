# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from retmobapp.extensions import login_manager
from retmobapp.public.forms import LoginForm
from retmobapp.user.forms import RegisterForm
from retmobapp.user.models import User
from retmobapp.utils import flash_errors

blueprint = Blueprint('public', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('You are logged in.', 'success')
            redirect_url = request.args.get('next') or url_for('user.members')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('public/home.html', form=form)


@blueprint.route('/logout/')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)


@blueprint.route('/about/')
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template('public/about.html', form=form)


@blueprint.route('/upload_task/')
def upload_task():
    return render_template('panelcontrol/upload_task.html')


@blueprint.route('/table/')
def table():
    return render_template('panelcontrol/table.html')

@blueprint.route('/chart/')
def chart():
    return render_template('panelcontrol/chart.html')

@blueprint.route('/tab-panel/')
def tabpanel():
    return render_template('panelcontrol/tab-panel.html')

@blueprint.route('/form/')
def form():
    return render_template('panelcontrol/form.html')    

@blueprint.route('/ui-elements/')
def ui_elements():
    """UI-ELEMENTS MEMBER"""
    return render_template('panelcontrol/ui-elements.html')


@blueprint.route('/empty')
def empty():
    return render_template('panelcontrol/empty.html')

@blueprint.route('/tasklist')
def tasklist():
    return render_template('panelcontrol/tasklist.html')
