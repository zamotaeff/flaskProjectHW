class FileNotPictureError(Exception):
    """Класс обработчик ошибки, когда файл не изображение"""

    def __init__(self, message=None):
        super().__init__(message)
