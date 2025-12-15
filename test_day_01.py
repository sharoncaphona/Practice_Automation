#start the playwright
from playwright.sync_api import sync_playwright

#function of the python
def test_day_01():
    with sync_playwright() as p:
        #Open the chrome browser
        browser = p.chromium.launch(headless=False)

        #open a new page
        page = browser.new_page()

        #navigate to the google page
        page.goto("https://www.google.com")

        #get the title of the page
        title = page.title()

        #print the title of the page
        print("Page title is : ", title)

        #close the browser
        browser.close()