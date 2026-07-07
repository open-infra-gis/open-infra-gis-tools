"""
Create a simple layer inventory from a WMS GetCapabilities XML document.

Usage:
python geoserver_getcapabilities_inventory.py
"""

from urllib.parse import urlencode
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import csv

WMS_URL = "https://example.com/geoserver/wms"
OUTPUT_CSV = "wms_layer_inventory.csv"

url = WMS_URL + ("&" if "?" in WMS_URL else "?") + urlencode({
    "service": "WMS",
    "request": "GetCapabilities",
})

xml_data = urlopen(url, timeout=60).read()
root = ET.fromstring(xml_data)

rows = []
for layer in root.findall(".//{*}Layer"):
    name = layer.find("{*}Name")
    title = layer.find("{*}Title")
    if name is not None and name.text:
        rows.append({
            "name": name.text,
            "title": title.text if title is not None else "",
        })

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "title"])
    writer.writeheader()
    writer.writerows(rows)

print(f"[DONE] {OUTPUT_CSV} | layers={len(rows)}")
