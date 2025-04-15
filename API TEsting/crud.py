import json, pytest
from playwright.sync_api import *
@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com",
        extra_http_headers={'Content-Type': 'application/json'},
    )
    yield api_context
    api_context.dispose()


def test_create_users(api_context: APIRequestContext):

#_______ featch  method
    # response = api_context.fetch(
    #     "user/add",
    #     method="POST",
    #     headers={'Content-Type': 'application/json'},
    #     data={
    #         "firstName": 'Muhammad',
    #         "lastName": 'Ovi',
    #         "age": 250,
    #         }
    # )



#____________context method

    response = api_context.post(
        "/users/add",
        data={
            "firstName": 'Muhammad',
            "lastName": 'Ovi',
            "age": 250,
        }
    )
#_________________________________________________________
    user_data = response.json()

    print(f"\n{user_data}")

    assert user_data["id"] == 209
    assert user_data["firstName"] == "Muhammad"

def test_update_user(api_context: APIRequestContext):

    print(api_context.get("users/1").json()['firstName'],['lastName'],['age'])

    response = api_context.put(
        "users/1",
        data={
            "firstName": 'John',
            "lastName": 'Owais',
            "age": 230,
        }
    )
    user_data = response.json()

    api_context.delete("users/1")

    print(user_data)

    assert user_data["lastName"] == "Owais"
    assert user_data["age"] == 230

