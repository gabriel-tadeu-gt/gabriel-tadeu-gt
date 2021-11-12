import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


config = {
'axes.spines.right': False,
'axes.spines.top': False,
'axes.edgecolor': '.4',
'axes.labelcolor': '.0',
'axes.titlesize': 'large',
'axes.labelsize': 'medium',
'figure.autolayout': True,
'figure.figsize': (4.5, 3.5),
'font.family': ['serif'],
'font.size': 10.0,
'grid.linestyle': '--',
'legend.facecolor': '.9',
'legend.frameon': True,
'savefig.transparent': True,
'text.color': '.0',
'xtick.labelsize': 'small',
'ytick.labelsize': 'small',
}
plt.style.use(['seaborn-whitegrid', 'seaborn-paper', 'seaborn-muted', config])

dados = pd.read_excel('planilha.xlsx', sheet_name='Página1')

t = dados['t']
d = dados['Distância']

for i in t:
    print(i)