from FormValidation.RegistrationForm import RegistrationForm
from flask import request, redirect, render_template, url_for
from User import User

def Register():
    Form = RegistrationForm(request.form)
    if request.method == 'POST'and Form.validate():
        if(User.CheckIfEmailExists(Form.Email.data)):
            LogInUser = User(Form.FirstName.data, Form.LastName.data, Form.Email.data, Form.PassWord.data)
            LogInUser.WriteToFile()
            return redirect(url_for("Index"))
        return render_template("Register.html", form=Form, Error="Email already in use.",)
    return render_template("Register.html", form=Form,)

