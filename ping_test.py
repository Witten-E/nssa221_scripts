#!/usr/bin/python3.9
import os
import time
import subprocess

# made by Eva Witten

def print_options():
    print('''
    1. Display the default gateway
    2. Test local connectivity
    3. Test remote connectivity
    4. Test DNS resolution
    5. Exit/quit the script''')
    


def default_gateway():
    command = "route -n | grep 'UG[ \t]' | awk '{print $2}'"
    try: 
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return "sybau default mf"
    
    
def ping_local():
    command = ["ping", "-c", "4", "127.0.0.1"]
    try: 
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return "sybau local mf"

def DNS_resolution():
    command = ['ping', '-c', '2', "www.google.com"]
    try: 
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return "sybau default mf"


def ping_command(destination):
    command = ['ping', '-c', '2', destination]
    try: 
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return "sybau default mf"
    
    
    
    
def main():
    false = True
    while false:
        print_options()
        choice = input('Enter number of choice: ')
        if choice == '1':
            os.system('clear')
            print("Your gateway :" + default_gateway())
        elif choice == '2':
            os.system('clear')
            print(ping_local())
        elif choice == '3':
            os.system('clear')
            print(ping_command("129.21.3.17"))
        elif choice == '4':
            os.system('clear')
            print(DNS_resolution())
        elif choice == '5':
            os.system('clear')
            print("Goodbye!")
            true = False
            false = true
        else: 
            print("womp womp do it right\n\n")
            
        
    

if __name__ == "__main__":
    main()
