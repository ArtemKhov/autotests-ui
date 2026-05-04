import pytest


@pytest.mark.xfail(reason='Найден баг, исправление в процессе, тест упадет')
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason='Баг уже исправлен, маркировка xfail выдаст XPASS')
def test_without_bug():
    pass


@pytest.mark.xfail(reason='Внешний сервис временно недоступен')
def test_external_services_is_unavailable():
    assert 1 == 2