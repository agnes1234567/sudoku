import pygame

from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from window import Window

def main():
    pygame.init()
    window = Window("Sudoku")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                window.mouse_click(pos)
            if event.type == pygame.KEYDOWN:
                window.key_press(event.key)     
        window.draw()
        pygame.display.update()
    
    pygame.quit()
    
    

    
if __name__ == "__main__":
    main()
