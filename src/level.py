# pylint: skip-file
import pygame

class Level:
    def __init__(self, level_data, screen):
        self.screen = screen
        self.level_data = level_data
        self.background_image = pygame.image.load(level_data["background"]).convert()
        self.background_image = pygame.transform.scale(self.background_image, (screen.get_width(), screen.get_height())) # Scale to screen size
        self.tile_size = level_data["tile_size"]
        self.tile_group = pygame.sprite.Group() # For walls
        self.engram_group = pygame.sprite.Group() # For engrams
        self.trap_group = pygame.sprite.Group() # For traps
        self.engrams_collected = 0 # Count of collected engrams

        self.setup_level()

    def setup_level(self):
        layout = self.level_data["layout"]
        tile_size = self.tile_size
        trap_image = pygame.image.load("assets/images/thrall.png").convert_alpha()
        engram_image = pygame.image.load("assets/images/engram.png").convert_alpha()


        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'W': # Wall
                    tile = pygame.sprite.Sprite()
                    tile.image = pygame.Surface((tile_size, tile_size))
                    tile.image.fill((100, 100, 100)) # Gray color for walls
                    tile.rect = tile.image.get_rect(topleft=(x, y))
                    self.tile_group.add(tile)
                elif cell == 'E': # Engram
                    engram = pygame.sprite.Sprite()
                    engram.image = pygame.transform.scale(engram_image, (tile_size, tile_size)) # Scale engram image
                    engram.rect = engram.image.get_rect(topleft=(x, y))
                    self.engram_group.add(engram)
                elif cell == 'T': # Trap
                    trap = pygame.sprite.Sprite()
                    trap.image = pygame.transform.scale(trap_image, (tile_size, tile_size)) # Scale trap image
                    trap.rect = trap.image.get_rect(topleft=(x, y))
                    self.trap_group.add(trap)

    def draw(self):
        self.screen.blit(self.background_image, (0, 0)) # Draw background first
        self.tile_group.draw(self.screen) # Draw tiles/walls
        # Engrams and traps are drawn in game.py's draw method for layering order