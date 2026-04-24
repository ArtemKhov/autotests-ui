import pytest
from playwright.sync_api import expect, Page

creds = {
    ("user.name@gmail.com", "password"): 'Invalid Email and Password',
    ("user.name@gmail.com", "  "): 'Invalid Email, empty Password',
    ("  ", "password"): 'Empty Email, invalid Password',
}


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "email, password",
    creds.keys(),
    ids=creds.values()
)
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str) -> None:
    # Переходим на страницу авторизации
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Находим поле "Email" и заполняем его
    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(email)

    # Находим поле "Password" и заполняем его
    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(password)

    # Находим и нажимаем по кнопке Login
    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    # Проверяем, что появилось сообщение об ошибке
    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')
