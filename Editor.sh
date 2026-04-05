#!/bin/bash

# Détecte le dossier actuel du script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Lance l'application en utilisant l'environnement local
npm start
