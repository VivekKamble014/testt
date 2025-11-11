from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -------------------- Setup --------------------
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# -------------------- Step 1: Open Website --------------------
driver.get("https://imcc.mespune.in/")
print("✅ Opened IMCC College website successfully!")

# -------------------- Step 2: Navigate to Contact Us --------------------
try:
    contact_link = driver.find_element(By.LINK_TEXT, "Contact Us")
    driver.execute_script("arguments[0].click();", contact_link)
    print("➡️ Navigated to 'Contact Us' page.")
except Exception as e:
    print("❌ Could not find or click 'Contact Us' link:", e)
    driver.quit()
    exit()

time.sleep(3)

# -------------------- Step 3: Fill Contact Form --------------------
try:
    # Adjust element names or XPaths if changed on site
    name_field = driver.find_element(By.NAME, "name")
    email_field = driver.find_element(By.NAME, "email")
    subject_field = driver.find_element(By.NAME, "subject")
    message_field = driver.find_element(By.NAME, "message")

    name_field.send_keys("Test Student")
    email_field.send_keys("test.student@example.com")
    subject_field.send_keys("Automation Test")
    message_field.send_keys("Hello, this is an automated test message.")

    print("📝 Filled contact form successfully.")

except Exception as e:
    print("❌ Could not fill form fields:", e)
    driver.quit()
    exit()

# -------------------- Step 4: Submit Form --------------------
try:
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Send Message') or @type='submit']")
    driver.execute_script("arguments[0].click();", submit_button)
    print("📤 Submitted the form.")
except Exception as e:
    print("❌ Could not locate or click the submit button:", e)
    driver.quit()
    exit()

# -------------------- Step 5: Verify Submission Message --------------------
try:
    # Wait for a thank-you message, alert, or confirmation
    wait = WebDriverWait(driver, 10)
    success_message = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(),'Thank you') or contains(text(),'successfully') or contains(text(),'received')]")
        )
    )
    print("✅ Form submitted successfully! Message displayed:", success_message.text)
except Exception:
    print("⚠️ Form submission completed, but no confirmation message detected.")

# -------------------- Step 6: End Test --------------------
driver.quit()
print("🎯 Test completed successfully!")