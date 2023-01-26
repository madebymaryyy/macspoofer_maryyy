#!/usr/bin/env python
import subprocess
import optparse

print("[HELLO] Thanks for paying attention to my MAC spoofer tool. ")
print("[WARNING] This tool was created only for educational/anonymity purposes. Don't use it for any malicious/suspicious things.")
print("[CREDITS] Made by: madebymaryyy // 2023")

def macchanger(interface, newmac):  ##funkce macchanger, zde se splni prikazy ktery prave meni mac adresu##
    print("[SUCCESS] Changing your MAC address for interface " + interface + " to " + newmac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", newmac])
    subprocess.call(["ifconfig", interface, "up"])
def get_arguments(): ##argumenty a k cemu jsou##
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Specify interface, use --help")
    parser.add_option("-m", "--mac", dest="newmac", help="Specify the name of new MAC address, use --help")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[ERROR] Please specify the interface, use --help for how-to")
    elif not options.newmac:
        parser.error("[ERROR] Please specify the MAC, use --help for how-to")
    return options

options = get_arguments()
macchanger(options.interface, options.newmac)


