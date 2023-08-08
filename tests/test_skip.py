"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import have, browser


'''
@pytest.fixture()
def browser():
    pass


def test_github_desktop(browser):
    browser.open('/')
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(browser):
    browser.open('/')
    browser.element('.flex-1 button').click()
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))'''