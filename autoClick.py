from colorama import Fore, Style
import os
import json
import time

# ----------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style
from datetime import datetime

# ----------------------------------------------------------------


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


# ----------------------------------------------------------------


def DisplayData(proxy):

    def proxyStatus():
        if proxy == "Active":
            return ("Proxy status: " + Fore.GREEN + proxy + Style.RESET_ALL)
        else:
            return ("Proxy status: " + Fore.RED + proxy + Style.RESET_ALL)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN +"AUTO CLICK SYSTEM" + Style.RESET_ALL)
    print("--------------------------------")
    print(proxyStatus())
    Link = input("Target: ")
    AdsElm = input("Select element: ")
    print("--------------------------------")

    with open("./Proxy List.json", 'r') as file:
        data = json.load(file)
        # formatted_data = json.dumps(data, indent=4
        # )
        index = 0
        count = 0
        while True:
        # while index < 10:
            for i in range(len(data)):
                item = data[i]
                # print(json.dumps(data[i], indent=4))
                print(count, end=" | ")
                ClickItem(Link, AdsElm,item, item.get("IP"))
                time.sleep(1)
                count +=1
            index += 1

    print("\n\n\n")
    


def CheckProxyList():
    
    with open("./Proxy List.json", 'r') as file:
        data = json.load(file)
        formatted_data = json.dumps(data, indent=4)
        for i in range(len(data)):
            ip_address = data[i]["IP"]
            print(ip_address)
        
    if len(data) > 0:
        return "Active"
    else:
        return "Inactive"
    # print (len(data))


DisplayData(CheckProxyList())