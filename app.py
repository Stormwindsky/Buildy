import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import os

class CustomNotepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notepad HTML Local - Engine v1.0")
        self.resize(1200, 800)

        self.browser = QWebEngineView()
        
        # Chemin mis à jour vers le dossier HTML
        path = os.path.abspath(os.path.join("HTML", "Editor.html"))
        self.browser.setUrl(QUrl.fromLocalFile(path))

        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomNotepad()
    window.show()
    sys.exit(app.exec())
