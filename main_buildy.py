import webview
import os
import json

class Api:
    def __init__(self):
        self.base_path = os.path.join(os.getcwd(), "Maps")
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
    
    # ... (autres méthodes inchangées)

def start_app():
    api = Api()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Modification ici : ajout du dossier HTML
    html_file = os.path.join(current_dir, "HTML", "notepad.html")
    
    window = webview.create_window(
        'BuildyPopupMaker', 
        html_file, 
        js_api=api, 
        width=1000, 
        height=700
    )
    webview.start()

if __name__ == "__main__":
    start_app()
