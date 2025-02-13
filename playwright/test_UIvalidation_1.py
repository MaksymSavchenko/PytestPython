import time
from playwright.sync_api import Page, expect


def test_ui_validation_dynamic_script(page:Page):
    #iPxoneX, Nokia Edge -> verify 2 items are showing in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    nokia_edge_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_edge_product.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    time.sleep(2)
    expect(page.locator(".media-body")).to_have_count(2)


time.sleep(5)