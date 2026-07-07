"""
Export all vector layers in the current QGIS project to a single GeoPackage.
Run inside QGIS Python Console.
"""

from pathlib import Path
from qgis.core import QgsProject, QgsMapLayerType, QgsVectorFileWriter, QgsCoordinateTransformContext

OUTPUT_GPKG = r"C:\GIS\project_layers_export.gpkg"
Path(OUTPUT_GPKG).parent.mkdir(parents=True, exist_ok=True)

options = QgsVectorFileWriter.SaveVectorOptions()
options.driverName = "GPKG"
options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteFile

first = True
for layer in QgsProject.instance().mapLayers().values():
    if layer.type() != QgsMapLayerType.VectorLayer:
        continue
    options.layerName = layer.name().replace(" ", "_")[:60]
    options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteFile if first else QgsVectorFileWriter.CreateOrOverwriteLayer
    error = QgsVectorFileWriter.writeAsVectorFormatV3(layer, OUTPUT_GPKG, QgsCoordinateTransformContext(), options)
    print(f"[EXPORT] {layer.name()} -> {OUTPUT_GPKG} | {error}")
    first = False
