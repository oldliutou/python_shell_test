import sys
import pygame
from settings import Settings
from ship import  Ship
import game_functions as gf
from pygame.sprite import Group
from  alien import Alien
def run_game():
    # 初始化pygame、设置和屏幕对象


    pygame.mixer.init()  # 初始化
    track = pygame.mixer.music.load("./music/bgm.mp3")  # 加载音乐文件
    pygame.mixer.music.play()  # 开始播放音乐流


    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("鸡你太美")
    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(screen,ai_settings)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人群
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship,aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)

        gf.update_screen(ai_settings, screen, ship, aliens,bullets)

run_game()