from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String

from app import db, login_manager
from app.base.util import hash_pass


class Admin(db.Model):
    __tablename__ = "Admin"
    __table_args__ = {'extend_existing': True}
    id = db.Column(Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(Binary)

    def __init__(self, username,email,password):
        self.username = username,
        self.email = email,
        self.password=hash_pass(password)

    # def __init__(self, **kwargs):
    #     for property, value in kwargs.items():
    #         # depending on whether value is an iterable or not, we must
    #         # unpack it's value (when **kwargs is request.form, some values
    #         # will be a 1-element list)
    #         if hasattr(value, '__iter__') and not isinstance(value, str):
    #             # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
    #             value = value[0]
    #
    #         if property == 'password':
    #             value = hash_pass(value)  # we need bytes here (not plain str)
    #
    #         setattr(self, property, value)

    def __repr__(self):
        return str(self.username)



def Admin_loader(id):
    return Admin.query.filter_by(id=id).first()


# @login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Admin.query.filter_by(username=username).first()
    return user if user else None


# admin = Admin({'username': 'saikiran', 'password': 'gonugunta', 'email': 'skiran252@gmail.com'})

