import csv
# to import la fonction qui va me donner pour chaque iteration le  minmax 
from nombre_transaction import get_nombre_transaction_and_minmax
import pandas as pd

min_max = 0.3 

data = pd.read_csv('produits_transactions.csv')
def calcul_nb_colonne():
    num_columns = data.shape[1]
    print(num_columns)


def item_1():
    '''on va generer pour chaque produit combien de fois il apparait et s'il est frequent ou non'''
    product_counts = data.drop(columns=['Transaction']).sum()
    # Afficher la fréquence d'apparition de chaque produit
    print("Fréquence d'apparition de chaque produit dans les transactions :")
    '''print(product_counts/9835)
    nb = 0
    for i in product_counts:
        nb = nb+1
        print(i/9835)
    print(nb)'''
    threshold = 0.02 * len(data)  # 3% des transactions
    frequent_items = []
    unfrequent_items = []
    # Vérifier la fréquence de chaque produit
    for product, count in product_counts.items():
        if count >= threshold:
            frequent_items.append(product)  # Ajouter le nom du produit
        else:
            unfrequent_items.append(product)  # Ajouter le nom du produit
    
    # Afficher les résultats
    print(f'Produits fréquents : {frequent_items}')
    print(f'Produits non fréquents : {unfrequent_items}')


calcul_nb_colonne()
item_1()