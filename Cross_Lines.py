#Pranav A's Cross_Lines
#First version created at July 2021
#Use Python 3 to execute
#Also download pygame.
#You can change the size of the lines by changing the value of the line_size.




import os
from typing import Sized
import pgzrun
# You can change the size of the board by changing the variables WIDTH,HEIGHT.
# I recommend to keep the variables WIDTH and HEIGHT under 1000 because it might take longer to render.
WIDTH = 750
HEIGHT = 750
def update() :
	global bigbox_y
	





def draw():
	screen.clear()
	screen.fill(("yellow"))
	size_x = WIDTH
# You can change the size of the lines by changing the value of the variable line_size.
	line_size = 20
	x = 0
	y = 0
	bigbox_y = 0

	y_size = HEIGHT
	bigbox_x = 0
	for i in range(1,10001):
		BigBox = Rect((bigbox_x ,bigbox_y),(line_size,y_size ))
		screen.draw.filled_rect(BigBox ,("orange"))
		bigbox_x += line_size * 2
		BigBox = Rect((x ,y),(size_x,line_size ))
		screen.draw.filled_rect(BigBox ,("red"))
		y += line_size * 2



pgzrun.go()