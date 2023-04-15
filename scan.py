#librerias
import os
import time
import subprocess

#colores
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RED = "\033[31m"
CYAN = "\033[36m"

#banner 
banner = """
{}{} ____   ____  ____  _   _ _   _ _____ ____    __        _______ ____  
/ ___| / ___|/ __ \| \ | | \ | |___ /|  _ \   \ \      / /___ /| __ ) 
\___ \| |   / / _` |  \| |  \| | |_ \| |_) |___\ \ /\ / /  |_ \|  _ \ 
 ___) | |__| | (_| | |\  | |\  |___) |  _ <_____\ V  V /  ___) | |_) |
|____/ \____\ \__,_|_| \_|_| \_|____/|_| \_\     \_/\_/  |____/|____/ 
             \____/{}                                                   
""".format(RED, BOLD, RESET)

def whatweb():
    os.system('clear')
    print("Enter the web url example:")
    print("{}URL >>> https://www.google.com{}".format(YELLOW, RESET))
    scan = input(">>> ")
    web = subprocess.getoutput('whatweb --no-error -v ' + str(scan))
    print("This may take a few seconds or minutes.")
    time.sleep(5)
    os.system('clear')
    print(web)

def ports():
    os.system('clear')
    print("Enter the IP or URL example:")
    print("{}IP >>> 96.124.xxx.xxx > www.google.com > https://www.google.com{}".format(YELLOW, RESET))
    nmap = input(">>> ")
    nmapSC = subprocess.Popen('sudo nmap -Pn -A -v ' + str(nmap), stdout=subprocess.PIPE, shell=True)
    print("This may take several minutes")
    time.sleep(5)
    os.system('clear')
    print(nmapSC.communicate()[0].decode('utf-8'))

def sql():
    os.system('clear')
    print("SQLMAP TEST")
    print("Enter the web url example:")
    print("{}www.web.com > https://www.web.com{}".format(YELLOW, RESET))
    url = input(">>> ")
    os.system("sqlmap -u " + url + " --dbs --forms --crawl=2")

#menu 
os.system('clear')
print(banner)
print("{}[1]{} >>> Web scan".format(BLUE, RESET))
print("{}[2]{} >>> Ports scan".format(BLUE, RESET))
print("{}[3]{} >>> SQL Test".format(BLUE, RESET))
print("{}[4]{} >>> EXIT SCRIPT".format(BLUE, RESET))
opt_menu = input(">>> ")
if opt_menu == "1":
    whatweb()
elif opt_menu == "2":
    ports()
elif opt_menu == "3":
    sql()
elif opt_menu == "4":
    exit()
else:
    print("{}Invalid option{}".format(RED, RESET))
