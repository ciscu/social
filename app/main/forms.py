from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
TextAreaField
from flask import request
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
Length
from flask_babel import Babel, lazy_gettext as _l, _
from app.models import User


class editProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(editProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))

class postForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired(), Length(
        min=0, max=140)])
    submit = SubmitField(_l('Submit'))

class searchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(searchForm, self).__init__(*args, **kwargs)
