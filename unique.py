import pandas as pd

data = pd.read_csv('results.csv')

data.sort_values(by=['Vina_score', 'Cluster', 'Ligand'], inplace=True, ascending=[True, True, True])

data.drop_duplicates(subset='Ligand', keep='first', inplace=True)

data.to_csv('unique.csv', index=False)

