import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style
from datetime import datetime

# Get current time
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")


def ClickItem(url, AdsElm, additional_info, IP, delay=4):
    try:
        # Initialize Chrome webdriver
        driver = webdriver.Chrome()
        driver.get(url)

        # Wait for the specified delay
        time.sleep(delay)

        # Switch to the iframe
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, AdsElm))
        )
        driver.switch_to.frame(iframe)

        # Wait for the <a> tag with href attribute to be clickable
        a_tag = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href]"))
        )

        # Attempt to click the <a> tag
        a_tag.click()

        # If the click succeeded, print success message
        print(f"{formatted_time} | {Fore.GREEN + IP + Style.RESET_ALL}\t| {Fore.GREEN + 'Succesfull' + Style.RESET_ALL}")

        # Switch back to the default content
        driver.switch_to.default_content()

        # Close the webdriver
        driver.quit()

    except Exception as e:
        # If the click failed, print error message
        print(f"{formatted_time} | {Fore.GREEN + IP + Style.RESET_ALL} | {Fore.RED + 'Failed' + Style.RESET_ALL}")
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    url = "https://littlejuly.com"
    additional_info = {
        "IP": "20.205.61.143",
        "PORT": "80",
        "ANON": "Elite",
        "COUNTRY": "Hong Kong",
        "ISO": "HK",
        "PING": 217
    }
    ClickItem(url, additional_info, additional_info.get("IP"))
