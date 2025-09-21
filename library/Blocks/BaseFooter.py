import allure
from library.BasePage import BasePage


class BaseFooter(BasePage):
    footer_block_css = 'footer[class*="Footer"]'
    social_block_css = f'{footer_block_css} div[class*="Socials"]'
    year_block_css = 'p[class*="h4"]'
    text_block_css = 'div[class*="FooterText"]'
    privacy_link_css = 'a[class*="text2"]'

    def check_element(self):
        with allure.step("Проверить наличие футура"):
            self.expect_to_be_visible(locator=self.footer_block_css)
            self.screenshot('FooterBlock_loaded', locator=self.footer_block_css)
        return self


class FullDataFooter(BaseFooter):
    button_css = f'{super().footer_block_css} button'
    about_text_css = 'p[class*="text2 Footer_text"]'
    contacts_block_css = f'{super().footer_block_css} div[class*="ContactsLinks"]'
    email_css = f'{contacts_block_css} a:nth-child(1)'
    phone_css = f'{contacts_block_css} a:nth-child(2)'
    telegramm_block_css = 'footer div[class*="Telegram"]'
    telegramm_css = f'{telegramm_block_css} a'
    documents_block_css = 'footer div[class*="Footer_documents"]'
    pdf_document_css = f'{documents_block_css} a:nth-child(1)'
    pitch_document_css = f'{documents_block_css} a:nth-child(2)'
    description_documents_css = f'{documents_block_css} p[class*="Documents_documentsDescription"]'
    logo_css = f'svg[class*="Footer_logo"'
