# This code is used to ensure that the maximum value for yolo labelling is 1.

import re
import glob

  

  
for file in glob.glob('*.txt'):


	
	with open(file) as f:
	    content = f.readlines()
	
	
	
	content = [x.strip() for x in content] 
	count_1 = 0
	final = ''
	for j in content:
		split = content[count_1].split()
	
		count_1 = count_1+1
		
		count_2= 0
		for i in split:
			 
			
			
			if count_2>0:
				val = float(i)
				
				if val>1:
					split[count_2] = '1'
					
				count_2= count_2 + 1
			else:
				count_2= count_2 + 1
				
				
	
		with open('output/'+file, "a") as a_file:
			new_line = " ".join(str(x) for x in split)
			a_file.write(new_line)
			a_file.write("\n")
	
	

	
		
		 
