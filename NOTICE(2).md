# NOTICE — Third-Party Attributions

This project (**Buildy Suite**) is released under the **MIT License**.
The following third-party libraries, fonts, and tools are used in this project and are credited below.

---

## Python Libraries

### pywebview
- **Repository:** https://github.com/r0x0r/pywebview
- **License:** BSD 3-Clause License
- **Usage:** Used to create native desktop windows rendering local HTML files (`main.py`, `main_buildy.py`).

### Pillow (PIL Fork)
- **Repository:** https://github.com/python-pillow/Pillow
- **License:** HPND License (Historical Permission Notice and Disclaimer)
- **Usage:** Used in `main.py` to generate and save 16×16 RGBA sprite images from pixel grid data.

### PyQt6 / PyQt6-WebEngine
- **Repository:** https://www.riverbankcomputing.com/software/pyqt/
- **License:** GPL v3 / Commercial (Riverbank Computing)
- **Usage:** Used in `app.py` as an alternative desktop wrapper to display the local `notepad.html` file via a WebEngine view.

---

## Fonts

### Press Start 2P
- **Source:** https://fonts.google.com/specimen/Press+Start+2P
- **Designer:** CodeMan38
- **License:** SIL Open Font License 1.1 (OFL)
- **Usage:** Pixel-art style font used in `index.html` (OC Player Maker UI).

---

## Web APIs & Services

### Google Fonts API
- **URL:** https://fonts.googleapis.com
- **Usage:** CDN delivery of the *Press Start 2P* font in `index.html`.
- **Terms:** https://developers.google.com/fonts/faq/privacy

---

## Browser / Runtime

### Chromium (via pywebview / QtWebEngine)
- pywebview uses the system's native webview (WebKit on macOS, WebView2/Edge on Windows, GTK WebKit on Linux).
- PyQt6 uses **QtWebEngine**, which is based on the **Chromium** project.
- **Chromium License:** BSD and others — https://chromium.googlesource.com/chromium/src/+/main/LICENSE

---

## Notes

- All original source code in this repository (Python scripts, HTML/CSS/JS logic, shell scripts) is the work of the project author and is licensed under the **MIT License**.
- Third-party components listed above retain their own respective licenses. Their inclusion does not alter the MIT License applied to the original source code.
- If you redistribute this project, please ensure compliance with each third-party license listed above.

---

*Last updated: 2025*
