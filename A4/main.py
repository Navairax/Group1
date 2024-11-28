#Extracting potential floors and ceilings:
#This section retrieves all ifcslab and ifccovering elements from the model, wich represents the building's IFC model. The model.by_type fetches elemts categorized as IfcSlab and IfcCovering. 
all_slabs = model.by_type("IfcSlab")
all_coverings = model.by_type("IfcCovering")

# This initializez 2 empty lists of, potential_floors and potential_ceilings, to store elements that might represent floors and ceilings.
potential_floors = []
potential_ceilings = []

#Potential floors: ifcslab elements with predefinestype set to floor or with names containing the word floor.
#Potential ceilings: IfcSlab elements with predefinedtype set to roof, names containing ceiling or cover, or ifccovering elements with predefinedtype set to ceiling or names containing ceiling.
#The for loop iterates over each IfcSlab element stored in all_slabs. 
#getattr() is used to get the value of the Predinedtype attribute of the slab element. If it dosen't exist, it will print out None. 

for slab in all_slabs:
    predefined_type = getattr(slab, "PredefinedType", None)
    name = getattr(slab, "Name", "").lower()
   
    # This checks if the predefinedType of the slab is FLOOR or if the name contains the word floor
    #If either condition is met, the slab is appended to the potential_floors list. 

    if predefined_type == "FLOOR" or "floor" in name:
        potential_floors.append(slab)

    # Fallback: consider slabs at lower elevations or named ambiguously as potential floors
    # It checks the PredefinedType is ROOF, or if the name contains ceiling og cover.
    # If any of these conditions are met, the slab is added to the potential_ceilings list. 

    elif predefined_type == "ROOF" or "ceiling" in name or "cover" in name:
        potential_ceilings.append(slab)

# The for loop iterates over each IfcCovering element stored in all_coverings.
# gettattr() is used to get the PredefinedType and NAme attributes of the covering element, with None as the default for PredefinedType if it dosen't exist.
for covering in all_coverings:
    predefined_type = getattr(covering, "PredefinedType", None)
    name = getattr(covering, "Name", "").lower()

    # Consider coverings with names containing 'ceiling' or predefined type as CEILING
    # This checks if the PredefinedType of the covering is CEILING or if its name contains ceiling.
    # If either condition is met, the covering is appended to the pontential_ceilings list. 
    if predefined_type == "CEILING" or "ceiling" in name:
        potential_ceilings.append(covering)

    # Fallback: consider coverings at higher elevations as potential ceilings
    elif "cover" in name or predefined_type is None:
        potential_ceilings.append(covering)


# Display the number of identified floors and ceilings:
# This section prints the total number of elements identified as potential floors and ceilings. 
# len(potential_floors) returns the number of items in the potential_floors list, and len(potential_ceilings) returns the number of items in the potential_ceilings list.
print("\nPotential floor and ceiling counts:")
print(f"Potential floor elements found: {len(potential_floors)}")
print(f"Potential ceiling elements found: {len(potential_ceilings)}")

# Displaying the counts:The code prints the number of potential ceiling elements found.
# The code inspects IfcSlab and IfcCovering elements, applying certain rules to classify them as potential floors or ceilings, and prints the count for each classification
