# code to plot multiple y-data (for example Rg of chain C1, C2, C3, and C4) with same x-axis temperature
import numpy as np
import matplotlib.pyplot as plt

#input file
file='Rg_vs_Temp_chain_4linker.xvg'

# Read the data, skipping header lines starting with '#' or '@'
with open(file, 'r') as f:
    data_lines = [line for line in f if not line.startswith(('#', '@'))]
    
# Load numerical data
data = np.loadtxt(data_lines)

# Extract columns
temperature = data[:, 0]  # x-axis
Rg_c1 = data[:, 1]           # y-axis (Rg)
err_c1 = data[:, 2]          # error (std deviation)
Rg_c2 = data[:, 3]           # y-axis (Rg)
err_c2 = data[:, 4]          # error (std deviation)
Rg_c3 = data[:, 5]           # y-axis (Rg)
err_c3 = data[:, 6]          # error (std deviation)
Rg_c4 = data[:, 7]           # y-axis (Rg)
err_c4 = data[:, 8]          # error (std deviation)

# Plotting
plt.figure(figsize=(8, 6))
plt.title("4-linkers", fontsize=18)
plt.errorbar(temperature, Rg_c1, yerr=err_c1, fmt='o-', capsize=4, label='Chain1', color='#00008B')
plt.errorbar(temperature, Rg_c2, yerr=err_c2, fmt='s-', capsize=4, label='Chain2', color='green')
plt.errorbar(temperature, Rg_c3, yerr=err_c3, fmt='^-', capsize=4, label='Chain3', color='red')
plt.errorbar(temperature, Rg_c4, yerr=err_c4, fmt='*-', capsize=4, label='Chain4', color='#8B0000')
plt.xlabel('Temperature (K)', fontsize=18)
plt.ylabel('Radius of Gyration (Rg) [nm]', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)
plt.legend(loc='best', fontsize=16, framealpha=0)
plt.tick_params(axis='y', labelsize=16)
plt.xticks(np.arange(270, 390, 20))  # x-ticks from 0 to 2.0 at step 0.5
plt.yticks(np.arange(0.60, 0.86, 0.05))  # y-ticks from 0 to 5.0 at step 1.0
plt.grid(True)
plt.tight_layout()

# Save the plot before showing
plt.savefig("Rg_pnipam-each_chains_4linkers.png", dpi=300, bbox_inches='tight', transparent=False)
plt.show()
