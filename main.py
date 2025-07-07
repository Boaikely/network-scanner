from scanner.arp_scan import discover_hosts
from scanner.port_scan import scan_open_ports
from scanner.mac_lookup import identify_vendor
from tabulate import tabulate
import csv
import os

# ANSI colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

def guess_os(vendor, ports):
    if "Apple" in vendor:
        return "macOS / iOS 🍏"
    elif "Samsung" in vendor or "Huawei" in vendor:
        return "Android 🤖"
    elif 62078 in ports:
        return "iOS Device 📱"
    elif 5555 in ports:
        return "Android Debug 🔧"
    elif 22 in ports and len(ports) == 1:
        return "Linux (SSH) 🐧"
    elif 3389 in ports:
        return "Windows (RDP) 🪟"
    else:
        return "Unknown 💭"

ip_range = input("Enter IP range to scan (e.g. 192.168.1.0/24): ")
hosts = discover_hosts(ip_range)

results = []
export_rows = []

for host in hosts:
    ip = host['ip']
    mac = host['mac']
    vendor = identify_vendor(mac)
    open_ports = scan_open_ports(ip)
    os_guess = guess_os(vendor, open_ports)

    if vendor == "Unknown Vendor":
        colored_vendor = f"{RED}{vendor}{RESET}"
    else:
        colored_vendor = f"{YELLOW}{vendor}{RESET}"

    ports_str = f"{GREEN}{', '.join(map(str, open_ports))} 🔐{RESET}" if open_ports else f"{RED}None ❌{RESET}"

    # Table output
    results.append([
        f"{CYAN}{ip}{RESET}",
        mac,
        f"{colored_vendor} ({os_guess})",
        ports_str
    ])

    # CSV output (clean ANSI codes)
    export_rows.append([
        ip,
        mac,
        f"{vendor} ({os_guess})",
        ", ".join(map(str, open_ports)) if open_ports else "None"
    ])

# Terminal table
print("\n📊 Scan Results:\n")
print(tabulate(results, headers=["IP Address", "MAC Address", "Device Type", "Open Ports"], tablefmt="fancy_grid"))

# Save to CSV
output_path = "output/scan_results.csv"
os.makedirs("output", exist_ok=True)
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["IP Address", "MAC Address", "Device Type", "Open Ports"])
    writer.writerows(export_rows)

print(f"\n📁 Results saved to: {output_path}")

