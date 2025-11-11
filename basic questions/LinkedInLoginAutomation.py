from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Step 1: Setup Chrome WebDriver
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

try:
    # Step 2: Open LinkedIn login page
    driver.get("https://www.linkedin.com/login")

    # Step 3: Wait for username and password fields to load
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))

    # Step 4: Enter dummy credentials
    username_input.send_keys("dummy_email@example.com")
    password_input.send_keys("dummy_password123")

    # Step 5: Click the "Sign in" button
    sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    sign_in_button.click()

    # Step 6: Wait for the page to load and print the title
    wait.until(EC.title_is_not("LinkedIn Login, Sign in | LinkedIn"))
    print("\nPage Title after login attempt:", driver.title)

except TimeoutException:
    print("\n❌ Timeout: Element not found or page took too long to load.")

except NoSuchElementException:
    print("\n❌ Error: One or more elements were not found on the page.")

except Exception as e:
    print(f"\n⚠️ An unexpected error occurred: {e}")

finally:
    # Step 7: Close the browser
    driver.quit()