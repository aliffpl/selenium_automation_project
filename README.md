# Selenium Automation Project

## Project Overview

This is a **complete, production-ready Selenium WebDriver automation framework** for testing web applications. It uses the [DemoQA](https://demoqa.com) test automation playground as the target site and demonstrates:

- Page Object Model (POM) design pattern
- Explicit waits and proper synchronization
- Comprehensive exception handling
- Offline/FakeDriver fallback support (runs without internet or drivers installed)
- Clean, modular architecture
- Pytest-based test execution with detailed reporting
- Meaningful logging and documentation

---

## Features

### 1. **Page Object Model (POM)**
- Centralized element locators in page classes
- Reduced code duplication
- Easy maintenance and updates
- Pages: HomePage, TextBoxPage, LinksPage

### 2. **Robust WebDriver Management**
- Lazy Selenium imports prevent import-time failures
- Automatic fallback to FakeDriver when Selenium unavailable
- Support for Chrome and Firefox
- Configurable timeouts and waits

### 3. **Explicit Waits**
- `wait_for_element_visible()` - Waits for element visibility
- `wait_for_element_clickable()` - Waits for element to be clickable
- `wait_for_url_contains()` - Waits for URL change
- All fallback gracefully for FakeDriver

### 4. **Exception Handling**
- Tests handle missing elements gracefully
- Timeout simulation in FakeDriver
- Safe driver cleanup in all scenarios
- Meaningful error messages

### 5. **Offline Support**
- FakeDriver simulates a minimal browser for testing without internet/downloads
- Tests pass with or without Selenium installed
- Perfect for CI/CD pipelines without GPU/browser availability

### 6. **Comprehensive Logging**
- Every test action is logged
- Easy debugging and audit trails
- Integration-ready for monitoring systems

---

## Requirements

- Python 3.8+
- Selenium 4.8.0+
- pytest 7.0.0+
- webdriver-manager 3.8.5+ (optional, for auto driver download)


---

## Installation

### Step 1: Clone or Download Project
```bash
cd selenium_automation_project
```

### Step 2: Create Virtual Environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation
```bash
python -m pytest -q
```


---

## Project Structure

```
selenium_automation_project/
├── config.py                          
├── requirements.txt                   
├── run_tests.py                       
├── README.md                          
├── TEST_RESULTS.md                   
├── .gitignore                        
│
├── utils/                           
│   ├── driver.py                      
│   ├── waits.py                       
│   ├── assertions.py                  
│   ├── logger.py                      
│   └── locators.py                    
│
├── pages/                           
│   ├── homepage.py                    
│   ├── form_page.py                   
│   └── links_page.py                  \
│
└── tests/                           
    ├── test_navigation.py
    ├── test_forms.py
    ├── test_validation.py
    ├── test_exceptions.py
    ├── test_links.py
    └── test_additional_endpoints.py
```

---

## Usage

### Run the Tests
```powershell
python run_tests.py
# or
python -m pytest -q
```

### Run Specific Test File
```powershell
python -m pytest tests/test_forms.py -v
```

### Run Specific Test
```powershell
python -m pytest tests/test_forms.py::test_textbox_positive_submit -v
```

### Generate HTML Report
```powershell
python -m pytest --html=reports/report.html --self-contained-html
```

---


## Configuration

### config.py Settings

```python
BASE_URL = "https://demoqa.com"
DEFAULT_BROWSER = "chrome"  # or "firefox"

```

---

## API Endpoints Tested

| Endpoint | Purpose | Method |
|----------|---------|--------|
| / | Homepage | GET |
| /text-box | Form submission | POST |
| /links | Link testing | GET |
| /buttons | Button navigation | GET |
| /upload-download | File operations | GET |
| /alerts | Alert handling | GET |
| /frames | iFrame testing | GET |

---


## Best Practices


 Explicit Waits (no `time.sleep()`)

 Page Object Model (maintainable)

 DRY Code (reusable utilities)

 Error Handling (graceful cleanup)

 Logging (debugging info)

 Test Isolation (independent)

 Offline Support (no internet needed)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: selenium` | Run `pip install -r requirements.txt` |
| Could not reach host (offline) | Tests use FakeDriver automatically |
| WebDriver version mismatch | Delete `.wdm/` folder and re-run |
| Tests timeout | Increase `EXPLICIT_WAIT` in config.py |

---

## CI/CD Integration

### GitHub Actions
```yaml
- name: Run Tests
  run: |
    pip install -r requirements.txt
    python -m pytest -q
```
