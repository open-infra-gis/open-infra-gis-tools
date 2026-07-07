"""
Audit field names and null counts for the active QGIS vector layer.
Run inside QGIS Python Console.
"""

layer = iface.activeLayer()
if layer is None:
    raise RuntimeError("No active layer selected.")

print(f"Layer: {layer.name()}")
print(f"Features: {layer.featureCount()}")

for field in layer.fields():
    null_count = 0
    for feature in layer.getFeatures():
        value = feature[field.name()]
        if value is None or value == "":
            null_count += 1
    print(f"{field.name()} | {field.typeName()} | null_or_empty={null_count}")
