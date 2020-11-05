import pygame


class Ship:

    def __init__(self, screen):
        """Инициализация корабля и задание начальной позиции"""
        self.screen = screen

        # Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Флаги перемещения корабля
        self.moving_right = False
        self.moving_left = False

    def update(self, step=1):
        if self.moving_right:
            self.rect.centerx += step
        if self.moving_left:
            self.rect.centerx -= step


    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)