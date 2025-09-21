from playwright.sync_api import Page
import pytest



@pytest.fixture()
def main_page(page: Page):
    page.goto()