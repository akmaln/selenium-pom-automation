# Selenium POM Automation Practice

UI automation projects built with **Python + Selenium WebDriver**, structured around the **Page Object Model (POM)** pattern and run with **PyTest**. Tests target [the-internet.herokuapp.com](https://the-internet.herokuapp.com), a standard sandbox for web automation practice.

## Tech Stack

- **Language:** Python 3.x
- **Browser automation:** Selenium WebDriver
- **Test framework:** PyTest
- **Design pattern:** Page Object Model (POM)

## What This Demonstrates

- **POM structure** — page classes hold locators and actions; test files hold assertions and flow, keeping the two cleanly separated
- **Shared base class** — common waits and actions (`click`, `find`, `enter_text`, `is_present`) live in a `BasePage` that every page inherits, keeping the page objects DRY
- **Explicit waits** — `WebDriverWait` with expected conditions instead of `sleep()`, used heavily in the dynamic-controls flows
- **Reusable fixtures** — driver lifecycle and per-page setup handled centrally in `tests/conftest.py`, so each test starts at the action
- **Parametrized tests** — `@pytest.mark.parametrize` drives the checkbox and dropdown tests with multiple data sets from a single test function
- **Screenshot on failure** — automatic capture via a PyTest hook for faster triage (output in `screenshots/`)

## Projects

| Project | Page Under Test | Concepts Exercised |
|---|---|---|
| **Checkboxes** | `/checkboxes` | State verification, conditional clicks, toggling |
| **Dropdown** | `/dropdown` | `Select` class, option selection and validation |
| **Dynamic Controls** | `/dynamic_controls` | Explicit waits on async DOM changes (enable/disable, add/remove) |

## Project Structure

```
pom_practice/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── checkbox_page.py
│   ├── dropdown_page.py
│   └── dynamic_controls_page.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_checkboxes.py
│   ├── test_dropdown.py
│   └── test_dynamic_controls.py
├── screenshots/
├── requirements.txt
└── README.md
```

## Setup

```bash
# Clone and enter the repo
git clone https://github.com/akmaln/selenium-pom-automation.git
cd selenium-pom-automation

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Tests

```bash
# Run everything
pytest

# Run a single project's tests
pytest tests/test_checkboxes.py

# Verbose output
pytest -v

# Run tests matching a keyword
pytest -k "dropdown"
```

## Notes

Selenium manages its own driver binaries via Selenium Manager (Selenium 4.6+), so no separate `chromedriver` download is required. Screenshots from failed runs are written to the `screenshots/` directory (gitignored).
