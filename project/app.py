import os
import logging

from flask import Flask, send_from_directory

from main.routes import main_blueprint
from search.routes import search_blueprint
from loader.routes import loader_blueprint

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

logging.basicConfig(
    filename=PATH + "app.log",
    filemode="a",
    format="%(asctime)s - %(funcName)s - %(levelname)s " "- %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)
app.register_blueprint(search_blueprint)

# app.register_blueprint(page_post_upload, url_prefix='/post')


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run()
