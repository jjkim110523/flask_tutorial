#Jinja2 template engine을 통해 편리하게 html rendering을 실행할 수 있다.

#수작업의 예시
from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def index():
    return "<html><body><h1>'Hello World!'</h1><body></html>"

#템플릿을 사용하기 위해서는 우선 디텍터리 구조를 알아야한다.

#어플리케이션 폴더
##ㄴHello.py(flask framework file)
##ㄴtemplates(템플릿 폴더)
####ㄴhello.html(템플릿 폴더 안에 html)

#디렉토리 구조를 세팅해줘야 정상적으로 작동한다.

@app.route("/hello/<user>")
def hello_name(user):
    return render_template("hello.html", name=user)

@app.route("/hello/score/<int:score>")
def hello_score(score):
    return render_template("hello_score.html", marks=score)

@app.route("/result")
def result():
    dict={"phy":50, "che":60, "maths":70}
    return render_template("result.html", result=dict)

if __name__=="__main__":
    app.run(debug=True)

#Jinga2와 관련된 정보
#{%...%} Statements
#{{...}} print 하고 싶은 정보
#{#...#} 주석처리
#...# #for Line Statement