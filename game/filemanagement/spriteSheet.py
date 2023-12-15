"""This module contains the SpriteSheet class."""
import pygame
from typing import List, Tuple


class SpriteSheet:
    """This class handles sprite sheets.

    Note: When calling images_at the rect is the format:
    (x, y, x + offset, y + offset)
    """

    def __init__(self, filename: str = None, color_key: pygame.Color | Tuple = None):
        """Load the sheet."""
        if isinstance(color_key, pygame.Color):
            self._color_key = (color_key.r, color_key.g, color_key.b)
        else:
            self._color_key = color_key
        if filename:
            try:
                self._sheet = pygame.image.load(filename).convert()
            except pygame.error as e:
                print(f"Unable to load spritesheet image: {filename}")
                raise SystemExit(e)

    def image_at(self, rectangle: tuple) -> pygame.Surface:
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size)
        if self._sheet:
            image.blit(self._sheet, (0, 0), rect)
            image.set_colorkey(self._color_key)
            return image
        else:
            print("atal ERROR!! no sprite sheet was set!")

    def images_at(self, rects: List[Tuple[int]]) -> List[pygame.Surface]:
        """Load multiple images and return them as a list."""
        return [self.image_at(rect) for rect in rects]

    def load_strip(self, rect, image_count: int) -> List[pygame.Surface]:
        """Load a strip of images, and return them as a list."""
        tuples = [
            (rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
            for x in range(image_count)
        ]
        return self.images_at(tuples)
