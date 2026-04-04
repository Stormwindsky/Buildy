import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import os

class CustomNotepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notepad HTML Local - Engine v1.0")
        self.resize(1200, 800)

        self.browser = QWebEngineView()
        
        # Chargement du fichier HTML local
        path = os.path.abspath("notepad.html")
        self.browser.setUrl(QUrl.fromLocalFile(path))

        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomNotepad()
    window.show()
    sys.exit(app.exec())
