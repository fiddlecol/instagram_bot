from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def main():
    global browser
    try:
        # Initialize the browser (make sure you have the correct driver)
        browser = webdriver.Firefox()  # Ensure chromedriver is in your PATH or provide the path

        # Navigate to the page
        browser.get("https://www.instagram.com")

        # Optionally wait a bit to ensure the page is fully loaded
        time.sleep(5)  # Wait for 5 seconds

        # Debugging output: print the page source to ensure the page is loaded correctly
        print("Page Source Before Login:", browser.page_source)

        # Fill in the username and password fields
        username = "fiddleodera"
        password = "Fi16dd87le1"

        # Locate the username and password fields and fill them in
        username_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password")))

        username_field.send_keys(username)
        password_field.send_keys(password)

        # Wait until the login button is enabled and clickable
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, '_acan _acap _acas _aj1- _ap30')]"))
        )

        # Click the login button
        login_button.click()

        # Wait for the page to load after login
        time.sleep(5)  # Adjust the sleep duration as needed

        # Debugging output: print the current URL and page source after login
        print("Current URL After Login:", browser.current_url)
        print("Page Source After Login:", browser.page_source)

        # Keep the browser open for inspection
        time.sleep(30)  # Keep the browser open for 30 seconds for manual inspection

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(30)  # Keep the browser open for inspection if there's an error

    finally:
        # Close the browser after inspection
        browser.quit()


if __name__ == "__main__":
    main()
