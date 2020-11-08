import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца"""
    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает его начальную позицию"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображени пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в верхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной позиции пришельца
        self.x = float(self.rect.x)

    # Выводит на экран пришельца в текущей позиции
    def bltime(self):
        """Выводит пришельца в текущем положении."""
        self.screen.blit(self.image, self.rect)
