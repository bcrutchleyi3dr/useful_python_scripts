# 
import glob
	
import xml.etree.ElementTree as ET

for filename in glob.glob('*.xml'):
	
	
	
	
	tree = ET.parse(filename)
	root = tree.getroot()
	root[0].text = "/media/data/TF_steel_defects/YOUR_FOLDER/images/test/"
	root[1].text = filename[0:-4]+'.jpg'
	root[2].text = "/media/data/TF_steel_defects/YOUR_FOLDER/images/test/" +root[1].text
	
	
	tree.write(filename)
	
	









