import time

from playwright.sync_api import Page, Playwright, expect


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
    page.get_by_label("Password").fill("learning1") #incorrect password
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("link", name="terms and conditions").click()
#    page.get_by_role("checkbox", name="terms").click()
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    # Incorrect  username/password assertion
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()


def test_firefox(playwright:Playwright):
    firefox_browser = playwright.firefox.launch(headless=False)
    # context = firefox_browser.new_context() #new set of cookies, cache Not needed for just 1 page
    page = firefox_browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning1") #incorrect password
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("link", name="terms and conditions").click()
#    page.get_by_role("checkbox", name="terms").click()
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    # Incorrect  username/password. assertion
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()

def test_child_window(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    with page.expect_popup() as new_page:
        page.locator(".blinkingText").click()
        child_page = new_page.value
        text = child_page.locator(".red").text_content()
        print('\n' + text.split(' ')[4])


time.sleep(5)
