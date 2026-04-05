import webview
import os
import re
from PIL import Image

class SpriteAPI:
    def __init__(self):
        if not os.path.exists('Skin'):
            os.makedirs('Skin')

    def save_sprite(self, data, filename):
        try:
            img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
            pixels = img.load()
            for i, color in enumerate(data):
                x, y = i % 16, i // 16
                if 'rgba(0, 0, 0, 0)' in color:
                    rgba = (0, 0, 0, 0)
                else:
                    nums = re.findall(r'\d+', color)
                    if len(nums) >= 3:
                        rgba = (int(nums[0]), int(nums[1]), int(nums[2]), 255)
                    else:
                        rgba = (255, 255, 255, 255)
                pixels[x, y] = rgba
            path = os.path.join('Skin', filename)
            img.save(path)
            return "✅ OK"
        except:
            return "❌ ERR"

api = SpriteAPI()
# Chemin mis à jour vers HTML/OCPM.html
window = webview.create_window('OC Player Maker', 'HTML/OCPM.html', js_api=api, width=750, height=650)
webview.start()
