from playwright.sync_api import sync_playwright, expect

def test_day_05():
    with sync_playwright() as p:
        #Open the chromium browser
        # browser = p.chromium.launch(headless=False)
        browser = p.chromium.launch(headless=True)

        #Open a new page
        page = browser.new_page()

        #Navigate to the example.com page
        page.goto("https://www.saucedemo.com/")

        #Use data-test attribute for this
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        #Check that login was successful using expect
        expect(page.locator(".title")).to_have_text("Products") 
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

        #Click the filter button and select "Price (high to low)" option
        page.click(".product_sort_container")
        page.select_option(".product_sort_container", "hilo")

        #Verify that the products are sorted by price from high to low
        expect(page.locator(".inventory_item_price").first).to_have_text("$49.99")
        expect(page.locator(".inventory_item_price").last).to_have_text("$7.99")

        #Click the filter button and select "Price (low to high)" option
        page.click(".product_sort_container")
        page.select_option(".product_sort_container", "lohi")

        #Verify that the products are sorted by price from low to high  
        expect(page.locator(".inventory_item_price").first).to_have_text("$7.99")
        expect(page.locator(".inventory_item_price").last).to_have_text("$49.99")


        #Close the browser
        browser.close()