from PIL import Image, ImageOps
import pygame


def get_image_1(size, mod=0):
    image = Image.open('images/image_1.png')
    image = image.resize(size, Image.ANTIALIAS)
    if mod == 1:
        return image
    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_free_image(name, size, mod=0):
    image = Image.open(name)
    image = image.resize(size, Image.ANTIALIAS)
    if mod == 1:
        return image
    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image
