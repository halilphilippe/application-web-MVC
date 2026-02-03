import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Stockage en mémoire
achats = []

# Fonction : produit le plus acheté
def top_produit(achats):
    if not achats:
        return None

    compteur = {}
    for achat in achats:
        produit = achat["produit"]
        quantite = achat["quantite"]
        compteur[produit] = compteur.get(produit, 0) + quantite

    return max(compteur, key=compteur.get)

# Route principale : ajout des achats
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        produit = request.form.get("produit")
        quantite = request.form.get("quantite")

        if produit and quantite and int(quantite) > 0:
            achats.append({
                "produit": produit,
                "quantite": int(quantite)
            })

        return redirect(url_for("index"))

    return render_template("achats.html", achats=achats)

# Route statistiques
@app.route("/stats")
def stats():
    top = top_produit(achats)
    return render_template("statistiques.html", top=top)

# Lancement serveur (IMPORTANT POUR RAILWAY)
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )