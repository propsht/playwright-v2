from playwright.sync_api import Page, expect, Request, Response, Route

def on_route(route:Route):
    response = route.fetch()
    body = response.text().replace(
        " enables reliable end-to-end testing for modern web apps.",
        "playwright awesome framework"
    )
    route.fulfill(
        response=response,
        body=body,
    )


    # route.fulfill(
    #     status=200,
    #     body="<html><body><h1>Custom Response!</h1></body></html>"
    # )

def test_docs_link(page: Page):
    page.route(
        "https://playwright.dev/python",
        on_route
    )


    page.goto("https://playwright.dev/python")
    page.pause()

