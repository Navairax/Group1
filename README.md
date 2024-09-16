# BIManalyst group 1
# Focus Area: Architecture, ceilings
# The claim: We are checking the floor to floor hight of every story in the building, and if it matches the claim made in the report. 
<img width="266" alt="image" src="https://github.com/user-attachments/assets/79eda680-0ed1-4983-8389-48f31095e5bf">, # Architectural Report: CES_BLD_24_06_ARC, page number: 22
# The code:
import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()

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
