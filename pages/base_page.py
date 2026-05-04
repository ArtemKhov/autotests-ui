from typing import Pattern

from playwright.sync_api import Page, expect


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

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)



