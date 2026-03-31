import time
import pyautogui

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
from tests.menu_helper import click_menu_item

driver = webdriver.Chrome()
driver.get("https://palengkeproph-test-prod.vercel.app/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

def slow_type(element, text, delay=0.2):
    # slow types text input
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

# def click_upload_stalls(driver, timeout=20):
#     # retry loop to handle re-render
#     end_time = time.time() + timeout
#     while time.time() < end_time:
#         try:
#             btn = driver.find_element(By.XPATH, "//button[normalize-space(text())='Upload Stalls']")
#             driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
#
#             btn.click()
#             print("✔ Upload Stalls clicked successfully")
#             return btn
#         except (StaleElementReferenceException, ElementClickInterceptedException):
#             time.sleep(0.3)
#     print("x - Failed to click Upload Stalls")
#     return None

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
    click_menu_item(driver, "Stall Inventory", is_submenu=True)
    time.sleep(0.5)  # wait for React rendering

    # close drawer
    # drawer_toggle = WebDriverWait(driver, 10).until(
    #     lambda d: d.find_element(By.CSS_SELECTOR, "button.MuiButtonBase-root.MuiIconButton-root")
    # )
    # drawer_toggle.click()
    # time.sleep(0.3)
    # print("✔ Drawer toggled (closed if it was open)")

    wait = WebDriverWait(driver, 10)
    upload_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Upload Stalls')]"))
    )
    upload_btn.click()

    # upload_stalls_btn = click_upload_stalls(driver)
    # if not upload_stalls_btn:
    #     raise Exception("x - Upload Stalls button could not be clicked.")


    dl_template_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Download Excel Template']")
    dl_template_btn.click()
    print("✔ Download Excel button clicked successfully")
    time.sleep(2)


    select_file_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Select Excel File']")
    select_file_btn.click()
    print("✔ Select Excel File button clicked successfully")
    time.sleep(2)

    # close file chooser dialog
    pyautogui.press('esc')
    time.sleep(2)

    file_input_selector = "input[type='file']"
    file_path = r"C:\Users\Admin\Downloads\ecm_stalls.xlsx"  # file upload path
    upload_file(file_input_selector, file_path)
    time.sleep(2)

    add_to_map_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Add to Map & Edit Layout']")
    add_to_map_btn.click()
    print("✔ Add to Map & Edit Layout button clicked successfully")
    time.sleep(2)

    # cancel_upload_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")
    # cancel_upload_btn.click()
    # print("✔ Canceled Upload")
    # time.sleep(2)

    save_layout_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Save Layout']")
    save_layout_btn.click()
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()
    print("✔ Save Layout button clicked successfully")
    time.sleep(2)

    # click map view button
    # map_view_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Map']")
    # map_view_btn.click()

    electric_label = driver.find_element(By.XPATH, "//label[.//span[text()='Electricity']]")
    electric_label.click()
    print("✔ Eletricity Utility Filter checked successfully")
    electric_label.click()
    time.sleep(1)

    water_label = driver.find_element(By.XPATH, "//label[.//span[text()='Water']]")
    water_label.click()
    print("✔ Water Utility Fitler checked successfully")
    water_label.click()
    time.sleep(1)

    drainage_label = driver.find_element(By.XPATH, "//label[.//span[text()='Drainage']]")
    drainage_label.click()
    print("✔ Drainage Utility Filter checked successfully")
    drainage_label.click()
    time.sleep(1)

    ventilation_label = driver.find_element(By.XPATH, "//label[.//span[text()='Ventilation']]")
    ventilation_label.click()
    print("✔ Ventilation Utility Filter checked successfully")
    ventilation_label.click()
    time.sleep(2)

    # add choosing of dropdown
    # to add


    # edit_layout_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Edit Layout']")
    # save_layout_btn.click()
    # print("✔ Edit Layout button clicked successfully")
    # time.sleep(2)

    export_map_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Export Map (PNG)']")
    export_map_btn.click()
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()
    print("✔ Export Map (PNG) button clicked successfully")
    time.sleep(2)

    center_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Center']")
    center_btn.click()
    print("✔ Center button clicked successfully")
    time.sleep(2)

    zoom_in_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Zoom In']")
    zoom_in_btn.click()
    print("✔ Zoom In button clicked successfully")
    time.sleep(2)

    save_layout_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Save Layout']")
    save_layout_btn.click()
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()
    print("✔ Save Layout button clicked successfully")
    time.sleep(2)

    # click table button
    table_view_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Table']")
    table_view_btn.click()



except Exception as e:
    print("Test Failed:", e)

finally:
    time.sleep(10)
    driver.quit()