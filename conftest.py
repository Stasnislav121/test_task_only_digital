from playwright.sync_api import Playwright, Browser, Page
import pytest
from library.Pages.MainPage import MainPage


@pytest.fixture()
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture()
def main_page(page: Page):
    main_page = MainPage(page)
    main_page.goto(timeout=10000).wait_for_overlay_hidden()
    return main_page
