import ifcopenshell

def checkRule(model):
    floors = model.by_type('IfcBuildingStorey')
import bpy

floors = [obj for obj in bpy.data.objects if "IfcBuildingStorey" in obj.name]

floors.sort(key=lambda obj: obj.location.z)

for i in range(1, len(floors)):
    floor1 = floors[i-1]
    floor2 = floors[i]
    
    z1 = floor1.location.z
    z2 = floor2.location.z
    
    elevation = z2 - z1
    print(f"Elevation between {floor1.name} and {floor2.name}: {elevation} Blender units")

    return result
