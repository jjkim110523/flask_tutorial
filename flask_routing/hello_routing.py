from flask import Flask

#다른 방법으로도 url route를 추가할 수 있다.

app=Flask(__name__)

#@app.route("/hello")

def hello_world():
    return "hello world"

app.add_url_rule("/hello", "hello_world", hello_world)

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)