from playwright.sync_api import Page, expect, Route, sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)

    iphone14 = playwright.devices["iPhone 14"]

    context = browser.new_context(
        # is_mobile=True,
        # has_touch=True,
        viewport={
            "width": 300,
            "height": 500,
        },
        color_scheme="dark",
        # permissions=,
        # geolocation=,
    )

    page =context.new_page()

    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="GET STARTED")

    link.click()

    page.set_viewport_size({
        "width": 1000,
        "height": 1000,
    })

    expect(page).to_have_url("https://playwright.dev/python/docs/intro")