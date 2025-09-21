import allure

from BaseUi import BaseUi
from playwright.sync_api import Page


class BasePage(BaseUi):
    url = 'https://only.digital'

    def __init__(self, page:Page, end_url):
        self.url = self.url + end_url
        super().__init__(page=page)

    def goto(self, timeout=10000):
        with allure.step(f'Перейти на страницу "{self.url}"'):
            self.page.goto(url=self.url, timeout=timeout)
