#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = 'C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/'
vals = pd.read_csv(path + 'tables/tableForHistograms.csv', encoding='utf_8')

# Using .hist from pandas
for c in range(13, 23):
    hist1 = vals.hist(column=vals.columns[c], grid=True, bins=20)
    plt.xlabel('Valor')
    plt.ylabel('Número de aparições')
    name = path + 'figures/' + vals.columns[c].replace("/", "") + '.png'
    plt.savefig(name, bbox_inches='tight', dpi=200)

# Using Seaborn
# sns.distplot(vals['Velocidade real eixo 1 (km/h)'], kde=False, bins=50)


#%%
