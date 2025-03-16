import json
import time

import pytest
from playwright.sync_api import Page, expect, Playwright
from utils.api_base import APIutils


with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api_utils = APIutils()
    order_id = api_utils.create_order(playwright)

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill(user_credentials["userEmail"])
    page.get_by_placeholder("enter your passsword").fill(user_credentials["userPassword"])
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close() #optional to clear the cache
    #print("{} {}".format("Order ID is:", order_id))