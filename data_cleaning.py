import pandas as pd

# Lire le fichier CSV
df = pd.read_csv('heart.csv')

# Filtrer les colonnes binaires (0 ou 1)
binary_columns = df.columns[df.isin([0, 1]).all()].tolist()

# Garder uniquement les colonnes binaires
df_binary = df[binary_columns]

# Enregistrer le DataFrame filtré dans un nouveau fichier CSV
df_binary.to_csv('cleaned_heart.csv', index=False)

print("Fichier 'cleaned_heart.csv' enregistré avec succès.")