## A3 - Group 1 - Analysts
### Our groups focus area is ceilings, and we have chosen to focus on the building report 2410. 

## The Claim: 
### The claim our tool is solving is to check the floor to floor height which is stated to be 3.8 meters and to try and to check the floor to ceiling height which is 2.9 meters on the standard office floors. This specific claim was chosen because the ceiling information in the reports is limited. This claim can be found in the architectural report 2410 on page 17 ( CES_BLD_24_10_ARC ) 

## Description of the tool: 

### The tool relies on the BIM software, Blendar, and the add on of visual studio code to validate the measurements by checking the IFC model dimensions directly. This will enbale the design team to verify throughout the design phase, to ensure that these two heights are accurate and also to ensure that the next floor is not overlapping or under the ceiling of the previous floor.  The concept behind this tool is that by checking the floor to floor and floor to ceiling heights, the design team can check that the heights satisfiy the minimum requirements and that the ceiling and floor do not overlap in the design. 

### The intendee goal of our tool was that the ifcOpenSHell tool in Python will check the heights and ensure that the floor to ceiling height is less than the floor to floor height. Once that runs true then there is no clashes between the floors. It serves as a sort of simple quick clash detection for a specific design aspect. 

### However, due to inconsistencies in how ceilings are labeled in the IFC model (e.g., as coverings, slabs, or ceilings), the tool also incorporates heuristic checks. These heuristics classify slabs and coverings as potential floors or ceilings to ensure their correct placement and prevent overlaps. The tool extracts building storeys, calculates their elevations, and checks if the actual floor-to-floor height aligns with the design requirements.

### The business value this could offer is that during the design phase, the architect can continously run these simple scripts to verify building measurements and avoid clashes, ensuring ceilings are placed correctly before the next floor. Beyond this specific use case, the Python script can be extended to analyze other parts of the building. It would also be financially less expensive to run a python script throughout the design phase and notice any error and adjust accordingly. Rather than run clash detection later on and have to spend more time and money to fix it. The tool would be an open sourced solution to anyone who needs to check their model and sure it is not clashing.

## Instructions to run the tool: 

### 1. Download all the necessary softwares such as visual studio code, blenderBIM and github.

### 2.  Make sure the IFC model is available and place it somewhere on your computer that is easily accessible and can be defined with a path in the script. 

### 3. Open the script, update the model_path line to match the path in your own computer

### 4. Run the script to check the IFC model, to extract the building storeys, to calculate the floor to floor height, and to correctly classify slabs and coverings as potential floors or ceilings. 

### 5. Check the results with whats in your current plan of the building/ report. 


## What Advanced Building Design Stage (A,B,C or D) would your tool be usefuL?

### The tool is useful in all stages of ADB, particulary in stage A during early stage design to check the model is not clashing. It is also useful throughout the other stages as a quick clash detection to be able to ensure that the model is set up correctly without having to necessary open the entire model. Running the script is as simple as pressing "play". 

## Which Advnanced Building Design subjects might use it?
### The tool is intended tobe used by the architectural subject as it focuses on the spatial layout. The other subjects can certainly use the tool to check the heights or even can adjust the script and check different measurements. 

## What information is required in the model for your tool to work?

### The building storey data is needed, specfically each storey information such as the Elevation. This will enable us to calculate the floor to floor height. The slab and covering information is needed specifcally the predefined type and name attributes. Overall, the model should be well structured and the items in the IFC should be more properly defined to ensure accurate proper infromation extraction and validation. 

