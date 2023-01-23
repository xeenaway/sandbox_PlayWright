from playwright.sync_api import Browser

from page_objects.about import PageAbout


class App:
    def __init__(self, browser: Browser, base_url: str):
        self.browser = browser
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url
        self.about = PageAbout(self.page)

    def goto(self, endpoint: str):
        self.page.goto(self.base_url + endpoint)

    def navigate_to(self, menu: str):
        self.page.locator("#container").get_by_role("link", name=menu).click()
        self.page.wait_for_load_state()

    def close(self):
        self.page.close()
        self.context.close()
