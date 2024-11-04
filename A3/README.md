## A3 - Group 1 - Analysts
### Our groups focus area is ceilings, and we have chosen to focus on the building report 2410. 

## The Claim: 
### The claim our tool is solving is to check the floor to floor height which is stated to be 3.8 meters and to check the floor to ceiling height which is 2.9 meters on the standard office floors. This specific claim has been chosen because the ceiling information in the reports is limited. This claim can be found in the architectural report 2410 on page 17 ( CES_BLD_24_10_ARC ) 

## Description of the tool: 

### The concept behind this tool is that by checking the floor to floor and floor to ceiling heights, the design team can check that the heights satisfiy the minimum requirements and that the ceiling and floor do not overlap in the design. The tool relies on the BIM software, Blendar, and the add on of visual studio code to validate the measurements by checking the IFC model dimensions directly.This will enbale the design team to verify throughout the design phase, to ensure that these two heights are accurate and also to ensure that the next floor is not overlapping or under the ceiling of the previous floor. 

### The ifcOpenSHell tool in Python is intended to check the heights and ensure that the floor to ceiling height is less than the floor to floor height. Once that runs true then there is no clashes between the floors. It serves as a sort of simple quick clash detection for a specific design aspect. The business value this could offer is that during the design phase, the architect can continously run these simple scripts to verify the measurements of the different parts of the building to ensure they dont clash. For this example, its ensuring the ceiling is placed before the next floor. However this simple python script could be extrapolated to all parts of the builidng. It would also be financially less expensive to run a python script throughout the design phase and notice any error and adjust accordingly. Rather than run clash detection later on and have to spend more time and money to fix it. The tool would be an open sourced solution to anyone who needs to check their model and sure it is not clashing.

# Instructions to run the tool: 


# What Advanced Building Design Stage (A,B,C or D) would your tool be usefuL?

## Which Advnanced Building Design subjects might use it?
### The tool is intended tobe used by the architectural subject in the course however the other subjects can certainly use the tool to check the heights or even can adjust the script and check different measurements. 

# What information is required in the model for your tool to work?

