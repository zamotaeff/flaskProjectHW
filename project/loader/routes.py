from flask import Blueprint, render_template, request

from .functions import add_new_post


loader_blueprint = Blueprint('loader_blueprint',
                             __name__,
                             template_folder='templates')


@loader_blueprint.route("/post/", methods=["GET"])
def page_post_form():
    """Предсталение для страницы загрузки нового поста"""

    return render_template('post_form.html')


@loader_blueprint.route("/post/", methods=["POST"])
def page_post_upload():
    """"""

    form_content = request.form.get('content')
    form_picture = request.files.get('picture')

    content, picture = add_new_post(form_content, form_picture)

    return render_template('post_uploaded.html',
                           picture=picture,
                           content=content)
