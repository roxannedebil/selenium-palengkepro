import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
from menu_helper import click_menu_item  # your existing helper

# --- SETUP DRIVER ---
driver = webdriver.Chrome()
driver.get("https://palengkeproph-test-prod.vercel.app/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# --- HELPER FUNCTIONS ---
def slow_type(element, text, delay=0.2):
    # Types text into a field with delay between characters
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

def click_upload_stalls(driver, timeout=20):
    # Clicks the 'Upload Stalls' button safely even if React keeps re-rendering the DOM.
    # retry loop to handle React re-render
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
    # Uploads a file to an <input type='file'> element.
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, input_selector))
    )
    file_input.send_keys(file_path)
    print(f"✔ File '{file_path}' uploaded successfully")

# --- MAIN SCRIPT ---
try:
    # --- LOGIN ---
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

    # --- NAVIGATE MENU ---
    click_menu_item(driver, "Stall Management", is_submenu=False)
    click_menu_item(driver, "Stall Inventory", is_submenu=True)
    time.sleep(0.5)  # wait for React rendering

    # --- CLOSE THE DRAWER ---
    drawer_toggle = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "button.MuiButtonBase-root.MuiIconButton-root")
    )
    drawer_toggle.click()
    time.sleep(0.3)  # wait for drawer animation
    print("✔ Drawer toggled (closed if it was open)")

    # --- CLICK UPLOAD STALLS ---
    upload_stalls_btn = click_upload_stalls(driver)
    if not upload_stalls_btn:
        raise Exception("x - Upload Stalls button could not be clicked.")

    dl_template_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Download Excel Template']")
    dl_template_btn.click()
    print("✔ Download Excel button clicked successfully")
    time.sleep(2)

    select_file_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Select Excel File']")
    select_file_btn.click()
    print("✔ Select Excel File button clicked successfully")
    time.sleep(2)

    file_input_selector = "input[type='file']"  # adjust if needed
    file_path = r"C:\Users\SANDRA\.fontconfig\Downloads\stall_upload_template.xlsx"  # example local file
    upload_file(file_input_selector, file_path)
    time.sleep(2)

    add_to_map_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Add to Map & Edit Layout']")
    add_to_map_btn.click()
    print("✔ Add to Map & Edit Layout button clicked successfully")
    time.sleep(2)

    save_layout_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Save Layout']")
    save_layout_btn.click()
    print("✔ Save Layout button clicked successfully")

except Exception as e:
    print("Test Failed:", e)

finally:
    time.sleep(10)  # pause to see result
    driver.quit()