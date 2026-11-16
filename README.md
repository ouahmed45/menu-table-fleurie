# La Table Fleurie – Menu Digital par QR Code

Le client scanne le QR code sur sa table pour découvrir la carte complète avec photos, prix et langues (Français, Arabe, Anglais).
Le serveur de salle prend ensuite la commande directement à table pour la saisir sur le logiciel de caisse (**Clyo Systems**).

## Fonctionnalités
- **Consultation mobile rapide** : Photos haute définition, catégories de plats, prix clairs en Dinars Algériens (DA).
- **Trilingue** : Français, Anglais et Arabe avec inversion automatique de l'interface en mode RTL.
- **Recherche instantanée** : Trouver un plat en quelques lettres.
- **Simulateur "Ma sélection"** : Le client peut composer sa sélection pour connaître son total indicatif avant que le serveur n'arrive.
- **Message de service clair** : Indication invitant le client à patienter pour l'arrivée du serveur.

## Pages
- `/`            Carte complète pour les clients
- `/?t=7`        Même carte avec affichage du numéro de table (détecté par le QR code)

## Lancer le serveur
Nécessite Node 18 ou supérieur (aucun module externe requis) :

```bash
node server.js
```

Le serveur écoute sur le port 3000 (`http://localhost:3000`). Vous pouvez définir la variable `PORT` si nécessaire.

## Mettre en ligne
Le site doit être hébergé sur une adresse publique avec HTTPS pour que les clients puissent y accéder depuis la 4G/Wi-Fi de leur smartphone.
Un hébergeur simple convient parfaitement (Render, Railway, Fly.io, VPS, etc.).

## Générer les QR Codes à imprimer
Installez les outils Python nécessaires :
```bash
pip install opencv-python numpy pillow
```

Générez les affiches des tables (ex: pour 20 tables) :
```bash
python make_qr.py https://votre-adresse.com 20
```

Le script génère :
- `qr/table-01.png` à `qr/table-20.png` (un QR code par table)
- `qr/menu-general.png` (QR code général pour l'entrée, les cartes ou les réseaux sociaux)

## Modifier la carte
Le fichier `menu.json` contient les familles de plats, les prix et les noms. Les photos associées se trouvent dans `public/img/`.

