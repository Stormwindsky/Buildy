#!/bin/bash

VENV_DIR="env"

# Vérification environnement
if [ ! -d "$VENV_DIR" ]; then
    echo "--- Initialisation Environnement ---"
    python3 -m venv --system-site-packages $VENV_DIR
fi

source $VENV_DIR/bin/activate

# Install des dépendances
pip install pywebview pillow

clear
echo "------------------------------------------------"
echo "        BUILDY SUITE - READY"
echo "------------------------------------------------"
echo " 1) OC Player Maker (main.py)"
echo " 2) BuildyPopupMaker (main_buildy.py)"
echo " 3) Launcher (launcher.py)"
echo "------------------------------------------------"
read -p "Choix : " CHOICE

case $CHOICE in
    1)
        python3 main.py
        ;;
    2)
        python3 main_buildy.py
        ;;
    3)
        python3 launcher.py
        ;;
    *)
        echo "Erreur choix."
        ;;
esac

deactivate
