from wtforms import Form, StringField, EmailField, PasswordField, validators, ValidationError, DateField
from wtforms.validators import DataRequired


class CustomerRegisterForm(Form):
   firstname = StringField("First Name:", [validators.DataRequired(
    ), validators.length(min=1, max=20, message=''), validators.Regexp(r'^[a-zA-Z]+$', message='First name should contain only letters')])
   lastname = StringField("Last Name:", [validators.DataRequired(), validators.length(
        min=1, max=20), validators.Regexp(r'^[a-zA-Z]+$', message='Last name should contain only letters')])
   email = EmailField('Email:', [validators.Email(), validators.DataRequired()])
   password = PasswordField('Password:', validators=[validators.Length(min=8, max=20, message='Password must be at least 8 characters long. Maximum is 20.'), validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match.')])
   confirm = PasswordField('Confirm password')
   dob = DateField("Date of Birth:", format='%Y-%m-%d',
                        validators=[DataRequired()])
   contactnumber = StringField("Contact Number:", [validators.DataRequired(), validators.Regexp('^[0-9]*$', message="Contact number can only contain numbers"), validators.length(min=8, max=8)])


class UserLoginForm(Form):
   email = EmailField('Email:', [validators.Email(), validators.DataRequired()])
   password = PasswordField('Password:', validators=[validators.Length(min=8, max=20, message='Password must be at least 8 characters long. Maximum is 20.'), validators.DataRequired()])

