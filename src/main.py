# pylint: skip-file
import pygame
from game import Game
from ui import MainMenu

def main():
    pygame.init()
    screen_width = 1200
    screen_height = 900
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Destiny 2 Platformer")

    game = Game(screen)
    main_menu = MainMenu(screen, game)

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            main_menu.handle_input(event) # Give input to main menu first

        if main_menu.is_active:
            main_menu.update()
            main_menu.draw()
        else:
            game.run(events) # Game loop runs when main menu is inactive

        pygame.display.flip()
        pygame.time.Clock().tick(60) # Limit to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()