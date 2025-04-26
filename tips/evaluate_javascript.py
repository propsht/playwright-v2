from playwright.sync_api import Page, expect, Route, sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)


    page =browser.new_page()

    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="GET STARTED")

    link.click()
