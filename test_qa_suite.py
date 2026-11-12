import pytest
from playwright.sync_api import sync_playwright, expect


def test_web_ui_navigation():
    """Validates page title, main heading, and navigation link on example.com."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")

        expect(page).to_have_title("Example Domain")
        heading = page.locator("h1")
        expect(heading).to_have_text("Example Domain")

        more_info_link = page.locator("a")
        expect(more_info_link).to_be_visible()
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
