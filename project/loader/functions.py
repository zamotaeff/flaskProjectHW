import json
import logging
import os
from json import JSONDecodeError

from .classes import FileNotPictureError


PATH = os.path.dirname(os.path.realpath(__file__)) + '/'

logging.basicConfig(
    filename=PATH + "../app.log",
    filemode="a",
    format="%(asctime)s - %(funcName)s - %(levelname)s " "- %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def load_posts_data_from_json(file_path=PATH + '../data/posts.json'):
    """Загружаем из файла json данные и оттдаем преобразованные"""

    with open(file_path, encoding='utf8') as file:
        try:
            return json.load(file)
        except FileNotFoundError as e:
            logger.info(e)
        except JSONDecodeError as e:
            logger.info(e)


def save_posts_data_to_json(posts):
    """Сохраняем данные постов в json"""

    with open(PATH + '../data/posts.json', 'w', encoding='utf-8') as file:
        try:
            json.dump(posts, file, ensure_ascii=False)

        except JSONDecodeError as e:
            logger.info(e)


def save_picture_file(picture):
    """"""

    # Имя файла
    filename = picture.filename
    if 'jpg' not in filename or 'png' not in filename:

        raise FileNotPictureError('Загружаемый файл не является изображением')

    # Сохраняем картинку под родным именем в папку uploads
    picture.save(PATH + f'../uploads/images/{filename}')


def add_new_post(content, picture):
    """Добавляем новый пост в файл"""

    posts = load_posts_data_from_json()

    # Имя файла
    filename = picture.filename

    # Когда файл не изображение
    try:
        save_picture_file(picture)
    except FileNotPictureError as e:
        logger.info(e)

    posts.append({'pic': f'/uploads/images/{filename}', 'content': content})

    save_posts_data_to_json(posts)

    return content, f'/uploads/images/{filename}'
