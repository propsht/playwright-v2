from playwright.sync_api import sync_playwright

# https://bootswatch.com/default/

with sync_playwright() as playwight:
    # launch a browser
    browser = playwight.chromium.launch(headless=False, slow_mo=5000)
    #creat a new page
    page = browser.new_page()
    #Visit playwright website
    #for elements
    page.goto("https://bootswatch.com/default/")
    # for pictures
    # page.goto("https://unsplash.com/")

    # #Locate a link element with "Doc" text
    # defaut_button = page.get_by_role('button', name="Default button")
    # heading = page.get_by_role('heading', name="Heading 2")
    #
    # defaut_button.highlight()
    # defaut_button.click()
    #
    # #radio button
    # radio_btn = page.get_by_role('radio', name="Option one is this and that—be sure to include why it's great")
    #
    # heading.highlight()
    #
    # radio_btn.highlight()
    # radio_btn.click()

    # #check box
    # check_btn = page.get_by_role('checkbox', name="Default checkbox")

    # check_btn.highlight()
    # check_btn.check()
#_____________________lable and placeholder______________________________________
    # email_input = page.get_by_label("Email address").highlight()
    # email_input = page.get_by_placeholder("Enter email").highlight()
    # page.pause()
    #
    # # password_input = page.get_by_label("Password").highlight()
    # password_input = page.get_by_placeholder("Password").highlight()
    # page.pause()
    #
    # example_textarea_input = page.get_by_label("Example textarea").highlight()
    # page.pause()
#____________________text and selected text contain_______________________________________

    # page.get_by_text("small button").highlight()
    # page.pause()
    # page.get_by_text("Middle").click()
    # page.pause()
    # #use when text include in sentence
    # page.get_by_text("fine print", exact=False
    #                  ).highlight()
    # page.pause()
    # use exact mach text
    # page.get_by_text(".text-danger", exact=True
    #                  ).highlight()
    # page.pause()
#___________________ Alt locator
    # page.get_by_alt_text("A woman standing on a beach next to the ocean").highlight()
    # page.get_by_alt_text("A woman standing on a beach next to the ocean").click()
    # page.pause()
#_______________________ Title
    # page.get_by_title("attribute").highlight()
    # page.pause()
#___________________________ CSS
    # page.locator("css=h1").highlight()
    # page.pause()
    # page.locator("footer").highlight()
    # page.pause()
    # page.locator("css=button.btn-outline-success").highlight()
    # page.pause()
    # page.locator("button#btnGroupDrop1").click()
    # page.pause()
    # page.locator("input[readonly]").highlight()
    # page.pause()
    # page.locator("input[value='correct value']").highlight()
    # page.pause()

# #______________- CSS
#     page.locator("css=nav.bg-dark a.nav-link.active").highlight()
#     page.pause()
#
#     page.locator("css=div.bs - component > ul.list - group").nth(1).highlight()
#     page.pause()
#_______________ CSS pseudo classes
    # page.locator("h1:text('Navbars')").highlight()
    # page.pause()
    # page.locator("h1:text-is('Navs')").highlight()
    # page.pause()
    #
    # page.locator(
    #     "div.dropdown-menu:visible"
    # ).highlight()
    # page.pause()
    #
    # page.locator("button.btn-primary").highlight()
    # page.pause()
    #
    # page.locator(
    #     ":nth-match(button.btn-primary, 4)"
    # ).highlight()
    # page.pause()
    #
    # page.locator(
    #     ":nth-match(button:text('Primary'), 1)"
    # ).highlight()
    # page.pause()
    #
    # page.locator(
    #     ":nth-match(button:text('Primary'), 3)"
    # ).highlight()
    # page.pause()
#________________- Xpath
    # page.locator("xpath=//h1").highlight()
    # page.locator("xpath=//h1[@id='navbars']").highlight()
    # page.pause()
    # page.locator("xpath=//input[@readonly]").highlight()
    # page.pause()
    # page.locator("(//input[@readonly]) [1]").highlight()
    # page.pause()
    # page.locator("xpath=//input[@value='wrong value']").highlight()

    # page.locator("//h1[ text() = 'Heading 1']").highlight()
    # page.pause()
    #
    # page.locator(
    #     "//h1[ contains(text(), 'Head') ]"
    # ).highlight()
    # page.pause()
    #
    # page.locator(
    #     "//button[ contains(@class, 'btn-outline-primary') ]"
    # ).highlight()
    # page.pause()

    # page.locator(
    #     "//input[ contains(@value, 'correct value') ]"
    # ).highlight()
    # page.pause()

#________________ Other Locators

    # page.get_by_role("button", name="Primary").locator("nth=1").highlight()
    # page.pause()
    #
    # page.locator("button").locator("nth=18").highlight()
    # page.pause()
    #
    # page.get_by_label("email address").locator("..").highlight()
    # page.pause()
    #
    # page.locator("id=btnGroupDrop1").highlight()
    # page.pause()
    # page.locator("div.dropdown").locator('visible=true')
    # page.pause()
    #
    # page.get_by_role("heading").filter(has_text="Heading").highlight()
    # page.pause()

    page.locator("div.bs-docs-section").highlight()
    page.pause()



















    browser.close()