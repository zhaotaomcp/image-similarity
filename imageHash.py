# -*- coding: utf-8 -*-

from PIL import Image
import imagehash

if __name__ == '__main__':
    img1 = "images/225.jpg"
    img2 = "images/226.jpg"
    phash1 = imagehash.phash(Image.open(img1))
    phash2 = imagehash.phash(Image.open(img2))
    distance = phash1 - phash2
    print(distance)
