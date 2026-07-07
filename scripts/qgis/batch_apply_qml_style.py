"""
Apply a QML style file to QGIS project layers whose names contain a keyword.
Run inside QGIS Python Console.
"""

from qgis.core import QgsProject

LAYER_NAME_CONTAINS = "YOUR_KEYWORD"
QML_STYLE_PATH = r"C:\GIS\styles\your_style.qml"

for layer in QgsProject.instance().mapLayers().values():
    if LAYER_NAME_CONTAINS.lower() in layer.name().lower():
        layer.loadNamedStyle(QML_STYLE_PATH)
        layer.triggerRepaint()
        print(f"[STYLE] Applied to {layer.name()}")
