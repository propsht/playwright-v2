import pytest
from playwright.sync_api import Page, expect

DOCS_URL = "https://playwright.dev/python/docs/intro"

def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")
    heading = page.locator("h1.hero__title")
    dropdown_menu = page.locator("ul.dropdown__menu")
    # link.click()

   # assert page.url == DOCS_URL

   # texting button
   #  expect(page).to_have_url(DOCS_URL)
   #  expect(page).to_have_title("Installation | Playwright Python")
   #  expect(link).to_be_visible()
   #  expect(link).not_to_be_visible()
   #  expect(link).not_to_be_hidden()

   # Testing title and h1
   #  expect(heading).to_contain_text("testing")
   #  expect(heading).to_have_text("Playwright enables reliable end-to-end testing for modern web apps.")

   #testing drop down menu
    expect(dropdown_menu).to_contain_text("Python")
    expect(dropdown_menu).to_contain_text("Java")
    expect(dropdown_menu).to_contain_text("Node.js")
    expect(dropdown_menu).to_contain_text(".NET")

#playwright codegen