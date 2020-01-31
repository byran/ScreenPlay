import os
from screenplay.ability import Ability
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.webdriver import WebDriver


class browse_the_web(Ability):
    def __init__(self, create_browser_function: type):
        self._create_browser_function = create_browser_function
        self._webdriver = None

    def clean_up(self):
        if self._webdriver != None:
            self._webdriver.quit()

    @property
    def browser(self) -> WebDriver:
        if self._webdriver == None:
            self._webdriver = self._create_browser_function()
        return self._webdriver

    @staticmethod
    def _create_Chrome_browser():
        chrome_options = ChromeOptions()
        if os.getenv('HEADLESS_BROWSER') != 'False':
            chrome_options.add_argument('--headless')
        return Chrome(chrome_options=chrome_options)

    @staticmethod
    def using_Chrome():
        return browse_the_web(browse_the_web._create_Chrome_browser)