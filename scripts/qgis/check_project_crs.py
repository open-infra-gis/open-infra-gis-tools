"""
Check CRS consistency for all vector layers in the current QGIS project.
Run inside QGIS Python Console.
"""

from qgis.core import QgsProject, QgsMapLayerType

EXPECTED_CRS_AUTHID = "EPSG:4326"

for layer in QgsProject.instance().mapLayers().values():
    if layer.type() != QgsMapLayerType.VectorLayer:
        continue
    status = "OK" if layer.crs().authid() == EXPECTED_CRS_AUTHID else "MISMATCH"
    print(f"[{status}] {layer.name()} | {layer.crs().authid()} | features={layer.featureCount()}")
