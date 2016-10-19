from flask import Flask, render_template, session, request, url_for, redirect
from PythonBackend import LogIn, Register, index

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(["zip" ,"rar"])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=["POST", "GET"])
def Index():
    return index(app.config["UPLOAD_FOLDER"])


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
