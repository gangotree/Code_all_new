# this python code is for time averaged Rg calculation along with its standard deviation (for entire range of data): for all four chains, here we have imported the all .xvg file. Avg values of each chains were shown as output
# Calculations for entire data frames

import numpy as np
# input the all filenames
chains=["Rg_nolink_chain1_270T.xvg","Rg_nolink_chain2_270T.xvg","Rg_nolink_chain3_270T.xvg","Rg_nolink_chain4_270T.xvg"]


# loop to consider all input files and also store the all three columns
for i, chain in enumerate(chains,start=1):
	col3 = []	# create an empty array to store the 3rd column, Rg values (when use the gmx polystat)
# read the input files and ignore the '#' and '@'
	with open(chain, 'r') as file:
    		for line in file:
        	# Skip comment lines
        		if line.startswith('#') or line.startswith('@'):
            			continue
        	# Split line into columns
        		parts = line.strip().split()
        		if len(parts) >= 3:
         		   col3.append(float(parts[2]))

## Convert to numpy array
	col3=np.array(col3)

# compute average and standard deviation of whole data
	R_gavg = np.mean(col3)
	R_gstdev=np.std(col3)

#print above values
	print(f"Chain {i}:")
	print(f"Average Rg of chain1 over all data frame: {R_gavg:.4f} nm")
	print(f"Standard Deviation: {R_gstdev}")
	
	
	
