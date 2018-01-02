from pathlib import Path

from unload_album_art import *

def test_unload_album_art_from_directory():
    dir = r'D:\audio\mp3'
    unload_album_art_from_directory(dir)

if __name__ == '__main__':
    test_unload_album_art_from_directory()