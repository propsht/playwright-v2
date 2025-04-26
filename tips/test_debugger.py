from playwright.sync_api import Page, expect, Route





def test_page__has_docs_link(page: Page):
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="docs")

    expect(link).to_be_visible()

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="GET STARTED")

    breakpoint()

    link.click()

    expect(page).to_have_url("https://playwright.dev/python/docs/intro")