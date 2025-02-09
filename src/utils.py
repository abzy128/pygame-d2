# pylint: skip-file
import pygame

def load_sound(path):
    sound = pygame.mixer.Sound(path)
    return sound

# You can add more utility functions here, like loading images if needed in a utility function.