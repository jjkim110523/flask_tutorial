from flask import Flask, render_template
app=Flask(__name__)

#디렉토리 구조를 만들어준다. ./static
@app.route("/static")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)