# code to plot one data set for example: Temperature vs Rg (used to plot Rg averaged over all 4 chains with temperature)
import numpy as np
import matplotlib.pyplot as plt

#input file
file='Rg_20mer_averaged.xvg'

# Read the data, skipping header lines starting with '#' or '@'
with open(file, 'r') as f:
    data_lines = [line for line in f if not line.startswith(('#', '@'))]
    
# Load numerical data
data = np.loadtxt(data_lines)

# Extract columns
temperature = data[:, 0]  # x-axis
Rg_cavg = data[:, 1]           # y-axis (Rg)
err_cavg = data[:, 2]          # error (std deviation)

# Plotting
plt.figure(figsize=(8, 6))
plt.title("Rg_Chain_20mer", fontsize=18)
plt.errorbar(temperature, Rg_cavg, yerr=err_cavg, fmt='o-', capsize=4, color='#00008B')
plt.xlabel('Temperature (K)', fontsize=18)
plt.ylabel('Radius of Gyration (Rg) [nm]', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)
plt.tick_params(axis='y', labelsize=16)
plt.xticks(np.arange(280, 340, 10))  # x-ticks from 0 to 2.0 at step 0.5
plt.yticks(np.arange(0.9, 1.41, 0.1))  # y-ticks from 0 to 5.0 at step 1.0
plt.grid(True)
plt.tight_layout()

# Save the plot before showing
plt.savefig("Rg_pnipam_chain_average_20mer.png", dpi=300, bbox_inches='tight', transparent=False)
plt.show()
