"""
Check basic WMS/WFS GetCapabilities availability for generic OGC service URLs.

Usage:
python check_ogc_service_status.py
"""

from urllib.parse import urlencode
from urllib.request import urlopen
from time import perf_counter

SERVICES = [
    {
        "name": "Example WMS",
        "base_url": "https://example.com/geoserver/wms",
        "service": "WMS",
    },
    {
        "name": "Example WFS",
        "base_url": "https://example.com/geoserver/wfs",
        "service": "WFS",
    },
]

TIMEOUT_SECONDS = 20

def capabilities_url(base_url, service):
    query = urlencode({"service": service, "request": "GetCapabilities"})
    separator = "&" if "?" in base_url else "?"
    return f"{base_url}{separator}{query}"

for item in SERVICES:
    url = capabilities_url(item["base_url"], item["service"])
    start = perf_counter()
    try:
        with urlopen(url, timeout=TIMEOUT_SECONDS) as response:
            body = response.read(500).decode("utf-8", errors="ignore")
            elapsed = perf_counter() - start
            ok = "Capabilities" in body or "WMS" in body or "WFS" in body
            print(f"[{'OK' if ok else 'CHECK'}] {item['name']} | {response.status} | {elapsed:.2f}s | {url}")
    except Exception as exc:
        elapsed = perf_counter() - start
        print(f"[ERROR] {item['name']} | {elapsed:.2f}s | {exc}")
