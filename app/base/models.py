from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String

from app import db, login_manager

from app.base.util import hash_pass

# enduser model for database
class User(db.Model, UserMixin):

    __tablename__ = 'User'

    id        = db.Column(Integer, primary_key=True)
    username  = db.Column(db.String(255), unique=True,nullable=False)
    email     = db.Column(db.String(255), unique=True,nullable=False)
    firstname = db.Column(db.String(255), nullable=False)
    lastname  = db.Column(db.String(255), nullable=False)
    password  = db.Column(Binary)
    age       = db.Column(Integer)
    gender    = db.Column(db.String(10))
    mobile    = db.Column(db.String(11))
    address   = db.Column(db.String(255))
    zipcode   = db.Column(Integer)
    primary_care_physician = db.Column(db.String(255),default="Not assigned")
    Secondary_doctor       = db.Column(db.String(255),default="Not assigned")
    Hospital_name          = db.Column(db.String(255),default="Not assigned")
    membership_level       = db.Column(db.Integer,default=1)
    subscription_to_alerts = db.Column(db.Boolean,default=False)
    permission_for_doctor  = db.Column(db.Boolean,default=False)
    Health_conditions_of_interest = db.Column(db.String(255))

    #constructor
    
    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass( value ) # we need bytes here (not plain str)
            
            if property == 'permission_for_doctor' or property=='subscription_to_alerts':
                value = {True:1,False:0}[value=='y']
            
                
            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)
class Doctor(db.Model):
    __tablename__ = 'doctor'

    id        = db.Column(Integer, primary_key=True)
    username  = db.Column(db.String(255), unique=True,nullable=False)
    firstname = db.Column(db.String(255), nullable=False)
    lastname  = db.Column(db.String(255), nullable=False)
    password  = db.Column(Binary)
    subscription_to_alerts = db.Column(db.Boolean,default=False)
    address   = db.Column(db.String(255))
    Hospital_Affiliation= db.Column(db.String(255), nullable=False)
    Specialization      = db.Column(db.String(255), nullable=False)
    affiliated_patients = db.Column(db.String(255), nullable=False)
    Baseline_rules      = db.Column(db.String(255), nullable=False)
    contact_Number      = db.Column(db.String(15))

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]

            if property == 'password':
                value = hash_pass( value )
            
            if property == 'subscription_to_alerts':
                value = {True:1,False:0}[value=='y']
            
                
            setattr(self, property, value)

class device(db.Model):
    id          = db.Column(Integer, primary_key=True)
    type        = db.Column(db.String(255), nullable=False)
    ownerid     = db.Column(db.String(255), nullable=False)
    addeddate   = db.Column(db.DATETIME, nullable=False)
    specialization = db.Column(db.String(255),nullable=False)



@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None
    
class Admin(db.Model):
    __tablename__ = 'Admin'
    id = db.Column(Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(Binary)

    def __init__(self, args):
        self.username = args['username'],
        self.email = args['email'],
        self.password = hash_pass(args['password'])