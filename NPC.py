#extensible npc class for objects that can move around the grid                
class NPC:
        #constructor                                                 
        #matrix is a two-dimensional array
        #x and y are integer coordinates
        #type is a defined global constant in main (e.g. FIGHTER = 'a')
        #color is also a defined global constant (e.g. BLUE = False)
        def __init__(self,matrix,x,y,type,color):
                self.x = x
                self.y = y
                self.alive=True
                self.type = type
                self.color = color

        #move method; should be called every turn for every object on the board
        def move(self,matrix,dx,dy):
                self.x+=dx
                self.y+=dy
                return((self.x,self.y))

        #call this method to kill an object                                          
        def die(self):
            self.alive = False
    
        def act(self):
            pass