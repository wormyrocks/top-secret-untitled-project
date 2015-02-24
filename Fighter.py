from NPC import NPC
import random
from constants import *


#Subclass for Fighter object                                                         
class Fighter(NPC):
        def __init__(self, matrix,x,y,color):
                self.sword=0
                NPC.__init__(self,matrix,x,y,FIGHTER,color)

        def move(self, matrix):
                #keeps track of whether move is legal



                exit_condition = False
                
                while not exit_condition:
                        #move 1 unit in a random direction (left, right, up, or down)                                                                                    
                        d = random.randint(-1,1)
                        if d !=0:
                                e = 0
                        else:
                                e = random.randint(0,1)*2-1
                        #if the random move isn't inside the bounds of the grid, calculate it again                                                                      
                        exit_condition = (self.x+d >= 0 and self.x+d < grid_x and 
                                          self.y + e >=0 and self.y+e < grid_y)
                #return the coordinates of the new position so that the turn method can move the object                                                                  
                return NPC.move(self,matrix,d,e)

        def act(self, matrix):
                self.sword = 0
                adjacents=(matrix[self.x+1][self.y] if self.x+1<len(matrix[0]) else None,
                           matrix[self.x-1][self.y] if self.x-1>=0 else None,
                           matrix[self.x][self.y+1] if self.y+1<len(matrix) else None,
                           matrix[self.y][self.y-1] if self.y-1>=0 else None);
                           
                for i in range (0, len(adjacents)):
                    if adjacents[i] != None and adjacents[i].type == FIGHTER and adjacents[i].color != self.color:
                        adjacents[i].die()
                        self.sword = i