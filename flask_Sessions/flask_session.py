"""
쿠키랑은 다르게 세션은 서버에 저장되어있는 데이터입니다.
세션은 서버의 임시 디렉토리에 저장되어 작동합니다. 각각의 
클라이언트는 세션 ID를 부여받습니다. 암호화가 된 데이터이기
때문에 Flask에서는 SECRET_KEY가 필요합니다.
"""

from flask import Flask, session, redirect, url_for, escape, request

app=Flask(__name__)
app.secret_key="asdfsdfg"

@app.route("/")
def index():
    if "username" in session:
        username=session["username"]
        return "Logged in as "+username+"<br>"+\
        "<b><a href='/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href='/login'></b>"+\
    "click here to log in</b></a>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        session["username"]=request.form["username"]
        return redirect(url_for("index"))
    return """
    <form action="" method="POST">
        <p><input type="text" name="username"/></p>
        <p><input type="submit" value="Login"/></p>
    </form>
            """

@app.route("/logout")
def logout():
    #유저가 세션 안에 있으면 삭제한다.
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ =="__main__":
    app.run(debug=True)