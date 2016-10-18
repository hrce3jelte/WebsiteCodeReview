from flask import Flask, render_template, session, request, url_for, redirect
from werkzeug.utils import secure_filename
from PythonBackend.Register import Register
from PythonBackend.LogIn import LogIn

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['py'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=["POST", "GET"])
def Index():
    if ("User" in session):
        if (request.method == "POST"):
            if ("file" not in request.files):
                return redirect(request.url)

            file = request.files["file"]

            if file.filename == "":
                return redirect(request.url)
            if file:
                filename = secure_filename(file.filename)
                file.save(app.config["UPLOAD_FOLDER"] + filename)

        print(session["User"])
        return render_template("indexLogedIn.html", User=session["User"], LogedIn=True)
    return render_template("index.html")


@app.route('/user/<username>')
def ShowUserProfile(username):
    # show the user profile for that user
    return render_template("UserName.html", UserName=username)


@app.route("/Register", methods=["POST", "GET"])
def register():
    return Register();


@app.route("/Clear")
def clear():
    session.clear()
    return redirect(url_for("Index"))


@app.route("/LogIn", methods=["POST", "GET"])
def login():
    return LogIn()


if __name__ == '__main__':
    app.secret_key = "123123123123"
    app.run(port=4995, debug=True)
