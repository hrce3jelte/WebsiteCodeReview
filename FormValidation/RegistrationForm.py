from wtforms import  StringField, validators, Form, PasswordField
from wtforms.fields.html5 import EmailField

#simple form to register
class RegistrationForm(Form):
    FirstName = StringField('FirstName', [validators.Length(min=4, max=25), validators.DataRequired()])
    LastName = StringField('LastName', [validators.Length(min=4, max=25), validators.DataRequired()])
    Email = EmailField('Email', [validators.Length(min=6, max=35), validators.DataRequired(), validators.Email()])
    PassWord = PasswordField("Password", [validators.DataRequired(), validators.EqualTo("Confirm", message="Password must match")])
    Confirm = PasswordField("Repeat Password")