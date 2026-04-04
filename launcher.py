import pygame
import sys
import os
import math
import shutil

# Initialisation Pygame
pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Buildy Launcher - GMOD Like - MIT License")
clock = pygame.time.Clock()

# Palette de couleurs
BG_COLOR       = (18, 18, 18)
ACCENT_COLOR   = (60, 120, 255)
TEXT_COLOR     = (240, 240, 240)
BTN_COLOR      = (30, 30, 30)
IMPORT_COLOR   = (46, 204, 113)
BACK_COLOR     = (231, 76, 60)
PANEL_COLOR    = (22, 22, 22)
ROW_COLOR      = (30, 30, 30)
ROW_HOVER      = (40, 40, 60)
ROW_SELECT     = (40, 60, 120)
SCROLL_COLOR   = (60, 60, 60)

font_main  = pygame.font.SysFont("Arial", 36, bold=True)
font_sub   = pygame.font.SysFont("Arial", 18, bold=True)
font_small = pygame.font.SysFont("Arial", 15)
font_mono  = pygame.font.SysFont("Courier New", 14)


# ─────────────────────────────────────────────
#  FILE BROWSER 100% PYGAME — zéro Tkinter
# ─────────────────────────────────────────────
class FileBrowser:
    def __init__(self, title="Choisir un fichier PNG", filter_ext=".png"):
        self.title      = title
        self.filter_ext = filter_ext.lower()
        default_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Skin")
        if os.path.exists(default_dir):
            self.current_dir = default_dir
        else:
            self.current_dir = os.path.expanduser("~")
        self.entries     = []
        self.selected    = None
        self.scroll      = 0
        self.hover_idx   = -1
        self.result      = None   # None = annulé, str = chemin choisi
        self.active      = True

        # Dimensions du panel
        self.W, self.H = 700, 480
        self.X = (WIDTH  - self.W) // 2
        self.Y = (HEIGHT - self.H) // 2
        self.ROW_H = 30
        self.LIST_Y = self.Y + 110
        self.LIST_H = self.H - 170

        self._scan()

    # ── Lecture du dossier ──────────────────
    def _scan(self):
        self.entries  = []
        self.scroll   = 0
        self.selected = None

        try:
            raw = os.listdir(self.current_dir)
        except PermissionError:
            raw = []

        dirs  = sorted([e for e in raw if os.path.isdir(os.path.join(self.current_dir, e))],  key=str.lower)
        files = sorted([e for e in raw if os.path.isfile(os.path.join(self.current_dir, e)) and e.lower().endswith(self.filter_ext)], key=str.lower)

        # Dossier parent
        parent = os.path.dirname(self.current_dir)
        if parent != self.current_dir:
            self.entries.append({"name": "..", "is_dir": True, "path": parent})

        for d in dirs:
            self.entries.append({"name": d, "is_dir": True,  "path": os.path.join(self.current_dir, d)})
        for f in files:
            self.entries.append({"name": f, "is_dir": False, "path": os.path.join(self.current_dir, f)})

    # ── Nombre de lignes visibles ────────────
    @property
    def visible_rows(self):
        return self.LIST_H // self.ROW_H

    # ── Dessin ──────────────────────────────
    def draw(self):
        # Overlay sombre
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        # Panneau principal
        panel = pygame.Rect(self.X, self.Y, self.W, self.H)
        pygame.draw.rect(screen, (20, 20, 28), panel, border_radius=14)
        pygame.draw.rect(screen, ACCENT_COLOR,  panel, 2, border_radius=14)

        # Titre
        t = font_sub.render(self.title, True, TEXT_COLOR)
        screen.blit(t, (self.X + 20, self.Y + 16))

        # Chemin courant
        path_txt = self.current_dir
        if len(path_txt) > 60:
            path_txt = "…" + path_txt[-57:]
        p = font_mono.render(path_txt, True, (120, 160, 255))
        screen.blit(p, (self.X + 20, self.Y + 50))

        # Séparateur
        pygame.draw.line(screen, (50, 50, 70), (self.X + 10, self.Y + 80), (self.X + self.W - 10, self.Y + 80))

        # En-têtes colonnes
        screen.blit(font_small.render("Type", True, (100, 100, 140)), (self.X + 20,  self.Y + 88))
        screen.blit(font_small.render("Nom",  True, (100, 100, 140)), (self.X + 80,  self.Y + 88))

        # Clip zone liste
        clip_rect = pygame.Rect(self.X, self.LIST_Y, self.W - 20, self.LIST_H)
        screen.set_clip(clip_rect)

        for i, entry in enumerate(self.entries[self.scroll: self.scroll + self.visible_rows]):
            real_i = i + self.scroll
            ry = self.LIST_Y + i * self.ROW_H

            # Couleur de fond de ligne
            if real_i == self.selected:
                row_col = ROW_SELECT
            elif i == self.hover_idx:
                row_col = ROW_HOVER
            else:
                row_col = ROW_COLOR if i % 2 == 0 else (35, 35, 35)

            pygame.draw.rect(screen, row_col, (self.X + 8, ry + 2, self.W - 28, self.ROW_H - 2), border_radius=6)

            # Icône
            icon = "📁" if entry["is_dir"] else "🖼"
            icon_color = (120, 180, 255) if entry["is_dir"] else IMPORT_COLOR
            ic = font_small.render("DIR" if entry["is_dir"] else "PNG", True, icon_color)
            screen.blit(ic, (self.X + 18, ry + 8))

            # Nom
            name_col = (160, 200, 255) if entry["is_dir"] else TEXT_COLOR
            nm = font_small.render(entry["name"], True, name_col)
            screen.blit(nm, (self.X + 78, ry + 8))

        screen.set_clip(None)

        # Scrollbar
        total = len(self.entries)
        if total > self.visible_rows:
            bar_h    = max(30, int(self.LIST_H * self.visible_rows / total))
            bar_y    = self.LIST_Y + int((self.LIST_H - bar_h) * self.scroll / (total - self.visible_rows))
            bar_x    = self.X + self.W - 14
            pygame.draw.rect(screen, (40, 40, 50),  (bar_x, self.LIST_Y, 8, self.LIST_H), border_radius=4)
            pygame.draw.rect(screen, SCROLL_COLOR,  (bar_x, bar_y, 8, bar_h),  border_radius=4)

        # Séparateur bas
        sep_y = self.Y + self.H - 60
        pygame.draw.line(screen, (50, 50, 70), (self.X + 10, sep_y), (self.X + self.W - 10, sep_y))

        # Fichier sélectionné
        if self.selected is not None and not self.entries[self.selected]["is_dir"]:
            sel_name = self.entries[self.selected]["name"]
            sel_txt = font_small.render(f"Sélectionné : {sel_name}", True, IMPORT_COLOR)
            screen.blit(sel_txt, (self.X + 20, sep_y + 8))

        # Boutons
        btn_cancel = pygame.Rect(self.X + self.W - 200, sep_y + 4,  90, 36)
        btn_ok     = pygame.Rect(self.X + self.W - 100, sep_y + 4,  90, 36)
        mp = pygame.mouse.get_pos()

        can_ok = self.selected is not None and not self.entries[self.selected]["is_dir"]

        c_cancel = (180, 50, 40)  if btn_cancel.collidepoint(mp) else BACK_COLOR
        c_ok     = (30, 180, 80)  if (btn_ok.collidepoint(mp) and can_ok) else ((60, 100, 60) if not can_ok else IMPORT_COLOR)

        pygame.draw.rect(screen, c_cancel, btn_cancel, border_radius=8)
        pygame.draw.rect(screen, c_ok,     btn_ok,     border_radius=8)

        screen.blit(font_small.render("Annuler", True, TEXT_COLOR), btn_cancel.move(10, 10))
        screen.blit(font_small.render("Ouvrir",  True, TEXT_COLOR), btn_ok.move(14, 10))

        return btn_cancel, btn_ok, can_ok

    # ── Événements ──────────────────────────
    def handle(self, event, btn_cancel, btn_ok, can_ok):
        mp = pygame.mouse.get_pos()

        # Hover
        for i in range(min(self.visible_rows, len(self.entries) - self.scroll)):
            ry = self.LIST_Y + i * self.ROW_H
            row_rect = pygame.Rect(self.X + 8, ry + 2, self.W - 28, self.ROW_H - 2)
            if row_rect.collidepoint(mp):
                self.hover_idx = i
                break
        else:
            self.hover_idx = -1

        if event.type == pygame.MOUSEWHEEL:
            self.scroll = max(0, min(self.scroll - event.y, max(0, len(self.entries) - self.visible_rows)))

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Boutons
            if btn_cancel.collidepoint(event.pos):
                self.active = False
                self.result = None
                return

            if btn_ok.collidepoint(event.pos) and can_ok:
                self.result = self.entries[self.selected]["path"]
                self.active = False
                return

            # Clic sur une ligne
            for i in range(min(self.visible_rows, len(self.entries) - self.scroll)):
                ry = self.LIST_Y + i * self.ROW_H
                row_rect = pygame.Rect(self.X + 8, ry + 2, self.W - 28, self.ROW_H - 2)
                if row_rect.collidepoint(event.pos):
                    real_i = i + self.scroll
                    entry  = self.entries[real_i]

                    if event.button == 1:  # Simple clic = sélection
                        self.selected = real_i

                    # Double-clic ou clic sur dossier = navigation
                    if entry["is_dir"]:
                        if event.button == 1:
                            self.current_dir = entry["path"]
                            self._scan()
                    break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.active = False
                self.result = None
            elif event.key == pygame.K_RETURN:
                if self.selected is not None:
                    entry = self.entries[self.selected]
                    if entry["is_dir"]:
                        self.current_dir = entry["path"]
                        self._scan()
                    else:
                        self.result = entry["path"]
                        self.active = False
            elif event.key == pygame.K_UP:
                if self.selected is None:
                    self.selected = 0
                else:
                    self.selected = max(0, self.selected - 1)
                    if self.selected < self.scroll:
                        self.scroll = self.selected
            elif event.key == pygame.K_DOWN:
                if self.selected is None:
                    self.selected = 0
                else:
                    self.selected = min(len(self.entries) - 1, self.selected + 1)
                    if self.selected >= self.scroll + self.visible_rows:
                        self.scroll = self.selected - self.visible_rows + 1


# ─────────────────────────────────────────────
#  LAUNCHER PRINCIPAL
# ─────────────────────────────────────────────
class Launcher:
    def __init__(self):
        self.running       = True
        self.state         = "HOME"
        self.transition_x  = 0
        self.target_x      = 0
        self.selected_sprite = "IDLE"
        self.skin_folder   = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Skin")
        self.sprites       = {}
        self.file_browser  = None   # instance FileBrowser active ou None

        if not os.path.exists(self.skin_folder):
            os.makedirs(self.skin_folder)

        self.load_skin_images()

    def load_skin_images(self):
        names = ["IDLE", "WALK", "RUN", "JUMP", "FALL"]
        for name in names:
            path = os.path.join(self.skin_folder, f"{name.capitalize()}.png")
            if os.path.exists(path):
                try:
                    img = pygame.image.load(path).convert_alpha()
                    self.sprites[name] = pygame.transform.scale(img, (150, 250))
                except Exception:
                    self.sprites[name] = None
            else:
                self.sprites[name] = None

    def open_file_browser(self):
        self.file_browser = FileBrowser(
            title=f"Choisir l'image PNG pour : {self.selected_sprite}",
            filter_ext=".png"
        )

    def draw_button(self, rect, text, color, is_hovered):
        draw_color = [min(c + 30, 255) for c in color] if is_hovered else color
        pygame.draw.rect(screen, draw_color, rect, border_radius=10)
        txt_surf = font_sub.render(text, True, TEXT_COLOR)
        txt_rect = txt_surf.get_rect(center=rect.center)
        screen.blit(txt_surf, txt_rect)

    def draw_home(self, offset):
        x = offset
        screen.blit(font_main.render("BUILDY", True, ACCENT_COLOR), (x + 50, 50))
        screen.blit(font_sub.render("Open Source GMOD-like", True, (100, 100, 100)), (x + 50, 90))

        btn_skin = pygame.Rect(x + 50, 180, 220, 55)
        self.draw_button(btn_skin, "SKIN EDITOR", BTN_COLOR, btn_skin.collidepoint(pygame.mouse.get_pos()))

        btn_play = pygame.Rect(x + WIDTH // 2 - 125, HEIGHT - 100, 250, 60)
        self.draw_button(btn_play, "OPEN THE GAME", ACCENT_COLOR, btn_play.collidepoint(pygame.mouse.get_pos()))

        return btn_skin, btn_play

    def draw_skin_editor(self, offset):
        x = WIDTH + offset
        screen.blit(font_main.render("SKIN EDITOR", True, TEXT_COLOR), (x + 50, 50))

        preview_rect = pygame.Rect(x + 380, 100, 450, 400)
        pygame.draw.rect(screen, (25, 25, 25), preview_rect, border_radius=20)
        pygame.draw.rect(screen, ACCENT_COLOR,  preview_rect, 2, border_radius=20)

        bounce      = math.sin(pygame.time.get_ticks() * 0.005) * 15
        current_img = self.sprites.get(self.selected_sprite)

        if current_img:
            img_rect = current_img.get_rect(center=(x + 605, 280 + bounce))
            screen.blit(current_img, img_rect)
        else:
            pygame.draw.rect(screen, (50, 50, 50), (x + 555, int(200 + bounce), 100, 160), border_radius=10)
            msg = font_sub.render("NO PNG", True, (150, 150, 150))
            screen.blit(msg, (x + 570, int(270 + bounce)))

        btn_import = pygame.Rect(x + 500, 430, 220, 45)
        self.draw_button(btn_import, f"IMPORT {self.selected_sprite}", IMPORT_COLOR, btn_import.collidepoint(pygame.mouse.get_pos()))

        btn_back = pygame.Rect(x + 50, HEIGHT - 80, 150, 45)
        self.draw_button(btn_back, "< BACK", BACK_COLOR, btn_back.collidepoint(pygame.mouse.get_pos()))

        sidebar_btns = []
        for i, name in enumerate(["IDLE", "WALK", "RUN", "JUMP", "FALL"]):
            rect  = pygame.Rect(x + 50, 140 + i * 65, 200, 50)
            color = ACCENT_COLOR if self.selected_sprite == name else BTN_COLOR
            self.draw_button(rect, name, color, rect.collidepoint(pygame.mouse.get_pos()))
            sidebar_btns.append((rect, name))

        return btn_back, btn_import, sidebar_btns

    def run(self):
        while self.running:
            screen.fill(BG_COLOR)

            self.transition_x += (self.target_x - self.transition_x) * 0.12

            h_skin, h_play   = self.draw_home(self.transition_x)
            e_back, e_import, e_list = self.draw_skin_editor(self.transition_x)

            # File browser par-dessus tout
            btn_cancel = btn_ok = None
            can_ok = False
            if self.file_browser and self.file_browser.active:
                btn_cancel, btn_ok, can_ok = self.file_browser.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Événements absorbés par le file browser en priorité
                if self.file_browser and self.file_browser.active:
                    self.file_browser.handle(event, btn_cancel, btn_ok, can_ok)

                    # Browser vient de se fermer ?
                    if not self.file_browser.active:
                        if self.file_browser.result:
                            dest = os.path.join(self.skin_folder, f"{self.selected_sprite.capitalize()}.png")
                            shutil.copy(self.file_browser.result, dest)
                            self.load_skin_images()
                        self.file_browser = None
                    continue   # ← on ne propage PAS l'event au launcher

                # Événements normaux du launcher
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == "HOME":
                        if h_skin.collidepoint(event.pos):
                            self.state    = "SKIN_EDITOR"
                            self.target_x = -WIDTH
                        if h_play.collidepoint(event.pos):
                            print("Lancement de Buildy...")

                    elif self.state == "SKIN_EDITOR":
                        if e_back.collidepoint(event.pos):
                            self.state    = "HOME"
                            self.target_x = 0
                        if e_import.collidepoint(event.pos):
                            self.open_file_browser()
                        for rect, name in e_list:
                            if rect.collidepoint(event.pos):
                                self.selected_sprite = name

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Launcher().run()
