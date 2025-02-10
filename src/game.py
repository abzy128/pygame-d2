# pylint: skip-file
import pygame
from level import Level
from player import Player
from utils import load_sound

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.level_index = 0
        self.levels = [] # Load levels in load_levels()
        self.player = None
        self.current_level = None
        self.playing = False # Game starts in main menu
        self.trap_sound = load_sound("assets/sounds/effects/thrall_explosion.mp3")
        self.engram_sound = load_sound("assets/sounds/effects/engram_pickup.mp3")
        self.font = pygame.font.Font("assets/fonts/NotoSans-Regular.ttf", 20) # Load font

        self.load_levels() # Load level data after initialization

    def load_levels(self):
        level1_data = {
            "background": "assets/images/background/europa_1.png",
            "music": "assets/sounds/music/beyond_light.mp3",
            "layout": [
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "W                                      W",
                "W                                      W",
                "W                                      W",
                "W         WWWWWWWW       WWWWWWWWWWWWWWW",
                "W                                      W",
                "W  T                 EE   T            W",
                "W WWWW     WWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "W          WWW                         W",
                "W                E                     W",
                "W    WWWW                            T W",
                "W    WWWWWWWWWWWWWWWWWWW               W",
                "W                    E                 W",
                "W                                T     W",
                "W                        WWWWWWWWWWWWW W",
                "W      E    WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "WT                                     W",
                "WWWWWWWW                               W",
                "W                                      W",
                "W                                      W",
                "W         E                            W",
                "W    T                                 W",
                "WWWWWWWWWWWWW                   E      W",
                "W                                      W",
                "W                                      W",
                "W               WWWWW         WWWWW    W",
                "W                                      W",
                "W                                      W",
                "W     T     T            T          T  W",
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            ],
            "tile_size": 30,
            "player_spawn": (1000, 700),
            "engram_count": 6,
        }
        level2_data = {
            "background": "assets/images/background/dreaming_city.png",
            "music": "assets/sounds/music/forsaken_dreaming_city_main.mp3",
            "layout": [
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "W                                      W",
                "W                                      W",
                "W                                      W",
                "W         WWWWWWWW       WWWWWWWWWWWWWWW",
                "W                                      W",
                "W  T                 EE   T            W",
                "W WWWW     WWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "W          WWW                         W",
                "W                E                     W",
                "W    WWWW                            T W",
                "W    WWWWWWWWWWWWWWWWWWW               W",
                "W                    E                 W",
                "W                                T     W",
                "W                        WWWWWWWWWWWWW W",
                "W      E    WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "WT                                     W",
                "WWWWWWWW                               W",
                "W                                      W",
                "W                                      W",
                "W         E                            W",
                "W    T                                 W",
                "WWWWWWWWWWWWW                   E      W",
                "W                                      W",
                "W                                      W",
                "W               WWWWW         WWWWW    W",
                "W                                      W",
                "W                                      W",
                "W     T     T            T          T  W",
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            ],
            "tile_size": 30,
            "player_spawn": (200, 200),
            "engram_count": 6,
        }
        level3_data = {
            "background": "assets/images/background/ascendant_plane.png",
            "music": "assets/sounds/music/forsaken_darkness_gathers.mp3",
            "layout": [
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "W                                      W",
                "W                                      W",
                "W                                      W",
                "W         WWWWWWWW       WWWWWWWWWWWWWWW",
                "W                                      W",
                "W  T                 EE   T            W",
                "W WWWW     WWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "W          WWW                         W",
                "W                E                     W",
                "W    WWWW                            T W",
                "W    WWWWWWWWWWWWWWWWWWW               W",
                "W                    E                 W",
                "W                                T     W",
                "W                        WWWWWWWWWWWWW W",
                "W      E    WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "WT                                     W",
                "WWWWWWWW                               W",
                "W                                      W",
                "W                                      W",
                "W         E                            W",
                "W    T                                 W",
                "WWWWWWWWWWWWW                   E      W",
                "W                                      W",
                "W                                      W",
                "W               WWWWW         WWWWW    W",
                "W                                      W",
                "W                                      W",
                "W     T     T            T          T  W",
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            ],
            "tile_size": 30,
            "player_spawn": (30, 500),
            "engram_count": 6,
        }

        self.levels = [level1_data, level2_data, level3_data]

    def start_game(self):
        self.level_index = 0
        self.load_level(self.level_index)
        self.playing = True

    def load_level(self, level_index):
        level_data = self.levels[level_index]
        pygame.mixer.music.load(level_data["music"]) # Load level music
        pygame.mixer.music.play(-1) # Play music in loop

        self.current_level = Level(level_data, self.screen) # Create level instance
        player_spawn = level_data["player_spawn"]
        self.player = Player(player_spawn, "assets/images/guardian.png") # Create player instance
        self.player.hp = 3 # Reset player health
        self.current_level.engrams_collected = 0 # Reset engram count

    def handle_input(self, event):
        if not self.playing: # Only process input if game is running
            return
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player.move_left()
            if event.key == pygame.K_RIGHT:
                self.player.move_right()
            if event.key == pygame.K_SPACE: # Jump action
                self.player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and self.player.velocity.x < 0:
                self.player.stop_x()
            if event.key == pygame.K_RIGHT and self.player.velocity.x > 0:
                self.player.stop_x()

    def run(self, events):
        if not self.playing:
            return # Don't run game logic if not playing

        for event in events:
            self.handle_input(event) # Handle events every frame
        self.update()
        self.draw()

    def update(self):
        if not self.playing:
            return

        self.player.update(self.current_level)

        # Check for engram collection
        engram_collisions = pygame.sprite.spritecollide(self.player, self.current_level.engram_group, False)
        engram_collision_index = len(engram_collisions) > 0 and self.current_level.engram_group.sprites().index(engram_collisions[0])
        if engram_collision_index:
            print("Engram collision. Collected:", self.current_level.engrams_collected)
            self.engram_sound.play()
            self.current_level.engram_group.sprites()[engram_collision_index].kill() # Remove engram
            self.current_level.engrams_collected += 1
            if self.current_level.engrams_collected == self.current_level.level_data["engram_count"]:
                self.level_index += 1
                if self.level_index < len(self.levels):
                    self.load_level(self.level_index) # Load next level
                else:
                    self.playing = False # Game finished all levels (Win condition)
                    pygame.mixer.music.stop() # Stop level music

        # Check for trap collision
        trap_collisions = pygame.sprite.spritecollide(self.player, self.current_level.trap_group, False)
        trap_collision_index = len(trap_collisions) > 0 and self.current_level.trap_group.sprites().index(trap_collisions[0])
        if trap_collision_index:
            if self.player.hp > 0:
                self.player.hp -= 1
                self.trap_sound.play()
                self.current_level.trap_group.sprites()[trap_collision_index].kill() # Remove trap
                self.player.rect.topleft = self.current_level.level_data["player_spawn"] # Reset player position
                print("Player respawned. Current HP:", self.player.hp)
                if self.player.hp <= 0:
                    print("Game Over! HP depleted.")
                    self.playing = False # Game Over condition (HP 0)
                    pygame.mixer.music.stop() # Stop level music

    def draw(self):
        if not self.playing:
            self.draw_game_over() # Draw game over screen if not playing
            return

        self.current_level.draw() # Draw level background and tiles
        self.current_level.engram_group.draw(self.screen) # Draw engrams
        self.current_level.trap_group.draw(self.screen) # Draw traps
        self.player.draw(self.screen) # Draw player

        # Display HP
        hp_text = self.font.render(f"HP: {self.player.hp}", True, (255, 255, 255))
        self.screen.blit(hp_text, (10, 10))

        # Display Engrams Collected
        engram_count_text = self.font.render(f"Engrams: {self.current_level.engrams_collected}/{self.current_level.level_data['engram_count']}", True, (255, 255, 255))
        self.screen.blit(engram_count_text, (10, 40)) 


    def draw_game_over(self):
        self.screen.fill((0, 0, 0)) # Black background
        game_over_text = None
        if self.level_index == len(self.levels) and self.current_level.engrams_collected == self.current_level.level_data["engram_count"]:
            game_over_text = self.font.render("CONGRATULATIONS! YOU WON!", True, (255, 255, 255))
        elif self.player.hp <= 0:
             game_over_text = self.font.render("GAME OVER! HP DEPLETED!", True, (255, 255, 255))
        else: # Exited mid game
            game_over_text = self.font.render("GAME OVER!", True, (255, 255, 255))


        text_rect = game_over_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(game_over_text, text_rect)
        restart_text = self.font.render("""Press SPACE to restart""", True, (255, 255, 255))
        quit_text = self.font.render("""Press ESC or Q to quit""", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 50))
        quit_rect = quit_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 100))
        self.screen.blit(restart_text, restart_rect)
        self.screen.blit(quit_text, quit_rect)
        pygame.display.flip()
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    self.start_game()
                    break
                if(event.key == pygame.K_ESCAPE or event.key == pygame.K_q):
                    pygame.quit()
                    quit()
        
    def stop_game(self):
        self.playing = False
        pygame.mixer.music.stop()
        self.level_index = 0 # Reset level for next play through