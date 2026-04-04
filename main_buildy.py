import webview
import os
import json

class Api:
    def __init__(self):
        # Création automatique du dossier Maps au lancement
        self.base_path = os.path.join(os.getcwd(), "Maps")
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    def check_folder(self, folder_name):
        full_path = os.path.join(self.base_path, folder_name)
        if os.path.exists(full_path):
            return {"exists": True}
        return {"exists": False}

    def create_folder(self, folder_name):
        try:
            os.makedirs(os.path.join(self.base_path, folder_name))
            return True
        except Exception as e:
            print(f"Erreur création dossier: {e}")
            return False

    def save_file(self, folder, filename, content):
        file_path = os.path.join(self.base_path, folder, f"{filename}.htmlbp")
        if os.path.exists(file_path):
            return {"status": "exists"}
        
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return {"status": "success"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def force_save(self, folder, filename, content):
        try:
            file_path = os.path.join(self.base_path, folder, f"{filename}.htmlbp")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        except:
            return False

def start_app():
    api = Api()
    # Chemin absolu vers le fichier HTML
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(current_dir, "notepad.html")
    
    window = webview.create_window(
        'BuildyPopupMaker Pro', 
        html_file, 
        js_api=api,
        width=1200, 
        height=800
    )
    webview.start()

if __name__ == "__main__":
    start_app()
