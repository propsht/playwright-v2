from playwright.sync_api import Page, expect

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/ajax")

    triger_btn = page.get_by_role("button", name="Button Triggering AJAX Request")
    triger_btn.click()


    paragraph = (page.locator("p.bg-success"))
    paragraph.wait_for()

    expect(paragraph).to_be_visible()