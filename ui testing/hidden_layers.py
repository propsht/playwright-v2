import pytest
from playwright.sync_api import TimeoutError, Page,expect

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/hiddenlayers")

    green_btn = page.locator("button#greenButton")

    green_btn.click()
    with pytest.raises(TimeoutError):
        green_btn.click(timeout=2000)