#-*-coding:utf-8-*-

#url_for() 함수는 특정 함수에 대해 URL을 동적으로 빌딩할 때 아주 유용하다.

from flask import Flask, redirect, url_for
app=Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello %s as Guest" %guest

@app.route("/user/<name>")
def hello_user(name):
    if name=="admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guest = name))

if __name__ == "__main__":
    app.run(debug=True)

#위 스크립트는 URL로 부터 유저의 이름을 받아 Hello <name>을 출력한다.
#URL의 이름 부분이 Admin일 경우와 Guest인 경우로 나누어져 있다.

#http://localhost:5000/user/admin
#http://localhost:5000/user/JJKim