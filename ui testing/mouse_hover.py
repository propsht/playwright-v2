import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(autouse=True)
def visit_test_page(page: Page):
    page.goto("http://uitestingplayground.com/mouseover")


def test_mouse(page: Page):
    link = page.get_by_title("Click me")
    link.hover(force=True)

    active_link = page.get_by_title("Active Link")
    #active_link.dblclick()
    active_link.click(click_count=2)

    click_counter = page.locator("span#clickCount")

    expect(click_counter).to_have_text("2")
