import pytest
from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"
@pytest.fixture
def playwright_page(page: Page):
    page.goto("https://playwright.dev/python/")
    return page

def test_page_has_docs_link(playwright_page: Page):


    link = playwright_page.get_by_role("link", name="Docs")
    link.click()

    assert link.is_visible()



def test_get_started_visits_docs(playwright_page: Page):


    link = playwright_page.get_by_role("link", name="GET STARTED")
    link.click()

    assert playwright_page.url == DOCS_URL

# run testwith browser and slow
# pytest test_app_plugin_version.py --headed --slowmo=1000

# run not on defoult browser
# pytest test_app_plugin_version.py --headed - browser=firefox

