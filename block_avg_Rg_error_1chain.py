# it will use for average Rg calculations for different blocks in a trajectory
# then it will be use for standard deviation (error bar) calculation using averaged Rg values of different blocks
# this code for block average is for one chain
# block size is 10 ns
# calculate the error: err=({Rg,i-Rg,avg}2/m)0.5 , where m is number of blocks, Rg,avg is average Rg over all data frames means over entire trajectory, Rg,i is the individual block average Rg

import numpy as np
# input the filename
chain1='Rg_nolink_chain1_270T.xvg'

# create an empty array to store the 3rd column, which actually have the Rg values (when use the gmx polystat)
col3 = []

# read the input files and ignore the '#' and '@'; and extract the third column
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

# compute average and standard deviation over entire data (means for full trajcetory (Rg,avg) in above expression)
R_gavg = np.mean(col3)
R_gstdev=np.std(col3)

#print above values
print(f"Overall average Rg of chain1 (entire trajectory): {R_gavg:.4f} nm")
print(f"Overall standard Deviation: {R_gstdev:.4f} nm")


# Block average calculations: each block have 10 ns interval means: 0-10, 10-20, 20-30, and so on.
block_size = 5000  # here 5000 represents the number of frame, it means it will be 100000 ps (or 10 ns)10 ns
total_frames=len(col3)
#print(total_frames)
num_blocks = total_frames // block_size
#print(num_blocks)

# Create again an empty array to store block averages
block_avgs = []

# loop to do the block average calculations for each block
for i in range(num_blocks):
	start=i*block_size
	#print(start)
	end =start+block_size
	#print(end)
	block=col3[start:end]
	if len(block)==block_size:	# check whether block size is matching or not
		block_avg=np.mean(block)	#average of particular block
		block_avgs.append(block_avg)
		print(f"Block {i+1} Average Rg (from {start} to {end} frames): {block_avg:.4f} nm")		

# Convert to numpy array for further computation
block_avgs = np.array(block_avgs)

# Now calculate the standard deviation (error bar using the above expression: err=({Rg,i-Rg,avg}2/m)0.5)
block_error=np.sqrt(np.sum((block_avgs-R_gavg)**2) / num_blocks)
print(f"\nBlock Averaged Rg Error (Standard Error Estimate): {block_error:.6f} nm")













