from pathlib import Path

def unload_album_art_from_directory(dir):
    dir_path = Path(dir).resolve()
    art_path = Path(dir_path.parent,dir_path.name + '_art')
    art_path.mkdir(exist_ok=True)

from mutagen import File

def unload_album_art(path):
    p = Path(path).resolve()
    art_path = Path(p.parent,p.stem+'.png')
    file = File(str(p)) # mutagen can automatically detect format and type of tags
    artwork = file.tags['APIC:'].data # access APIC frame and grab the image
    with open(art_path, 'wb') as img:
       img.write(artwork) # write artwork to new image

unload_album_art(r"D:\audio\mp3\Videogame\Nintendo\Street Fighter 2\02 Clamato Fever (Menu).mp3")
