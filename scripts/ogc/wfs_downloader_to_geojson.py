"""
Download WFS features to GeoJSON using generic parameters.

Usage:
python wfs_downloader_to_geojson.py
"""

from urllib.parse import urlencode
from urllib.request import urlopen
from pathlib import Path

WFS_URL = "https://example.com/geoserver/wfs"
TYPENAME = "workspace:layer_name"
OUTPUT_GEOJSON = "wfs_output.geojson"

params = {
    "service": "WFS",
    "version": "2.0.0",
    "request": "GetFeature",
    "typeNames": TYPENAME,
    "outputFormat": "application/json",
}

url = WFS_URL + ("&" if "?" in WFS_URL else "?") + urlencode(params)

with urlopen(url, timeout=60) as response:
    data = response.read()

Path(OUTPUT_GEOJSON).write_bytes(data)
print(f"[DONE] {OUTPUT_GEOJSON}")
