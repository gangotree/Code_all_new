# it will use for average Rg calculations for different blocks in a trajectory
# then it will be use for standard deviation (error bar) calculation using averaged Rg values of different blocks
# this code for block average is for four chains
# block size is 10 ns
# calculate the error: err=({Rg,i-Rg,avg}2/m)0.5 , where m is number of blocks, Rg,avg is average Rg over all data frames means over entire trajectory, Rg,i is the individual block average Rg

import numpy as np

# Input filenames for the four chains (Rg files)
chains = ["Rg-nolinkchain1-270T.xvg", "Rg-nolinkchain2-270T.xvg", "Rg-nolinkchain3-270T.xvg", "Rg-nolinkchain4-270T.xvg"]

# Block size: 5000 frames = 10 ns (we will divide the 100 ns trajectory into 10 equal blocks)
block_size = 5000

# Output file for summary
output_summary = 'Average-Rg_block_error-270T.xvg'

# Store block errors for error propagation calculation
all_block_errors = []


# Write following headers to summary file
with open(output_summary, 'w') as fout:
    fout.write("@title \"Rg Analysis for Multiple Chains\"\n")
    fout.write("@xaxis label \"Chain Index\"\n")
    fout.write("@yaxis label \"Rg (nm)\"\n")
    fout.write("# Columns: Chain_index  Rg_avg  Rg_stddev  Block_Error\n")

    # Loop through each chain file (each .xvg file)
    for chain_index, filename in enumerate(chains, start=1):
        Rg_inp = []		# input .xvg file

        # Read Rg values from file (3rd column)
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith('#') or line.startswith('@'):	# ignore the commented lines
                    continue
                parts = line.strip().split()
                if len(parts) >= 3:
                    Rg_inp.append(float(parts[2]))	# store the Rg values from 3rd column

        Rg_inp = np.array(Rg_inp)	#convert into array
        total_frames = len(Rg_inp)	#count the number of frames based on its size
        num_blocks = total_frames // block_size	# now calculate the number of blocks in a trajectory

        # Average and standard deviation over full trajectory
        Rg_avg = np.mean(Rg_inp)
        Rg_std = np.std(Rg_inp)

        # Block averaging calculations
        block_avgs = []		# create an empty array to store the calculated block average values
        for i in range(num_blocks):
            start = i * block_size
            end = start + block_size
            block = Rg_inp[start:end]
            if len(block) == block_size:
                block_avg = np.mean(block)
                block_avgs.append(block_avg)
                print(f"Chain {chain_index}, Block {i+1} Average Rg (from {start} to {end} frames): {block_avg:.4f} nm")

        #convert the block average values into an array
        block_avgs = np.array(block_avgs)

        # Error calculation from block averages
        block_error = np.sqrt(np.sum((block_avgs - Rg_avg) ** 2) / num_blocks)
        all_block_errors.append(block_error)

        # Print to terminal
        print(f"\n=== Chain {chain_index} ===")
        print(f"Overall Average Rg: {Rg_avg:.4f} nm")
        print(f"Overall Standard Deviation: {Rg_std:.4f} nm")
        print(f"Block Average Error: {block_error:.6f} nm\n")

        # Write to output file
        fout.write(f"{chain_index} {Rg_avg:.6f} {Rg_std:.6f} {block_error:.6f}\n")
# Error propagation after loop (combine the each block error)
propagated_error = np.sqrt(np.sum(np.array(all_block_errors) ** 2))
print(f"\n=== Propagated Block Error Across All Chains ===")
print(f"Combined Error over all chains: {propagated_error:.6f} nm")

# Optional: append propagated error to output file
with open(output_summary, 'a') as fout:
    fout.write(f"# Propagated_Error {propagated_error:.6f}\n")












