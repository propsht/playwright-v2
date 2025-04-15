from playwright.sync_api import *

def on_api_call(route: Route):
#______- get data and change
    response = route.fetch()
    user_data =response.json()

    user_data["lastName"] = "Tom"
    user_data["age"] = 33

    route.fulfill(
        response=response,
        json=user_data,
    )

#______Static data
    # route.fulfill(
    #     json={
    #         "firstName": 'John',
    #         "lastName": 'Owais',
    #         "age": 230,
    #     }
    #)

def test_user_api(page: Page):
    USERS_API_URL = "https://dummyjson.com/users/1"

    page.route(USERS_API_URL, on_api_call)

    response = page.goto(USERS_API_URL)

    print("Got data", response.json())
