#Cookies를 읽어오기 위해서는 make_response를 적용하여 set_cookie를 진행한 뒤
#request.cookies에서 get을 사용하면 된다.

from flask import Flask, render_template, request, make_response

app=Flask(__name__)

#작동 순서1: index 페이지에 들어가서 아이디를 입력하면 nm 이라는 변수명으로 /setcookie로 보낸다.
@app.route("/")
def index():
    return render_template("index.html")

#작동순서2: readcookie 페이지에서 nm값을 받아서 userID 쿠키를 만든다. 쿠키로 저장되어있다.
@app.route("/setcookie", methods=["POST", "GET"])
def setcookie():
    if request.method=="POST":
        user=request.form["nm"]

        resp=make_response(render_template("readcookie.html"))
        resp.set_cookie("userID", user)
    
    return resp

#작동순서3: setcookie에서 링크를 누르면 getcookie 페이지로 넘어가고 userID를 보여준다.
@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("userID")
    return "<h1>welcom " +name+ "</h1>"

if __name__=="__main__":
    app.run(debug=True)