#Flask에서 파일을 업로드하는 것은 생각보다 간단하다.
#request.files와 함께라면 보다 손쉽게 파일 업로드 html을 만들 수 있다.

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app=Flask(__name__)


@app.route("/upload")
def upload_file():
    return render_template("upload.html")

@app.route("/uploader", methods=["GET","POST"])
def uploader():
    if request.method=="POST":
        UPLOAD_FOLDER = 'C:\\Users\\JJ\\Documents\\GitHub\\flask_tutorial\\flask_Upload_file\\data\\'
        app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
        
        f=request.files["file"]
        f.save(app.config["UPLOAD_FOLDER"]+secure_filename(f.filename))
        return "file uploaded successfully"

if __name__=="__main__":
    app.run(debug=True)