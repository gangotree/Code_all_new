import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# List of filenames and corresponding custom labels
filenames = ["Rg-nolinkchain1-370T.txt", "Rg-nolinkchain2-370T.txt", "Rg-nolinkchain3-370T.txt", "Rg-nolinkchain4-370T.txt", "Rg_1chain_370T.txt"]
labels = ["chain1-370K", "chain2-370K", "chain3-370K", "chain4-370K", "free-chain-370K"]

# Create a plot
plt.figure(figsize=(8, 6))
# color code: #00008B = dark blue; #8B0000 = dark red; #FF8C00 =  dark orange; #006400 = dark green
colors = ["#00008B", "#8B0000", "#000000", "#FF8C00", "#006400"]  # High-contrast colors codes

# Loop through each file and process
for i, (filename, label) in enumerate(zip(filenames, labels)):
    try:
        if not os.path.isfile(filename):
            raise FileNotFoundError

        # Load the data (skipping comment lines)
        data = np.loadtxt(filename, dtype=float, comments=("#", "@"), skiprows=0)

        # Debug: print shape of data
        print(f"Loaded {filename} with shape {data.shape}")

        # Ensure the file has at least 3 columns (index 2)
        if data.ndim == 1 or data.shape[1] < 3:
            print(f"Warning: {filename} does not contain at least 3 columns.")
            continue

        # Select third column (Rg values)
        rg_values = data[:, 2]

        # Plot probability distribution using KDE
        sns.kdeplot(rg_values, label=label, linestyle='-', fill=False, bw_adjust=1, alpha=0.5, linewidth=2.5, color=colors[i])

    except FileNotFoundError:
        print(f"Error: {filename} not found. Please check the file path.")
    except Exception as e:
        print(f"Error while processing {filename}: {e}")

# Add title and axis labels
plt.title("Rg_PNIPAM-370K", fontsize=18)
plt.xlabel("Rg (nm)", fontsize=18)
plt.ylabel("P(Rg)", fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)
plt.xticks(np.arange(0.60, 0.91, 0.05))  # x-ticks from 0 to 2.0 at step 0.5
plt.yticks(np.arange(0, 36, 7))  # y-ticks from 0 to 5.0 at step 1.0
#plt.ylim(0, 50)
plt.tick_params(axis='y', labelsize=16)
plt.tight_layout()
plt.legend(fontsize=14)
plt.tight_layout()

# Save the plot before showing
plt.savefig("Rg_probability_distribution-pnipam-370K.png", dpi=370, bbox_inches='tight', transparent=False)
plt.show()

