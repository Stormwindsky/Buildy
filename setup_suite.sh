#!/bin/bash

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}--- Buildy Suite: Fixing GObject Introspection ---${NC}"

# 1. Installation de la dépendance MANQUANTE (girepository-2.0)
echo -e "${BLUE}[1/2] Installing missing system dependency...${NC}"
sudo apt update
sudo apt install -y libgirepository1.0-dev gobject-introspection gir1.2-glib-2.0

# 2. Recréation propre du VENV avec accès au système
echo -e "${BLUE}[2/2] Rebuilding environment with system access...${NC}"

# On rase l'ancien env qui est bloqué
rm -rf env

# On crée le venv avec --system-site-packages pour que 'gi' soit visible
python3 -m venv --system-site-packages env

# Installation des dépendances restantes
./env/bin/python3 -m pip install --upgrade pip
./env/bin/pip install pywebview pillow pygame

# 3. Vérification de l'interface
echo -e "${BLUE}--- Final Check ---${NC}"
if ./env/bin/python3 -c "import gi; gi.require_version('Gtk', '3.0'); print('GTK Bridge OK')" &> /dev/null; then
    echo -e "${GREEN}[SUCCESS] L'interface graphique est ENFIN opérationnelle !${NC}"
else
    echo -e "${RED}[FAIL] Le pont GTK est toujours capricieux.${NC}"
    exit 1
fi

echo -e "${GREEN}C'est bon ! Relance ton menu (run_app.sh).${NC}"
