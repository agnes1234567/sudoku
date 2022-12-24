import pygame
from constants import OFFSET, LINE_WIDTH, NUMBER_OF_ROWS, NUMBER_OF_COLS, BOARD_SIZE, FONT
from sudoku_solver import Sudoku_solver
from sudoku_creator import Sudoku_creator


class Board:
    def __init__(self, screen):
        self.width = BOARD_SIZE - OFFSET * 2
        self.height = BOARD_SIZE - OFFSET * 2
        self.rows = NUMBER_OF_ROWS
        self.cols = NUMBER_OF_COLS
        self.screen = screen
        self.font = pygame.font.SysFont(FONT, 35)
        self.grid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.selected = None
        self.solver = Sudoku_solver()
        self.creator = Sudoku_creator()
        
        
    
    def draw(self):
        for i in range(0, self.width + 1, self.width // self.rows):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (255, 255, 255),
                             (i + OFFSET, 0), (i + OFFSET, self.height), LINE_WIDTH)
            else:
                pygame.draw.line(self.screen, (255, 255, 255),
                                (i + OFFSET, 0), (i + OFFSET, self.height), LINE_WIDTH // 2)
        for i in range(0, self.height + 1, self.height // self.cols):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (255, 255, 255),
                                (0 + OFFSET, i), (self.width + OFFSET, i), LINE_WIDTH)
            else:
                pygame.draw.line(self.screen, (255, 255, 255),
                                (0 + OFFSET, i), (self.width + OFFSET, i), LINE_WIDTH // 2)
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] != 0:
                    self.draw_value(row, col)
        
        self.draw_selected()
    
    def draw_value(self, row, col):
        value = self.grid[row][col]
        if self.value_full(value):
            color = (0, 255, 0)
        else:
            color = (255, 255, 255)
        text = self.font.render(str(value), True, color)
        x = col * self.width // self.cols + OFFSET * 6
        y = row * self.height // self.rows + OFFSET * 2
        self.screen.blit(text, (x, y))
        
    def draw_selected(self):
        if self.selected:
            pygame.draw.rect(self.screen, (250,100,250), (self.selected[1] * self.width // self.cols + OFFSET,
                                                            self.selected[0] * self.height // self.rows,
                                                            self.width // self.cols,
                                                            self.height // self.rows), LINE_WIDTH)
 
    
    def set_value(self, row, col, value):
        if self.is_valid(row, col, value):
            self.grid[row][col] = value
            self.selected = None
  
    
    def get_value(self, row, col):
        return self.grid[row][col]
    
    def set_selected(self, row, col):
        self.selected = (row, col)
    
    def mouse_click(self, pos):
        x, y = pos
        row = y // (self.height // self.rows)
        col = x // (self.width // self.cols)
        self.set_selected(row, col)
        
    def keyboard_input(self, value):
        if self.selected:
            self.set_value(self.selected[0], self.selected[1], value)
    
    def is_valid(self, row, col, value):
        for i in range(self.rows):
            if self.grid[row][i] == value:
                return False
        for i in range(self.cols):
            if self.grid[i][col] == value:
                return False
            
        subgrid_positions = self.get_subgrid_positions(row, col)
        for pos in subgrid_positions:
            x, y = pos
            if self.grid[x][y] == value:
                return False
        return True
    
    def get_subgrid_positions(self, row, col):
        subgrid_positions = []
        for i in range(3):
            for j in range(3):
                subgrid_positions.append((row - row % 3 + i, col - col % 3 + j))
        return subgrid_positions
    
    def is_full(self):
        for num in range(1, 10):
            if not self.value_full(num):
                return False
        return True
    
    def value_full(self, value):
        count_in_grid = len([ value for row in self.grid for val in row if val == value])
        return count_in_grid == 9
    
    def clear(self):
        self.grid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.selected = None
        
    def set_up_level(self, level):
        self.clear()
        if level > 3:
            self.creator.create()
            self.grid = self.creator.grid
        else:
            self.read_level_from_file(level)
                
    def read_level_from_file(self, level):
        filepath = 'levels/' + str(level) + '.txt'
        with open(filepath, 'r') as f:
            for row in range(self.rows):
                values = f.readline().split(',')
                for col in range(self.cols):
                    self.set_value(row, col, int(values[col]))
                    
    def solve(self):
        res = self.solver.solve(self.grid)
        if res:
            self.grid = res
        else:
            print('No solution found')
    
                    
    
    