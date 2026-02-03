from app import top_produit

# données test
achats_test = [
    {"produit": "pomme", "quantite": 1},
    {"produit": "poire", "quantite": 1},
    {"produit": "pomme", "quantite": 1}
]

resultat = top_produit(achats_test)

if resultat == "pomme":
    print("Test réussi")
else:
    print("Test échoué")
