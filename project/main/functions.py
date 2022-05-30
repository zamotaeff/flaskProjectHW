from loader.functions import load_posts_data_from_json


def get_all_posts():
    """Собираем все посты и отдаем их на рендер"""

    return load_posts_data_from_json()
