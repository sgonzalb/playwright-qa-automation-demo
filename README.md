# playwright-qa-automation-demo
End-to-End Web UI &amp; REST API automated test suite using Playwright and Python.
# 🎭 Web UI & REST API Test Automation (Playwright + Python)

Automated end-to-end (E2E) quality assurance suite demonstrating UI validation and REST API contract verification using **Playwright** and **Pytest**.

## 🚀 Test Coverage
- **UI Functional Validation:** Verifies page rendering, navigation flows, and element visibility on a public demo web application.
- **REST API Verification:** Validates HTTP status codes (`200 OK`), JSON response schema, and payload integrity against public endpoints.
- **Headless Execution:** Configured for fast CI/CD execution in headless browser mode.

## 🛠️ Tech Stack
- **Framework:** Playwright (Python) & Pytest
- **Target:** Web UI & RESTful JSON APIs

## ▶️ How to Run
```bash
pip install -r requirements.txt
playwright install chromium
playwright install-deps chromium
pytest -v
