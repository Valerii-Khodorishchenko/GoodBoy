from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


from .models import MAX_LENGTH_NAME

MESSAGE_REQUIRED = 'Обязательное поле'
MESSAGE_TOO_LONG = 'Не длинее {} символов'.format(MAX_LENGTH_NAME)

ACTIVITY_NAME = 'Занятие'
ACTIVITY_DESCRIPTION = 'Описание'
SUBMIT = 'Создать'


class ActivityForm(FlaskForm):
    name = StringField(
        ACTIVITY_NAME,
        validators=(
            DataRequired(message=MESSAGE_REQUIRED),
            Length(max=MAX_LENGTH_NAME, message=MESSAGE_TOO_LONG)           
        )
    )
    description = TextAreaField(
        ACTIVITY_DESCRIPTION,
        validators=(
            Optional(),
        )
    )
    submit = SubmitField(SUBMIT)
