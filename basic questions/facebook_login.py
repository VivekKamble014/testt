# facebook_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def facebook_login(username="dummy_email@example.com", password="dummy_password"):
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.facebook.com/")
        wait = WebDriverWait(driver, 15)

        email = wait.until(EC.presence_of_element_located((By.ID, "email")))
        pwd = wait.until(EC.presence_of_element_located((By.ID, "pass")))

        email.clear(); email.send_keys(username)
        pwd.clear(); pwd.send_keys(password)

        # Click Sign in
        signin = driver.find_element(By.NAME, "login")
        signin.click()

        # Wait for possible error or title change
        try:
            wait.until(EC.any_of(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'The email or mobile number')]")),
                EC.title_is_not("Facebook - log in or sign up")
            ))
        except Exception:
            pass

        time.sleep(1)  # small pause for title to update
        print("Page title after attempt:", driver.title)
    except TimeoutException:
        print("❌ Timeout: elements not found in time.")
    except NoSuchElementException as e:
        print("❌ Element not found:", e)
    except Exception as e:
        print("⚠️ Unexpected error:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    facebook_login(username="wrong_email@example.com", password="wrongpassword")