import time

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

    # # close drawer
    # drawer_toggle = WebDriverWait(driver, 10).until(
    #     lambda d: d.find_element(By.CSS_SELECTOR, "button.MuiButtonBase-root.MuiIconButton-root")
    # )
    # drawer_toggle.click()
    # time.sleep(0.3)
    # print("✔ Drawer toggled (closed if it was open)")

    driver.switch_to.default_content()

    view_history_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='View Lease History']"))
    )
    view_history_btn.click()
    print("✔ View Lease History button clicked successfully")
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
    print("✔ Closed View Lease History successfully")
    time.sleep(2)

    # iframe = driver.find_element(By.TAG_NAME, "iframe")
    # driver.switch_to.frame(iframe)
    #
    # # now find & click your button
    # btn = driver.find_element(By.XPATH, "//svg[@data-testid='HistoryIcon']/ancestor::button")
    # btn.click()

    # switch back


    # delete_stall_btn = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Delete Stall']"))
    # )
    # delete_stall_btn.click()
    # alert = driver.switch_to.alert
    # time.sleep(1)
    # alert.accept()
    # print("✔ Delete Stall button clicked successfully")
    # time.sleep(2)

    ready_for_leasing_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to Lease Creation']"))
    )
    ready_for_leasing_btn.click()
    print("✔ Ready for Leasing button clicked successfully")

    # LEASE CREATION
    next_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))
    )
    next_btn.click()
    print("✔ Selected a Stall and clicked Next button successfully")

    tenant_name_box = wait.until(EC.presence_of_element_located((By.NAME, "tenantName")))
    business_name_box = wait.until(EC.presence_of_element_located((By.NAME, "tenantBusinessName")))
    contact_number_box = wait.until(EC.presence_of_element_located((By.NAME, "tenantContact")))
    email_address_box = wait.until(EC.presence_of_element_located((By.NAME, "tenantEmail")))
    address_box = wait.until(EC.presence_of_element_located((By.NAME, "tenantAddress")))
    print("✔ Tenant Information fields found")

    tenant_name_box.send_keys("Johnny Depth")
    time.sleep(1)
    business_name_box.send_keys("Johnny Meat Shop")
    time.sleep(1)
    contact_number_box.send_keys("09179189767")
    time.sleep(1)
    email_address_box.send_keys("johnny.d@email.com")
    time.sleep(1)
    address_box.send_keys("123 Quezon City")
    time.sleep(1)
    print("✔ Entered Tenant Information successfully")
    next_btn.click()
    time.sleep(3)
    print("✔ Clicked Next button successfully")

    # LEASE TERMS
    lease_start_box = wait.until(EC.presence_of_element_located((By.NAME, "leaseStart")))
    lease_end_box = wait.until(EC.presence_of_element_located((By.NAME, "leaseEnd")))
    monthly_rate_box = wait.until(EC.presence_of_element_located((By.NAME, "monthlyRate")))
    security_deposit_box = wait.until(EC.presence_of_element_located((By.NAME, "securityDeposit")))
    payment_term_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Payment Terms']/following::div[@role='combobox'][1]")))
    additional_info_box = wait.until(EC.presence_of_element_located((By.NAME, "remarks")))
    print("✔ Lease Information fields found")


    lease_start_box.clear()
    lease_start_box.send_keys("03-31-2026")
    time.sleep(1)
    lease_end_box.clear()
    lease_end_box.send_keys("03-31-2027")
    time.sleep(1)
    monthly_rate_box.send_keys("15000")
    time.sleep(1)
    security_deposit_box.send_keys("6000")
    time.sleep(1)

    payment_term_dropdown.click()
    option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Daily']")))
    option.click()
    time.sleep(2)

    additional_info_box.send_keys("Sample Remarks Test")
    time.sleep(3)
    print("✔ Entered Tenant Information successfully")
    next_btn.click()
    print("✔ Clicked Next button successfully")
    time.sleep(3)

    submit_for_approval_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit for Approval']")))
    # print("✔ Submit for Approval button found")
    submit_for_approval_btn.click()
    print("✔ Submit for Approval button clicked successfully")
except Exception as e:
    print("Test Failed:", e)

finally:
    time.sleep(10)
    driver.quit()