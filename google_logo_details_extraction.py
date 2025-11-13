from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def google_logo_details_extraction():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.google.com/")
        wait = WebDriverWait(driver, 15)

        # Wait until the Google logo is fully loaded
        logo = wait.until(EC.presence_of_element_located((By.ID, "hplogo")))

        # Wait an additional 3 seconds to ensure full load
        time.sleep(3)

        # Extract logo details
        logo_src = logo.get_attribute("src")
        logo_alt = logo.get_attribute("alt")
        logo_height = logo.get_attribute("height")
        logo_width = logo.get_attribute("width")
        logo_size = logo.size  # This gives a dict with 'height' and 'width'

        # Print the extracted details
        print("Google Logo Details:")
        print(f"Source URL (src): {logo_src}")
        print(f"Alt Text: {logo_alt}")
        print(f"Height (attribute): {logo_height}")
        print(f"Width (attribute): {logo_width}")
        print(f"Dimensions (size): Height = {logo_size['height']}, Width = {logo_size['width']}")

    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    google_logo_details_extraction()
