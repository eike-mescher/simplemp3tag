from pathlib import Path
from PIL import Image

def resize_cover_art(path):
    path = Path(path).resolve()
    cover_path = Path(path.parent,'cover.jpg')
    img = Image.open(str(path))
    #Crop
    width, height = img.size
    if height / width > 1:
        crop_tuple = (0,int((height - width)/2.0),width,int((height + width)/2.0))
    else:
        crop_tuple = (int((width - height)/2.0),0,int((width + height)/2.0),height)
    img = img.crop(crop_tuple)
    
    img = img.resize((800,800))
    
    img = img.save(str(cover_path),quality=40)
    
    return cover_path
