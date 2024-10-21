from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed

# Counters for test results
test_passed = 0
test_failed = 0

# Define icons for passed and failed tests
passed_icon = "✅"  # Checkmark for passed tests
failed_icon = "❌"   # Cross mark for failed tests

# Create lists to store test results
passed_tests = []
failed_tests = []

# Function to run tests
def run_test(test_name, test_function):
    global test_passed, test_failed
    try:
        test_function()
        passed_tests.append(test_name)  # Store passed test
        test_passed += 1
    except AssertionError as e:
        failed_tests.append(f"{test_name}: {str(e)}")  # Store failed test
        test_failed += 1

# Test Cases

def reset_form():
    driver.get("file:///C:/Users/mewad/OneDrive/Desktop/STE%20Micro%20Project/registration.html")
    time.sleep(1)

# Test Case 1: Check Title
def test_title():
    reset_form()
    assert "Registration Form" in driver.title, "Title mismatch"

# Test Case 2: Check for Presence of Form Elements
def test_form_elements_present():
    reset_form()
    assert driver.find_element(By.ID, "name")
    assert driver.find_element(By.ID, "email")
    assert driver.find_element(By.ID, "address")
    assert driver.find_element(By.ID, "city")
    assert driver.find_element(By.ID, "state")
    assert driver.find_element(By.ID, "zip")
    assert driver.find_element(By.ID, "country")
    assert driver.find_element(By.ID, "phone")
    assert driver.find_element(By.ID, "terms")
    assert driver.find_element(By.ID, "register-btn")

# Test Case 3: Valid Form Submission
def test_valid_submission():
    reset_form()
    driver.find_element(By.ID, "name").send_keys("Jane Doe")
    driver.find_element(By.ID, "email").send_keys("jane.doe@example.com")
    driver.find_element(By.ID, "address").send_keys("456 Side St")
    driver.find_element(By.ID, "city").send_keys("Othertown")
    driver.find_element(By.ID, "state").send_keys("TX")
    driver.find_element(By.ID, "zip").send_keys("67890")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "phone").send_keys("0987654321")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert driver.find_element(By.ID, "success-msg").is_displayed(), "Form submission failed with valid data"

# Test Case 4: Empty Name
def test_empty_name():
    reset_form()
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "address").send_keys("123 Main St")
    driver.find_element(By.ID, "city").send_keys("Anytown")
    driver.find_element(By.ID, "state").send_keys("CA")
    driver.find_element(By.ID, "zip").send_keys("12345")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "phone").send_keys("1234567890")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert not driver.find_element(By.ID, "success-msg").is_displayed(), "Form submitted with empty name"

# Test Case 5: Empty Email
def test_empty_email():
    reset_form()
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "address").send_keys("123 Main St")
    driver.find_element(By.ID, "city").send_keys("Anytown")
    driver.find_element(By.ID, "state").send_keys("CA")
    driver.find_element(By.ID, "zip").send_keys("12345")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "phone").send_keys("1234567890")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert not driver.find_element(By.ID, "success-msg").is_displayed(), "Form submitted with empty email"

# Test Case 6: Invalid Email Format
def test_invalid_email():
    reset_form()
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("invalid-email")
    driver.find_element(By.ID, "address").send_keys("123 Main St")
    driver.find_element(By.ID, "city").send_keys("Anytown")
    driver.find_element(By.ID, "state").send_keys("CA")
    driver.find_element(By.ID, "zip").send_keys("12345")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "phone").send_keys("1234567890")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert not driver.find_element(By.ID, "success-msg").is_displayed(), "Form submitted with invalid email format"

# Test Case 7: Empty Address
def test_empty_address():
    reset_form()
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "city").send_keys("Anytown")
    driver.find_element(By.ID, "state").send_keys("CA")
    driver.find_element(By.ID, "zip").send_keys("12345")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "phone").send_keys("1234567890")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert not driver.find_element(By.ID, "success-msg").is_displayed(), "Form submitted with empty address"

# Test Case 8: Empty City
def test_empty_city():
    reset_form()
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "address").send_keys("123 Main St")
    driver.find_element(By.ID, "state").send_keys("CA")
    driver.find_element(By.ID, "zip").send_keys("12345")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "phone").send_keys("1234567890")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert not driver.find_element(By.ID, "success-msg").is_displayed(), "Form submitted with empty city"

# Test Case 9: Empty State
def test_empty_state():
    reset_form()
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "address").send_keys("123 Main St")
    driver.find_element(By.ID, "city").send_keys("Anytown")
    driver.find_element(By.ID, "zip").send_keys("12345")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "phone").send_keys("1234567890")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert not driver.find_element(By.ID, "success-msg").is_displayed(), "Form submitted with empty state"

# Test Case 10: Empty Zip Code
def test_empty_zip():
    reset_form()
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "address").send_keys("123 Main St")
    driver.find_element(By.ID, "city").send_keys("Anytown")
    driver.find_element(By.ID, "state").send_keys("CA")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "phone").send_keys("1234567890")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert not driver.find_element(By.ID, "success-msg").is_displayed(), "Form submitted with empty zip code"

# Test Case 11: Empty Country
def test_empty_country():
    reset_form()
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "address").send_keys("123 Main St")
    driver.find_element(By.ID, "city").send_keys("Anytown")
    driver.find_element(By.ID, "state").send_keys("CA")
    driver.find_element(By.ID, "zip").send_keys("12345")
    driver.find_element(By.ID, "phone").send_keys("1234567890")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert not driver.find_element(By.ID, "success-msg").is_displayed(), "Form submitted with empty country"

# Test Case 12: Empty Phone Number
def test_empty_phone():
    reset_form()
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "address").send_keys("123 Main St")
    driver.find_element(By.ID, "city").send_keys("Anytown")
    driver.find_element(By.ID, "state").send_keys("CA")
    driver.find_element(By.ID, "zip").send_keys("12345")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert not driver.find_element(By.ID, "success-msg").is_displayed(), "Form submitted with empty phone number"

# Test Case 13: Unchecked Terms and Conditions
def test_unchecked_terms():
    reset_form()
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "address").send_keys("123 Main St")
    driver.find_element(By.ID, "city").send_keys("Anytown")
    driver.find_element(By.ID, "state").send_keys("CA")
    driver.find_element(By.ID, "zip").send_keys("12345")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "phone").send_keys("1234567890")
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert not driver.find_element(By.ID, "success-msg").is_displayed(), "Form submitted without checking terms and conditions"

# Test Case 14: Valid Data Submission with All Fields
def test_valid_data_submission():
    reset_form()
    driver.find_element(By.ID, "name").send_keys("Jane Doe")
    driver.find_element(By.ID, "email").send_keys("jane.doe@example.com")
    driver.find_element(By.ID, "address").send_keys("456 Side St")
    driver.find_element(By.ID, "city").send_keys("Othertown")
    driver.find_element(By.ID, "state").send_keys("TX")
    driver.find_element(By.ID, "zip").send_keys("67890")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "phone").send_keys("0987654321")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert driver.find_element(By.ID, "success-msg").is_displayed(), "Form submission failed with valid data"

# Test Case 15: Zip Code with Letters
def test_zip_code_with_letters():
    reset_form()
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "address").send_keys("123 Main St")
    driver.find_element(By.ID, "city").send_keys("Anytown")
    driver.find_element(By.ID, "state").send_keys("CA")
    driver.find_element(By.ID, "zip").send_keys("123AB")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "phone").send_keys("1234567890")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert not driver.find_element(By.ID, "success-msg").is_displayed(), "Form submitted with invalid zip code"

# Test Case 16: Phone Number with Special Characters
def test_phone_number_with_special_characters():
    reset_form()
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "address").send_keys("123 Main St")
    driver.find_element(By.ID, "city").send_keys("Anytown")
    driver.find_element(By.ID, "state").send_keys("CA")
    driver.find_element(By.ID, "zip").send_keys("12345")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "phone").send_keys("123-456-7890")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "register-btn").click()
    time.sleep(1)
    assert driver.find_element(By.ID, "success-msg").is_displayed(), "Form submission failed with valid phone number"

# Load the registration form
driver.get("file:///C:/Users/mewad/OneDrive/Desktop/STE%20Micro%20Project/registration.html")

# Run all tests
run_test("Test Title Check", test_title)
run_test("Test Form Elements Presence", test_form_elements_present)
run_test("Test Valid Form Submission", test_valid_submission)
run_test("Test Empty Name", test_empty_name)
run_test("Test Empty Email", test_empty_email)
run_test("Test Invalid Email Format", test_invalid_email)
run_test("Test Empty Address", test_empty_address)
run_test("Test Empty City", test_empty_city)
run_test("Test Empty State", test_empty_state)
run_test("Test Empty Zip Code", test_empty_zip)
run_test("Test Empty Country", test_empty_country)
run_test("Test Empty Phone Number", test_empty_phone)
run_test("Test Unchecked Terms and Conditions", test_unchecked_terms)
run_test("Test Valid Data Submission with All Fields", test_valid_data_submission)
run_test("Test Zip Code with Letters", test_zip_code_with_letters)
run_test("Test Phone Number with Special Characters", test_phone_number_with_special_characters)

# Summary of test results
print("\nTest Results:")
print(f"Passed: {test_passed} {passed_icon}")
print(f"Failed: {test_failed} {failed_icon}")

# Display test results with icons
print("\nDetailed Results:")
for test in passed_tests:
    print(f"{passed_icon} {test}")
for test in failed_tests:
    print(f"{failed_icon} {test}")

# Close the driver
driver.quit()
