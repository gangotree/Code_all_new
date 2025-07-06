# this python code is for time averaged Rg calculation along with its standard deviation (for entire range of data): for single chain, here we have imported the single .xvg file

import numpy as np
# input the filename
chain1='Rg_nolink_chain1_270T.xvg'

# create an empty array to store the 3rd column, which actually have the Rg values (when use the gmx polystat)
col3 = []

# read the input files and ignore the '#' and '@'
with open(chain1, 'r') as file:
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
print(f"Average Rg of chain1 over all data frame: {R_gavg}")
print(f"Standard Deviation: {R_gstdev}")
