from playwright.sync_api import sync_playwright

def test_day_02():
    with sync_playwright() as p:
        # Open the chromium browser
        # browser = p.chromium.launch(headless=False)
        browser = p.chromium.launch(headless=True)

        # Open a new page
        page = browser.new_page()

        # Navigate to the example.com page
        page.goto("https://www.saucedemo.com/")

        #Use id for this
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click

        # #Use class for this
        # page.locator(".input_error").nth(0).fill("standard_user")
        # page.locator(".input_error").nth(1).fill("secret_sauce")
        # page.locator(".submit-button").click()

        # #Use Role for this
        # page.get_by_role("textbox", name="Username").fill("standard_user")
        # page.get_by_role("textbox", name="Password").fill("secret_sauce")
        # page.get_by_role("button", name="Login").click()
        
        # Close the browser
        browser.close()