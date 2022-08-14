import sys
import time
import random
import requests
import colorama

from bs4 import BeautifulSoup
from halo import Halo
from colorama import Fore, Back, Style, init



# Create the session and set the proxies.
proxies = {'http': 'socks5://127.0.0.1:9050',
           'https': 'socks5://127.0.0.1:9050'}

s = requests.Session()
s.proxies = proxies

# Terminal Spinner
spinner = Halo(text='Loading', color='green', spinner='hamburger')

try:
    spinner.start()
    time.sleep(2)
    spinner.text = 'Verifying the Connections'
    ## Proxy
    r = s.get('https://check.torproject.org/')
    spinner.succeed('It works!')
    spinner.stop()
except requests.ConnectionError as e:
    spinner.start()
    time.sleep(2)
    spinner.color = 'red'
    spinner.text = 'URL Error - Empty URL or Wrong URL'
    time.sleep(2)
    spinner.fail('URL Validation Error - May be Tor is Not Enabled')
    spinner.stop()
    print("OOPS!! Connection Error.")
    ## Normal Request
    p = requests.get('https://check.torproject.org/')
    BS = BeautifulSoup(p.text, "html.parser")
    METATAG = BS.select('h1.off')[0].text.strip()
    print(METATAG)
except requests.Timeout as e:
    print("OOPS!! Timeout Error")
except requests.RequestException as e:
    spinner.start()
    time.sleep(2)
    spinner.color = 'red'
    spinner.text = 'Wrong URL or Empty Field'
    time.sleep(2)
    spinner.fail('Wrong URL or Empty Field')
    spinner.stop()
    print("OOPS!! General Error")
except (KeyboardInterrupt, SystemExit):
    spinner.stop()
    print("okay, Cancelled")
    sys.exit(1)
else:
    print(r.url + " - Reading URL")
    BS = BeautifulSoup(r.text, "html.parser")
    METATAG = BS.select('h1.not')[0].text.strip()
    print(METATAG)


# Server_Status

session = requests.Session()

session.trust_env = False

r = session.get("https://anonfiles.com")

print("\n\n[+] Server_Status: " + str(r))


# API_Requests

response = requests.get('https://api.anonfiles.com')

print("\n\n[+] API_Status: " + str(response))

response.raise_for_status()

print("[+] ERROR_API: " + str(response.raise_for_status()))


# status_code

print("\n\n[+] STATUS_CODE: " + str(response.status_cod>


def openfile():
        global result
        result = open(sys.argv[1], "w")
        print(f"\n\n[+] All valid links will be in {sys.argv[1]}")
        print("")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = int(1)
length = int(10)


def scan():
        for n in range(number):
                pswd =''
                for i in range(length):
                        pswd += random.choice(chars)
        main_url = "https://anonfiles.com/" + pswd
        r = requests.get(main_url)
        if r.status_code == 200:
                print(f"{Fore.WHITE}[{Fore.GREEN}200{Style.RESET_ALL}] {main_url} exists!")
                result.write(main_url + "\n")
        else:
                print(f"{Fore.WHITE}[{Fore.RED}404{Style.RESET_ALL}] {main_url} does not exist")


# STOPT

def main():
        try:
                openfile()
                print(banner)
                while True:
                        scan()
        except KeyboardInterrupt:
                print(f"\n\n{Fore.RED}STOPT{Fore.RESET} \n\nAll results has been writed in {sys.argv[1]}")
        except:
                print(argserror)

main()
