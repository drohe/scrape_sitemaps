import os
import csv
import pathlib
import xml.etree.ElementTree as ET

directory = pathlib.Path(__file__).parent.resolve() #gets the path for the directory this file is saved in
sitemapdir = 'test' #the name of the directory where all your sitemap files are saved which should be a sibling (in the same directory) as this script file
dir = os.path.join(directory,sitemapdir)
projectOutput = input("Enter a name for this project folder: ") # YOU WILL BE PROMPTED IN THE COMMAND LINE TO NAME YOUR PROJECT
outputcsv = projectOutput +".csv" #the path for your CSV file
## Creating your CSV file
f = csv.writer(open(outputcsv, "w+", newline="\n", encoding="utf-8"))
f.writerow(['URLs'])

for xmlfile in os.listdir(dir):
    file = os.path.join(dir,xmlfile)
    with open(file) as xml:  
        # create element tree object
        tree = ET.parse(xml)

        # get root element
        root = tree.getroot()
        #set the tag name for the <loc> tag
        tag_name = "{http://www.sitemaps.org/schemas/sitemap/0.9}loc" #Double-check your tag name using  print([elem.tag for elem in root.iter()])
        for loc in root.iter(tag_name):
            f.writerow([loc.text])