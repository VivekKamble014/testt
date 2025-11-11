# generic_login_template.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

def automate_login(
    login_url,
    username_value,
    password_value,
    username_locator=(By.NAME, "username"),
    password_locator=(By.NAME, "password"),
    submit_locator=(By.XPATH, "//button[@type='submit']"),
    wait_seconds=15
):
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, wait_seconds)

    try:
        driver.get(login_url)
        user = wait.until(EC.presence_of_element_located(username_locator))
        pwd = wait.until(EC.presence_of_element_located(password_locator))
        user.clear(); user.send_keys(username_value)
        pwd.clear(); pwd.send_keys(password_value)

        submit = driver.find_element(*submit_locator)
        submit.click()

        # Wait shortly for title change or error message - you can customize this
        try:
            wait.until(EC.title_contains("Dashboard"))
            print("✅ Looks like login succeeded (title contains 'Dashboard'). Title:", driver.title)
        except Exception:
            print("ℹ️ Login attempted. Current title:", driver.title)
    except TimeoutException:
        print("❌ Timeout waiting for elements. Check selectors and page load.")
    except Exception as e:
        print("⚠️ Error:", e)
    finally:
        driver.quit()

# Example usage (fill correct selectors for target site)
if __name__ == "__main__":
    automate_login(
        login_url="https://example.com/login",
        username_value="dummy_user",
        password_value="dummy_pass",
        username_locator=(By.ID, "email"),      # adapt per site
        password_locator=(By.ID, "passwd"),     # adapt per site
        submit_locator=(By.CSS_SELECTOR, "button.login")
    )