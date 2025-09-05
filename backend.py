from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)

# Autoriser le front servi en local (ex: python -m http.server 5500)
CORS(
    app,
    resources={r"/*": {"origins": ["http://127.0.0.1:5500", "http://localhost:5500"]}},
    supports_credentials=False,  # passe à True si tu utilises des cookies/credentials côté front
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "Accept"]
)

DATA_FILE = os.path.join(os.path.dirname(__file__), "candidats.json")


def read_all():
    """Lit tous les candidats (NDJSON)."""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return [json.loads(ligne) for ligne in f if ligne.strip()]
    except FileNotFoundError:
        return []


def write_all(candidats):
    """Écrit la liste complète des candidats en NDJSON."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        for c in candidats:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")


@app.route('/ajouter_candidat', methods=['POST', 'OPTIONS'])
def ajouter_candidat():
    # Réponse au préflight CORS
    if request.method == 'OPTIONS':
        return ('', 204)

    data = request.get_json(force=True, silent=True) or {}

    # Lire existants
    candidats = read_all()
    dernier_id = max((c.get("id", 0) for c in candidats), default=0)

    # Ajouter ID
    data["id"] = dernier_id + 1

    # Enregistrer (append une ligne)
    with open(DATA_FILE, 'a', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")

    return jsonify({"message": "Candidat ajouté avec succès", "id": data["id"]}), 200


@app.route('/candidats', methods=['GET'])
def get_candidats():
    return jsonify(read_all()), 200


@app.route('/supprimer_candidat/<int:candidat_id>', methods=['DELETE', 'OPTIONS'])
def supprimer_candidat(candidat_id: int):
    # Réponse au préflight CORS
    if request.method == 'OPTIONS':
        return ('', 204)

    candidats = read_all()
    nouveaux_candidats = [c for c in candidats if c.get("id") != candidat_id]

    # Si rien n'a été supprimé
    if len(nouveaux_candidats) == len(candidats):
        return jsonify({"message": "Candidat introuvable", "id": candidat_id}), 404

    # Réécriture du fichier
    write_all(nouveaux_candidats)
    return jsonify({"message": "Candidat supprimé avec succès", "id": candidat_id}), 200

    
@app.route('/modifier_candidat/<int:candidat_id>', methods=['PUT', 'OPTIONS'])
def modifier_candidat(candidat_id):
    # Réponse au préflight CORS
    if request.method == 'OPTIONS':
        return ('', 204)

    data = request.get_json(force=True, silent=True) or {}

    candidats = read_all()
    candidat_trouve = False

    for i, c in enumerate(candidats):
        if c.get("id") == candidat_id:
            candidats[i] = {**c, **data, "id": candidat_id}  # fusionne les données
            candidat_trouve = True
            break

    if not candidat_trouve:
        return jsonify({"message": "Candidat introuvable", "id": candidat_id}), 404

    write_all(candidats)
    return jsonify({"message": "Candidat modifié avec succès", "id": candidat_id}), 200

if __name__ == '__main__':
    # IMPORTANT: toutes les routes doivent être définies AVANT ce point
    app.run(host='127.0.0.1', port=5000, debug=True)