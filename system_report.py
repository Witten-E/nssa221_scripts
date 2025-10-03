#!/usr/bin/env python3

# Author: Eva Witten
# Date: 2025-09-30
import os
import platform
import subprocess
from datetime import datetime

def run_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()

def dns():
    with open("/etc/resolv.conf") as f:
        lines = f.readlines()
        dns_servers = [line.split()[1] for line in lines if line.startswith("nameserver")]
        primary_dns = dns_servers[0] if len(dns_servers) > 0 else "Not found"
        secondary_dns = dns_servers[1] if len(dns_servers) > 1 else "Not found"
        return f"Primary DNS: {primary_dns}\nSecondary DNS: {secondary_dns}"

def cpu_model():
    with open("/proc/cpuinfo") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("model name"):
                return line.split(":", 1)[1].strip()

def cpu_count():
    with open("/proc/cpuinfo") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("cpu cores"):
                return line.split(":", 1)[1].strip()

def main():
    os.system("clear")
    hostname = platform.node()
    logfile = os.path.expanduser(f"~/{hostname}_system_report.log")
    with open(logfile, "w") as f:
        def log_and_print(line):
            print(line)
            f.write(line + "\n")
        log_and_print(f"System Report for {hostname}")
        log_and_print(f"Date: {datetime.now()}")
        log_and_print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        log_and_print(f"Hostname: {run_command(['hostname'])}")
        log_and_print(f"Domain suffix: {run_command(["hostname", "-d"])}")
        log_and_print(f"IPv4 address: {run_command(["hostname", "-I"])}")
        log_and_print(f"Default gateway: {run_command(["ip", "route", "show", "default"])}")
        log_and_print(f"Network mask: {run_command(["ip", "-o", "-f", "inet", "addr", "show"])}")
        log_and_print(f"DNS servers: {dns()}")
        log_and_print(f"OS: {platform.system()}")
        log_and_print(f"Kernel: {platform.release()}")
        log_and_print(f"Disk space: {run_command(["df", "-h", "/"])}")
        log_and_print(f"CPU model: {cpu_model()}")
        log_and_print(f"CPU count: {cpu_count()}")
        log_and_print(f"RAM: {run_command(["free", "-h"])}")


if __name__ == "__main__":
    main()
