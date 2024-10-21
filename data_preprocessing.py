import csv

# Fonction pour lire le fichier .csv et extraire toutes les transactions et produits
def extraire_produits_et_transactions(fichier_csv):
    produits_uniques = set()  # Ensemble pour stocker les produits uniques
    transactions = []         # Liste pour stocker les transactions

    # Lire le fichier .csv
    with open(fichier_csv, 'r') as fichier:
        reader = csv.reader(fichier)
        for ligne in reader:
            # Chaque ligne représente une transaction, ajouter à la liste des transactions
            transactions.append(ligne)
            # Ajouter les produits à l'ensemble
            produits_uniques.update(ligne)
    
    return produits_uniques, transactions

# Fonction pour créer le fichier .csv de sortie
def creer_fichier_csv(fichier_sortie, produits, transactions):
    # Trier les produits pour un meilleur ordre dans le fichier CSV
    produits = sorted(produits)

    # Ouvrir un fichier CSV en mode écriture
    with open(fichier_sortie, 'w', newline='') as fichier:
        writer = csv.writer(fichier)
        
        # Écrire l'en-tête (produits)
        writer.writerow(['Transaction'] + produits)
        
        # Écrire les transactions avec des "1" et "0"
        for i, transaction in enumerate(transactions):
            ligne = [1 if produit in transaction else 0 for produit in produits]
            writer.writerow([f'Transaction {i+1}'] + ligne)

# Nom du fichier .csv d'entrée
fichier_csv = 'groceries2.csv'

# Extraire les produits et les transactions
produits, transactions = extraire_produits_et_transactions(fichier_csv)

# Nom du fichier .csv de sortie
fichier_sortie = 'produits_transactions.csv'

# Créer le fichier .csv avec les données binaires
creer_fichier_csv(fichier_sortie, produits, transactions)

print(f"Le fichier '{fichier_sortie}' a été créé avec succès.")
