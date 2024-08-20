import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()

        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        # self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width=self.screen.get_rect().width
        # self.settings.screen_height=self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type== pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self,event):
        """响应按下"""
        print(f'keydown {event.key}')
        if event.key==pygame.K_RIGHT:
            print('moving_right True')
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            print('moving_left True')
            self.ship.moving_left=True
        elif event.key==pygame.K_q:
            print('K_q True')
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
    def _fire_bullet(self):
        """创建一颗子弹,并将其加入编组bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
            
    def _check_keyup_events(self,event):
        """响应释放"""
        print('KEYUP True')
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
            print('moving_right False')
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False
            print('moving_left False')
    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()
        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        #每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()

        
if __name__=='__main__':
    #创建游戏实例并运行游戏
    ai=AlienInvasion()
    ai.run_game()