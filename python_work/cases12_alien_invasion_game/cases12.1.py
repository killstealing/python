import sys
import pygame

class User:
    def __init__(self,sky_game):
        self.screen=sky_game.screen
        self.screen_rect=sky_game.screen.get_rect()
        self.image=pygame.image.load('python/python_work/alien_invasion/images/ship.bmp')
        self.rect=self.image.get_rect()

        self.rect.center=self.screen_rect.center
    def blitme(self):
        self.screen.blit(self.image,self.rect)


class Sky:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption('blue sky')
        self.user=User(self)
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            # for event in pygame.event.get():
            #     if event.type==pygame.QUIT:
            #         sys.exit
            # self.screen.fill((0,0,255))
            # pygame.display.flip()
            # self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit
    def _update_screen(self):
        self.screen.fill((0,0,255))
        self.user.blitme()
        pygame.display.flip()


if __name__=='__main__':
    sky=Sky()
    sky.run_game()