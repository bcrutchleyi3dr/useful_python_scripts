import glob
import os
count = 29
for filename in glob.glob('*.jpg'):
	start = 'sharp00'
	count = count +1
	num = str(count)
	end = '.jpg'
	new_name = start + num + end
	os.rename(filename, new_name)
	 
	
	
	
	
