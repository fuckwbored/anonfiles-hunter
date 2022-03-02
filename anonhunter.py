import random
import requests
import sys
import requests
from colorama import Fore, Back, Style
from colorama import init

init(autoreset=True)
banner = '''

                           _____ __          __                __           
  ____ _____  ____  ____  / __(_) /__  _____/ /_  __  ______  / /____  _____
 / __ `/ __ \/ __ \/ __ \/ /_/ / / _ \/ ___/ __ \/ / / / __ \/ __/ _ \/ ___/
/ /_/ / / / / /_/ / / / / __/ / /  __(__  ) / / / /_/ / / / / /_/  __/ /    
\__,_/_/ /_/\____/_/ /_/_/ /_/_/\___/____/_/ /_/\__,_/_/ /_/\__/\___/_/  

Telegram => t.me/termuxqew                                                                           
'''

chars = 'abcdefghijklnopqrstuvwxyz12345678901234567890QWERTYUIOPASDFGHJKLZXCVBNM'
number = int(1)
length = int(10)

argserror = f'''
{banner}
Error! You missed 1 arg!!!
usage: python3 anon.py output.file

ex: python3 anon.py output.txt
'''

def openfile():
	global result
	result = open(sys.argv[1], "w")
	print(f"[+] All valid links will be in {sys.argv[1]}")
	print("")


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

def main():
	try:
		openfile()
		print(banner)
		while True:
			scan()
	except KeyboardInterrupt:
		print(f"Good bye =) \n\nAll results has been writed in {sys.argv[1]}")
	except:
		print(argserror)

main()
