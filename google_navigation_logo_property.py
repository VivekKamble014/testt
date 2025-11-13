from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def google_navigation_logo_property():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.google.com/")
        wait = WebDriverWait(driver, 15)

        # Wait until the Google logo is fully loaded
        logo = wait.until(EC.presence_of_element_located((By.ID, "hplogo")))

        # Wait an additional 3 seconds
        time.sleep(3)

        # Open "About" - Google has "About" in the bottom right footer
        about_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "About")))
        about_link.click()

        # Wait for About page to load
        wait.until(EC.title_contains("About"))

        # Select "Company info" - on About page, click "Our company"
        company_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Our company")))
        company_link.click()

        # Wait for Company info page
        wait.until(EC.title_contains("Our company"))

        # Go return to about - use browser back
        driver.back()

        # Wait for About page
        wait.until(EC.title_contains("About"))

        # Good return to Google.com - back to Google
        driver.back()

        # Wait for Google.com
        wait.until(EC.title_contains("Google"))

        # Print any property of the logo, e.g., src attribute
        logo_src = logo.get_attribute("src")
        print(f"Logo src: {logo_src}")

    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    google_navigation_logo_property()
