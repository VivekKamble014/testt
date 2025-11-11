from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Step 1: Open website
driver.get("https://imcc.mespune.in/")
print("✅ Website opened successfully!")

time.sleep(3)

# Step 2: Click on Student Login (update selector if necessary)
try:
    login_link = driver.find_element(By.LINK_TEXT, "Student Login")
    login_link.click()
    print("➡️ Navigated to Student Login Page")
except:
    print("❌ Could not find 'Student Login' link.")
    driver.quit()
    exit()

time.sleep(3)

# Step 3: Enter login credentials (replace IDs or XPaths as per actual portal)
try:
    driver.find_element(By.NAME, "username").send_keys("your_username")
    driver.find_element(By.NAME, "password").send_keys("your_password")
    driver.find_element(By.NAME, "login").click()
    print("🔐 Attempted to login")
except:
    print("❌ Unable to locate login elements")

time.sleep(3)

# Step 4: Verify successful login
if "dashboard" in driver.current_url.lower():
    print("✅ Login successful! Dashboard loaded.")
else:
    print("⚠️ Login may have failed. Check credentials or locator paths.")

driver.quit()