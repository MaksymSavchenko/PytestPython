import json
import time

import pytest
from playwright.sync_api import Page, expect, Playwright

from pageObjects.login import LoginPage
from pageObjects.dashboard import DashBoardPage
from utils.api_base import APIutils


with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, user_credentials):
    user_name = user_credentials['userEmail']
    user_password = user_credentials['userPassword']
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api_utils = APIutils()
    order_id = api_utils.create_order(playwright,user_credentials)

    login_page = LoginPage(page)
    login_page.navigate()
    dashboard_page = login_page.login(user_name, user_password)
    orders_history_page = dashboard_page.select_orders_nav_link()
    order_details_page = orders_history_page.select_order(order_id)
    order_details_page.verify_order_message()





    context.close() #optional to clear the cache
    #print("{} {}".format("Order ID is:", order_id))