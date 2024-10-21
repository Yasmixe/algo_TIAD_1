import csv

# on a 9835

fichier_csv = 'produits_transactions.csv'

def get_nombre_transaction_and_minmax(ficher_csv):
        nb = 1 
        with open(fichier_csv, 'r') as fichier:
         reader = csv.reader(fichier)
         for ligne in reader:
               nb = nb +1
        print(f'nombre de transactions est {nb}') 
        minmax = (9835 * 30) / 100
        print(minmax)



get_nombre_transaction_and_minmax(ficher_csv=fichier_csv)