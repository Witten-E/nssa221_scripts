#!/usr/bin/env python3

# Author: Eva Witten
# Date: 2025-14-30
import os
import platform
import subprocess
from datetime import datetime
from geoip import geolite2 as gl

LOGFILE = "syslog.log"

def run_command(cmd):
    result = subprocess.run(['bash', '-c', cmd], capture_output=True, text=True)
    return result.stdout.strip()

def find_tens(list):
    result = {}
    for ip in list:
        if ip in result.keys():
            result[ip] += 1
        else:
            result[ip] = 0
    to_be_deleted = []
    for ip in result.keys():
        if result[ip] < 10:
            to_be_deleted.append(ip)
    for ip in to_be_deleted:
        del result[ip]
        
    return result


def main():
    run_command('clear')
    date = datetime.now().strftime("%B %d, %Y")
    print(f"Attacker Report: {date}\n\nCOUNT   IP ADDRESS          COUNTRY")
    ips = run_command("grep -oE 'from ([0-9]{1,3}\.){3}[0-9]{1,3}' "+ LOGFILE +" | awk '{print $2}'")
    ips = ips.strip().split("\n")
    counts = find_tens(ips)
    counts = sorted(counts.items(), key=lambda item: item[1])
    for ip in counts:
        print(f"{ip[1]:<8}{ip[0]:<20}{gl.lookup(ip[0]).to_dict()['country']}")




if __name__ == "__main__":
    main()
