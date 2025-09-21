import allure
from playwright.sync_api import expect, Page, Locator


class BaseUi:
    def __init__(self, page: Page):
        self.page = page

    def get_element_by_locator(self, selector=None, has_text=None, has_not_text=None, has=None,
                               has_not=None) -> Locator:
        all_params = {
            'selector': selector,
            'has_text': has_text,
            'has_not_text': has_not_text,
            'has': has,
            'has_not': has_not
        }
        d = {k: v for k, v in all_params.items() if v is not None}
        el = self.page.locator(**d)
        el.scroll_into_view_if_needed()
        return el

    def expect_to_be_visible(self, locator: str, has_text=None, has_not_text=None, has=None, has_not=None,
                             timeout=5000, el_name=None):
        all_params = {
            'selector': locator,
            'has_text': has_text,
            'has_not_text': has_not_text,
            'has': has,
            'has_not': has_not
        }

        step_msg = f'Ожидание, что элемент css = {locator} будет отображаться на странице' if el_name is None \
            else f'Ожидание, что [{el_name}], css = {locator} будет отображаться на странице'
        with allure.step(step_msg):
            err_msg = f'Невозможно дождаться отображения элемента css = {locator}:' if el_name is None \
                else f'Невозможно дождаться отображения [{el_name}], css = {locator}:'
            expect(self.get_element_by_locator(**all_params), err_msg).to_be_visible(timeout=timeout)
            return self

    def check_element_is_visible(self, locator: str, has_text=None, has_not_text=None, has=None, has_not=None) -> bool:
        all_params = {
            'selector': locator,
            'has_text': has_text,
            'has_not_text': has_not_text,
            'has': has,
            'has_not': has_not
        }

        with allure.step(f'Проверить, что элемент {locator} виден на странице'):
            return self.get_element_by_locator(**all_params).is_visible()

    def click_element(self, locator: Locator):
        locator.click()
        return self

    def click_element_by_locator(self, selector: str):
        el = self.get_element_by_locator(selector=selector)
        with allure.step(f'Кликнуть по элементу "{selector}"'):
            self.click_element(locator=el)
            return self

    def get_text(self, selector: str, has_text=None, has_not_text=None, has=None, has_not=None) -> str:
        all_params = {
            'selector': selector,
            'has_text': has_text,
            'has_not_text': has_not_text,
            'has': has,
            'has_not': has_not
        }
        with allure.step(f'Получить текст у элемента "{selector}"'):
            return self.get_element_by_locator(**all_params).inner_text()

    def expect_to_have_text(self, locator: str, text: str, has_text=None, has_not_text=None, has=None, has_not=None,
                            timeout=5000) -> bool:
        all_params = {
            'selector': locator,
            'has_text': has_text,
            'has_not_text': has_not_text,
            'has': has,
            'has_not': has_not
        }
        with allure.step(f'Ожидание, что элемент "{locator}" имеет текст "{text}"'):
            return expect(self.get_element_by_locator(**all_params)).to_have_text(text, timeout=timeout)

    def screenshot(self, name, locator=None, timeout=None):
        path = f'screenshots/{name}.jpg'
        if locator:
            el = self.get_element_by_locator(selector=locator)
            el.screenshot(path=path, type='jpeg')
        else:
            self.page.screenshot(path=path, type='jpeg', timeout=timeout)
        allure.attach.file(path, name=name, attachment_type=allure.attachment_type.JPG)
