class parachute:
  def __init__(self):
      self._stages ={
0: """
            ___  
           /___\ 
           \   / 
            \ /               
             0   
            /|\  
            / \  
          
           ^^^^^^^""",

1:"""                 
           /___\ 
           \   / 
            \ /  
             0   
            /|\  
            / \  
                    
           ^^^^^^^""",
                   
2:"""          
           \   / 
            \ /  
             0   
            /|\  
            / \  
          ^^^^^^^""",

3:"""          
            \ /  
             0   
            /|\  
            / \  
          ^^^^^^^""",

4:"""
             x   
            /|\  
            / \  
          
          ^^^^^^^"""}
  def display_parachute(self,int):
    """this function will display the selected stage of the parachute
    args: 
          self. this is the object
          int. a number between 1-4 that will indicate the stage of the parachute. 
    """
    print(self._stages[int])