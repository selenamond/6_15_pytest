"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import have, browser


@pytest.fixture(scope='function', autouse=False,
                params=[(1366, 768), (1920, 1080), (414, 896), (375, 667)],
                ids=['desktop', 'desktop', 'mobile', 'mobile'])
def browser_window(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.config.window_width, browser.config.window_height = request.param
    browser.config.timeout = 6
    yield browser
    browser.quit()


def mobile_browser_window(width, height):
    return width < height


def test_github_desktop(browser_window):
    if mobile_browser_window(browser.config.window_width,
                             browser.config.window_height):
        pytest.skip('Этот тест только для декстопных размеров экрана')
    browser.open('/')
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(browser_window):
    if not mobile_browser_window(browser.config.window_width,
                                 browser.config.window_height):
        pytest.skip('Этот тест только для мобильных размеров экрана')
    browser.open('/')
    browser.element('.flex-1 button').click()
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
