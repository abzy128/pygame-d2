# pylint: skip-file
import pygame

class MainMenu:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.is_active = True # Main menu starts active
        self.font = pygame.font.Font("assets/fonts/NotoSans-Regular.ttf", 30)
        self.menu_items = ["Play", "Exit"]
        self.selected_index = 0
        self.menu_color = (200, 200, 200)
        self.selected_color = (255, 255, 255)

    def handle_input(self, event):
        if not self.is_active: # Only handle input if main menu is active
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_index = (self.selected_index - 1) % len(self.menu_items)
            elif event.key == pygame.K_DOWN:
                self.selected_index = (self.selected_index + 1) % len(self.menu_items)
            elif event.key == pygame.K_RETURN: # Enter key
                self.select_option()

    def select_option(self):
        selected_option = self.menu_items[self.selected_index]
        if selected_option == "Play":
            self.is_active = False # Deactivate main menu
            self.game.start_game() # Start the game
        elif selected_option == "Exit":
            pygame.quit()
            quit()

    def update(self):
        pass # No updates needed for main menu in this example

    def draw(self):
        self.screen.fill((50, 50, 50)) # Dark gray background for menu
        title_text = self.font.render("Destiny 2 Platformer", True, self.selected_color)
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, 150))
        self.screen.blit(title_text, title_rect)

        menu_start_y = 300
        for index, item in enumerate(self.menu_items):
            color = self.selected_color if index == self.selected_index else self.menu_color
            text_surface = self.font.render(item, True, color)
            text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, menu_start_y + index * 50))
            self.screen.blit(text_surface, text_rect)