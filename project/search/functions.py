import logging
import os

from loader.functions import load_posts_data_from_json


PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

logging.basicConfig(
    filename=PATH + "../app.log",
    filemode="a",
    format="%(asctime)s - %(funcName)s - %(levelname)s " "- %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def search_post_by_tag(tag):
    """Производим поиск по тегу и отдаем список постов"""

    json_data = load_posts_data_from_json()

    posts = [item for item in json_data if tag.lower() in item['content'].lower()]

    logger.info(f'Поисковый запрос {tag}, найден {len(posts)}')

    return posts
