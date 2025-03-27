from playwright.sync_api import TimeoutError, Page,expect

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com")

    load_delay_link = page.get_by_role("link", name="Load Delay")

    load_delay_link.click()

    btn = page.get_by_role("button", name='Button Appearing After Delay')
    btn.wait_for(timeout=10000)

    expect(btn).to_be_visible()

