from flask import render_template, request
from User import User
from FormValidation.LogInForm import LogInForm


def LogIn():
    Form = LogInForm(request.form)
    if(request.method == "POST" and Form.validate()):
        if(User.LogIn(Form.PassWord.data, Form.Email.data)):
            return ("LogIn")
    return render_template("LogIn.html", form=Form)
