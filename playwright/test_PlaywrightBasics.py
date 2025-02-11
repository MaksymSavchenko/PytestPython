from playwright.sync_api import Page

def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() #new set of cookies, cache
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

#chromium headless mode 1 single context
def test_playwrightShortCut(page:Page): #page - fixture; Page - class
    page.goto("https://rahulshettyacademy.com")
