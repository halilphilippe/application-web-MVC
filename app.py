from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Stockage en mémoire (liste des achats)
achats = []

# Fonction top produit
def top_produit(achats):
    if not achats:
        return None
    compteur = {}
    for achat in achats:
        produit = achat['produit']
        compteur[produit] = compteur.get(produit, 0) + achat['quantite']
    return max(compteur, key=compteur.get)

# Route formulaire d'achats
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        produit = request.form.get("produit")
        quantite = int(request.form.get("quantite", 0))
        if produit and quantite > 0:
            achats.append({"produit": produit, "quantite": quantite})
        return redirect(url_for("index"))
    return render_template("achats.html", achats=achats)

# Route statistiques
@app.route("/stats")
def stats():
    top = top_produit(achats)
    return render_template("statistiques.html", top=top)

if __name__ == "__main__":
    app.run(debug=True)
