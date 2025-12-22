import pytest

from playwright.sync_api import sync_playwright, expect

#use for the smoke testing suites
# @pytest.mark.smoke

#use for the regression testing suites
@pytest.mark.regression

def test_user_login_action_logout():
    with sync_playwright() as p:
        # Open browser
        browser = p.chromium.launch(headless=False)
        # browser = p.chromium.launch(headless=True)
        # Open a new page
        page = browser.new_page()

        # Navigate to the example.com page
        page.goto("https://www.saucedemo.com/")

        # Use data-test attribute for this
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Check that login was successful using expect
        expect(page.locator(".title")).to_have_text("Products")
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

        #Add a product to the cart and verify using expect
        page.click("#add-to-cart-sauce-labs-backpack")
        expect(page.locator(".shopping_cart_badge")).to_have_text("1")

        # Add another product to the cart and verify using expect
        page.click("#add-to-cart-sauce-labs-bike-light")
        expect(page.locator(".shopping_cart_badge")).to_have_text("2")

        # Remove one product from the cart and verify using expect
        page.click(".shopping_cart_link")
        page.click("#remove-sauce-labs-backpack")
        expect(page.locator(".shopping_cart_badge")).to_have_text("1")

        # Proceed to checkout
        page.click("#checkout")
        expect(page.locator(".title")).to_have_text("Checkout: Your Information")

        # Fill in checkout information
        page.fill("#first-name", "Dhanush")
        expect(page.locator("#first-name")).to_have_value("Dhanush")
        page.fill("#last-name", "Kasturiraja")
        expect(page.locator("#last-name")).to_have_value("Kasturiraja")
        page.fill("#postal-code", "600127")
        expect(page.locator("#postal-code")).to_have_value("600127")

        # Continue to the next step of checkout and verify
        page.click("#continue")
        expect(page.locator(".title")).to_have_text("Checkout: Overview")

        # Finish the checkout process and verify
        page.click("#finish")
        expect(page.locator(".title")).to_have_text("Checkout: Complete!")

        #Redirect to the home page and verify
        page.click("#back-to-products")
        expect(page.locator(".title")).to_have_text("Products")

        #Click the navigation menu and click logout button and verify
        page.click("#react-burger-menu-btn")
        page.click("#logout_sidebar_link")
        expect(page).to_have_url("https://www.saucedemo.com/")

        #Close the browser
        browser.close()