import time

from playwright.sync_api import Page, expect


def test_hide_display_and_placeholder(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example"))
    time.sleep(1)
    page.get_by_role("button", name="Hide").click()
    time.sleep(1)
    expect(page.get_by_placeholder("Hide/Show Example"))
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(1)


def test_alert_boxes(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(1)
    page.on("dialog", lambda dialog: dialog.accept())  #mambda calls anonymous function
    page.get_by_role("button", name="Confirm").click()
    time.sleep(3)

def test_mouse_hover(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    time.sleep(3)
    page.get_by_role("link", name="Top").click()
    time.sleep(3)

def test_frame_handling(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link", name="All Access plan").click()
    expect(page_frame.locator("body")).to_contain_text("All Access Subscription")  # body locator - entire page
    time.sleep(3)


#Check the price of Rice is 37
#Identify the price column
# identify rice row
# extract the price

def test_tabel_handling(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            price_col_value = index
            print(f"Price column value is {price_col_value}")
            break

    rice_row = page.locator("tr").filter(has_text="Rice")
    #print(f"Rice row is {rice_row}")
    expect(rice_row.locator("td").nth(price_col_value)).to_have_text("37")
