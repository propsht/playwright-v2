from playwright.sync_api import Page, expect, Request, Response, Route

def on_route(route:Route):

    if route.request.resource_type == "image":
        route.abort()
    else:
        route.continue_()



    # print("Request aborted:", route.request)
    # route.abort()
    #_____ to send custom data
    #route.request.post_data = "data"
    #route.continue_()


def test_docs_link(page: Page):
    page.route(
            "**",
            # "**/*.png",
            # "https://playwright.dev/python/img/playwright-logo.svg",
            on_route

    )
    # page.route(
    #     "https://playwright.dev/python",
    #     on_route
    # )



    page.goto("https://playwright.dev/python")

    page.screenshot(path="play1.jpg", full_page=True)
