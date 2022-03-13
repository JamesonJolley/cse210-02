import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()
       
        

    def get_segments(self):
        return self._segments

    # old will depracate
    #def move_next(self):
    #    # move all segments
    #    for segment in self._segments:
    #        segment.move_next()
    #    # update velocities
    #    for i in range(len(self._segments) - 1, 0, -1):
    #        trailing = self._segments[i]
    #        previous = self._segments[i - 1]
    #        velocity = previous.get_velocity()
    #        trailing.set_velocity(velocity)

    def move_next(self):
        #move the head
        head = self.get_head()
        head.move_next()
        #add new actor
        can_trail = True
        # logic to avoid duplicate segments in the same position 
        for segment in self._segments:
            if head.get_position().equals(segment.get_position()):
                if segment != head:
                    can_trail = False
                    break
        if can_trail:
            self.leave_trail()
   
    
    # fution for apending segments as the tral: Jameosn
    def leave_trail(self):
        '''
        creates and apends a new segment at the position of the head
        '''
        #makes a new segment
        segment = Actor()
        segment.set_position(self.get_head().get_position())
        segment.set_text('#')
        segment.set_color(constants.GREEN)
        self._segments.append(segment)



    def get_head(self):
        return self._segments[0]

    # old will depracate
#    def grow_tail(self, number_of_segments):
#        for i in range(number_of_segments):
#            tail = self._segments[-1]
#            velocity = tail.get_velocity()
#            offset = velocity.reverse()
#            position = tail.get_position()#.add(offset)
#            
#            segment = Actor()
#            segment.set_position(position)
#            segment.set_velocity(velocity)
#            segment.set_text("#")
#            segment.set_color(constants.GREEN)
#            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self): 
        #he x and y variables have to be a multiple of the cell size or the collision detection will not work: Jameson
        x = int(constants.CELL_SIZE)
        y = int(constants.CELL_SIZE *30)

        
        position = Point(x * constants.CELL_SIZE, y)
        text = "@" 
        color = constants.YELLOW 

        segment = Actor()
        segment.set_position(position)
        segment.set_text(text)
        segment.set_color(color)
        self._segments.append(segment)
        

""" this class is an example of inheritance an polymorphism, 
    here I am using the class above (inheritance)
    and then making my changes to create the red snake (polymorphism) :Omarlin"""
class snake_2 (Snake):
    


    def _prepare_body(self):
        #he x and y variables have to be a multiple of the cell size or the collision detection will not work: Jameson 
        x = int(constants.CELL_SIZE )
        y = int(constants.CELL_SIZE * 5)
       
        position = Point(x * constants.CELL_SIZE, y)
        text = "@" 
        color = constants.YELLOW 

        segment = Actor()
        segment.set_position(position)
        segment.set_text(text)
        segment.set_color(color)
        self._segments.append(segment)
        

    # this makes the tral, we are makeing it red with polymorphism  : Jameson
    def leave_trail(self):
        '''
        creates and apends a new segment at the position of the head
        '''
        #makes a new segment
        segment = Actor()
        #sets the position
        segment.set_position(self.get_head().get_position())
        segment.set_text('#')
        segment.set_color(constants.RED)
        self._segments.append(segment)