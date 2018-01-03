from pathlib import Path
from PIL import Image
import re
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TCON, APIC, TALB, TIT2, TPE2, TPE1, TRCK, error

PATTERN = re.compile('(\d*)[ -]*(.*)')


def autotagmp3(mp3_dir):
    def get_subdirs(dir):
        return (x for x in dir.iterdir() if x.is_dir())

    def get_tracks(dir):
        return (x for x in dir.iterdir() if x.is_dir())
    
    mp3_dir = Path(mp3_dir).resolve()
    
    for genre_dir in get_subdirs(mp3_dir):
        genre = genre_dir.name
        print(f'Genre: {genre}')
        for artist_dir in get_subdirs(genre_dir):
            artist = artist_dir.name
            print(f'    Artist: {artist}')
            for album_dir in get_subdirs(artist_dir):
                album = album_dir.name
                album_cover_source_path = Path(album_dir,'cover_source.jpg')
                album_cover_path = resize_cover_art(album_cover_source_path)
                album_cover = album_cover_path.read_bytes()
                #album_cover = open(album_cover_path, 'rb').read()

                
                print(f'        Album: {album}')
                for track in album_dir.glob('*.mp3'):
                    track_filename = track.stem
                    track_no, track_name = match_object = PATTERN.match(track_filename).groups()
                    track_no = str(int(track_no))
                    print(f'            Track {track_no}: {track_name}')
                    set_tags(
                        path=str(track.resolve()),
                        cover_art=album_cover,
                        title=track_name,
                        album = album,
                        genre=genre,
                        artist=artist,
                        track_no=track_no
                    )

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

def set_tags(path,cover_art,genre,artist,title,album,track_no):
    str(Path(path).resolve())
    tags = ID3()
    tags["APIC"] = APIC(
            encoding=3, # 3 is for utf-8
            mime='image/jpeg', # image/jpeg or image/png
            type=3, # 3 is for the cover image
            desc='Cover',
            data=cover_art
        )
    
    tags["TCON"] = TCON(encoding=3,text=[genre])
    tags["TALB"] = TALB(encoding=3,text=[album])
    tags["TIT2"] = TIT2(encoding=3,text=[title])
    tags["TPE1"] = TPE1(encoding=3,text=[artist])
    tags["TPE2"] = TPE2(encoding=3,text=[artist])
    tags["TRCK"] = TRCK(encoding=3,text=[track_no])

    tags.save(str(Path(path).resolve()),v2_version=3)
