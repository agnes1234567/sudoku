import pygame
from board import Board
from information_box import Information_box
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BOARD_SIZE, OFFSET, LINE_WIDTH
from menu import Menu

class Window:
    def __init__(self, title):
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.board = Board(self.screen)
        self.info_box = Information_box(self.screen)
        self.menu = Menu(self.screen)

        pygame.display.set_caption(title)
        self.state = 0
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.state == 0:
            self.menu.draw()
        else:
            self.board.draw()
            self.info_box.draw()
        
    def mouse_click(self, pos):
        x, y = pos
        if self.state == 0:
            self.state = self.menu.mouse_click(pos)
            if self.state != 0:
                self.board.set_up_level(self.state)
        elif x < BOARD_SIZE and y < BOARD_SIZE:
            self.board.mouse_click(pos)
        else:
            respone = self.info_box.mouse_click(pos)
            if respone == 1:
                self.state = 0
            elif respone == 2:
                self.board.solve()
    
    def key_press(self, key):
        if self.board.selected:
            row, col = self.board.selected
            if key == pygame.K_LEFT:
                self.board.set_selected(row, col - 1)
            elif key == pygame.K_RIGHT:
                self.board.set_selected(row, col + 1)
            elif key == pygame.K_UP:
                self.board.set_selected(row - 1, col)
            elif key == pygame.K_DOWN:
                self.board.set_selected(row + 1, col)
            elif key == pygame.K_1:
                self.board.set_value(row, col, 1)
            elif key == pygame.K_2:
                self.board.set_value(row, col, 2)
            elif key == pygame.K_3:
                self.board.set_value(row, col, 3)
            elif key == pygame.K_4:
                self.board.set_value(row, col, 4)
            elif key == pygame.K_5:
                self.board.set_value(row, col, 5)
            elif key == pygame.K_6:
                self.board.set_value(row, col, 6)
            elif key == pygame.K_7:
                self.board.set_value(row, col, 7)
            elif key == pygame.K_8:
                self.board.set_value(row, col, 8)
            elif key == pygame.K_9:
                self.board.set_value(row, col, 9)
            elif key == pygame.K_DELETE:
                self.board.set_value(row, col, 0)
        
        if self.board.is_full():
            print("You win!")
    
    
    
    