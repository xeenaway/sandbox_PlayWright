from playwright.sync_api import sync_playwright
from pytest import fixture

from page_objects.app import App


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session', params=['chromium', 'firefox', 'webkit'], ids=['chromium', 'firefox', 'webkit'])
def get_browser(get_playwright, request):
    browser = request.param
    headless = request.config.getini('headless')
    headless = True if headless == 'True' else False

    if browser == 'chromium':
        browser = get_playwright.chromium.launch(headless=headless)
    elif browser == 'firefox':
        browser = get_playwright.firefox.launch(headless=headless)
    elif browser == 'webkit':
        browser = get_playwright.webkit.launch(headless=headless)
    else:
        assert False, 'unsupported browser type'

    yield browser
    browser.close()


@fixture(scope='session')
def desktop_app(get_browser, request):
    base_url = request.config.getini('base_url')
    app = App(get_browser, base_url=base_url)
    app.goto('/')
    yield app
    app.close()


def pytest_addoption(parser):
    parser.addini('base_url', help='Base url of the site under test', default='https://python.org')
    parser.addini('headless', help='Run browser in headless mode', default='True')
