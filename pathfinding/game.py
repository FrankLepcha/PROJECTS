import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))  # this is how the display is going to be
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:  # creating a class called spot.basically function as node
    def _innit_(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width # to draw a cube. origin point.
        self.y = col * width #to draw a cube. origin point.
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self): #indexing through row collums
        return self.row, self.col

    def is_closed(self): # defined a function in order to identify what spot is closed. IE red is used.
        return self.color == RED

    def is_open(self): #open area in the display
        return self.color == GREEN

    def is_barrier(self): #barrier in the display
        return self.color == BLACK

    def is_start(self): #starting color
        return self.color == ORANGE

    def is_end(self): #ending color
        return self.color == PURPLE

    def make_start(self):
        return self.color == ORANGE

    def reset(self):
        self.color == WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREY

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):  # drawing a rectangle in pygame
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False

def h(p1, p2):  # created a new function p1 and p2. Essetinally works as (x,y) or (row,colloum)
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

    # Creating a function that defines and implements grid using the for loops with "[]" brackets. Also uses row and colloum to make grid also
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid

def draw_grid(win, rows, width):  # draws a horizontal line
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (0, j * gap), (j * gap, width))  # draws a vertical line

def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def hget_clicked_pos(pos, rows, width):  # functions created to display color of the mouse on the program
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    return row, col

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    while run:
        draw(win,grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]:  # when the left mouse button is pushed. 0 i left
                pos = pygame.mouse.get_pos()  # gives us the position
                row, col = hget_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # when the right mouse button is pushed
                pos = pygame.mouse.get_pos()  # gives us the position
                row, col = hget_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None
                pass

        pygame.quit()


main(WIN,WIDTH)