"""
flask에서 자주 사용되는 데이터 형태는 다음과 같다.

Form: 딕셔너리 타입의 데이터로 key:value 형태로 구성되어있는 파라미터이다.
args: URL에서 ?다음에 해당하는 파라미터 값이다.
Cookies: 딕셔너리 타입의 데이터로 Cookie의 name과 value를 갖고 있다.
files: 업로드할 파일
method: 현재 request 방법이다.
"""

from flask import Flask, render_template, request
app=Flask(__name__)

#처음 홈페이지에 접속하면 student.html에 접속한다.
@app.route("/")
def student():
    return render_template("student.html")

#student.html에서 데이터를 받으면 result.html에 적용하여 렌더링 해준다.
@app.route("/result", methods=["POST","GET"])
def result():
    if request.method=="POST":
        result=request.form
        return render_template("result.html", result=result)

if __name__=="__main__":
    app.run(debug=True)