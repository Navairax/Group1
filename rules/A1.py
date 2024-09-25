# BIManalyst Group 01
import ifcopenshell

def checkRule(model):

    floors = model.by_type('IfcBuildingStorey')
    
    floors.sort(key=lambda obj: obj.ObjectPlacement.RelativePlacement.Location.Coordinates[2])

    for i in range(1, len(floors)):
        floor1 = floors[i-1]
        floor2 = floors[i]
        
        z1 = floor1.ObjectPlacement.RelativePlacement.Location.Coordinates[2]
        z2 = floor2.ObjectPlacement.RelativePlacement.Location.Coordinates[2]
        
        elevation = z2 - z1
        print(f"Elevation between {floor1.name} and {floor2.name}: {elevation} Blender units")
        
#things = file.by_type('IfcBuildingStorey')
#print("num of elevations", len(things))
        

