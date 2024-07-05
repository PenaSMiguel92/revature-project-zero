# project0-cli

### Project: Blood Glucose and BMI Tracking App 

## Background

Type Two diabetes is becoming an increasing problem in the United States, where most people won't know they have it until it starts to present symptoms.  
This type of diabetes arises from the body's inability to process sugar in the blood, which can cause it to accumulate over time and damage tissues like the retina, arms, legs, inhibit the immune system, impede healing from an injury, among others. 
Treatment for Type Two Diabetes involves weight loss, excercise, and tracking blood glucose concentrations.

The body mass index (BMI), while not perfect, can provide a decent guideline for weight loss. It is defined as the user's mass (in kilograms) divided by height squared (in meters).
The blood glucose concentration (BGC), can provide some insight into the user's ability to process sugar. This is usually measured with a meter, prescribed by a doctor. 

This application will provide a command line interface that will make it easy to track the user's BGC and BMI over time. 

## Project Requirements
- CLI will ask user to choose from a number of options: (S)how history, (R)eport BGC and BMI, (C)lose the application.
- The application will read a CSV file. It will need to read the past time, BGC, and BMI and display a history chart using matplotlib.
- The application will write to the same CSV file, and append to it the user's recently reported BGC and BMI. 
- User input shall be validated by first checking to see if they selected an appropriate menu option, and then when prompting for BGC, weight, and height. The appropriate units are used, as well as the typing. 
- This program will use classes to represent BGC and BMI, and their respective data validation methods. A file handling class will take in BGC and BMI objects, and write the data accordingly. Exception classes will be used to notify the user that something went wrong with their input, and they must try again. 
-  

## Tech Stack
- Python 3.x
    - matplotlib
    - pandas
    - numpy
    - csv
    - exceptions
    - datetime
- Git (+ Github) 

