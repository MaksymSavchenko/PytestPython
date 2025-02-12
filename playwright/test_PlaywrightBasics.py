import time

from playwright.sync_api import Page, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() #new set of cookies, cache
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

#chromium headless mode 1 single context
def test_playwrightShortCut(page:Page): #page - fixture; Page - class
    page.goto("https://rahulshettyacademy.com")

def test_core_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning1")
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("link", name="terms and conditions").click()
#    page.get_by_role("checkbox", name="terms").click()
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    # Incorrect  username/password. assertion
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()

    time.sleep(5)
