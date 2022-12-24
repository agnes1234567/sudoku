import pygame
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, FONT, HEADER

class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(FONT, 20)
        self.width = WINDOW_WIDTH // 2
        self.height = WINDOW_HEIGHT 
        self.x = WINDOW_WIDTH // 4
        self.y = WINDOW_HEIGHT // 6
        self.header = self.font.render(HEADER, 1, (255, 255, 255))
        self.easy_button = pygame.Rect(self.x, self.y + 50, self.width, self.height // 10)
        self.medium_button = pygame.Rect(self.x, self.y + 150, self.width, self.height // 10)
        self.hard_button = pygame.Rect(self.x, self.y + 250, self.width, self.height // 10)
        self.random_button = pygame.Rect(self.x, self.y + 350, self.width, self.height // 10)
        
    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.easy_button)
        pygame.draw.rect(self.screen, (255, 255, 255), self.medium_button)
        pygame.draw.rect(self.screen, (255, 255, 255), self.hard_button)
        pygame.draw.rect(self.screen, (255, 255, 255), self.random_button)
        
        easy_text = self.font.render('Easy', 1, (0, 0, 0))
        medium_text = self.font.render('Medium', 1, (0, 0, 0))
        hard_text = self.font.render('Hard', 1, (0, 0, 0))
        random_text = self.font.render('Random', 1, (0, 0, 0))
        
        easy_rect = easy_text.get_rect(center=(self.x + self.width // 2, self.y + 85))
        medium_rect = medium_text.get_rect(center=(self.x + self.width // 2, self.y + 185))
        hard_rect = hard_text.get_rect(center=(self.x + self.width // 2, self.y + 285))
        random_rect = random_text.get_rect(center=(self.x + self.width // 2, self.y + 385))
        header_rect = self.header.get_rect(center=(self.x + self.width // 2, self.y + 20))
        
        self.screen.blit(self.header, header_rect)
        self.screen.blit(easy_text, easy_rect)
        self.screen.blit(medium_text, medium_rect)
        self.screen.blit(hard_text, hard_rect)
        self.screen.blit(random_text, random_rect)
        
    def mouse_click(self, pos):
        if self.easy_button.collidepoint(pos):
            return 1
        if self.medium_button.collidepoint(pos):
            return 2
        if self.hard_button.collidepoint(pos):
            return 3
        if self.random_button.collidepoint(pos):
            return 4
        return 0