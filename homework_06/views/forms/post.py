from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CreatePostForm(FlaskForm):
    name = StringField(
        label="user name",
        name="user-name",
        validators=[
            DataRequired(),
            Length(min=6, max=16)
        ]
    )

    post = StringField(
        label="post",
        name="post-body",
        validators=[
            DataRequired(),
            Length(min=15, max=300),
        ]
    )
