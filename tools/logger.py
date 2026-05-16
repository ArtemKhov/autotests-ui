import logging


def get_logger(name: str) -> logging.Logger:
    # инициализируем новый логгер
    logger = logging.getLogger(name)
    # выставляем уровень логирования
    logger.setLevel(logging.DEBUG)

    # инициализируем хендлер (куда пишем лог). StreamHandler - в консоль, FileHandler - в файл
    handler = logging.StreamHandler()
    # выставляем уровень логирования у хендлера
    handler.setLevel(logging.DEBUG)

    # задаем форматер (в каком формате будут писаться сообщения в лог)
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

    handler.setFormatter(formatter) # в наш хендлер устанавливаем наш форматтер

    # хендлер (который уже включает наш форматтер) устанавливаем в наш логгер
    logger.addHandler(handler)

    # возвращаем лог
    return logger