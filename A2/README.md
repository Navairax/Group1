## Assignment A2

## A2a: About your group
### 2
### 2
### 0
### Total score: 4

## Focus area
## We are analysists and our focus area is cealing

## A2b: Identify claim

### The report we have chosen is building 2410
### The claim we are checking is the floor-to-floor height which is set at 3.8 meters and the floor-to-ceiling height which is 2.9 meters on standard office floors.
### The claim is made in the architectur report, page 17

### The reason we chose this claim is that the cealing information in the reports are limited and the chosen report is the only one that adresses the floor-to-ceiling height.

## A2c: Use Case
### To check the claim, you would compare the design specification for the floor-to-floor and floor-to-ceiling heights provided in the architectural report (3.8 meters and 2.9 meters, respectively) with the actual measurements in the BIM model. 
### Use BIM software blender to validate the measurements, checking the model dimenson directly. 

### This would need to be checked during the design review phase. The claim needs to be checked before the final design is approved to ensure that the model meets the architectural specifications.

### This claim relies the Architectural Report, page 17, where the floor-to-floor and floor-to-ceiling heights are mentioned. 
### The BIM model must contain the accurate height information to verify the claim
### Input form O&M, constructability review, and end-user feedback may influence design acceptability, as shown in the diagram.

### Design phase: This verification occurs during the design phase, where dimensions are checked and confirmed before proceeding to construction.

### The required BIM purpose for the project is Generate. This purpose focuses on creating information about the facility to ensure the design meets the requirements for ceinling and floor heights. 
### The use cases that help in the projekt are Prescribe and Size. 
Prescribe: this use case helps identify and specify the necessary elements/rooms within the building, ensuring that the design adheres to the requirements for ceiling height as outlined in the architectural reports.
Size: this use case is crucial for validating the dimensions of ceiling and floor heights, ensuring that they meet the required specifications. It involves checking that all elements are accurately sized.

## A2d: Scope the use case

### The scope of the use case is highlighted in the BPMN diagram in the black box, specifically the red box where the script would check the floor to ceiling height


## A2e: Tool idea

### The ifcOpenSHell tool in Python is intended to check the floor to floor height and check the floor to ceiling height and ensure that the floor to ceiling height is less than the floor to floor height. Once that runs true then there is no clashes between the floors. It serves as a sort of simple quick clash detection for a specific design aspect. The business value this could offer is that during the design phase, the architect can continously run these simple scripts to verify the measurements of the different parts of the building to ensure they dont clash. For this example, its ensuring the ceiling is placed before the next floor. However this simple python script could be extrapolated to all parts of the builidng. It would also be financially less expensive to run a python script throughout the design phase and notice any error and adjust accordingly. Rather than run clash detection later on and have to spend more time and money to fix it. The societal value our tool would bring is that it would offer an open sourced solution to anyone who needs to check their model and sure it is not clashing. 

## A2f: Information Requirements 

### We need to extract the following information from the BIM model:
### The vertical distance between the top of one floor to the top of the floor directly above it
### The vertical distance from the top of the floor to the underside of the ceiling
### Any properties related to hegiht that might be defined in the model. 

### In an IFC model, the relevant information for ceiling and floor heights can can typically be found in the following entities:

### IfcBuildingStorey:
### Location: This represents each floor or level in the building
### Attributes - ElevationOfRefHeight: Indicates the vertical position of the storey relative to a reference level, whic is useful for determining the floor-to-floor height.

### IfcSpace:
### Attributes - Height: Indicates the ceiling height of the space
### Attributes - BoundedBy: References the enclosing elements (walls, ceilibgs) that can help determine the avaliavle height.

### IfcCeiling:
### Location: Represents ceiling elements in a building.
### Attributes - Height: While not always directly present, the position of the ceiling in relation to the storey elevation can be inferred. The thickness or offset of the ceiling can also be considered when calculating the floor-to-ceiling height.

### Whether this information is in the model depends on how comprehensive the BIM model is. In well-structured BIM models, especially those intended for architectural analysis, you can expect to find:
### Floor-to-floor heights defined through the IfcBuildingStorey elevation attributes
### Ceiling heights defined in the IfcSpace or associated with IfcCeiling

### Yes, to extract ceiling and height-realted information from an IFV model usinf IfcOpenShell, you have to do the following:
### Begin by using IfcOpenShell to open the IFC file. This typically involves using the ifcopenshell.open() function to read the file into memory.
### Then use the model.by_type() method to retrieve instances of specific IFC entities:
### - IfcBuildingStorey
### - IfcSPace
### - IfcCeiling

### Then extract the elevation and height information
### Calculate the floor-to-floor and floor-to-ceiling heights

### By following these steps in IfcOpenShell, we can effectively extract height-related information from an IFC model and analyze the floor-to-floor and floor-to-ceiling heights. 


## A2g: Identify appropriate software licence

### We have choosen GPL-3.0 as the license for our project because it contains source code and is intended to be open source. GPL-3.0 ensures that others can use, modify and distribute the code while also requiring them to share their changes under the same license. This choice protects the project from being made proprietary and promotes collaboration within the open-source community. 
