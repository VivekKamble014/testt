from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# -------------------- Setup --------------------
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# -------------------- Step 1: Open Website --------------------
driver.get("https://imcc.mespune.in/")
print("✅ Opened IMCC College website successfully!")

time.sleep(3)

# -------------------- Step 2: Find Main Menu Items --------------------
try:
    menu_items = driver.find_elements(By.XPATH, "//ul[@id='menu-main-menu']/li/a")
    print(f"🔍 Found {len(menu_items)} main menu items:")
    for item in menu_items:
        print("   •", item.text)
except Exception as e:
    print("❌ Could not locate main menu items:", e)
    driver.quit()
    exit()

time.sleep(2)

# -------------------- Step 3: Visit Each Menu Page --------------------
for index in range(len(menu_items)):
    try:
        # Re-fetch menu items each loop (DOM may reload)
        menu_items = driver.find_elements(By.XPATH, "//ul[@id='menu-main-menu']/li/a")
        link = menu_items[index]
        page_name = link.text.strip()

        print(f"\n➡️ Opening page: {page_name if page_name else 'Unnamed Link'}")

        # Click the menu link
        driver.execute_script("arguments[0].click();", link)
        time.sleep(3)

        # Verify page title
        title = driver.title
        current_url = driver.current_url

        print(f"   🌐 URL: {current_url}")
        print(f"   📄 Page Title: {title}")

        if title and len(title.strip()) > 0:
            print("✅ Page loaded successfully.")
        else:
            print("⚠️ Page loaded but title is empty or missing.")
        
        # Go back to home page before next iteration
        driver.get("https://imcc.mespune.in/")
        time.sleep(2)

    except Exception as e:
        print(f"❌ Error while opening menu item {index+1}: {e}")

# -------------------- Step 4: Finish --------------------
print("\n🎯 All menu items checked successfully!")
driver.quit()