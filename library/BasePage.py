import allure

from .BaseUi import BaseUi
from playwright.sync_api import Page


class BasePage(BaseUi):
    base_url = 'https://only.digital/'
    overlay_css = 'div[class*="Preloader_root"]'

    def __init__(self, page: Page, end_url=''):
        self.url = self.base_url + end_url
        super().__init__(page=page)

    def goto(self, timeout=10000):
        with allure.step(f'Перейти на страницу "{self.url}"'):
            self.page.goto(url=self.url, timeout=timeout)
        return self

    def wait_for_overlay_hidden(self):
        with allure.step(f'Подождать скрытия оверлея'):
            self.get_element_by_locator(selector=self.overlay_css).wait_for(state='hidden')
        return self
