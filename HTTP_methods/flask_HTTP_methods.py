#-*-coding:utf-8-*-
#http 프로토콜은 www에서 데이터 통신을 하는데 있어 가장 기본적인 방법이다.
#GET, HEAD, POST, PUT, DELETE 방법에 대해 간략하게 알아둘 것

#flask는 기본적으로 GET방식이다. 하지만 route()에서 명시적으로 선언하면 바꿀 수 있다.
#예제 login.html
"""
<html>
    <body>
        <form action="http://localhost:5000/login"  method="post">
            <p>Enter Name:</p>
            <p><input type="text" name ="nm" /></p>
            <p><input type="submit" value="submit" /></p>
        </form>
    </body>
</html>
"""

from flask import Flask, redirect, url_for, request
app=Flask(__name__)

@app.route("/success/<name>")
def success(name):
    return "welcome %s" %name

#flask app은 POST방식과 GET방식을 모두 받도록 설정할 수 있다.
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        #POST방식으로 받을 경우 request.form["input tag의 변수?"]
        user=request.form["nm"]
        return redirect(url_for("success", name=user))
    else:
        #GET방식으로 받을 경우 request.args.get("input tag의 변수?")
        user=request.method=="GET"
        user=request.args.get("nm")
        return redirect(url_for("success", name=user))

if __name__=="__main__":
    app.run(debug=True)