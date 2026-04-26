from playwright.sync_api import Page


class BasePage:
    # принимает страницу
    def __init__(self, page: Page):
        self.page = page

    # метод для открытия ссылок
    def visit(self, ulr: str):
        self.page.goto(ulr, wait_until="networkidle")

    # метод перезагрузки страницы
    def reload(self):
        self.page.reload(wait_until="domcontentloaded")




