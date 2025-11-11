# instagram_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import sys

def instagram_login(username="dummy_user", password="dummy_pass"):
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # enable if you want headless
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.instagram.com/accounts/login/")
        wait = WebDriverWait(driver, 15)

        # Wait for username and password inputs
        user_el = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        pass_el = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        user_el.send_keys(username)
        pass_el.send_keys(password)

        # Submit: button[type="submit"]
        submit = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit.click()

        # Wait for either a known error element or some page change (example: presence of nav or title change)
        try:
            wait.until(EC.any_of(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'incorrect')]")),
                EC.presence_of_element_located((By.XPATH, "//nav"))  # nav exists on successful login
            ))
        except Exception:
            pass

        print("Page title after attempt:", driver.title)
    except TimeoutException:
        print("❌ Timeout: page elements did not load in time.")
    except NoSuchElementException as e:
        print("❌ Element not found:", e)
    except Exception as e:
        print("⚠️ Unexpected error:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    # replace with dummy/test creds only
    instagram_login(username="dummy_user@example.com", password="dummy_password")