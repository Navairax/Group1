# BIManalyst group 1
# Focus Area: Architecture, ceilings
# The claim: We are checking is the floor to floor hight of every story in the building, and if it matches the claim made in the report. 
<img width="266" alt="image" src="https://github.com/user-attachments/assets/79eda680-0ed1-4983-8389-48f31095e5bf">, # Architectural Report: CES_BLD_24_06_ARC, page number: 22
# The code:
import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()

import bpy

# It looks for all objects in the Blender, (bpy.data.objects) whose name contains "IfcBuildingStorey". These objects represent building stories (floors) in an IFC model.

floors = [obj for obj in bpy.data.objects if "IfcBuildingStorey" in obj.name]

# The floors are sorted based on their height (Z-coordinate) to ensure they are ordered from lowest to highest. This allows the script to calculate the elevation difference between consecutive floors.
floors.sort(key=lambda obj: obj.location.z)

# The code loops through pairs of adjacent floors, taking each pair ex. floor 1 and floor 2, floor 2 and floor 3).
# For each pair, it extracts their Z-coordinates (z1 and z2), which represents their heights.
# It then calculates the elevation difference by subtracting z1 from z2.

for i in range(1, len(floors)):
    floor1 = floors[i-1]
    floor2 = floors[i]
    
    z1 = floor1.location.z
    z2 = floor2.location.z
    
    elevation = z2 - z1
    print(f"Elevation between {floor1.name} and {floor2.name}: {elevation} Blender units")

# Then it prints the elevation difference between the floors.


![image](https://github.com/user-attachments/assets/c1ec1831-ded5-42cb-ad2d-79cbc28c81d4)

