import time

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

def click_upload_stalls(driver, timeout=20):
    # retry loop to handle re-render
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            btn = driver.find_element(By.XPATH, "//button[normalize-space()='Upload Stalls']")
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
            btn.click()
            print("✔ Upload Stalls clicked successfully")
            return btn
        except (StaleElementReferenceException, ElementClickInterceptedException):
            time.sleep(0.3)
    print("x - Failed to click Upload Stalls")
    return None

def upload_file(input_selector, file_path):
    # uploads a file to an <input type='file'> element.
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, input_selector))
    )
    file_input.send_keys(file_path)
    print(f"✔ File '{file_path}' uploaded successfully")

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

    # driver.switch_to.default_content()

    view_history_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='View History']"))
    )
    view_history_btn.click()
    alert = driver.switch_to.alert
    time.sleep(1)
    print("✔ View History button clicked successfully")
    time.sleep(2)

    # rows = table.find_elements(By.TAG_NAME, "tr")
    # if len(rows) > 0:
    #     print(f"Table has {len(rows)} rows ✅")
    # else:
    #     print("Table is empty ❌")

    # icon = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='HistoryIcon']"))
    # )
    # icon.click()  # click the SVG itself
    # print("✔ View History button clicked successfully")
    # time.sleep(2)

    close_history_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Close']")
    close_history_btn.click()
    print("✔ Closed View History successfully")
    time.sleep(2)

    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

    # now find & click your button
    btn = driver.find_element(By.XPATH, "//svg[@data-testid='HistoryIcon']/ancestor::button")
    btn.click()

    # switch back


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



except Exception as e:
    print("Test Failed:", e)

finally:
    time.sleep(10)
    driver.quit()