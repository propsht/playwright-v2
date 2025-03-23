import pytest
from playwright.sync_api import BrowserContext, Page

DOCS_URL = "https://playwright.dev/python/docs/intro"
@pytest.fixture(autouse=True)
def trace_test(context: BrowserContext):
    # setup
    context.tracing.start(
        name="playwright trace",
        screenshots=True, #make screenshots of website frame by frame
        snapshots=True, # before and after action will see website
        sources=True, #sourcr code of each action
    )
    yield
    context.tracing.stop(path="trace.zip")


def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()

    assert page.url == DOCS_URL

#view trace http://trace.playwright.dev/




