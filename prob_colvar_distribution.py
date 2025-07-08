import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data_list = []
def frange(start, stop, step):
    return [round(start + i * step, 1) for i in range(int((stop - start) / step) + 1)]
dist_values = frange(1.0, 3.0, 0.1)
for val in dist_values:
    filename = f"COLVAR-K5000/COLVAR_{val}"
    df = pd.read_csv(filename, delim_whitespace=True, comment='#', header=None)
    df.columns = ["time", "dist", "rest"]
    data_list.append(df)

plt.figure(figsize=(5, 4))
#color = ["blue", "red", "green", "yellow", "cyan", "orange"]
colors = sns.color_palette("hsv", n_colors=21)

for i, df in enumerate(data_list):
    sns.histplot(df["dist"], kde=True, stat="probability", color=colors[i], bins=100,alpha=0.5)

plt.title('Probability')
plt.xlabel('Rg')
plt.ylabel('P(Rg)')
plt.savefig(f"test.pdf", dpi=300)
