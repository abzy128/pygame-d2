# pylint: skip-file
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, spawn_position, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 40))
        self.rect = self.image.get_rect(topleft=spawn_position)
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 1
        self.jump_force = -30
        self.on_ground = False
        self.hp = 3 # Initial health points

    def move_left(self):
        self.velocity.x = -self.speed

    def move_right(self):
        self.velocity.x = self.speed

    def stop_x(self):
        self.velocity.x = 0

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_force
            self.on_ground = False

    def apply_gravity(self):
        self.velocity.y += self.gravity
        if self.velocity.y > 10: # Limit falling speed
            self.velocity.y = 10

    def update(self, level):
        self.apply_gravity()
        self.rect.x += self.velocity.x
        # X-axis collision
        collision_tiles_x = pygame.sprite.spritecollide(self, level.tile_group, False)
        for tile in collision_tiles_x:
            if self.velocity.x > 0: # Moving right
                self.rect.right = tile.rect.left
                self.velocity.x = 0
            elif self.velocity.x < 0: # Moving left
                self.rect.left = tile.rect.right
                self.velocity.x = 0

        self.rect.y += self.velocity.y

        # Y-axis collision
        collision_tiles_y = pygame.sprite.spritecollide(self, level.tile_group, False)
        if collision_tiles_y:
            for tile in collision_tiles_y:
                if self.velocity.y > 0: # Falling down
                    self.rect.bottom = tile.rect.top
                    self.velocity.y = 0
                    self.on_ground = True
                elif self.velocity.y < 0: # Jumping up
                    self.rect.top = tile.rect.bottom
                    self.velocity.y = 0
        else:
            self.on_ground = False # Not on ground if no collision on y-axis

    def check_collision_with_group(self, level, group): # added level as argument, though not used in this version. Keep it for potential future use/consistency if needed.
        if group == level.trap_group: # Check if it's trap group
            collided_sprites = pygame.sprite.spritecollide(self, group, True) # False - don't remove trap
        else: # For other groups (like engrams), keep removing
            collided_sprites = pygame.sprite.spritecollide(self, group, True) # True - remove sprite on collision

        if collided_sprites:
            # If there's a collision, just return True
            return True
        return False # No collision

    def draw(self, screen):
        screen.blit(self.image, self.rect)