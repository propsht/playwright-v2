import pytest
from playwright.sync_api import Page, expect, TimeoutError

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/visibility")

    hide_btn = page.get_by_role("button", name="Hide")
    remove_btn = page.get_by_role("button", name="Removed")
    zero_width_btn = page.get_by_role("button", name="Zero Width")
    overlapped_btn = page.get_by_role("button", name="Overlapped")
    opacity_0_btn = page.get_by_role("button", name="Opacity 0")
    hidden_btn = page.get_by_role("button", name="Visibility Hidden")
    display_none_btn = page.get_by_role("button", name="Display None")
    offscreen_btn = page.get_by_role("button", name="Offscreen")

    hide_btn.click()

    expect(remove_btn).to_be_hidden()

    expect(zero_width_btn).to_have_css("width", "0px")

    with pytest.raises(TimeoutError):
        overlapped_btn.click(timeout=2000)

    expect(opacity_0_btn).to_have_css("opacity", "0")

    expect(hidden_btn).to_be_hidden()

    expect(display_none_btn).to_be_hidden()

    expect(offscreen_btn).not_to_be_in_viewport()



