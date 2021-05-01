from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField , SubmitField, SelectField , TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from email_validator import validate_email
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    username = StringField('Enter Your Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Your Email Address',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("There's an account with that email")
    
    def validate_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("That user name is taken")


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')