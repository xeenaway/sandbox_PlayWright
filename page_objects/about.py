from playwright.sync_api import Page


class PageAbout:
    def __init__(self, page: Page):
        self.page = page

    def check_category_exist(self, test_name: str):
        return self.page.query_selector(f'css=h2 >> text="{test_name}"') is not None
