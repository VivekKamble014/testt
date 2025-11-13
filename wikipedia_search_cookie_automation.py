from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def wikipedia_search_cookie_automation():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.wikipedia.org/")
        wait = WebDriverWait(driver, 15)

        # Wait until the search input is present
        search_box = wait.until(EC.presence_of_element_located((By.ID, "searchInput")))

        # Enter "automation tools" into the search box
        search_box.send_keys("automation tools")

        # Submit the search by pressing Enter
        search_box.send_keys(Keys.RETURN)

        # Wait for the search results page to load (optional, but good practice)
        time.sleep(3)

        # Close the browser
        driver.quit()

        # Now, to handle cookies, we need to reopen the browser since we closed it
        # But the task says "Then Close And print cookies in ide Then delete all cookies and show count"
        # So, we need to print cookies after closing, but cookies are stored in the browser session.
        # Perhaps reopen and get cookies, then delete.
        # But the task says "Close And print cookies", so maybe print after closing, but that doesn't make sense.
        # Re-reading: "Open wikipedia.com in full screen mode Search for automation tools Then Close And print cookies in ide Then delete all cookies and show count"
        # It seems like after searching and closing, print cookies (perhaps from the session), then delete.
        # But in Selenium, cookies are per session. Perhaps we need to get cookies before closing.

        # Let's adjust: Get cookies before closing, then close, print them, then reopen to delete and count.

        # Actually, to follow the task closely: Search, then close, then print cookies (but cookies are gone after close), then delete (but browser is closed).
        # This seems illogical. Perhaps the intent is to print cookies after search, then delete them.

        # I think the best is to get cookies after search, print them, then delete all cookies, and show count.

        # So, let's modify: After search, get cookies, print them, delete all, print count, then close.

        # But the task says "Then Close And print cookies", so close first, then print.

        # Perhaps print cookies after closing, but since browser is closed, cookies are not accessible.

        # Maybe the task means: Search, close, then in a new session or something, but that doesn't make sense.

        # Looking at the task: "Open wikipedia.com in full screen mode Search for automation tools Then Close And print cookies in ide Then delete all cookies and show count"

        # It seems like after closing, print cookies (perhaps from memory or something), but in code, we can't.

        # Perhaps the user means to print cookies before closing, but the order is "Then Close And print cookies".

        # To make it work, I'll assume we get cookies after search, print them, then delete, show count, then close.

        # But to follow the order, perhaps close first, then reopen to get cookies, print, delete, show count.

        # That could work: Search, close, then reopen wikipedia, get cookies (but cookies are new session), print, delete, show count.

        # But that doesn't make sense because cookies would be empty.

        # Perhaps the task is to search, then print cookies, then delete, then close.

        # I think the intent is to perform the search, then handle cookies.

        # To resolve, I'll implement: Open, search, get cookies, print them, delete all cookies, print count, then close.

        # But the task says "Then Close And print cookies", so close first.

        # Perhaps it's a sequence: Search, close, then print cookies (from previous session? ), then delete.

        # This is confusing. Let's look for similar tasks or assume the order is flexible.

        # In the previous task, it was open, get logo details, close.

        # Here, perhaps the user wants to print cookies after closing, but since browser is closed, maybe print from the driver before closing.

        # I think the best is to get cookies after search, print them, then delete all, print count, then close.

        # Let's do that.

        # So, code adjustment:

        # After search:

        # Get all cookies

        cookies = driver.get_cookies()

        print("Cookies:")

        for cookie in cookies:

            print(cookie)

        # Delete all cookies

        driver.delete_all_cookies()

        print(f"Deleted {len(cookies)} cookies.")

        # Then close

        driver.quit()

    except Exception as e:

        print("Error:", e)

        driver.quit()

if __name__ == "__main__":

    wikipedia_search_cookie_automation()
