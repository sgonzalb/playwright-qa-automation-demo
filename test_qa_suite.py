import pytest
from playwright.sync_api import sync_playwright, expect


def test_web_ui_login_flow():
    """Validates positive user authentication flow on a QA practice web application."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")

        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        page.click("button[type='submit']")

        flash_message = page.locator("#flash")
        expect(flash_message).to_contain_text("You logged into a secure area!")
        browser.close()


def test_rest_api_endpoint():
    """Validates HTTP 200 status and JSON schema from a public REST API."""
    with sync_playwright() as p:
        request_context = p.request.new_context()
        response = request_context.get("https://jsonplaceholder.typicode.com/posts/1")

        assert response.status == 200
        body = response.json()
        assert body["id"] == 1
        assert "title" in body
        assert "body" in body
        request_context.dispose()
