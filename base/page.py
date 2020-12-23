from page.open_page_hsl import OpenInHsl



class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_hsl(self):
        return OpenInHsl(self.driver)