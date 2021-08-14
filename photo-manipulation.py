# photo-manipulation
from PIL import Image
me = Image.open("me.png")
bg = Image.open("background.png")
bg.paste(me, (0,0), me)
bg.show()
