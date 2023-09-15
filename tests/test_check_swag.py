from pages.swag_labs import SwagLabs
from conftest import browser


def test_icon(browser):
    check_icon = SwagLabs(browser)
    check_icon.visit()
    assert check_icon.exist_icon()


def test_name(browser):
    check_name = SwagLabs(browser)
    check_name.visit()
    assert check_name.field_name()


def test_password(browser):
    check_password = SwagLabs(browser)
    check_password.visit()
    assert check_password.password_field()
