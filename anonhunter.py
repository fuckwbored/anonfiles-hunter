import argparse
import requests
import random
import time
import colorama
from bs4 import BeautifulSoup
from halo import Halo
from colorama import Fore, Back, Style, init

init(autoreset=True)

banner = '''
'''

# Terminal Spinner
spinner = Halo(text='Loading', color='green', spinner='hamburger')

# Set up proxies for Tor network
proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}

# Create the session and set the proxies
s = requests.Session()
s.proxies = proxies

try:
    spinner.start()
    time.sleep(2)
    spinner.text = 'Verifying the Connections Tor Network.'

    # Verify that Tor network is enabled
    r = s.get('https://check.torproject.org')
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
    print("OOPS!! General Error.")

except (KeyboardInterrupt, SystemExit):
    spinner.stop()
    print("okay, Cancelled.")
    sys.exit(1)

else:
    print(r.url + " - Reading URL")
    BS = BeautifulSoup(r.text, "html.parser")
    METATAGS = BS.select('h1')
    if METATAGS:
        METATAG = METATAGS[0].text.strip()
        print(METATAG)
    else:
        print("No Meta Tags Found")

# Server Status
session = requests.Session()
session.trust_env = False
r = session.get("https://anonfiles.com")
print("\n\n[+] Server_Status: " + str(r))

# API Requests & status_code
response = requests.get('https://api.anonfiles.com')
print("\n\n[+] API_Status: " + str(response))
response.raise_for_status()
print("[+] ERROR_API: " + str(response.raise_for_status()))
print("\n\n[+] STATUS_CODE: " + str(response.status_code))

def get_file_info_api(file_id):
    url = f"https://api.anonfiles.com/v2/file/{file_id}/info"
    response = s.get(url)
    data = response.json()
    return data

def generate_ids(chars, length, number):
    ids = []
    for i in range(number):
        id = ''
        for j in range(length):
            id += random.choice(chars)
        ids.append(id)
    return ids

def check_file_exists(file_id):
    data = get_file_info_api(file_id)
    if data['status']:
        print('File name:', data['data']['file']['metadata']['name'])
        print('File size:', data['data']['file']['metadata']['size']['readable'])
        print('File URL:', data['data']['file']['url']['short'])
    else:
        print(f"File ID {file_id} does not exist on Anonfiles")

def main():
    parser = argparse.ArgumentParser(description='Anonfiles Hunter')
    parser.add_argument('-t', '--file_id', type=str, help='Anonfiles file ID')
    parser.add_argument('-o', '--output', type=str, help='Output file for results')
    args = parser.parse_args()

    file_id = args.file_id

    if file_id:
        check_file_exists(file_id)
    else:
        print("No file ID provided.")

    if args.output:
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        length = 10
        number = 100
        ids = generate_ids(chars, length, number)

        with open(args.output, 'w') as f:
            for id in ids:
                data = get_file_info_api(id)
                if data['status']:
                    f.write(f"{id}\n")
                    print(f"File ID {id} exists on Anonfiles")
                else:
                    print(f"File ID {id} does not exist on Anonfiles")

if __name__ == '__main__':
    main()
