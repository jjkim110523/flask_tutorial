#form 필드를 아주 간단하게 자동으로 작성할 수 있는 기능이다.
#텍스트, 체크박스, 숫자, 라디오버튼, 드롭다운, 텍스트 영역,
#패스워드, 제출버튼이 있다.

#또한 validator class가 있어 양식을 만드는데 있어 필요충분 조건을
#확인할 수 있다.

from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, SelectField, RadioField

from wtforms import validators, ValidationError

class ContactForm(Form):
    name=TextField("Name of Student", [validators.Required("Please enter your name.")])

    Gender=RadioField("Gender", choices=[("M", "Male"), ("F", "Female")])
    Address=TextAreaField("Address")

    email=TextField("Email", [validators.Required("Please enter your email address."),
    validators.Email("Please enter your email address.")])

    Age=IntegerField("age")
    language=SelectField("Languages", choices=[("cpp","C++"), ("py","Python")])

    submit=SubmitField("Send")