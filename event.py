from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
from time import perf_counter

import asyncio
# https://bootswatch.com/default/

#for event listener
# def on_load(page):
#     print("Page loaded:", page)
# def on_request(request):
#     print("Request sent:", request)
#
# def on_filechooser(file_chooser):
#     print("File chooser opened")
#     file_chooser.set_files("file.txt")

# def on_dialog(dialog):
#     print("Dialog opened:", dialog)
#     dialog.accept("playwright is cool")

    # dialog.accept()
    # dialog.dismiss()

def on_download(dowload):
    print("Download received ")
    dowload.save_as("night.jpg")




with (sync_playwright() as playwight):
    # launch a browser
    browser = playwight.chromium.launch(headless=False, slow_mo=5000)
    #creat a new page
    page = browser.new_page()
    # print("Page loading...")
    # start = perf_counter()

    #Visit playwright website
    #for elements
    # page.goto("https://bootswatch.com/default/")

#__________Auto Waiting
    # # button = page.get_by_role("button", name="Primary").first
    # # button.click()
    #
    # link = page.locator("a.dropdown-item").first
    # # link.click(timeout=2_000)
    # link.click(force=

# __________Page Navigator Events
    # page.goto(
    #     "https://playwright.dev/python/",
    #         wait_until='load', all resorces fro html load and display
    #         # wait_until='domcontentloaded', when html parsed and displayed
    #         # wait_until='commit', respond from server
    #         # wait_until= 'networkidle', when all networks are finished with analitycs
    # )

    # time_take = perf_counter() - start
    # print(f"...Page si loaded in {round(time_take, 2)}s")



#__________Custom Waiting
    # page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")
    #
    # link = page.get_by_role("link", name="2015")
    # link.click()
    #
    # print("Loading movies...")
    # start = perf_counter()
    # # table_data_2 = page.locator("td.film-title").nth(2)
    # # table_data_2.wait_for()
    # # table_data_2.wait_for(state='visible')
    # page.wait_for_selector(selector="td.film-title")
    #
    # time_taken = perf_counter() - start
    # print(f"... movies are loaded, in {round(time_taken,2)}s!")



#__________Event Listeners
    # page.on("load", on_load)
    #page.once("load", on_load)
    # page.on("domcontentloaded", on_load)
    # page.on("close", on_load)
    # page.on("response", on_load)on_load
    # page.on("request", on_request)

    # page.on("filechooser", on_filechooser)

    # page.goto("https://bootswatch.com/default/")

    # file_input = page.get_by_label("Default file input example")
    # file_input.click()

    #after done listener
    # page.remove_listener("load", on_load)

#__________Handiling Dialogs
    # page.goto("https://testpages.eviltester.com/styled/alerts/alert-test.html")
    #
    # page.on("dialog", on_dialog)

    # alert_btn = page.get_by_text("Show alert box")
    # alert_btn = page.get_by_text("Show confirm box")
    # alert_btn = page.get_by_text("Show prompt box")
    # alert_btn.click()





#__________Download Files
    # page.goto("https://unsplash.com/photos/the-night-sky-with-stars-above-a-rock-formation-NvBV-YwlgBw")
    #
    # page.once("download", on_download)
    #
    # download_btn = page.get_by_text("Download free")
    #
    # with page.expect_download() as download_info:
    #     download_btn.click()

    # download = download_info.value
    # download.save_as("night_sky.jpg")
    # or create listener




#__________What is Sync and Async




#__________Sync Playwright


















    browser.close()