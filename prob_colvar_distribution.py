import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data_list = []
def frange(start, stop, step):
    return [round(start + i * step, 1) for i in range(int((stop - start) / step) + 1)]
dist_values = frange(1.2, 1.5, 0.1)
for val in dist_values:
    filename = f"COLVAR-K1000/COLVAR_{val}"
    df = pd.read_csv(filename, delim_whitespace=True, comment='#', header=None)
    df.columns = ["time", "dist", "rest"]
    data_list.append(df)

plt.figure(figsize=(5, 4))
for i, df in enumerate(data_list):
    color = "red" if i < 4 else "blue"
    sns.histplot(df["dist"], kde=True, stat="probability", color=color, bins=100)

plt.title('Probability')
plt.xlabel('Rg')
plt.ylabel('P(Rg)')
plt.savefig('distribution-K1000.pdf', dpi=300)
plt.show()

