import allure
from library.BasePage import BasePage


class BaseFooter(BasePage):
    def __init__(self, page):
        super().__init__(page=page)

    footer_block_css = 'footer[class*="Footer"]'
    social_block_css = f'{footer_block_css} div[class*="Socials"]'
    year_block_css = 'p[class*="h4"]'
    copyright_css = 'div[class*="FooterText"]'
    privacy_link_css = 'a[class*="text2"]'

    def check_element(self):
        with allure.step('Проверить наличие футура'):
            self.expect_to_be_visible(locator=self.footer_block_css, el_name='Блок футера')
            self.screenshot('FooterBlock_loaded')
        return self

    def check_social_block(self):
        with allure.step('Проверить блок социальных сетей'):
            self.expect_to_be_visible(locator=self.social_block_css,el_name='Блок социальных сетей')
        return self

    def check_year_text(self, expected_text: str):
        with allure.step('Проверить текст c годами в футере'):
            self.expect_to_have_text(locator=self.year_block_css, text=expected_text)
        return self

    def check_copyright(self, expected_text: str):
        with allure.step('Проверить наличие текста "creative digital production"'):
            self.expect_to_be_visible(locator=self.copyright_css, el_name='Копирайт в футере')
            self.expect_to_have_text(locator=self.copyright_css, text=expected_text)
        return self

    def check_privacy_link(self):
        with allure.step('Проверить наличие политика конфиденциальности'):
            self.expect_to_be_visible(locator=self.privacy_link_css, el_name='Политика конфиденциальности')
        return self

    def go_to_privacy_link(self):
        with allure.step('Перейти по ссылке на политику конфиденциальности'):
            self.click_element_by_locator(selector=self.privacy_link_css)
        return self


