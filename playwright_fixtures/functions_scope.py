from playwright.sync_api import Page, expect, BrowserContext

def test_page_has_docs_link(context: BrowserContext, page: Page):
    #context.add_cookies()
    #context.grant_permissions('notifications')

    page = context.new_page()

    page.goto("https://playwright.dev/python/")

    doc_link = page.get_by_role("link", name="Docs")
    expect(doc_link).to_be_visible()


def test_get_started_visits_docs(page: Page):
    page.goto("https://playwright.dev/python/")

    get_started_link = page.get_by_role("link", name="GET STARTED")
    get_started_link.click()

    expect(page).to_have_url("https://playwright.dev/python/docs/intro")