#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def bins_labels(bins, **kwargs):
    bin_w = (max(bins) - min(bins)) / (len(bins) - 1)
    plt.xticks(np.arange(min(bins)+bin_w/2, max(bins), bin_w), bins, **kwargs)
    plt.xlim(bins[0], bins[-1])

path = "C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/"
vals = pd.read_csv(path + "tables/tableForHistograms.csv", encoding="utf_8")

# Customisation of matplotlib
COLOR = "black"
plt.rcParams["text.color"] = COLOR
plt.rcParams["axes.labelcolor"] = COLOR
plt.rcParams["xtick.color"] =  COLOR
plt.rcParams["ytick.color"] = COLOR
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.max_open_warning"] = 0

# Using .hist from pandas
# Generating histograms with variables from column "value"
for c in range(13, 23):
    hist1 = vals.hist(column=vals.columns[c], grid=True, bins=25, color="#66cc99")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    name = path + "figures/" + vals.columns[c].replace("/", "") + ".png"
    plt.savefig(name, bbox_inches="tight", dpi=300, transparent=True)

# Generating dataframe with rows with errors
df = vals.loc[vals["error_type"] != -1].reset_index()
df.drop("index", axis=1, inplace=True)

# Generating histogram with errors
bins = range (1, 7)
hist_error = df.hist(column="error_type", bins=bins, grid=True, color="#66cc99")
bins_labels(bins, fontsize=20)
plt.title("Error types")
plt.xlabel("Error")
plt.ylabel("Frequency")
name = path + "figures/" + "Errors" + ".png"
plt.savefig(name, bbox_inches="tight", dpi=300, transparent=True)

# Generating histograms from rows with errors, from values from column
# "value"
for c in range(13, 23):
    hist_error_value = df.hist(column=df.columns[c], grid=True, 
                       bins=25, color="#ff3333")
    name = vals.columns[c].replace("/", "") + " in errors"
    plt.title(name)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig(path + "figures/" + name + ".png", bbox_inches="tight", dpi=300, 
                transparent=True)

# Generating histograms with and withour errors
kwargs = dict(alpha=0.5, bins=25, density=True, stacked=True)
for c in range(13, 23):
    plt.close("all")
    withoutErrorsColumn = vals[[vals.columns[c]]].copy()
    withErrorsColumn = df[[df.columns[c]]].copy()
    minValue = withoutErrorsColumn.iloc[:, 0].min() if \
               withoutErrorsColumn.iloc[:, 0].min() < withErrorsColumn.iloc[:, 0].min() else \
               withErrorsColumn.iloc[:, 0].min()
    maxValue = withoutErrorsColumn.iloc[:, 0].max() if \
               withoutErrorsColumn.iloc[:, 0].max() > withErrorsColumn.iloc[:, 0].max() else \
               withErrorsColumn.iloc[:, 0].max()
    plt.hist(withoutErrorsColumn.iloc[:, 0], **kwargs, color='g', label="Without errors")
    plt.hist(withErrorsColumn.iloc[:, 0], **kwargs, color='r', label="With errors")
    name = vals.columns[c].replace("/", "") + " with and without errors"
    plt.gca().set(title=name, ylabel="Frequency")
    plt.xlim(minValue, maxValue)
    plt.legend()
    plt.savefig(path + "figures/" + name + ".png", bbox_inches="tight", dpi=300, 
                transparent=True)

"""for c in range(13, 23):
    plt.close("all")
    withoutErrorsColumn = vals[[vals.columns[c]]].copy()
    withErrorsColumn = df[[df.columns[c]]].copy()
    minValue = withoutErrorsColumn.iloc[:, 0].min() if \
               withoutErrorsColumn.iloc[:, 0].min() < withErrorsColumn.iloc[:, 0].min() else \
               withErrorsColumn.iloc[:, 0].min()
    maxValue = withoutErrorsColumn.iloc[:, 0].max() if \
               withoutErrorsColumn.iloc[:, 0].max() > withErrorsColumn.iloc[:, 0].max() else \
               withErrorsColumn.iloc[:, 0].max()
    bins = np.linspace(start=minValue, num=25, stop=maxValue)
    plt.hist(withoutErrorsColumn.iloc[:, 0], bins=bins, 
             color="#66cc99", alpha=0.5, label="Without errors")
    plt.hist(withErrorsColumn.iloc[:, 0], bins=bins, 
             color="#ff3333", alpha=0.5, label="With errors")
    name = vals.columns[c].replace("/", "") + " with and without errors"
    plt.title(name)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend(loc="upper right")
    plt.savefig(path + "figures/" + name + ".png", bbox_inches="tight", dpi=300, 
                transparent=True)"""


#%%
