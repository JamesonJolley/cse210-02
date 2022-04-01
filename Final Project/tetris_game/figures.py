import random
from colors import colors
class Figure:
    #Each of the figure and their different rotations
    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],

        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  
        
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        
        [[1, 2, 5, 6]],
    ]
    def __init__(self, x,y):
        """Creates a new object.
        The purpose of this class is to create an object with the specified (x,y)
        cordiantes
        
        Args:
            x(int):  the x cordinates
            y(int):  the y coordinates
        
        """
        self._x = x
        self._y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1,len(colors) -1)
        self.rotation = 0
    def image(self):
        """This returns the type of figure with its respective rotation. 
            
            Returns: 
                tuple: the figure type and rotation
        """
        return self.figures[self.type][self.rotation]
    def rotate(self):
        """Rotates the figure"""
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])

    def get_x(self):
        """Gets the x coordinates

            Returns: 
                int: the x coordinates
        """
        return self._x
    def get_y(self):
        """Gets the x coordinates

            Returns: 
                int: the x coordinates
        """
        return self._y
    
    def get_type(self):
        """Gets the type of figure

            Returns:
                int: the type of figure
        """
        return self.type
    
    def get_color(self):
        """Gets the color of the figure

            Returns:
                int: the color of the figure
        """
        return self.color
    
    def get_rotation(self):
        """Gets the rotation of the figure

            Returns:
                int: the rotaion of the figure
        """
        return self.rotation

#---------------Setters-------------------
    
    def set_x(self,x):
        """Sets the x coordinates for the figure

            Args:
                x (int): the x coordinates of the figure
        """
        self._x = x
    
    def add_x (self,x):
        """Adds to the x corrdintates of the figure

            Args: 
                x (int): the coordinates of the figure
        """
        self._x += x
    

    def set_y(self,y):
        """Sets the y coordinates

            Args:
                y (int): the y coordiantes of the figure
        """
        self._y = y
    
    def add_y(self,y):
        """Adds to the y coordinates
        
            Args:
                y (int): the y coordiantes of the figure
        """
        self._y += y
    
    def subtract_y(self,y):
        """ Subtracts from the y coordinates

                Args:
                    y (int): the y coordiantes of the figure
        
        """
        self._y -= y


    def set_rotation(self,rotation):
        """Sets the new rotation of the figure

                Args:
                rotation (int): the new rotation of the figure
        """
        self.rotation = rotation
