from enum import Enum
from typing import Self

from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


# Список тестируемых браузеров
class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


# Тестовые данные юзера для тестов
class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


# Тестовые данные (например путь до файла для тестов)
class TestData(BaseModel):
    image_png_file: FilePath


# Основные настройки: путь до тестируемой страницы, режим запуска браузера, ссылка на список браузеров,
# ссылка не тестового юзера, ссылка на тестовые данные,
# пути для сохранения видео, трейсинга, скриншотов / путь до состояния браузера
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",  # Указываем, из какого файла читать настройки
        env_file_encoding="utf-8",  # Указываем кодировку файла
        env_nested_delimiter=".",  # Указываем разделитель для вложенных переменных
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    allure_results_dir: DirectoryPath # Добавили новое поле
    browser_state_file: FilePath

    def get_base_url(self) -> str:
        return f"{self.app_url}/"

    @classmethod
    def initialize(cls) -> Self: # Возвращает экземпляр класса Settings
        # Указываем пути
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        browser_state_file = FilePath("browser-state.json")
        allure_results_dir = DirectoryPath("./allure-results")  # Создаем объект пути к папке

        # Создаем директории, если они не существуют
        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)  # Создаем папку allure-results, если она не существует
        allure_results_dir.mkdir(exist_ok=True)

        # Возвращаем модель с инициализированными значениями
        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir, # Передаем allure_results_dir в инициализацию настроек
            browser_state_file=browser_state_file
        )


settings = Settings.initialize()