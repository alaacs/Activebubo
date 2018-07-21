# ActiveBubo

## Introduction
This project was developed in the scope of the course Python in GIS at the Institute for Geoinformatics at the University of Münster in Germany as the concluding assignment.

The class was divided into groups of 4-5 students. The students were to select one of two provided spatial datasets. Next the students had to browse the information in the dataset and come up with one or more research questions they wanted to investigate.

The problems addressed by the research questions had to be solved using the content learned in the course, namely using python scripting.
The full process including all of the steps for data preprocessing, processing, analysis and visualisation had to be implemented into python scripts for full automation.

## Data
The datasets provided for this final assignment were derived from Movebank, a free online database of animal tracking data hosted by the Max Planck Institute for Ornithology. One of the datasets contains GPS tracks for migratory trajectories of the White-Fronted Goose in Northern Europe and Russia from 2007 to 2008. The other includes GPS tracks for Eagle Owl trajectories in various parts of Germany from 2011 to 2017. In contrast to the Geese, Eagle Owls do not migrate, meaning this dataset covers a much smaller area. Both datasets were provided as shapefiles, with the emitted GPS pulses as points, and the full trajectories as multilines.

The team started by browsing the datasets and their attributes. It emerged that the owl dataset contained considerably more features, since more specimina were tracked and the time frame is much larger. Furthermore it includes many more attribute fields, containing a larger variety of information. The group finally concluded that the owl dataset provides greater analysis opportunities without having to look for further data sources, and therefore this dataset was chosen for our project. One potential disadvantage of using this larger dataset was performance, which had to be handled carefully when developing the code.


The owl dataset contains over 518000 point features for the GPS signals of the tracking devices. In total tracking data from 22 owl specimina are present in the dataset. Apart from the coordinates, each feature has almost 30 attributes, including the timestamp of the signal, the owl ID the tracker was attached to and the speed, heading, height and temperature at the time of the signal. A metadata excel sheet was also provided with the dataset, with additional information about the individual animals (e.g. gender, notes on the loggers and the individual owls etc.).

## Install plugin on your Computer
1. Copy the whole folder content into QGIS plugins folder, it lies in this directory (Windows)
>C:\Users\{User}\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\activebubo\chartimages
2. Run QGIS as administrator
3. Install ActiveBubo plugin:
  * From QGIS menu click **plugins** then **Manage and Install Plugins..**
  * Search for ActivBubo and enable it

## Use ActiveBubo Plugin
- Choose the shapefile location by browsing for it from the top left browse file box
- Fields will be populated automatically with default fields, but change Time, Owl Id, and Speed fields if necessary using the corresponding comboboxes
-  Use the QueryBuilder to filter the records of the shapefile if necessary.
An example query is by default shown on the UI.

## Contact Us
For any queries, difficulties in installation and/or usage please contact one of the team.

- Yousef Qamaz - qamazyousef@gmail.com
- Alaa Abdelfattah - al373480@uji.es
- Kirubamohan Nanjappan - nkirubamohan@gmail.com
- Nicholas Azenui Asanga
- Daniel Marsh-Hunn - al373405@uji.es
