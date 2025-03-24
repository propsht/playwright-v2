from playwright.sync_api import Page, expect

def test_page_has_get_started_link(page: Page):
  #  page.goto("https://playwright.dev/python")
    page.goto("https://bootswatch.com/default/")

#______________ Option menu assertions
    # option_menu = page.get_by_label("Example select")
    # expect(option_menu).to_have_value("1")

    multi_option_menu = page.get_by_label("Example multiple select")
    expect(multi_option_menu).to_have_values([])
    multi_option_menu.select_option(["2", "4"])
    expect(multi_option_menu).to_have_values(["2", "4"])




#_________CHECK BOX ___________________
    # checked_checkbox = page.get_by_label("Checked checkbox")
    # default_checkbox = page.get_by_label("Default checkbox")
    #
    # expect(checked_checkbox).to_be_checked()
    # expect(default_checkbox).not_to_be_checked()


#________________INPUT_________________________
    # input = page.get_by_placeholder("Search docs")
    #
    # #input is hidden before button click
    # expect(input).to_be_hidden()
    #
    # # search button
    # search_btn = page.get_by_role("button", name="Search")
    # search_btn.press("Control+KeyK")
    # #should pop the search menu
    # expect(input).to_be_editable()
    # expect(input).to_be_empty()
    #
    # #type some query in the input
    # query = "assertions"
    # input.fill(query)
    # expect(input).to_have_value(query)




#playwright codegen