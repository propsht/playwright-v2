import pytest
from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture(autouse=True, scope="function")
#scope = function, session, module
def visit_playwright(page: Page):
    page.goto("https://playwright.dev/python/")

    yield page

    page.close()
    print("\n [ Fixture ]: page closed!")
def test_page_has_docs_link(page: Page):


    link = page.get_by_role("link", name="Docs")
    link.click()

    assert link.is_visible()



def test_get_started_visits_docs(page: Page):
    page.goto("https://playwright.dev/python/")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()

    assert page.url == DOCS_URL

# run testwith browser and slow
# pytest test_app_plugin_version.py --headed --slowmo=1000

# run not on defoult browser
# pytest test_app_plugin_version.py --headed - browser=firefox

