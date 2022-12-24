
import pygame
from constants import OFFSET, FONT, BOARD_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH

class Information_box:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(FONT, 30)
        self.y = BOARD_SIZE + OFFSET
        self.x = OFFSET
        self.width = WINDOW_WIDTH - OFFSET * 2
        self.height = WINDOW_HEIGHT - BOARD_SIZE - OFFSET * 2
        self.back_button = pygame.Rect(self.x + self.width // 8, self.y + self.height // 3, self.width // 4, self.height // 3)
        self.solve_button = pygame.Rect(self.x + (self.width // 8) * 5,
                                        self.y + self.height // 3, self.width // 4, self.height // 3)
        self.back_text = self.font.render('Back', 1, (0, 0, 0))
        self.solve_text = self.font.render('Solve', 1, (0, 0, 0))
        
    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.back_button)
        pygame.draw.rect(self.screen, (255, 255, 255), self.solve_button)
        
        back_rect = self.back_text.get_rect(center=(self.x + self.width // 4, self.y + self.height // 2))
        solve_rect = self.solve_text.get_rect(center=(self.x + (self.width // 4) * 3, self.y + self.height // 2))
        
        self.screen.blit(self.back_text, back_rect)
        self.screen.blit(self.solve_text, solve_rect)
        
        
        
        
    def mouse_click(self, pos):
        if self.back_button.collidepoint(pos):
            return 1
        if self.solve_button.collidepoint(pos):
            return 2
        return 0
        
                