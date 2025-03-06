import time
from playwright.sync_api import Page, expect, Playwright
from utils.api_base import APIutils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api_utils = APIutils()
    api_utils.create_order(playwright)

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()

