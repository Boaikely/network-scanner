import csv
import os

VENDOR_FILE = os.path.join(os.path.dirname(__file__), "mac-vendors.csv")
mac_db = {}

with open(VENDOR_FILE, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        if len(row) >= 2:
            raw_prefix = row[1].strip().replace("-", ":").upper()
            prefix = ":".join(raw_prefix.split(":")[0:3])
            vendor = row[2].strip()
            mac_db[prefix] = vendor

def identify_vendor(mac):
    normalized = mac.upper().replace("-", ":")
    prefix = ":".join(normalized.split(":")[0:3])
    return mac_db.get(prefix, "Unknown Vendor")


