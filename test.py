from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/ajouter_candidat', methods=['POST'])
def ajouter_candidat():
    data = request.get_json()
    with open('candidats.json', 'a') as f:
        f.write(json.dumps(data) + "\n")
    return jsonify({"message": "Candidat ajouté avec succès"}), 200

@app.route('/candidats', methods=['GET'])  
def get_candidats():
    candidats = []
    try:
        with open('candidats.json', 'r') as f:
            for line in f:
                candidats.append(json.loads(line))
    except FileNotFoundError:
        pass
    return jsonify(candidats)

if __name__ == '__main__':
    app.run(debug=True)