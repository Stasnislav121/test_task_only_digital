from library.BasePage import BasePage


class MainPage(BasePage):
    url = ''

    def __init__(self, page):
        super().__init__(page=page, end_url=self.url)

    def check_footer(self):
        from library.Blocks.FullDataFooter import FullDataFooter
        footer = FullDataFooter(page=self.page)
        footer.check_element()
        return footer
