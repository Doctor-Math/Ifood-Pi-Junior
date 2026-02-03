# session.py
from playwright.sync_api import sync_playwright

class BrowserSession:
    def __init__(self, headless=False):
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.firefox.launch(
            headless=self.headless,
            args=[
                "--no-sandbox"
            ]
        )

        # Versao anterior, creachá em python.
        #
        #self.context = self.browser.new_context(
        #    viewport={"width": 1280, "height": 800},
        #    user_agent=(
        #        "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) "
        #        "Gecko/20100101 Firefox/121.0"
        #    )
        #)
        #

        # Versao de render um pouco mais segura deixando a cargo do playwright decidir oq fazer
        self.context = self.browser.new_context(
            viewport={"width": 1280, "height": 800}
        )

        self.page = self.context.new_page()

        return self.page

    def stop(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()
