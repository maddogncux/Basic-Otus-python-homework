# flask app based on lesson 4

from flask import Flask, render_template
from flask_migrate import Migrate
# import config
from views.posts import post_app
from models import db
from os import getenv

app = Flask(__name__)

# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__)
#
#     @app.route("/", endpoint="index")
#     def index_page():
#         return render_template("index.html")
#     # # Simple route
#     # @app.route('/')
#     # def hello_world():
#     #     return jsonify({
#     #         "status": "success",
#     #         "message": "Hello World!"
#     #     })
#
#     return app

# app = create_app()

CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

db.app = app
db.init_app(app)
# db.drop_all()
migrate = Migrate(app, db, compare_type=True)

app.register_blueprint(post_app, url_prefix="/post/")

# with app.app_context():
# db.drop_all()
# db.create_all()
#   db.drop_all()


@app.route("/", endpoint="index")
def index_page():
    return render_template("index.html")


@app.route("/about/", endpoint="about")
def about_page():
    return render_template("about.html")


# @app.route("/post/", endpoint="posts")
# def post_page():
#     return render_template("posts.html")


@app.route("/cookies/", endpoint="Cookies")
def cookies_page():
    return render_template("Cookies.html")


if __name__ == "__main__":
    app.run(debug=True)
