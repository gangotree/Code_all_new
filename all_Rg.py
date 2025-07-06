# in this python code i have copied the 3rd column (which is Rg) of each file (Rg.xvg, generated from gmx_polystat) into a separate files and also average over all chains. Averaging was done to get the Rg averaged over all chains in a system.
import numpy as np

#enter the .xvg input files
Rg_files = ['Rg_nolink_chain1_270T.xvg', 'Rg_nolink_chain2_270T.xvg', 'Rg_nolink_chain3_270T.xvg', 'Rg_nolink_chain4_270T.xvg']
output_file = 'Rg_combined_averaged.xvg'

# List to store data arrays
data_columns = []

# Process each file
for file in Rg_files:
    with open(file, 'r') as f:
        # ignore header lines
        data_lines = [line for line in f if not line.startswith(('#', '@'))]
    #load the numeric data
    data=np.loadtxt(data_lines)
    #extract time (1st column) and the 3rd column (index 2)
    time=data[:,0]
    col3=data[:,2]
    
    #save the extracted columns
    data_columns.append(col3)


# Stack all third columns into a single array (shape: N x 4)
all_col3 = np.column_stack(data_columns)

# Compute average across columns (axis=1)
average_col = np.mean(all_col3, axis=1)

# Combine all for output: time | col3_file1 | col3_file2 | col3_file3 | col3_file4 | average
final_output = np.column_stack((time, all_col3, average_col))

# Save to file
header = "Time\tFile1_Col3\tFile2_Col3\tFile3_Col3\tFile4_Col3\tAverage"
np.savetxt(output_file, final_output, fmt='%.6f', delimiter='\t', header=header, comments='')



