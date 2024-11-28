# A3: The script below is intended to analyze the building design ifc file.
# Its intended to extract information about the building storeys, calculates floor to floor heights, and idendifies potential floows and ceilings. 

# Imports the path and ifcopenshell library
from pathlib import Path
import ifcopenshell

# Defines model_path as a path looking at the IFC file
model_path = Path("/Users/hajarbenjdya/Downloads/CES_BLD_24_10_ARC.ifc")
# Checks if the path leads to a file otherwise, prints an error message. 
if not model_path.is_file():
    raise FileNotFoundError(f"No file found at {model_path}!")

try:
    model = ifcopenshell.open(model_path)
    print("Model opened successfully.")

except Exception as e:
    print(f"An error occurred while opening the model: {e}")

# To extract IfcBuildingStorey elements and store them in 'storeys'
storeys = model.by_type("IfcBuildingStorey")

# TO filter out storeys without an Elevation attribute and sort them by Elevation
storeys_with_elevation = [
    storey for storey in storeys if getattr(storey, "Elevation", None) is not None
]

# To sort the filtered storeys by their elevation attribute 
storeys_with_elevation.sort(key=lambda s: s.Elevation)


# To print floor-to-floor heights label 
print("Floor-to-Floor Heights:")
# Runs an iterative code to collect all the stories and selects between them
for i in range(1, len(storeys_with_elevation)):
    storey1 = storeys_with_elevation[i - 1]
    storey2 = storeys_with_elevation[i]

    # to retrieve elevation, and labeling it 0 if its missing
    z1 = getattr(storey1, "Elevation", 0)
    z2 = getattr(storey2, "Elevation", 0)

    # to get the names of storeys, 
    name1 = getattr(storey1, "Name", f"Storey {i}")
    name2 = getattr(storey2, "Name", f"Storey {i+1}")

    #Calculates the height diffference between the storeys and prints the result
    height_difference = z2 - z1
    print(f"Height between {name1} and {name2}: {height_difference} IFC units")
