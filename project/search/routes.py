from flask import Blueprint, render_template, request

from .functions import search_post_by_tag


search_blueprint = Blueprint('search_blueprint',
                             __name__,
                             template_folder='templates')


@search_blueprint.route("/search/", methods=['GET'])
def page_search():
    """Представление, которое обрабатывает запрос поиска"""

    request_arg = request.args.get('s')

    if request_arg:

        return render_template('post_list.html', items=search_post_by_tag(request_arg))
