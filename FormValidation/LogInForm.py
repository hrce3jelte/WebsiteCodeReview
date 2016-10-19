from wtforms import StringField, PasswordField, Form, validators


#simple form to login
class LogInForm(Form):
    Email = StringField("Email", [validators.DataRequired()])
    PassWord = PasswordField("Password", [validators.DataRequired()])