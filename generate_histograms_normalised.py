#%%
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

firstColumn = 9
lastColumn = 19
path = "C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/"
path2 = "figures/"
vals = pd.read_csv(path + "tables/tableForHistograms.csv", encoding="utf_8")

# Customisation of matplotlib
COLOR = "black"
plt.rcParams["text.color"] = COLOR
plt.rcParams["axes.labelcolor"] = COLOR
plt.rcParams["xtick.color"] =  COLOR
plt.rcParams["ytick.color"] = COLOR
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.max_open_warning"] = 0

for c in range(firstColumn, lastColumn):
    # Generating dataframe with rows with errors
    tableWithErrors = vals.loc[vals["error_type"] != -1].iloc[:, c].reset_index()
    tableWithErrors.drop("index", axis=1, inplace=True)
    tableWithErrors = tableWithErrors.iloc[:,0].values

    # Generating dataframe with rows without errors
    tableWithoutErrors = vals.loc[vals["error_type"] == -1].iloc[:, c].reset_index()
    tableWithoutErrors.drop("index", axis=1, inplace=True)
    tableWithoutErrors = tableWithoutErrors.iloc[:,0].values

    ##computing the bin properties (same for both distributions)
    num_bin = 50
    bin_lims = np.linspace(0,max(max(tableWithErrors), max(tableWithoutErrors)),num_bin+1)
    bin_centers = 0.5*(bin_lims[:-1]+bin_lims[1:])
    bin_widths = bin_lims[1:]-bin_lims[:-1]

    ##computing the histograms
    hist1, _ = np.histogram(tableWithErrors, bins = bin_lims)
    hist2, _ = np.histogram(tableWithoutErrors, bins = bin_lims)

    ##normalizing
    hist1b = hist1/np.max(hist1)
    hist2b = hist2/np.max(hist2)

    fig, (ax1,ax2) = plt.subplots(nrows = 1, ncols = 2)
    plt.subplots_adjust(wspace = 0.4)

    ax1.bar(bin_centers, hist1, width = bin_widths, align = 'center', alpha = 0.6, color = 'r')
    ax1.bar(bin_centers, hist2, width = bin_widths, align = 'center', alpha = 0.6, color = 'g')
    ax1.set_xlabel("Value")
    ax1.set_ylabel("Frequency")
    ax1.legend(["With errors", "Without errors"], loc="upper right")
    ax1.set_title("Original")

    ax2.bar(bin_centers, hist1b, width = bin_widths, align = 'center', alpha = 0.6, color = 'r')
    ax2.bar(bin_centers, hist2b, width = bin_widths, align = 'center', alpha = 0.6, color = 'g')
    ax2.legend()
    ax2.set_xlabel("Value")
    ax2.set_ylabel("Normalisation")
    ax2.legend(["With errors", "Without errors"], loc="upper right")
    ax2.set_title("Normalised")

    name = vals.columns[c].replace("/", "").replace(" ", "_") + "_with_and_without_errors_normalised"
    plt.savefig(path + path2 + name + ".png", bbox_inches="tight", dpi=400, 
                    transparent=True)
    # plt.show()
#%%