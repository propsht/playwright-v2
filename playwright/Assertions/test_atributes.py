import re
from playwright.sync_api import Page, expect

def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    docs_link = page.get_by_role("link", name="Docs")

    # expect(docs_link).to_have_class("navbar__item navbar__link")
    # element contain class contain
    # expect(docs_link).to_have_class(
    #     re.compile(r"navbar__link")
    # )
    # element class start navbar
    # expect(docs_link).to_have_class(
    #     re.compile(r"^navbar__")
    # )

    # element have id
    # expect(docs_link).to_have_id("")

    expect(docs_link).to_have_attribute(
        "href", "/python/docs/intro"
    )

#playwright codegen