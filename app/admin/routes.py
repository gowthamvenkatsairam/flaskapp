from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (current_user, login_required, login_user, logout_user)
from jinja2 import TemplateNotFound
from app import db, login_manager
from app.admin import blueprint
from app.admin.forms import AdminLoginForm

from app.base.util import verify_pass

from app.admin.models import  Admin


@blueprint.route('/admin', methods=['GET', 'POST'])
def admin():
    return redirect(url_for('admin_blueprint.adminlogin'))

@blueprint.route('/adminlogin',methods=['POST'])
def login():
    admin_login = AdminLoginForm(request.form)

    if 'login' in request.form:
        username = request.form['username']
        password = request.form['password']
        # Locate user
        adminuser = Admin.query.filter_by(username=username).first()

        # Check the password
        if adminuser and verify_pass(password, adminuser.password):
            login_user(adminuser)
            print("admin logged in")
            return redirect(url_for('admin_blueprint.adminlogin'))

        # Something (user or pass) is not ok
        return render_template('adminlogin.html', msg='Wrong user or password', form=admin_login)

    if not current_user.is_authenticated:
        return render_template('adminlogin.html',
                               form=admin_login)
    return redirect(url_for('admin_blueprint.adminlogin'))
