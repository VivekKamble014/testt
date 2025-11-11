# youtube_video_search.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import time

def youtube_search_and_play(search_query="Python tutorial for beginners"):
    # ---------- Setup ----------
    options = Options()
    # Keeping it natural (no headless or mute)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 15)

    try:
        # 1️⃣ Open YouTube
        driver.get("https://www.youtube.com/")
        print("✅ Opened YouTube")

        # 2️⃣ Wait for search box and enter query
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
        search_box.clear()
        search_box.send_keys(search_query)
        print(f"🔍 Entered search query: {search_query}")

        # 3️⃣ Click the search button
        search_button = wait.until(EC.element_to_be_clickable((By.ID, "search-icon-legacy")))
        search_button.click()
        print("✅ Clicked search button")

        # 4️⃣ Wait for results to appear and click the first video
        first_video = wait.until(
            EC.element_to_be_clickable((By.XPATH, '(//a[@id="video-title"])[1]'))
        )
        video_title = first_video.get_attribute("title")
        print(f"▶️ Opening first video: {video_title}")
        first_video.click()

        # 5️⃣ Let video play for 10 seconds
        time.sleep(10)
        print("🎬 Played video for 10 seconds")

    except TimeoutException:
        print("❌ Timeout: YouTube elements not loaded properly.")
    except Exception as e:
        print("⚠️ Error:", e)
    finally:
        driver.quit()
        print("✅ Browser closed")

if __name__ == "__main__":
    youtube_search_and_play("Python tutorial for beginners")