from gc import freeze
import imp
from operator import truediv
from turtle import width
from figures import Figure

class tetris:
    level = 2
    score = 0
    state = 'start'
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    figure = None

    def __init__(self, height, width):
        self.height = height
        self.width = width

        for i in range (height):
            new_line = []
            for j in range (width):
                new_line.append(0)
            self.field.append(new_line)
    def new_figure(self):
        self.figure = Figure(3,0)
    def intersects(self):
        intersection = False
        for i in range  (4):
            for j in range (4):
                if i * 4 + j in self.figure.image():
                    if i +self.figure.y > self.height - 1 or \
                        j + self.figure.x > self.width - 1 or \
                        j + self.figure.x < 0 or \
                        self.field [i + self.figure.y][j + self.figure.x]>0:
                            intersection = True
        return intersection
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j+ self.figure.x]= self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def break_lines(self):
            lines = 0
            for i in range (1,self.height):
                zeros = 0
                for j in range (self.width):
                    if self.field[i][j] == 0:
                        zeros +=1
                if zeros ==0:
                    lines += 1
                    for i1 in range(i, 1,-1):
                        for j in range(self.width):
                            self.field[i1][j] = self.field[i1-1][j]
            self.score += lines ** 2
                    
    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1 
        self.freeze()
    
    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -=1
            self.freeze()
    def go_side(self , dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x
    def rotate (self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation