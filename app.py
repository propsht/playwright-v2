from playwright.sync_api import sync_playwright


with sync_playwright() as playwight:
    # launch a browser
    browser = playwight.chromium.launch(headless=False, slow_mo=3000)
    #creat a new page
    page = browser.new_page()
    #Visit playwright website
    page.goto("https://playwright.dev/python/")

    #Locate a link element with "Doc" text
    doc_button = page.get_by_role('link', name="Doc")

    doc_button.click( )

    #Get the url
    print ("Docs: ", page.url)

    browser.close()