import random,time,sys
from NPC import NPC
from Fighter import Fighter
from constants import *

#instantiate matrix object
matrix=[[None for i in range (grid_x)] for j in range(grid_y)]

#run this method every round to handle placing new objects and then running turns
def round(matrix):
        if( raw_input("Please enter the word rules if you would" +
                      " like rules for taking a turn: ") == "rules" ):
		print "Enter your move in the format 'type x y' with spaces."

        red_placement = raw_input("Please enter the Red Team move: ").split()
	red_type = red_placement[0]
	red_x = int(red_placement[1])
	red_y = int(red_placement[2])
	
        blue_placement = raw_input("Please enter the Blue Team move: ").split()
	blue_type = blue_placement[0]
	blue_x = int(blue_placement[1])
	blue_y = int(blue_placement[2])

	matrix[red_x][red_y] = new_npc(red_type, matrix, red_x, red_y, RED)
        matrix[blue_x][blue_y] = new_npc(blue_type, matrix, blue_x, blue_y, BLUE)

	for i in range(20):
		turn(matrix)
		time.sleep(1)

#run this method every turn to handle moving all objects
def turn(matrix):
	#assign a temp matrix and copy all  objects in original matrix into
        #their new positions in temp matrix
	matrix_tmp=[[None for i in range (grid_x)] for j in range(grid_y)]
	for i in range(grid_x):
		for j in range (grid_y):
			if matrix[i][j] != None and matrix[i][j].alive:
				#move each object in the matrix
				new_coords = matrix[i][j].move(matrix)
				#to the matrix copy
				matrix_tmp[new_coords[0]][new_coords[1]]=matrix[i][j]
	#copy the temp matrix to the new matrix
	matrix=matrix_tmp
	#print the matrix
	printmatrix(matrix)
		
#print every object in the matrix, plus a coordinate system
def printmatrix(matrix):
	#print the top coordinate axis
	print ' ',
        for i in range (0, grid_y):
		print i%10,
        print ''

	#loop to print the actual characters 
	for i in range (0,grid_x):
		print i%10, #<-- this is the side coordinate axis
		for j in range (0, grid_y):
			if matrix[i][j]==None:
				print '.',
			else:
				#print the matrix item uppercase only if the NPC
                                #is on the red team
				if (matrix[i][j].color == BLUE): print matrix[i][j].type,
				else: print matrix[i][j].type.upper(),
		print ''
	print ''

#make a new npc based on user input
def new_npc(type, matrix, x, y, color):
	if type == FIGHTER:
		return Fighter(matrix, x, y, color)
	else:
		return

#populate the matrix with test values
matrix[3][3]=Fighter(matrix,3,3,BLUE)
matrix[6][6]=Fighter(matrix,6,6,RED)

#run the turn() method indefinitely
while True:
	round(matrix)
        time.sleep(1)
