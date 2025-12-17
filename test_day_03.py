from playwright.sync_api import sync_playwright

def test_day_03():
    with sync_playwright() as p:
        # Open the chromium browser
        browser = p.chromium.launch(headless=False)

        # Open a new page
        page = browser.new_page()

        # Navigate to the example.com page
        page.goto("https://www.saucedemo.com/")

        # Use data-test attribute for this
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        #Check that login was successful
        assert "Products" in page.text_content(".title")
        assert page.url == "https://www.saucedemo.com/inventory.html"

        page.click("#add-to-cart-sauce-labs-backpack")
        assert "1" in page.text_content(".shopping_cart_badge")

        # Close the browser
        browser.close()