#!/bin/bash

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}--- Buildy Suite: Installation (Python + Node.js) ---${NC}"

# 1. Gestion du fichier .gitignore
if [ ! -f .gitignore ]; then
    echo -e "${BLUE}[0/2] Création du fichier .gitignore...${NC}"
    cat <<EOF > .gitignore
env/
node_modules/
LICENSE
EOF
    echo -e "${GREEN}Fichier .gitignore créé avec succès.${NC}"
else
    echo -e "${BLUE}[0/2] Le fichier .gitignore existe déjà, étape ignorée.${NC}"
fi

# 2. Dépendances système
sudo apt update
sudo apt install -y nodejs npm python3-venv

# 3. Installation Electron (pour l'option 4)
echo -e "${BLUE}[1/2] Installation des modules Node.js...${NC}"
npm install

# 4. Installation Python (pour options 1, 2, 3)
echo -e "${BLUE}[2/2] Configuration de l'environnement Python...${NC}"
rm -rf env
python3 -m venv --system-site-packages env
./env/bin/pip install pywebview pillow pygame

echo -e "${GREEN}[SUCCESS] Configuration terminée. L'option 4 utilisera Electron.${NC}"
