def click_menu_item(driver, item_text, is_submenu=False, wait_time=10, collapse_parent=False):
    # Click a menu or submenu item by visible text.
    # Avoid stale element issues by locating elements fresh each time.

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    wait = WebDriverWait(driver, wait_time)

    if is_submenu:
        # Locate submenu fresh each time
        element = wait.until(lambda d: d.find_element(
            By.XPATH, f"//span[text()='{item_text}']/ancestor::a"
        ))
    else:
        element = wait.until(lambda d: d.find_element(
            By.XPATH, f"//span[text()='{item_text}']"
        ))

    # Scroll into view before clicking (Material-UI safe)
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
    element.click()
    print(f"✔ Clicked {'submenu' if is_submenu else 'menu'}: {item_text}")

    time.sleep(0.5)  # wait for animation

    if is_submenu and collapse_parent:
        # Locate parent fresh to avoid stale reference
        try:
            parent_menu = wait.until(lambda d: element.find_element(
                By.XPATH, "./ancestor::div[contains(@class,'MuiCollapse-root')]/preceding-sibling::li//span"
            ))
            driver.execute_script("arguments[0].click();", parent_menu)
            print(f"✔ Collapsed parent menu: {parent_menu.text}")
            time.sleep(0.3)
        except:
            print("⚠️ Could not collapse parent menu (skipping)")