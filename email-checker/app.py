from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
        # Launch the browser
        browser = playwright.chromium.launch(
            headless=False,  # Set to True for headless execution
            slow_mo=500,      # Slow down execution for debugging
            args=["--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled"]
        )
        # Create a new context with the provided storage state
        context = browser.new_context(
            storage_state="/Users/propsht/Documents/QA/projects/playwright-v2/playwright/.auth/storage_state.json"
        )
        page = context.new_page()

        # Navigate to Gmail
        page.goto("https://mail.google.com")
        page.pause()

        page.wait_for_selector("div.UI", state="attached")  # Wait for the inbox to load

        new_emails = []
        emails = page.locator("div.UI table tr")



        # Iterate through emails and check for new ones
        for email in emails.all():
            is_new_email = email.locator(
                "td li[data-tooltip='Mark as read']"
            ).count() == 1

            if is_new_email:
                sender = email.locator("td span[email]:visible").inner_text()
                title = email.locator("td span [data-thread-id]:visible").inner_text()
                new_emails.append([sender, title])

        # Print results
        if len(new_emails) == 0:
            print("No new emails📫!")
        else:
            print(f"{len(new_emails)} new email(s) 📩!")
            print("-" * 30)
            for new_email in new_emails:
                print(new_email[0] + ":", new_email[1])
                print("-" * 30)


        # Close the browser and context
        context.close()
        browser.close()
