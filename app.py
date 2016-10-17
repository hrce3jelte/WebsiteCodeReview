from flask import Flask, render_template
from PythonBackend.Register import Register
from PythonBackend.LogIn import LogIn
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def Index():
    return "Jelte Boelens"


@app.route('/user/<username>')
def ShowUserProfile(username):
    # show the user profile for that user
    return render_template("UserName.html", UserName=username)


@app.route("/Register", methods=["POST", "GET"])
def register():
    return Register();

@app.route("/LogIn", methods=["POST", "GET"])
def login():
    return LogIn()
if __name__ == '__main__':
    app.run(port=4995, debug=True)
