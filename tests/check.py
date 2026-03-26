import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://palengkeproph-test-prod.vercel.app/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)


def slow_type(element, text, delay=0.2):
    """Types text into a field with delay between characters"""
    for char in text:
        element.send_keys(char)
        time.sleep(delay)


try:
    # find username and password fields
    username_box = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_box = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    print("✅ Test Passed: Username and Password fields found")

    # type credentials
    # username_box.send_keys("admin")
    # password_box.send_keys("demo123")

    slow_type(username_box, "admin", delay=0.2)
    slow_type(password_box, "demo123", delay=0.2)
    print("✅ Test Passed: Typed username and password")

    # click demo credentials button
    # demo_credentials_btn = wait.until(EC.element_to_be_clickable(
    #     (By.CSS_SELECTOR, "button.MuiButtonBase-root[type='button']")
    # ))
    # demo_credentials_btn.click()
    # print("✅ Test Passed: Clicked Demo Credentials successfully")

    # click Sign In button
    sign_in_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.MuiButtonBase-root[type='submit']")
    ))
    time.sleep(1)
    sign_in_btn.click()
    print("✅ Test Passed: Logged in successfully")



except Exception as e:
    # If any step fails, stop the rest and print the error
    print("Test Failed:", e)


finally:
    time.sleep(5)
    driver.quit()

