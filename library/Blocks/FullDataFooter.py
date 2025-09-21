from .BaseFooter import BaseFooter
import allure


class FullDataFooter(BaseFooter):
    button_css = f'{BaseFooter.footer_block_css} button'
    about_text_css = 'p[class*="text2 Footer_text"]'
    contacts_block_css = f'{BaseFooter.footer_block_css} div[class*="ContactsLinks"]'
    email_css = f'{contacts_block_css} a:nth-child(1)'
    phone_css = f'{contacts_block_css} a:nth-child(2)'
    telegram_block_css = 'footer div[class*="Telegram"]'
    telegram_css = f'{telegram_block_css} a'
    documents_block_css = 'footer div[class*="Footer_documents"]'
    pdf_document_css = f'{documents_block_css} a:nth-child(1)'
    pitch_document_css = f'{documents_block_css} a:nth-child(2)'
    description_documents_css = f'{documents_block_css} p[class*="Documents_documentsDescription"]'
    logo_css = f'svg[class*="Footer_logo"]'

    def check_contacts_block(self):
        with allure.step("Проверить наличие блока контактов"):
            self.expect_to_be_visible(locator=self.contacts_block_css, el_name="Блок контактов")
        return self

    def check_email_link(self, expected_email=None):
        with allure.step('Проверить ссылку email'):
            self.expect_to_be_visible(locator=self.email_css, el_name="Email")
            self.expect_to_have_text(locator=self.email_css, text=expected_email)
        return self

    def check_phone_link(self, expected_phone=None):
        with allure.step('Проверить ссылку телефона'):
            self.expect_to_be_visible(locator=self.phone_css, el_name='Телефон')
            self.expect_to_have_text(locator=self.phone_css, text=expected_phone)
        return self

    def check_telegram_block(self, expected_telegram):
        with allure.step("Проверить наличие блока Telegram"):
            self.expect_to_be_visible(locator=self.telegram_block_css,el_name="Блок Telegram")

            with allure.step('Проверить контакт Telegram'):
                self.expect_to_be_visible(locator=self.telegram_css, el_name='Контакт телеграма')
                self.expect_to_have_text(locator=self.telegram_css, text=expected_telegram)
        return self

    def check_documents_block(self):
        with allure.step("Проверить наличие блока документов"):
            self.expect_to_be_visible(locator=self.documents_block_css, el_name='Блок документов')

            with allure.step('Проверить наличие документа PDF'):
                self.expect_to_be_visible(locator=self.pdf_document_css, el_name="PDF документ")

            with allure.step('Проверить наличие документа Pitch'):
                self.expect_to_be_visible(locator=self.pitch_document_css,el_name="Pitch документ")
        return self

    def check_logo(self):
        with allure.step("Проверить наличие логотипа в футере"):
            self.expect_to_be_visible(locator=self.logo_css, el_name="Логотип футера")
        return self
