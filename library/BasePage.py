from BaseUi import BaseUi


class BasePage(BaseUi):
    url = 'https://only.digital'

    def __init__(self, end_url):
        self.url = self.url + end_url
        super().__init__()

    def goto(self, timeout=10000):
        self.page.goto(url=self.url, timeout=timeout)

