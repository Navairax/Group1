# Video title: How to Identify Mislabeled Building Elements
# Video Link: https://www.youtube.com/watch?v=1ctDLXtbFwI

# Summary
## The video tutorial is designed to help BIM users identify and correct mislabelled building elements, focusing specifically on ceilings that might be incorrectly labelled as slabs, coverings or other elements. By using Python and ifcopenshell, you will learn how to load and analyze IFC models, check for inconsistencies and correct classification of architectural components. This ensures that the BIM data is correctly classified for better architecture project management and data analysis. The viewers will gain insights on how to apply this method to other mislabelled elements, providing a comprehensive approach in improving BIM data quality. 

# Role: OpenBIM Analyst
# Learning level: Level 2
## This tutorial is designed for those who support the analysis and interoperability of OpenBIM models. As an OpenBIM analyst, you will develop the ability to analyze property sets within IFC files and create pyhton scripts using ifcopenshell to detect and correct data discrepancies. This skill set enables you to support model accuracy.  

# Focus Area: Architecture
# BIM use: The tutorial emphasizes the importance of precise data classification in architectural models.
## The tutorial walks you through the process of identifying and correcting mislabelled ceilings and generalizing this process for other building elements. It includes practical, step-by-step instructions for python, in using ifcopenshell, and writing scripts that can be adapted for different mislabelling issues in BIM projects. The goal is to provide BIM analysts with hands-on skills for maintaining consistent and accurate data representation in their work.  

# Sections covered in the video:
## 1. Introduction to IFC models and the impact of mislabelled Data: Understand why mislabelled components can lead to project issues and how correcting them improves data quality and interoperability. 

## 2. Setup: Setting up ifcopenshell  

## 3.Loading  and analyzing in IFC file: How to load an IFC model into python.  

## 4. Identifying mislabelled ceilings: A code demonstration that shows how to find ceilings that may be incorrectly labelled as slabs or coverings and correct them. 

## Read the video description for more details. 

# Explanation of Results
## The results then show that there are 23 potential floor elements and 17 potential ceiling elements. The BIM model and report show that building is 23 floors with 24 ceilings, meaning that the results were accurate with counting the floor elements and inaccurate with the ceiling elements. This is because ceilings were inaccurately labelled and even with the python script collecting all the known names for the ceilings, there are still some inconsistencies in the naming. 
# How to use the code on other building elements. 
 ## 1.	Understand the IFC building elements labelling. IfcSlab and IfcCovering elements typically represent floors, ceilings, roofs, & coverings.	There is also IfcWall, IfcWindow, IfcDoor, etc 
  ## 2.	Research the attributes the specific building elemetns use to define their roles or types ( for example, PredefinedType, Name) 	This will help to classify and identify them into the potential categories 
  ## 3.	Modify the script	Replace IfcSlab and IfcCovering with the desired element type (e.g., IfcWall, IfcDoor) using model.by_type("ElementType")	Then adjust the rules for classification based on attributes like PredefinedType or keywords in Name.
  ## 4.	Load the Ifc model and run the script 
  ## 5.	Review the grouped elements and verify that they are accounted for. Alternatively open the BIM viewer and check there. 


