## BIManalyst group 1
## Focus Area: Architecture, ceilings
### The claim: We are checking the floor to floor height of every story in the building, and if it matches the claim made in the report. 
<img width="266" alt="image" src="https://github.com/user-attachments/assets/79eda680-0ed1-4983-8389-48f31095e5bf">, 
### Architectural Report: CES_BLD_24_06_ARC, page number: 22

### It looks for all objects in the Blender, (bpy.data.objects) whose name contains "IfcBuildingStorey". These objects represent building stories (floors) in an IFC model.


### The floors are sorted based on their height (Z-coordinate) to ensure they are ordered from lowest to highest. This allows the script to calculate the elevation difference between consecutive floors.


### The code runs through pairs of adjacent floors, taking each pair. Fx, floor 1 and floor 2, floor 2 and floor 3).
### For each pair, it extracts their Z-coordinates (z1 and z2), which represents their heights.
### It then calculates the elevation difference by subtracting z1 from z2.


### Then it prints the elevation difference between the floors. It shows in the output of the cod, that the height from floor to floor is 3,8 meters.


![image](https://github.com/user-attachments/assets/c1ec1831-ded5-42cb-ad2d-79cbc28c81d4)

### To get the number of elevations, we ran 'things = file.by_type('IfcBuildingStorey'): 



