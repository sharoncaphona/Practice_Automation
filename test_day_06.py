from playwright.sync_api import sync_playwright, expect

def test_day_06():
    with sync_playwright() as p:
        #Open browser
        # browser = p.chromium.launch(headless=False)
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        #Navigate to the example.com page
        page.goto("https://the-internet.herokuapp.com/")
        page.click("text=Multiple Windows")

        #Verify we are on the correct page
        expect(page.locator("h3")).to_have_text("Opening a new window")

        #Click the link that open a new window
        with context.expect_page() as new_page_info:
            page.click("text=Click Here")
        new_page = new_page_info.value
        new_page.wait_for_load_state()

        #Verify the new window content
        expect(new_page.locator("h3")).to_have_text("New Window")

        #Close the  browser
        browser.close()