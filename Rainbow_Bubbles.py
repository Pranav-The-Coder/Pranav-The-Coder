#Pranav A's "Rainbow Bubbles"
#First version created at July 2021
#Use Python 3 to execute
#Also download pygame.
#You can change the size of the circles/bubbles by changing the value for the variable radius

import os
from typing import Sized
import pgzrun
a = 330 - 330 * 2
b = 230 - 230 * 2

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

def draw():
	

	
	screen.fill(("black"))
	screen.draw.filled_circle((400,300),30,"yellow")
	


	brown_x = 450
	pur_y = 250
	#change radius to change the size of the circle
	radius = 30
	x = 450
	y = 350
	white_x = 350
	for i in range(1,1000):
		screen.draw.filled_circle((x,y),radius,"pink")
		screen.draw.filled_circle((white_x,y),radius,"white")
		screen.draw.filled_circle((white_x,pur_y),radius,"purple")
		screen.draw.filled_circle((brown_x,pur_y),radius,"brown")
		screen.draw.filled_circle((white_x,300),radius,"red")
		screen.draw.filled_circle((x,300),radius,"green")
		screen.draw.filled_circle((400,pur_y),radius,"orange")
		screen.draw.filled_circle((400,y),radius,"blue")


		x += radius
		y += radius
		pur_y -= radius
		white_x -= radius
		brown_x += radius


pgzrun.go()









