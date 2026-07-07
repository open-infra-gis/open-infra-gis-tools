"""
Print basic area/length summary for vector layers in the current QGIS project.
Run inside QGIS Python Console.
"""

from qgis.core import QgsProject, QgsWkbTypes, QgsMapLayerType

for layer in QgsProject.instance().mapLayers().values():
    if layer.type() != QgsMapLayerType.VectorLayer:
        continue
    geom_type = QgsWkbTypes.geometryType(layer.wkbType())
    total = 0.0
    for f in layer.getFeatures():
        g = f.geometry()
        if not g or g.isEmpty():
            continue
        if geom_type == QgsWkbTypes.LineGeometry:
            total += g.length()
        elif geom_type == QgsWkbTypes.PolygonGeometry:
            total += g.area()
    print(f"{layer.name()} | features={layer.featureCount()} | total={total}")
