from flask import session, request, redirect, render_template
from werkzeug.utils import secure_filename

#the index for the website it checks if you're logged in or not and then renders a template based on that
# there is also code to upload a file to the specified folder
#TODO make the upload thing more general
def index(UploadFolder):
    if ("User" in session):
        if (request.method == "POST"):
            if ("file" not in request.files):
                return redirect(request.url)

            file = request.files["file"]

            if file.filename == "":
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(UploadFolder + filename)

        print(session["User"])
        return render_template("indexLogedIn.html", User=session["User"], LogedIn=True)
    return render_template("index.html")