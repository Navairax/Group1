# Explicit Summary: 

## How to Identify Mislabeled Building Elements and Reclassify Them
### This tutorial teaches identifying and correcting mislabeled building elements, focusing on misclassified ceilings. Using python, ifcopenshell, and the BIM model to ensure that the labelling inconsisities are reclassified. 

# Introduction:
### The video tutorial is designed to explain to BIM users identify and correct mislabelled building elements, focusing specifically on ceilings that might be incorrectly labelled as slabs, coverings or other elements. By using Python and ifcopenshell, you will learn how to load and analyze IFC models, check for inconsistencies and correct classification of architectural components. This ensures that the BIM data is correctly classified for better architecture project management and data analysis. They will gain insights on how to apply this method to other mislabelled elements, providing a comprehensive approach in improving BIM data quality. 

## Video title: How to Identify Mislabeled Building Elements
## Video Link: https://www.youtube.com/watch?v=1ctDLXtbFwI

# Role: OpenBIM Analyst
## Learning level: Level 2
### This tutorial is designed for those who support the analysis and interoperability of OpenBIM models. As an OpenBIM analyst, you will develop the ability to analyze property sets within IFC files and create pyhton scripts using ifcopenshell to detect and correct data discrepancies. This skill set enables you to support model accuracy.  

# Focus Area: Architecture
## BIM use: The tutorial emphasizes the importance of precise data classification in architectural models.
### The tutorial walks you through the process of identifying and correcting mislabelled ceilings and generalizing this process for other building elements. It includes practical, step-by-step instructions for python, in using ifcopenshell, and writing scripts that can be adapted for different mislabelling issues in BIM projects. The goal is to provide BIM analysts with hands-on skills for maintaining consistent and accurate data representation in their work.  

## Sections covered in the video:
### 1. Introduction to IFC models and the impact of mislabelled Data: Understand why mislabelled components can lead to project issues and how correcting them improves data quality and interoperability. 

### 2. Setup: Setting up ifcopenshell  

### 3. Loading  and analyzing in IFC file: How to load an IFC model into python.  

### 4. Identifying mislabelled ceilings: A code demonstration that shows how to find ceilings that may be incorrectly labelled as slabs or coverings and correct them. 

### 5. How to use the code on other builidng elements. This step by step can be found in the video description for more details. 

## Explanation of Results:
### The results then show that there are 23 potential floor elements and 17 potential ceiling elements. The BIM model and report show that building is 23 floors with 24 ceilings, meaning that the results were accurate with counting the floor elements and inaccurate with the ceiling elements. This is because ceilings were inaccurately labelled and even with the python script collecting all the known names for the ceilings, there are still some inconsistencies in the naming. 

# How to use the code on other building elements:
 ### 1.	Understand the IFC building elements labelling. IfcSlab and IfcCovering elements typically represent floors, ceilings, roofs, & coverings.	There is also IfcWall, IfcWindow, IfcDoor, etc 
  ### 2.	Research the attributes the specific building elemetns use to define their roles or types ( for example, PredefinedType, Name) 	This will help to classify and identify them into the potential categories 
  ### 3.	Modify the script	Replace IfcSlab and IfcCovering with the desired element type (e.g., IfcWall, IfcDoor) using model.by_type("ElementType")	Then adjust the rules for classification based on attributes like PredefinedType or keywords in Name.
  ### 4.	Load the Ifc model and run the script 
  ### 5.	Review the grouped elements and verify that they are accounted for. Alternatively open the BIM viewer and check there. 

# Further Considerations 
### The teach tool we developed in A4 was able to collect 17 out of the 24 mislabeled ceiling elements and count them as 'potential ceilings'. Given more time and resources, we would have been able to collect all 24 mislabeled ceiling elements by running many more iterations of our script. In this instance you would need numerous iterations of our tool to collect all mislabeled elements. It is a semi-manual process of finding one item mislabeled, then adding that to our script and the script automatically counts any elements with that name. Ideally, if we had managed to collect all 24 mislabeled ceiling elements, then we would have been able to check the floor to ceiling height. The floor to ceiling height is a part of our assignment 3 tool and would make it so the clash detection could be used for both floor to floor and floor to ceiling. Our overall goal was to semi automate the process of identifying mislabeled elements to make it efficient. Such that if an individual or an organization is given a huge mislabeled IFC file with many inconsistencies, then they would be able tO collect and count those inconsistent naming using our simple python script. 


# Feedback of other Architecture BIM Groups
### Group 4: The groups tool on gathering  material information and calculating the volume of the building elements to find the CO2 emissions is a nice idea. Its helpful as its intended to be used during the early stages of the design process. The group did have some issues in the IFC model as they could not always match the building elements to materials. If the IFC model had a more robust system for the elements where there was also a material and an amount, then this tool has a lot of potential to be used in the industry as a pre LCA. 

### Group 8: The groups tool is about space optimization by finding the necessary information, understanding the space management, and then trying to connect that information. There were issues in their tool with the optimzation as the ifc model has inconsistencies. Thereby they could not find the exact floor number needed to extract the information and to connect it. The concept is nice in theory, however the application appears to be much more complex. 

### Overall: The Architecture BIM groups had some really insightful tools but the overlying theme among all groups is that there IFC model has way too many inconsistencies/mislabelling. This major flaw in the IFC models makes it hard to have working tools. Fortunately, the tool our group developed solves some of this problem by attempting to identify and reclassify mislabeled elements. 

