# ZooBook Automation Framework

## Overview

ZooBook Automation Framework is a **Python + Selenium WebDriver** based UI test automation framework developed to automate important end-to-end workflows of the ZooBook application.

The framework is structured using the **Page Object Model (POM)** design pattern to keep test scripts clean, maintainable, scalable, and reusable.

The primary automated workflow includes:

- Creating a new customer/patient.
- Adding a booking for the patient.
- Checking whether the patient already exists.
- Handling an existing patient by changing/inactivating the patient's current state.
- Validating the overall customer and booking workflow.

---

## Technology Stack

- **Programming Language:** Python
- **Automation Tool:** Selenium WebDriver
- **Design Pattern:** Page Object Model (POM)
- **Test Execution:** Python-based test cases
- **Configuration Management:** Separate configuration layer
- **Test Data Management:** Dedicated test data directory
- **Reporting:** Test execution reports
- **Logging:** Execution logs for debugging and traceability

---

## Framework Architecture

The project follows a layered automation architecture:

```text
ZooBookAssesment/
│
├── Config/
│   └── Application and framework configuration
│
├── base/
│   └── Browser setup and reusable Selenium functionality
│
├── locators/
│   └── Web element locators
│
├── pages/
│   └── Page Object Model classes and application actions
│
├── testcases/
│   └── Automated test scenarios
│
├── testdata/
│   └── Test input data
│
├── Reports/
│   └── Automation execution reports
│
├── logs/
│   └── Framework and test execution logs
│
├── Commands.txt
│   └── Useful commands for executing the framework
│
└── README.md
    └── Project documentation
```

---

## Folder Structure

### `Config`

Contains framework-level and application-level configuration.

Typical configuration may include:

- Application URL
- Browser configuration
- Environment details
- Timeout values
- Test execution settings

Keeping configuration separate allows the same automation framework to run against different environments without modifying the actual test scripts.

---

### `base`

The `base` layer contains reusable Selenium functionality required by multiple test cases and page objects.

It may be responsible for:

- Initializing Selenium WebDriver
- Launching the browser
- Browser configuration
- Opening the application URL
- Managing browser sessions
- Common waits
- Common Selenium actions
- Closing the browser after execution

The purpose of the base layer is to avoid duplicate Selenium setup code across test cases.

---

### `locators`

This directory contains element locators used to identify UI elements within the ZooBook application.

Examples include:

- ID
- XPath
- CSS Selector
- Name
- Class Name

Separating locators from test logic improves maintainability.

If an application element changes, its locator can be updated from one location instead of changing several test scripts.

---

### `pages`

The `pages` directory represents the **Page Object Model layer**.

Each application page or major feature should have its own page class.

For example:

```text
pages/
├── LoginPage.py
├── CustomerPage.py
├── PatientPage.py
└── BookingPage.py
```

Page classes contain reusable application actions such as:

```python
create_customer()
search_patient()
create_booking()
deactivate_patient()
```

Test cases call these methods rather than directly interacting with Selenium elements.

This makes the automation scripts easier to understand and maintain.

---

### `testcases`

Contains the actual automated test scenarios.

The test cases combine page-level methods to validate complete business workflows.

Example workflow:

```text
Launch Application
       ↓
Login
       ↓
Navigate to Customer/Patient Module
       ↓
Search Patient
       ↓
Patient Exists?
   ↓          ↓
  Yes         No
   ↓           ↓
Deactivate    Create New
Patient       Patient
      \       /
       ↓     ↓
       Create Booking
            ↓
       Validate Booking
            ↓
         Test Pass
```

Test cases should primarily contain:

- Test steps
- Business validations
- Assertions

Complex Selenium implementation should remain inside the page classes.

---

### `testdata`

Contains reusable data required by automation scripts.

Example data may include:

- Customer names
- Patient information
- Contact information
- Booking information
- Login credentials
- Test-specific values

Keeping test data separate makes the framework easier to maintain and enables data-driven testing.

---

### `Reports`

Stores automation execution results.

Reports help identify:

- Passed tests
- Failed tests
- Execution status
- Failure details
- Test execution history

Reports are useful when automation runs locally or through a CI/CD pipeline.

---

### `logs`

Stores framework execution logs.

Logging provides additional details about automation execution, such as:

```text
Browser launched
Application opened
Customer searched
Patient found
Patient deactivated
Booking created
Test passed
```

When a test fails, logs help identify the exact step where the failure occurred.

---

## Automated Business Flow

The core automation scenario currently focuses on the customer/patient booking process.

### Step 1 — Launch Application

The Selenium WebDriver initializes the configured browser and opens the ZooBook application.

### Step 2 — Customer/Patient Search

The automation searches for the patient/customer using the available identification information.

### Step 3 — Existing Patient Validation

The framework checks whether the patient already exists in the system.

If the patient does not exist:

```text
Create New Customer/Patient
```

If the patient already exists:

```text
Identify Existing Patient
        ↓
Update / Inactivate Current State
        ↓
Continue Required Workflow
```

### Step 4 — Patient Creation

For a new patient, the automation enters the required information and creates the record.

### Step 5 — Booking Creation

After identifying or creating the patient, the automation navigates to the booking functionality.

Required booking information is entered automatically.

### Step 6 — Validation

The framework validates whether the expected booking/customer workflow has completed successfully.

### Step 7 — Reporting and Logging

Execution information is stored in:

```text
Reports/
logs/
```

This provides traceability for both successful and failed automation runs.

---

## Design Pattern

The framework follows the **Page Object Model (POM)**.

Instead of writing Selenium code directly inside every test:

```python
driver.find_element(...).click()
driver.find_element(...).send_keys(...)
```

the framework keeps application actions inside page classes.

For example:

```python
customer_page.create_customer()
booking_page.create_booking()
```

### Benefits

- Better code reuse
- Easier maintenance
- Reduced duplicate code
- Cleaner test cases
- Easier debugging
- Better scalability
- Improved readability

---

## Automation Architecture

The overall framework flow can be represented as:

```text
                Test Cases
                    │
                    ▼
              Page Objects
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       Locators          Test Data
          │                   │
          └─────────┬─────────┘
                    ▼
              Base Selenium
                    │
                    ▼
               WebDriver
                    │
                    ▼
             ZooBook Web App
                    │
             ┌──────┴──────┐
             ▼             ▼
           Logs          Reports
```

---

## Prerequisites

Before running the framework, ensure that the following are installed:

```text
Python 3.x
pip
Google Chrome / supported browser
Compatible WebDriver
```

Verify Python:

```bash
python --version
```

Verify pip:

```bash
pip --version
```

---

## Clone Repository

```bash
git clone https://github.com/haroondhanyal/ZooBookAssesment.git
```

Navigate to the project:

```bash
cd ZooBookAssesment
```

---

## Install Dependencies

If the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Typical dependencies for this type of framework include:

```text
selenium
pytest
```

---

## Test Execution

Automation tests can be executed from the terminal depending on the existing test runner configuration.

For standard Python execution:

```bash
python <test_file>.py
```

If PyTest is configured:

```bash
pytest
```

For detailed PyTest output:

```bash
pytest -v
```

For a specific test:

```bash
pytest testcases/<test_file>.py -v
```

---

## Recommended Framework Improvements

The existing framework can be further enhanced by adding:

- PyTest fixtures
- `requirements.txt`
- `.env` environment configuration
- Explicit waits instead of static waits
- Screenshot capture on failure
- HTML reporting
- Allure reporting
- Test tagging
- Data-driven testing
- Parallel test execution
- Browser parameterization
- Retry mechanism for flaky tests
- CI/CD integration using GitHub Actions
- Dockerized Selenium execution

---

## Recommended Future Structure

For further scalability, the project can evolve into:

```text
ZooBookAssesment/
│
├── config/
│   ├── config.py
│   └── .env
│
├── base/
│   ├── driver_factory.py
│   └── base_page.py
│
├── locators/
│   ├── customer_locators.py
│   └── booking_locators.py
│
├── pages/
│   ├── customer_page.py
│   └── booking_page.py
│
├── tests/
│   ├── test_customer.py
│   └── test_booking.py
│
├── testdata/
│   └── test_data.json
│
├── utilities/
│   ├── logger.py
│   ├── waits.py
│   └── screenshots.py
│
├── reports/
├── screenshots/
├── logs/
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Key Automation Principles

The framework is designed around:

**Maintainability**  
Application changes should require minimum updates to automation code.

**Reusability**  
Common Selenium actions and page methods should be reusable across tests.

**Separation of Concerns**  
Locators, page actions, data, configuration, and test scenarios remain separate.

**Scalability**  
New ZooBook modules and scenarios can be added without restructuring the entire framework.

**Traceability**  
Reports and logs provide execution history and failure information.

---

## Project Summary

ZooBook Automation Framework demonstrates a structured approach to UI test automation using **Python and Selenium WebDriver**.

The current automation focuses on customer/patient management and booking workflows while the modular Page Object Model architecture provides a foundation for adding additional ZooBook scenarios in the future.

The project demonstrates practical implementation of:

- Selenium WebDriver
- Python automation
- Page Object Model
- Modular framework design
- Test data separation
- Reusable locators
- Automated customer/patient workflows
- Booking automation
- Logging
- Reporting
