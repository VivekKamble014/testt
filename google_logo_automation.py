from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def google_logo_automation():
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

        # Print a property of the logo, e.g., the src attribute
        print("Logo src attribute:", logo.get_attribute("src"))

    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    google_logo_automation()
