# main.py
from session import BrowserSession

def main():
    session = BrowserSession(headless=False)
    page = session.start()
    page.goto("https://www.ifood.com.br")

    print("Título:", page.title())

    session.stop()

if __name__ == "__main__":
    main()