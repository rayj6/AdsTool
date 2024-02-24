from colorama import Fore, Style
import os
import json
from tool import ClickItem
import time



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
# CheckProxyList()