## TalentJump – Application Web de Gestion des Candidatures

# ✅ Prérequis :
- Python 3.8+ installé
- pip pour installer les dépendances
- Navigateur web (Chrome, Firefox, etc.)

**🚀 Installation et Lancement**

# 1. Installer les dépendances
Dans le dossier du projet, exécute :

``pip install flask flask-cors``


# 2. Lancer le serveur Flask (Back-end)
Dans le dossier contenant backend.py :

``python backend.py``

**Le serveur sera disponible sur :**
👉 http://127.0.0.1:5000

# 3. Servir la page HTML (Front-end)

**⚠️ Ne pas ouvrir le fichier HTML en double-cliquant (sinon Origin: null → erreur CORS).**

À la place, lance un serveur local :

```python -m http.server 5500```


**Puis ouvre dans ton navigateur :**
👉 http://127.0.0.1:5500/TalentJumpAcceuil.html

# 📌 Fonctionnalités de l’application
- Ajouter un nouveau candidat
- Visualiser la liste des candidats
- Modifier les informations ou le statut d’un candidat (ex: En attente, Entretien, Refusé)
- Supprimer un candidat
- Trier et filtrer les candidats pour retrouver une information rapidement
- Recherche par mot-clé
- Sauvegarde et chargement des données dans un fichier JSON
* Statistiques simples (ex: nombre de candidats par statut)
## 🛠️ Architecture du Projet
# 1. Back-End (Python + Flask)
**backend.py :**
Fournit une API REST pour gérer les candidats (CRUD)
Sauvegarde les données dans un fichier candidats.json
Gère les requêtes CORS pour autoriser le front-end
Endpoints principaux :

GET /candidats → Liste des candidats
POST /ajouter_candidat → Ajouter un candidat
PUT /modifier_candidat/<id> → Modifier un candidat
DELETE /supprimer_candidat/<id> → Supprimer un candidat

# 2. Front-End (HTML, CSS, JS)
TalentJumpAcceuil.html : Page d’accueil
TalentJumpCandidats.html : Liste des candidats (affichage sous forme de cartes)
ajouter.html : Formulaire pour ajouter un candidat
Fonctionnalités JS :

fetch() pour consommer l’API Flask
Mise à jour dynamique de la liste des candidats
Alertes et rechargement après modification ou suppression

# 🌍 Contexte du Projet
Talent Jump – Studio International
Talent Jump est un studio innovant qui connecte artistes et labels musicaux prestigieux.
Notre plateforme permet aux chanteurs et musiciens émergents de présenter leur art à des professionnels de l’industrie musicale à travers le monde.

# ✅ Bonnes pratiques
Toujours lancer le serveur Flask avant d’ouvrir le front-end
Ne pas ouvrir les fichiers HTML directement (utiliser http.server)
Vérifier la console du navigateur pour les erreurs CORS ou réseau

# 💡 Prochaines améliorations possibles :

Authentification (login admin)
Export CSV / PDF
