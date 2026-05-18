import platform
import sys

from config import settings


def create_allure_environment_file():
    # Создаем список из элементов в формате {key}={value}
    # url / с каким ключом запускали браузер / тестовые данные / путь до видео, скриншотов / json файлы и тд
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    # добавляем информацию на какой OS запускали
    items.append(f'os_info={platform.system()}, {platform.release()}')
    # добавляем информацию на какой версии python запускали
    items.append(f'python_version={sys.version}')
    # Собираем все элементы в единую строку с переносами
    properties = '\n'.join(items)

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)  # Записываем переменные в файл