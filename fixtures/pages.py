import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


@pytest.fixture
def login_page(chromium_page: Page):
    return LoginPage(page=chromium_page)