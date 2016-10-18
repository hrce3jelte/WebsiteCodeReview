from flask import render_template, request, url_for, session, redirect
from User import User
from FormValidation.LogInForm import LogInForm


def LogIn():
    Form = LogInForm(request.form)
    if(request.method == "POST" and Form.validate()):
        if(User.LogIn(Form.PassWord.data, Form.Email.data)):
            UserLogInNow = User.GetUserByEmail(Form.Email.data)
            session["User"] = str(UserLogInNow)
            return redirect(url_for("Index"))
    return render_template("LogIn.html", form=Form)
