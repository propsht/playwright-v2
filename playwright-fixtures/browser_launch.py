import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500,
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return{
        **browser_context_args,
        "storage_state": "/Users/propsht/Documents/QA/projects/playwright-v2/playwright/.auth/storage_state.json"


    }




def test_page_has_docs_link(page: Page):
    page.goto("https://playwright.dev/python/")

    doc_link = page.get_by_role("link", name="Docs")

    expect(doc_link).to_be_visible()

def test_visit_google_account(page: Page):
    page.goto("https://accounts.google.com")

    page.screenshot(path="accounts.jpg")


# def test_get_started_visits_docs(page: Page):
#     page.goto("https://playwright.dev/python/")
#
#     get_started_link = page.get_by_role("link", name="GET STARTED")
#     get_started_link.click()
#
#     expect(page).to_have_url("https://playwright.dev/python/docs/intro")