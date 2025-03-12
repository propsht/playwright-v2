from playwright.sync_api import sync_playwright
from creds import *

with sync_playwright() as playwright:  # Fixed variable name
    # Use persistent session for login storage
    browser = playwright.chromium.launch(
        headless=False, slow_mo=500,
        args=["--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled"]
    )
    context = browser.new_context()

    # Get the first page in the context
    page = context.new_page()

    # Navigate to Google login
    page.goto("https://accounts.google.com")

    # Fill in Email
    email_input = page.get_by_label("Email or phone")
    email_input.fill(EMAIL)

    # Click "Next"
    next_btn = page.get_by_role("button", name="Next")
    next_btn.click()

    # Wait for password input to be visible
    page.wait_for_selector("input[type='password']")

    # Fill in Password
    password_input = page.get_by_label("Enter your password")
    password_input.fill(PASSWORD)

    # Click "Next" after entering password
    next_btn = page.get_by_role("button", name="Next")
    next_btn.click()

    # Save authentication state after full login
    context.storage_state(path="playwright/auth/storage_state.json")

    # Pause for debugging
    page.pause()

    # Close context and browser
    context.close()
    browser.close()
