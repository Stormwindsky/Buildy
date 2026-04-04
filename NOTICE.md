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

### pygame
- **Repository:** https://github.com/pygame/pygame
- **License:** LGPL v2.1
- **Usage:** Installed as part of the environment setup (`setup_suite.sh`) for potential game-related extensions of the suite.

### GObject Introspection (gi / PyGObject)
- **Repository:** https://gitlab.gnome.org/GNOME/pygobject
- **License:** LGPL v2.1
- **Usage:** Used on Linux to bridge the GTK graphical interface layer required by pywebview (`setup_suite.sh`). Relies on system packages `libgirepository1.0-dev`, `gobject-introspection`, and `gir1.2-glib-2.0`.

---

## JavaScript / Node.js

### Electron
- **Repository:** https://github.com/electron/electron
- **License:** MIT License
- **Version:** ^30.5.1
- **Usage:** Used in `main.js` and `package.json` to wrap `test.html` as a standalone desktop application window.

### Three.js
- **Repository:** https://github.com/mrdoob/three.js
- **License:** MIT License
- **Version:** 0.160.0
- **CDN:** https://unpkg.com/three@0.160.0/
- **Usage:** Used in `test.html` to render an interactive 3D model viewer with scene management, lighting, and camera controls. Includes the `OrbitControls` addon for mouse-based navigation.

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

### unpkg CDN
- **URL:** https://unpkg.com
- **Usage:** CDN delivery of Three.js and OrbitControls modules in `test.html`.
- **Terms:** https://unpkg.com

---

## Browser / Runtime

### Chromium (via pywebview / QtWebEngine / Electron)
- pywebview uses the system's native webview (WebKit on macOS, WebView2/Edge on Windows, GTK WebKit on Linux).
- PyQt6 uses **QtWebEngine**, which is based on the **Chromium** project.
- Electron bundles its own **Chromium** instance as a desktop runtime.
- **Chromium License:** BSD and others — https://chromium.googlesource.com/chromium/src/+/main/LICENSE

---

## Notes

- All original source code in this repository (Python scripts, HTML/CSS/JS logic, shell scripts) is the work of the project author and is licensed under the **MIT License**.
- Third-party components listed above retain their own respective licenses. Their inclusion does not alter the MIT License applied to the original source code.
- If you redistribute this project, please ensure compliance with each third-party license listed above.

---
