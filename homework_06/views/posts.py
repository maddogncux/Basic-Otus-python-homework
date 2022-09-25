from flask import Blueprint, render_template, request, url_for, redirect
# from werkzeug.exceptions import NotFound, BadRequest
from models import Post, db

from views.forms.post import CreatePostForm

post_app = Blueprint("post_app", __name__)

# USER ={
#     1 : "first ",
#     2 : "second",
#     3 : "i love cookies"
# }
# POST ={
#     1 : "first ",
#     2 : "second",
#     3 : "i love cookies"
# }


@post_app.route("/", endpoint="posts")
def get_post():
    post = Post.query.all()
    return render_template("post/posts.html", post=post)


@post_app.route("/<int:post_id>/", methods=["GET", "POST"], endpoint="one_post")
def get_one_post(post_id: int):
    # post_body = POST.get(post_id)
    # if post_body is None:
    #     raise NotFound(f"Post #{post_id} Not Found!")
    # if request.method == "GET":
    #     return render_template(
    #         "post/one_post.html",
    #     post_id = post_id,
    #     post_body = post_body,
    #     )
    # if request.method == "POST":
    # POST.pop(post_id)
    #

    # post = db.session.get(Post, post_id)
    # if post is None:
    #     raise NotFound(f"Post #{post_id} not found")

    post = Post.query.get_or_404(post_id, f"Post #{post_id} not found")
    if request.method == "GET":
        return render_template("post/one_post.html", post=post)

    # if request.method == "GET":
    #     post = Post.query.get_or_404(post_id, f"Post #{post_id} not found")
    #         return render_template("post/one_post.html", post=post)

    if request.method == "POST":
        db.session.delete(post)
        db.session.commit()
        return redirect("/post/")

    # return render_template("post/one_post.html", post=post)
    # return render_template("post/posts.html", )


@post_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_post():
    form = CreatePostForm()
    if request.method == "GET":
        return render_template("post/add_post.html", form=form)
    print(request.form)
    # post_name = request.form.get('user-name')
    # # post_name = post_name.strip()
    # if not post_name:
    #     raise BadRequest("Name cant be empty!")
    post_name = form.name.data
    # name_id = len(USER)+1
    # USER[name_id] = post_name

    # post_body = request.form.get('post-body')
    # if not post_body:
    #     raise BadRequest("post can't be empty!")
    post_body = form.post.data
    # post_id = len(POST) + 1
    # POST[post_id] = post_body

    post = Post(name=post_name, post=post_body)    # make chek for unic names
    db.session.add(post)
    db.session.commit()

    url = url_for("post_app.one_post", post_id=post.id)
    return redirect(url)
