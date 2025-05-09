import json,pytest
from playwright.sync_api import *
@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
    )
    yield api_context
    api_context.dispose()


def test_users_search(api_context: APIRequestContext):

    query = "Emily"
    response = api_context.get(f"/users/search?q={query}")

    user_data = response.json()

    print("Users found:", user_data["total"])

    for user in user_data["users"]:
        print("Checking user:", user["firstName"])
        assert query in user["firstName"]
