from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField,SelectField,BooleanField
from wtforms.validators import InputRequired, Email, DataRequired,Length
## login and registration
class LoginForm(FlaskForm):
    username = TextField    ('Username', id='username_login'   , validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login'        , validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username  = TextField('Username'     , id='username_create' , validators=[DataRequired()])
    email     = TextField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
    password  = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])
    firstname = TextField('firstname'    , id="first_name"      , validators=[DataRequired()])
    lastname  = TextField('lastname'     , id="last_name"      , validators=[DataRequired()])
    age       = SelectField('age'        , id="age",default="select your age ", choices=[(number,str(number)) for number in range(1,100)],validators=[DataRequired()])
    gender    = SelectField('gender'     , id='gender',choices=[('Male', 'Male'),('Female', 'Female')],validators=[DataRequired()])
    mobile    = TextField('mobile'       , id="mobile_field"     , validators=[DataRequired(),Length(min=10,max=11)])
    address   = TextField('address'      , id="address_field"    , validators=[DataRequired()])
    zipcode   = TextField('zipcode'      , id = 'zipcode_field',validators=[DataRequired()])
    primary_care_physician = TextField('primary_care_physician'   , id = 'primary_care_physician_field', validators=[DataRequired()])
    Secondary_doctor       = TextField('Secondary_doctor'         , id = 'Secondary_doctor_field',validators=[DataRequired()])
    Hospital_name          = TextField('Hospital_name'            , id = 'Hospital_name_field',validators=[DataRequired()])
    Health_conditions_of_interest=TextField('Health_conditions_of_interest' , id="Health_conditions_of_interest_field", validators=[DataRequired()])
    membership_level       = SelectField('membership_level'       ,choices=[(number,str(number)) for number in range(1,5)], id = 'membership_level_field',validators=[DataRequired()])
    subscription_to_alerts = BooleanField('subscription_to_alerts',id = 'subscription_to_alerts_field')
    permission_for_doctor  = BooleanField('permission_for_doctor ', id = 'permission_for_doctor_field')

class Doctorform(FlaskForm):
    username  = TextField('Username'     , id='username_create' , validators=[DataRequired()])
    password  = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])
    firstname = TextField('firstname'    , id="first_name"      , validators=[DataRequired()])
    lastname  = TextField('lastname'     , id="last_name"      , validators=[DataRequired()])
    address   = TextField('address'      , id="address_field"    , validators=[DataRequired()])
    subscription_to_alerts = BooleanField('subscription_to_alerts',id = 'subscription_to_alerts_field')
    Hospital_Affiliation   = TextField('Hospital_Affiliation'     ,id="Hospital_Affiliation_field" , validators=[DataRequired()])
    Specialization         = TextField('Specialization'           ,id="Specialization_field"       , validators=[DataRequired()])
    affiliated_patients    = TextField('affiliated_patients'      ,id="affiliated_patients_field"  , validators=[DataRequired()])
    Baseline_rules         = TextField('Baseline_rules '          ,id="Baseline_rules_field"       , validators=[DataRequired()])
    contact_Number         = TextField('contact_Number'           ,id="contact_Number_field"       , validators=[DataRequired(),Length(min=9,max=15)])