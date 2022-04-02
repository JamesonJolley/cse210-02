from figures import Figure
from pygame import mixer
class tetris:


    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        self.level = 2
        self.zoom = 20
        self.x = 100
        self.y = 60
        self.figure = None



        for i in range (height):
            new_line = []
            for j in range (width):
                new_line.append(0)
            self.field.append(new_line)

    #---------------------Getters
    def get_height(self):
        """Returns the height of the object

            Returns:
                (int): Returns the height of the object
        """
        return self.height

    def get_width(self):
        """Returns the width of the object

            Returns:
                (int): Returns the width of the object
        """
        return self.width
    
    def get_field(self,x,y):
        """Returns the field of the object

            Args:
            x (int): the x value of the object
            y (int): the y value of the object

            Returns:
                (list): Returns the field of the object
        """
        return self.field[x][y]
    
    def get_score(self):
        """Returns the score of the object

            Returns:
                (int): Returns the score of the object
        """
        return self.score
    
    def get_state(self):
        """Returns the state of the object

            Returns:
                (str): Returns the state of the object
        """
        return self.state
    
    def get_level(self):
        """Returns the level of the object

            Returns:
                (int): Returns the level of the object
        """
        return self.level
    
    def get_zoom(self):
        """Returns the zoom of the object

            Returns:
                (int): Returns the zoom of the object
        """
        return self.zoom
    
    def get_x(self):
        """Returns the x coordinates of the object

            Returns:
                (int): Returns the x coordinates of the object
        """
        return self.x
    
    def get_y(self):
        """Returns the y coordinates of the object

            Returns:
                (int): Returns the y coordinates of the object
        """
        return self.y
    
    def get_figure(self):
        """Returns the figure

            Returns:
                (obj): returns and object with the current figure. 
        """
        return self.figure



#---------------------Setters
    def set_state(self,state):
        """Sets a new state

            Args:
            state (str): the state of the game. 
        """
        self.state = state





    def new_figure(self):
        """Creates a new figure"""
        self.figure = Figure(3,0)
    def intersects(self):
        """Determines if the player has crossed the top line and if the figures collide with each other"""
        intersection = False
        for i in range  (4):
            for j in range (4):
                if i * 4 + j in self.figure.image():
                    if i +self.figure.get_y() > self.height - 1 or \
                        j + self.figure.get_x() > self.width - 1 or \
                        j + self.figure.get_x() < 0 or \
                        self.field [i + self.figure.get_y()][j + self.figure.get_x()]>0:
                            intersection = True
        return intersection
    def freeze(self):
        """Freezes the current figure."""
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.get_y()][j+ self.figure.get_x()]= self.figure.get_color()
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def break_lines(self):
            """Determines if there are lines to break"""
            lines = 0
            
            for i in range (1,self.height):
                zeros = 0
                for j in range (self.width):
                    if self.field[i][j] == 0:
                        zeros +=1
                if zeros ==0:
                    lines += 1
                    
                    #music effect
                    break_sound = mixer.Sound('Assets/line_break.wav')
                    break_sound.play()
                    
                    for i1 in range(i, 1,-1):
                        for j in range(self.width):
                            self.field[i1][j] = self.field[i1-1][j]
            self.score += lines ** 2
                    
    def go_space(self):
        """this will bring the falling figure down to the bottom"""
        while not self.intersects():
            self.figure.add_y(1)
        self.figure.subtract_y(1) 
        self.freeze()
    
    def go_down(self):
        """speed up the figure to come down faster"""
        self.figure.add_y(1)
        if self.intersects():
            self.figure.subtract_y(1)
            self.freeze()
    def go_side(self , dx):
        """change the direction of the figure"""
        old_x = self.figure.get_x()
        self.figure.add_x(dx)
        
        if self.intersects():
            self.figure.set_x(old_x)

    def rotate (self):
        """change the rotation of the figure"""
        old_rotation = self.figure.get_rotation()
        self.figure.rotate()
        if self.intersects():
            self.figure.set_rotation(old_rotation)