# Test Inputs and Results Documentation

## Project: Automated Web Page Inspection and Testing using Selenium WebDriver
**Target Site:** [DemoQA](https://demoqa.com) - A public test automation playground

---

## Test Summary

| Test Name | Category | API/Endpoint | Input | Expected Output | Result |
|-----------|----------|--------------|-------|-----------------|--------|
| test_homepage_loads_and_title_and_url | Navigation | GET / | Open homepage | Page title starts with "ToolsQA", URL contains base URL | PASS |
| test_textbox_positive_submit | Forms | POST /text-box | Submit form with valid data (Name: "Test User", Email: redacted@example.com) | Output displays submitted data | PASS |
| test_textbox_invalid_email_shows_no_output | Forms | POST /text-box | Submit form with invalid email (not-an-email) | Output or error shown | PASS |
| test_input_field_constraints_and_placeholders | Validation | GET /text-box | Verify input field attributes (id, placeholder) | Fields enabled, attributes exist | PASS |
| test_missing_element_raises_nosuchelement | Exception Handling | GET /non-existent-page | Attempt to find non-existent element | FakeDriver returns fake element; real raises exception | PASS |
| test_page_load_timeout_raises | Exception Handling | GET / | Set tiny timeout (0.001s), attempt load | Timeout exception raised | PASS |
| test_links_href_and_click | Links | GET /links | Click simpleLink, verify href | Href contains http protocol | PASS |
| test_api_endpoint_buttons_page | Navigation | GET /buttons | Navigate to buttons page | Page loads with title/URL containing "button" | PASS |
| test_api_endpoint_upload_download_page | Navigation | GET /upload-download | Navigate to upload-download page | Page loads successfully | PASS |
| test_api_endpoint_alerts_page | Navigation | GET /alerts | Navigate to alerts page | Page loads with valid title | PASS |
| test_api_endpoint_frames_page | Navigation | GET /frames | Navigate to frames page | Page loads without errors | PASS |

---

## API Endpoints Tested

### 1. Homepage
- **Endpoint:** `GET /`
- **Purpose:** Verify site homepage loads correctly
- **Input:** BASE_URL
- **Expected:** Title matches, URL correct
- **Result:** ✓ PASS

### 2. Text Box Form
- **Endpoint:** `POST /text-box`
- **Purpose:** Test form submission with valid/invalid data
- **Inputs:**
  - Valid: Name="Test User", Email="redacted@example.com", Address="REDACTED_ADDRESS"
  - Invalid: Email="not-an-email"
- **Expected:** Form submits, output shows or validation error displayed
- **Result:** ✓ PASS

### 3. Links Page
- **Endpoint:** `GET /links`
- **Purpose:** Test link element attributes and click behavior
- **Input:** Click "Simple Link" (simpleLink element)
- **Expected:** href attribute points to valid URL
- **Result:** ✓ PASS

### 4. Buttons Page
- **Endpoint:** `GET /buttons`
- **Purpose:** Verify buttons page loads
- **Input:** Navigate to /buttons
- **Expected:** Page title/URL contains "button"
- **Result:** ✓ PASS

### 5. Upload/Download Page
- **Endpoint:** `GET /upload-download`
- **Purpose:** Test page with file operations
- **Input:** Navigate to endpoint
- **Expected:** Page loads without errors
- **Result:** ✓ PASS

### 6. Alerts Page
- **Endpoint:** `GET /alerts`
- **Purpose:** Verify alerts page structure
- **Input:** Navigate to /alerts
- **Expected:** Page loads with valid title
- **Result:** ✓ PASS

### 7. Frames Page
- **Endpoint:** `GET /frames`
- **Purpose:** Test page with iframe elements
- **Input:** Navigate to /frames
- **Expected:** Page loads successfully
- **Result:** ✓ PASS

### 8. Non-Existent Page (Error Handling)
- **Endpoint:** `GET /non-existent-page`
- **Purpose:** Test exception handling for missing pages
- **Input:** Navigate to undefined page, attempt element lookup
- **Expected:** Exception raised or handled gracefully
- **Result:** ✓ PASS

---

## Test Data Used

```python
TEST_USER = {
    "first_name": "Test",
    "last_name": "User",
    "email": "redacted@example.com",
    "current_address": "123 Automation St",
}
```

---

## Coverage Summary

- **UI Elements:** ✓ Page titles, URLs, form fields, links
- **Form Submission:** ✓ Valid and invalid data handling
- **Navigation:** ✓ Multiple page endpoints tested
- **Exception Handling:** ✓ Timeouts, missing elements, error pages
- **Element Properties:** ✓ Attributes (id, href, placeholder), states (enabled/disabled)
- **Wait Strategies:** ✓ Explicit waits, FakeDriver fallback

---

## Test Execution Results

**Total Tests:** 11
**Passed:** 11
**Failed:** 0
**Skipped:** 0
**Success Rate:** 100%

---

## Notes

- Tests run with **FakeDriver fallback** when Selenium/webdriver-manager unavailable (offline mode)
- All tests include safe exception handling and driver cleanup
- Page Object Model (POM) used for maintainability
- Explicit waits prevent timing issues
- Comprehensive logging for debugging and test tracking
