
import time
from selenium import webdriver
from menu_helper import click_menu_item
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

    # Stall Management
    click_menu_item(driver, "Stall Management", is_submenu=False)
    time.sleep(0.5)  # wait for animation
    # click_menu_item(driver, "Stall Inventory", is_submenu=True)
    # time.sleep(0.5)
    # click_menu_item(driver, "Stall Available", is_submenu=True)

    # Lease Management
    click_menu_item(driver, "Lease Management", is_submenu=False)
    time.sleep(0.5)
    # click_menu_item(driver, "Lease Records", is_submenu=True)
    # click_menu_item(driver, "Lease Approval", is_submenu=True)
    # click_menu_item(driver, "Lease Renewal", is_submenu=True)

    click_menu_item(driver, "Tenant Management", is_submenu=False)
    time.sleep(0.5)
    click_menu_item(driver, "Market Collections", is_submenu=False)
    time.sleep(0.5)

    # click_menu_item(driver, "Payment Recording", is_submenu=True)
    # click_menu_item(driver, "Collection Management", is_submenu=True)

    click_menu_item(driver, "User Management", is_submenu=False)
    time.sleep(0.5)
    click_menu_item(driver, "Security Management", is_submenu=False)
    time.sleep(0.5)
    click_menu_item(driver, "Settings", is_submenu=False)
    time.sleep(0.5)
    click_menu_item(driver, "Dashboard", is_submenu=False)
    time.sleep(0.5)

except Exception as e:
    # If any step fails, stop the rest and print the error
    print("Test Failed:", e)


finally:
    time.sleep(10)
    driver.quit()

