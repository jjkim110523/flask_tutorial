#-*-coding:utf-8-*-

from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    #host, port, debug, options를 파라미터로 받는다.
    app.run(host="0.0.0.0", debug=True)

#서버를 파이썬으로 실행시킨 후 로컬호스트로 접속하여 hello world 글귀를 확인해본다.

