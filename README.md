# 🔍 Python Network Scanner

A Linux-based Python tool to discover devices on your local network, identify vendors, guess operating systems, scan common ports, and export results.

## 📦 Features

- ARP-based host discovery
- MAC address vendor lookup (IEEE OUI list)
- OS type guessing (Linux, Android, iOS, etc.)
- Port scanning (22, 80, 443, etc.)
- Colored terminal output + emoji highlights 😎
- CSV export to `output/scan_results.csv`

## 🛠 Requirements

- Python 3
- `scapy`, `tabulate`
- Root privileges to scan network interfaces

Install requirements:
```bash
pip install -r requirements.txt
