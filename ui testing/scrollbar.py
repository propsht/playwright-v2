from playwright.sync_api import Page, expect

def test_dynamic_scrollbar(page: Page):
    page.goto("http://uitestingplayground.com/scrollbars")

    btn = page.get_by_role("button", name="Hiding Button")

    btn.scroll_into_view_if_needed()
    #btn.click()

    page.screenshot(path="test-scrollbar.jpg")

    expect(btn).to_be_visible()