
from wtforms import StringField,Form,FloatField
from wtforms.validators import Length,Email,EqualTo,InputRequired,NumberRange
from models import User
class ResgitForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[Length(max=20,min=6)])
    password = StringField(validators=[Length(min=6,max=16)])
    password_repeat = StringField(validators=[EqualTo('password')])
    deposit = FloatField(validators=[InputRequired()])


class LoginForm(Form):
    email = StringField(validators=[Email()])
    password = StringField(validators=[Length(min=6,max=16)])

    # def validate(self):
    #     result = super().validate()
    #     if not result:
    #         return False
    #
    #     email = self.email.data
    #     password = self.password.data
    #     user = User.query().filter(User.email==email,User.password==password).first()
    #     if not user:
    #         self.email.errors.append('邮箱或密码错误！')
    #
    #         return False
    #     return True

class TransferForm(Form):
    email = StringField(validators=[Email()])
    money = FloatField(validators=[NumberRange(1,1000000)])


