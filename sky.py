import sys
import pygame
from star import Star
from random import randint

class Sky:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.background_screen = (255,255,255)
        self.screen = pygame.display.set_mode((1200,700))
        pygame.display.set_caption("Viewing the star")

        self.stars = pygame.sprite.Group()
        self._create_fleet()
        # self.random_number = randint(-10,10)


    def _create_fleet(self):
        star = Star(self)
        # self.stars.add(star)
        # star_width = star.rect.width
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (700 - 2 * star_height):
            while current_x < (1200 - 2 * star_width):
                new_star = Star(self)
                random_number = randint(-50,50)
                new_star.x = current_x 
                new_star.rect.x = current_x + random_number
                new_star.rect.y = current_y + random_number
                self.stars.add(new_star)
                current_x += 2 * star_width

            current_x = star_width 
            current_y += 2 * star_height    




    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()    

            self.screen.fill(self.background_screen)
            self.stars.draw(self.screen)
            pygame.display.flip()  
            self.clock.tick(60)          


if __name__ == "__main__":
    shine = Sky()
    shine.run()

