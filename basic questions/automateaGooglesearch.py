from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Step 1: Setup Chrome browser
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

try:
    # Step 2: Open Google
    driver.get("https://www.google.com/")

    # Step 3: Wait for search bar to load
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

    # Step 4: Enter search query
    search_query = "Top 10 programming languages 2025"
    search_box.send_keys(search_query)

    # Step 5: Press Enter to search
    search_box.send_keys(Keys.RETURN)

    # Step 6: Wait for search results to load
    results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h3")))

    # Step 7: Print titles of first 5 search results
    print("\nTop 5 Search Results for:", search_query)
    print("-" * 50)
    for i, result in enumerate(results[:5], start=1):
        print(f"{i}. {result.text}")

finally:
    # Step 8: Close the browser
    driver.quit()