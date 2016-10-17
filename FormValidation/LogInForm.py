from wtforms import StringField, PasswordField, Form, validators

class LogInForm(Form):
    Email = StringField("Email", [validators.DataRequired()])
    PassWord = PasswordField("Password", [validators.DataRequired()])