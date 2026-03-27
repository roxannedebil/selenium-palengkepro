import time
import pyautogui

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
from menu_helper import click_menu_item  # your existing helper

driver = webdriver.Chrome()
driver.get("https://palengkeproph-test-prod.vercel.app/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

def slow_type(element, text, delay=0.2):
    # slow types text input
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

try:
    # sign in
    username_box = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_box = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    print("✔ Username and Password fields found")

    slow_type(username_box, "admin")
    slow_type(password_box, "demo123")
    print("✔ Typed username and password")

    sign_in_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.MuiButtonBase-root[type='submit']")
    ))
    time.sleep(1)
    sign_in_btn.click()
    print("✔ Logged in successfully")

    click_menu_item(driver, "Stall Management", is_submenu=False)
    click_menu_item(driver, "Stall Available", is_submenu=True)
    time.sleep(0.5)  # wait for React rendering

    # close drawer
    drawer_toggle = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "button.MuiButtonBase-root.MuiIconButton-root")
    )
    drawer_toggle.click()
    time.sleep(0.3)
    print("✔ Drawer toggled (closed if it was open)")

    # Wait for table
    # Wait for table to appear using XPath
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[3]/table"))
    )

    # Wait for rows to load (skip header if any)
    rows = WebDriverWait(driver, 10).until(
        lambda d: table.find_elements(By.TAG_NAME, "tr") if table.find_elements(By.TAG_NAME, "tr") else False
    )

    if len(rows) <= 1:
        print("Error: Table is empty or only header")
    else:
        print(f"Table has {len(rows) - 1} data rows ")

        # Skip header row by starting from index 1
        for index, row in enumerate(rows[1:], start=2):  # start=2 for user-friendly row number
            try:
                # Find the "View History" button inside this row
                history_btn = WebDriverWait(row, 5).until(
                    EC.element_to_be_clickable((By.XPATH, ".//button[@aria-label='View History']"))
                )

                # Scroll into view
                driver.execute_script("arguments[0].scrollIntoView(true);", history_btn)

                # Click the button
                history_btn.click()
                print(f"✔ Clicked 'View History' icon on row {index} ")
                break  # stop if only first data row is needed

            except Exception as e:
                print(f"No button in row {index} or not clickable ❌: {e}")

    time.sleep(2)
    close_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Close']")
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", close_btn)
    close_btn.click()
    print(f"✔ Clicked Close Button successfully.")
    time.sleep(2)


    delete_stall_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Delete Stall']"))
    )
    delete_stall_btn.click()
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()
    print("✔ Delete Stall button clicked successfully")
    time.sleep(2)

    ready_for_leasing_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Ready for Leasing']"))
    )
    ready_for_leasing_btn.click()
    print("✔ Ready for Leasing button clicked successfully")
    time.sleep(2)

    # create new lease




except Exception as e:
    print("Test Failed:", e)

finally:
    time.sleep(10)
    driver.quit()