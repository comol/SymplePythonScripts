import os
from PIL import Image

Image.MAX_IMAGE_PIXELS = 1000000000  

path = u'Path to file dir' # поменяем директорию на ту, где у нас расположены картинки

print(path)
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
     for file in f:
        if ('.tif' in file or '.tiff' in file or '.dib' in file) and (not '.png' in file):            
            fullpath = os.path.join(r, file)
            if not os.path.exists(fullpath + ".png"):
                try:                    
                    im = Image.open(fullpath)
                    im.save(fullpath + ".png", "PNG")
                except:
                    print("error converting file " + fullpath)
