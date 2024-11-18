# The code path from pathlib and ifcopenshell to handle file paths and IFC file operations

from pathlib import Path
import ifcopenshell

#It tries to open an IFC model at the specified path. if the file does not exist, a filenotfounderror will be the output.If the file is successfully opened, it prints model opened successfully

model_path = Path("C:/Users/navai/OneDrive/Skrivebord/3. semester/41934 Vidergående BIM/CES_BLD_24_10_ARC.ifc")
if not model_path.is_file():
    raise FileNotFoundError(f"No file found at {model_path}!")

try:
    model = ifcopenshell.open(model_path)
    print("Model opened successfully.")

except Exception as e:
    print(f"An error occurred while opening the model: {e}")

# Extract IfcBuildingStorey elements and their elevations.The code retrieves all ifcbuildingstorey elements from the model using model.by_type(ifcbuiildingstorey)
storeys = model.by_type("IfcBuildingStorey")

# Filter out storeys without an Elevation and sort them by Elevation. it filters out storeys that have an elevaation attribute set to None and sorts the remaining storeys by their elevation value.
storeys_with_elevation = [
    storey for storey in storeys if getattr(storey, "Elevation", None) is not None
]
storeys_with_elevation.sort(key=lambda s: s.Elevation)

# Calculating floor-to-floor heights.
# It calculates and prints the height difference between storeys by iterating over the sorted storeys. 
#For each pair of adjacent storeys, the code gets elevation attribute and calculates the difference (z2-z1). it also retrieves the Name attribute to label the output.abs
#The resulta are printed in the format: "Height between [storey 1] and [storey 2]: [height difference] IFC units"
print("Floor-to-Floor Heights:")
for i in range(1, len(storeys_with_elevation)):
    storey1 = storeys_with_elevation[i - 1]
    storey2 = storeys_with_elevation[i]
    
    z1 = getattr(storey1, "Elevation", 0)
    z2 = getattr(storey2, "Elevation", 0)
    
    name1 = getattr(storey1, "Name", f"Storey {i}")
    name2 = getattr(storey2, "Name", f"Storey {i+1}")
    
    height_difference = z2 - z1
    print(f"Height between {name1} and {name2}: {height_difference} IFC units")
#Extracting potential floors and ceilings:
# Extract IfcSlab and IfcCovering elements. The code retrieves all ifcslab and ifccovering elements from the model
all_slabs = model.by_type("IfcSlab")
all_coverings = model.by_type("IfcCovering")

# Use heuristics to identify potential floors and ceilings, even if mislabeled
potential_floors = []
potential_ceilings = []

#Potential floors: ifcslab elements with predefinestype set to floor or with names containing the word floor.
#Potential ceilings: IfcSlab elements with predefinedtype set to roof, names containing ceiling or cover, or ifccovering elements with predefinedtype set to ceiling or names containing ceiling.
for slab in all_slabs:
    predefined_type = getattr(slab, "PredefinedType", None)
    name = getattr(slab, "Name", "").lower()
    
    # Consider slabs with names containing 'floor' or predefined type as FLOOR
    if predefined_type == "FLOOR" or "floor" in name:
        potential_floors.append(slab)
    # Fallback: consider slabs at lower elevations or named ambiguously as potential floors
    elif predefined_type == "ROOF" or "ceiling" in name or "cover" in name:
        potential_ceilings.append(slab)

for covering in all_coverings:
    predefined_type = getattr(covering, "PredefinedType", None)
    name = getattr(covering, "Name", "").lower()
    
    # Consider coverings with names containing 'ceiling' or predefined type as CEILING
    if predefined_type == "CEILING" or "ceiling" in name:
        potential_ceilings.append(covering)
    # Fallback: consider coverings at higher elevations as potential ceilings
    elif "cover" in name or predefined_type is None:
        potential_ceilings.append(covering)

# Display the number of identified floors and ceilings
print("\nPotential floor and ceiling counts:")
print(f"Potential floor elements found: {len(potential_floors)}")
print(f"Potential ceiling elements found: {len(potential_ceilings)}")

#Displaying the counts:The code prints the number of potential ceiling elements found.

#EXPLANATION OF OUTPUT
#Model Output: The model was successfully opened, as indicated by "model opened succesfully"
#Floor-to-Floor heights:The code prints the height differences between consecutive levels in the model:
#-The output shows that the height between different levels is approximatelt 3800 ifcs units. (level 0-1 is 7600)

#POTENTIAL FLOOR AND CEILING COUNTS:
# 23 potential floor elemetns: these could be slabs or elements matching the criteria for floors based on their predefinedtype or name
# 17 potential ceilings elements: these could be slabs or covering that match the criteria for ceilings based on their predefinedtype or name. 

#INTERPRETATION
# The codes analysis helps identify storey heights
# The potential floor and ceiling counts indicate elements that are suspected to be mislabelled or require verification. This is important for ensuring the BIM models data integrity, as mislabelled elements can lead ro errors in analysis and project planning,

