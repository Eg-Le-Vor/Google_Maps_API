import pytest


@pytest.fixture()
def set_up():
    print('\nНачало теста.')
    yield
    print('\n\nКонец теста.')

@pytest.fixture(scope="module")
def set_group():
    print('\n\nВход в систему.')
    yield
    print('\nВыход из системы.')