#!/usr/bin/env python3

# Author: Eva Witten
# Date: 2025-14-30
import os
import platform
import subprocess
from datetime import datetime

def run_command(cmd):
    result = subprocess.run(['bash', '-c', cmd], capture_output=True, text=True)
    return result.stdout.strip()

def print_options():
    print('''
    1. Create a Symbolic Link
    2. Delete a Symbolic Link
    3. Generate a symbolic link report
    4. Exit/quit the script''')

def create_symlink():
    choice = input("Enter the name of the file you want to create a symbolic link for:")
    print(run_command('ln -s "choice" "$HOME/Desktop/choice"'))


def delete_symlink():
    choice = input("Enter the name of the file you want to delete a symbolic link for:")
    print(run_command('unlink "$HOME/Desktop/choice"'))

def generate_symlink_report():
    # Lists all symbolic links in the student home directory, including target paths.
    print(run_command('find "$HOME/Desktop/" -type l -exec ls -l {} \;'))
    # Provides a total count of symbolic links in the user’s home directory.
    print(run_command('echo "Total symbolic links: $(find "$HOME/Desktop/" -type l | wc -l)"'))


def main():
    quit = False
    while quit == False:
        print_options()
        choice = input('Enter number of choice: ')
        # os.system('clear')
        if choice == '1':
            print(create_symlink())
        elif choice == '2':
            print(delete_symlink())
        elif choice == '3':
            print(generate_symlink_report())
        elif choice == '4':
            print("Goodbye!")
            quit = True
        elif choice == 'quit':
            print("Goodbye!")
            quit = True
        else: 
            print("womp womp do it right\n\n")

if __name__ == "__main__":
    main()