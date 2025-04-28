from creds import *
from playwright.sync_api import *


def test_create_issue(api_context: APIRequestContext):
    issue_data = {
        "title": "[BUG] That Went Wrong",
        "body": "Whe do it this, that failed",
    }

    issue = api_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REP}/issues",
        data=issue_data
    )
    assert issue.ok

def test_take_issues_screenshot(page: Page):
    page.goto(f"https://github.com/{GITHUB_USER}/{GITHUB_REP}/issues")
    page.screenshot(path="issues-page.jpg", full_page=True)

def test_issue_in_repo(api_context: APIRequestContext):
    all_issues = api_context.get(
        f"/repos/{GITHUB_USER}/{GITHUB_REP}/issues"
    )
    assert all_issues.ok


    new_issue = [
        issue
        for issue in all_issues.json()
        if issue["title"] == "[BUG] That Went Wrong"
    ][0]

    assert new_issue["body"] == "Whe do it this, that failed"