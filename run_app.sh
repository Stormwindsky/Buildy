#!/bin/bash

VENV_DIR="env"

# Vérification environnement Python pour les options 1, 2, 3
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv --system-site-packages $VENV_DIR
fi

source $VENV_DIR/bin/activate

clear
echo "------------------------------------------------"
echo "        BUILDY SUITE - READY"
echo "------------------------------------------------"
echo " 1) OC Player Maker (Python/WebView)"
echo " 2) BuildyPopupMaker (Python/WebView)"
echo " 3) Launcher (Pygame)"
echo " 4) 3D Editor (Electron / Three.js)"
echo "------------------------------------------------"
read -p "Choix : " CHOICE

case $CHOICE in
    1) python3 main.py ;;
    2) python3 main_buildy.py ;;
    3) python3 launcher.py ;;
    4) 
        echo "Lancement de l'éditeur 3D avec Electron..."
        npx electron . 
        ;;
    *) echo "Erreur choix." ;;
esac

deactivate
