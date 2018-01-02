from autotagmp3 import resize_cover_art

def test_resize_cover_art():
    path = r"D:\audio\mp3\Audiobook\Ohrenbär\Dollie und Schwein\cover_source.jpg"
    #path = r"D:\audio\mp3\Videogame\Deep Silver\Lost Horizon\cover_source.jpg"
    return resize_cover_art(path)

if __name__ == '__main__':
    p = test_resize_cover_art()
    print(p)