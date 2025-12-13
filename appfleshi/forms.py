from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length, length, equal_to
from appfleshi.models import User

class PhotoForm(FlaskForm):
    photo = FileField('Foto', validators=[DataRequired()])
    caption = StringField('Legenda', validators=[Length(max=300)])
    submit = SubmitField('Postar')

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class RegisterForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Nome de Usuário', validators=[DataRequired(), length(min=2, max=20)])
    password = PasswordField('Senha', validators=[DataRequired(), length(min=6, max=60)])
    confirm_password = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Cadastrar')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            return ValidationError("E-mail já cadastrado!")
        return None