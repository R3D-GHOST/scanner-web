#librerias
import os
import time
import subprocess
#colores

#banner 
banner = """
 ____   ____  ____  _   _ _   _ _____ ____    __        _______ ____  
/ ___| / ___|/ __ \| \ | | \ | |___ /|  _ \   \ \      / /___ /| __ ) 
\___ \| |   / / _` |  \| |  \| | |_ \| |_) |___\ \ /\ / /  |_ \|  _ \ 
 ___) | |__| | (_| | |\  | |\  |___) |  _ <_____\ V  V /  ___) | |_) |
|____/ \____\ \__,_|_| \_|_| \_|____/|_| \_\     \_/\_/  |____/|____/ 
             \____/                                                   

"""
def whatweb():
    os.system('clear')
    print("enter the web url example")
    print("URL >>> https://www.google.com")
    scan = input(">>> ")
    web = subprocess.getoutput('whatweb --no-error -v ' + str(scan))
    print("This may take a few seconds or minutes.")
    time.sleep(5)
    os.system('clear')
    print(web)
def ports():
    os.system('clear')
    print("enter the ip or url example")
    print("IP >>> 96.124.xxx.xxx > www.google.com > https://www.google.com")
    nmap = input(">>> ")
    nmapSC = subprocess.Popen('sudo nmap -Pn -A -v ' + str(nmap))
    print("This may take several minutes")
    time.sleep(5)
    os.system('clear')
    print(nmapSC)
def sql():
    os.system('clear')
    print("SQLMAP TEST")
    print("enter the web url example")
    print("www.web.com > https://www.web.com")
    url = input(">>> ")
    os.system("sqlmap -u" +url+  " --dbs --forms --crawl=2")
#menu 
os.system('clear')
print(banner)
print("[1] >>> Web scan ")
print("[2] >>> Ports scan")
print("[3] >>> SQL Test")
print("[4] >>> EXIT SCRIPT")
opt_menu = input(">>> ")
if opt_menu == "1":
    whatweb()
if opt_menu == "2":
    ports()
if opt_menu == "3":
    sql()
if opt_menu == "4":
    exit
else:
    print("Invalid Error")