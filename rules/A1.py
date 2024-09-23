import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()

import bpy

def calculate_floor_elevations():
    # Get the IFC file (you may want to handle the case where the file is not found)
    file = IfcStore.get_file()

    # Find all objects that are part of the building storey
    floors = [obj for obj in bpy.data.objects if "IfcBuildingStorey" in obj.name]

    # Sort floors by their Z-coordinate (height)
    floors.sort(key=lambda obj: obj.location.z)

    # Calculate elevations between floors
    for i in range(1, len(floors)):
        floor1 = floors[i-1]
        floor2 = floors[i]
        
        z1 = floor1.location.z
        z2 = floor2.location.z
        
        elevation = z2 - z1
        print(f"Elevation between {floor1.name} and {floor2.name}: {elevation} Blender units")

# Call the function
calculate_floor_elevations()
