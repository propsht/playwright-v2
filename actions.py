from playwright.sync_api import sync_playwright

# https://bootswatch.com/default/

with (sync_playwright() as playwight):
    # launch a browser
    browser = playwight.chromium.launch(headless=False, slow_mo=5000)
    #creat a new page
    page = browser.new_page()
    #Visit playwright website
    #for elements
    page.goto("https://bootswatch.com/default/")



    #___________Mouse Actions
    # button = page.get_by_role("button", name="Block button").first
    # button.click()
    # button.dblclick()
    # button.dblclick(delay=500)
    # button.click(button="right")
    # button.click(modifiers=["Shift"])
    # button.click(modifiers=["Shift", "ctrl"])
    #
    # outline_button = page.locator("button,btn-outline-primarly")
    # outline_button.hover()

    # ___________Input fill
    # page.get_by_placeholder("Enter email").highlight()

    # page.get_by_placeholder("Enter email").highlight()
    # page.pause()
    #
    # page.get_by_placeholder("Enter email").fill("test@test.com")
    # page.pause()
    #
    # page.get_by_placeholder("Enter email").type("test@test.com", delay=500)
    # page.pause()
    #
    # valid_input = page.get_by_label("Valid input").first.highlight()
    # page.pause()
    #
    # valid_input.input_value()
    # print(valid_input)
    #____
    # doen't works with verible
    # put2 = page.get_by_placeholder("Enter email")
    # put2.highlight()
    # page.pause()
    #
    # put2.fill("test@test.com")
    # page.pause()


    #___________Radios, Chackboxes and Switches
    # page.get_by_label("Option two can be something else and selecting it will deselect option one").highlight()
    # page.pause()
    # page.get_by_label("Option two can be something else and selecting it will deselect option one").check()
    # page.pause()
    #
    # page.get_by_label("Default checkbox").highlight()
    # page.pause()
    # page.get_by_label("Default checkbox").check()
    # page.pause()
    # page.get_by_label("Default checkbox").is_checked()
    # page.pause()
    # page.get_by_label("Default checkbox").uncheck()
    # page.pause()
    #
    # page.get_by_label("Default checkbox").set_checked(True)
    # page.pause()
    # page.get_by_label("Default checkbox").set_checked(False)
    # page.pause()
    #
    # page.get_by_label("Default checkbox").click()
    # page.pause()
    # page.get_by_label("Default checkbox").click()
    # page.pause()
    #
    #
    # page.get_by_label("Default switch checkbox input").highlight()
    # page.pause()
    # page.get_by_label("Default switch checkbox input").check()
    # page.pause()
    # page.get_by_label("Default switch checkbox input").uncheck()
    # page.pause()


    #___________Select Option Form Option Menu
    #
    # page.get_by_label("Example select").highlight()
    # page.pause()
    # page.get_by_label("Example select").select_option("4")
    # page.pause()

    # page.get_by_label("Example multiple select").highlight()
    # page.pause()
    # page.get_by_label("Example multiple select").select_option(["2","4"])
    # page.pause()


    #___________Dropdown Menu
    # page.locator("button#btnGroupDrop1").click()
    #
    # page.locator("div.dropdown-menu:visible").highlight()
    # page.pause()
    # page.locator("div.dropdown-menu:visible a:text('Dropdown link')").last.highlight()
    # page.pause()
    # page.locator("div.dropdown-menu:visible a:text('Dropdown link')").last.click()
    # page.pause()


    #___________Upload Files
    # file_input = page.get_by_label("Default file input example")
    # file_input.highlight()
    # page.pause()
    # file_input.set_input_files("file.txt")
    # page.pause()

    # page.get_by_label("Default file input example").highlight()
    # page.pause()
    # page.get_by_label("Default file input example").set_input_files("file.txt")
    # page.pause()


    #multiple files upload
    # page.get_by_label("Default file input example").set_input_files("file.txt", "app.py")

    # # File chooser
    # with page.expect_file_chooser() as fc_info:
    #     page.get_by_label("Default file input example").click()
    #     file_chooser = fc_info.value
    #     file_chooser.set_files("app.py")
    # page.pause()


    #___________Keyboard Schotcuts
    text_area = page.get_by_label("Example textarea")
    text_area.fill("word")
    page.pause()

    text_area.press("KeyW")
    text_area.press("KeyO")
    text_area.press("KeyR")
    text_area.press("Shift+KeyD")
    page.pause()

    text_area.press("Control+ArrowLeft")
    page.pause()
    text_area.press("Control+ArrowRight")
    page.pause()








browser.close()