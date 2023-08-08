"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.fixture(scope='function', autouse=False,
                params=[(1920, 1080), (375, 667)])
def browser_manager(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.config.timeout = 6
    yield browser
    browser.quit()


desktop = pytest.mark.parametrize('browser_manager', [(1920, 1080)], indirect=True)
mobile = pytest.mark.parametrize('browser_manager', [(375, 667)], indirect=True)


@desktop
def test_github_desktop(browser_manager):
    browser.open('/')
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


@mobile
def test_github_mobile(browser_manager):
    browser.open('/')
    browser.element('.flex-1 button').click()
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
