from flask import Blueprint, render_template

from .functions import get_all_posts

main_blueprint = Blueprint('main_blueprint',
                           __name__,
                           template_folder='templates')


@main_blueprint.route("/", methods=['GET'])
def page_index():
    """Представление главной страницы, получаем посты
    и передаем на рендер шаблона"""

    return render_template('index.html', items=get_all_posts())

