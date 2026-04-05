const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
    const win = new BrowserWindow({
        width: 1200,
        height: 800,
        backgroundColor: '#05050f',
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true
        }
    });

    // Utilise path.join pour être compatible peu importe l'emplacement du dossier
    win.loadFile(path.join(__dirname, 'HTML', 'Editor.html'));
    
    // Optionnel : win.setMenu(null); // Pour cacher la barre de menu
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});
