from playwright.sync_api import *



def test_page_has_docs_link(
        playwright: Playwright,
        browser: Browser,
        browser_type: BrowserType,
        browser_name: str,
        browser_channel: str, "chrome",
        is_firefox: bool,
        is_chromium: bool,
        is_webkit: bool,
):
    page = browser.new_page()

    # if browser_type == playwright.chromium:
    #     pass # chromium specific code
    # elif browser_type == playwright.firefox:
    #     pass # firefox specific code

    if is_chromium:
        pass


    page.goto("https://playwright.dev/python/")

    doc_link = page.get_by_role("link", name="Docs")
    expect(doc_link).to_be_visible()


def test_get_started_visits_docs(browser, page: Page):
    page.goto("https://playwright.dev/python/")

    get_started_link = page.get_by_role("link", name="GET STARTED")
    get_started_link.click()

    expect(page).to_have_url("https://playwright.dev/python/docs/intro")