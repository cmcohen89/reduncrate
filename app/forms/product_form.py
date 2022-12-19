from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, URL


categories = {
    1: "Gear",
    2: "Style",
    3: "Cars",
    4: "Tech",
    5: "Shelter",
    6: "Vices",
    7: "Body",
    8: "Etc",
}


# ------------------------------ PRODUCT FORM ------------------------------ #


class ProductForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[
            DataRequired(),
            Length(min=4, message="A title of at least 4 characters would be better!"),
        ],
    )
    description = StringField(
        "Description",
        validators=[
            DataRequired("Make sure to provide a brief description!"),
            Length(
                min=10,
                message="A description of at least 10 characters would be better!",
            ),
        ],
    )
    detailed_description = TextAreaField(
        "Detailed Description",
        validators=[
            DataRequired("Please fill out the details section!"),
            Length(
                min=75,
                message="Give a few more details and your product will be more appealing! (Please provide at least 75 characters)",
            ),
        ],
    )
    category_id = SelectField(
        "Category",
        choices=[(k, v) for k, v in categories.items()],
        validators=[
            DataRequired(
                "You must select a category. Not sure? That's what Etc. is for!"
            )
        ],
    )
    price = IntegerField("Price", validators=[DataRequired(), NumberRange(0)])
    preview_img_url = StringField(
        "Preview Image URL",
        validators=[
            DataRequired(),
            Length(
                min=0,
                max=1500,
                message="The image URL must be less than 1500 characters.",
            ),
            URL(message="Please enter a valid URL for your image."),
        ],
    )
    submit = SubmitField("Submit")


class ProductUpdateForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[
            DataRequired(),
            Length(min=4, message="A title of at least 4 characters would be better!"),
        ],
    )
    description = StringField(
        "Description",
        validators=[
            DataRequired("Make sure to provide a brief description!"),
            Length(
                min=10,
                message="A description of at least 10 characters would be better!",
            ),
        ],
    )
    detailed_description = TextAreaField(
        "Detailed Description",
        validators=[
            DataRequired("Please fill out the details section!"),
            Length(
                min=75,
                message="Give a few more details and your product will be more appealing! (Please provide at least 75 characters)",
            ),
        ],
    )
    category_id = SelectField(
        "Category",
        choices=[(k, v) for k, v in categories.items()],
        validators=[
            DataRequired(
                "You must select a category. Not sure? That's what Etc. is for!"
            )
        ],
    )
    price = IntegerField("Price", validators=[DataRequired(), NumberRange(0)])
    submit = SubmitField("Submit")
