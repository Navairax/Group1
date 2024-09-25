# BIManalyst Group 01
import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()

import bpy

def checkRule(floors):
    
    floors.sort(key=lambda obj: obj.location.z)
    
    for i in range(1, len(floors)):
        floor1 = floors[i-1]
        floor2 = floors[i]
        
        z1 = floor1.location.z
        z2 = floor2.location.z
        
        elevation = z2 - z1
        print(f"Elevation between {floor1.name} og {floor2.name}: {elevation} Blender units")

floors = [obj for obj in bpy.data.objects if "IfcBuildingStorey" in obj.name]

checkRule(floors)

things = file.by_type('IfcBuildingStorey')
print("num of elevations in IFC-model:", len(things))
        

