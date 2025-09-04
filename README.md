# TalentJump – Instructions d’exécution

## ✅ Prérequis
- **Python 3.8+** installé
- **pip** pour installer les dépendances
- Navigateur web (Chrome, Firefox, etc.)

---

## 1. Installer les dépendances
Dans le dossier du projet, exécute :


**pip install flask flask-cors**

## 2. Lancez le serveur flask

**python backend.py**

## 3. Servir la page HTML (Front-end)
⚠️ **Ne pas ouvrir le fichier HTML en double-cliquant (sinon Origin: null → erreur CORS).**

**python -m http.server 5500**

**Puis ouvre :**
👉 http://127.0.0.1:5500/TalentJumpAcceuil.html


## 

## 

## **Étape 1 : Mise en contexte**

## 

## **Talent Jump qu’est-ce que c’est ?** 

 

**Talent Jump \- Studio International**

Talent Jump est un studio international innovant qui sert de pont entre artistes talentueux et labels musicaux prestigieux. Notre plateforme offre aux chanteurs et musiciens émergents l'opportunité unique de présenter leur art à des professionnels de l'industrie musicale à travers le monde.

Fondée en 2018, notre entreprise combine expertise artistique et technologie de pointe pour identifier les talents authentiques. Nous proposons des sessions d'enregistrement professionnelles, du coaching vocal et instrumental, ainsi qu'un accompagnement personnalisé dans le développement de carrière.

Notre réseau mondial de partenaires comprend des labels indépendants et majors, permettant aux artistes de trouver la structure qui correspond parfaitement à leur univers musical et leurs ambitions.

# **Etape 2 : problématique**

Comment une application web interne permettrai de centraliser et de gérer les candidatures de manière simple et efficace en palliant les oublis et la perte de temps.

# **Etape 3 : choix de conception**

* Ajouter un nouveau candidat.  
* Visualiser la liste de tous les candidats.  
* Modifier le statut d'un candidat (ex: "En attente", "Entretien", "Refusé").  
* Trier et filtrer les candidats pour retrouver une information rapidement.  
* Suppression d'un candidat.  
* Sauvegarde et chargement de la liste de candidats dans un fichier simple (ex: .json ou .csv).  
* Utilisation d'une enum en Java pour gérer le statut de la candidature.  
* Ajout d'une fonctionnalité de recherche par mot-clé.  
* Création d'une page de statistiques simples.

 

**1\. Front-End**

Une interface claire, responsive et professionnelle.

* index.html : Une page d'accueil présentant l'outil TalentJump.  
* candidats.html : Une page affichant la liste des candidats. La présentation sous forme de cartes (cards) est encouragée pour un design moderne.  
* ajouter.html : Un formulaire soigné pour saisir les informations d'un candidat : Prénom/Nom, Email, Poste visé, Compétences, Lien CV.

**2\. Back-End Console**

Une application en ligne de commande (console) codée en Java.

* Candidat.java : Un modèle clair (attributs, constructeur, getters/setters).  
* GestionCandidats.java : Contient la structure de données (ArrayList\<Candidat\>) et implémente les méthodes de gestion (CRUD, tri, filtre).  
* **Lien entre Java et Web** : Le programme Java doit pouvoir générer un fichier HTML (ex: rapport\_candidats.html) qui affiche la liste à jour des candidats.

 

 

 

