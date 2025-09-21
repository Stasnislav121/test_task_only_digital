from library.BasePage import BasePage


class MainPage(BasePage):
    url = ''

    def __init__(self):
        super().__init__(end_url=self.url)


    def check_footer(self):
        pass

