from playwright.sync_api import Playwright, Browser, Page
import pytest
from library.Pages.MainPage import MainPage


@pytest.fixture()
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture()
def page(browser: Browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture()
def main_page(page):
    main_page = MainPage(page)
    main_page.goto(timeout=10000)
    return main_page


def test_footer_main_page(main_page):
    footer = main_page.check_footer().check_social_block() \
        .check_year_text(expected_text='© 2014 - 2025') \
        .check_privacy_link() \
        .check_contacts_block() \
        .check_email_link(expected_email='hello@only.digital') \
        .check_phone_link(expected_phone='+7 (495) 740 99 79') \
        .check_telegram_block(expected_telegram='@onlydigitalagency') \
        .check_documents_block() \
        .check_logo()
    print()
