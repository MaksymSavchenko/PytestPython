import time

from playwright.sync_api import Page, expect


def test_hide_display_and_placeholder(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example"))
    time.sleep(1)
    page.get_by_role("button", name="Hide").click()
    time.sleep(1)
    expect(page.get_by_placeholder("Hide/Show Example"))
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(1)


def test_alert_boxes(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(1)
    page.on("dialog", lambda dialog:dialog.accept()) #mambda calls anonymous function
    page.get_by_role("button", name="Confirm").click()
    time.sleep(3)

def test_frame_handling(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link", name="All Access plan").click()
    expect(page_frame.locator("body")).to_contain_text("All Access Subscription") # body locator - entire page
    time.sleep(3)
