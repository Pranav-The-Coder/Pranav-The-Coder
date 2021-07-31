#Pranav A's Tetris Game
#First version created at June 2021
#Use Python 3 to execute
#Also download pygame.

import os
from typing import Sized
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

import pgzrun
import random
WIDTH = 300
HEIGHT = 660
size = WIDTH/10
box_len = 25
box_width = 25
box_x = WIDTH/2 - size/2
cur_x=WIDTH/2
cur_y=0
pieces = []
num = 1
current_piece = []
counter = 0
fall_time = 10
cleared_rows = 0
is_game_over = False
draw_game_over = False


#list of 22 rows
rows = []

def reset_rows():
    global rows

    rows = []
    for i in range(0, 22):
    # each row is a least 10 spaces
        rows.append(0)

reset_rows()
    
def check_collision(direction=None):

    #TODO Do we need update_current in here?
    global cur_x
    if direction == 'left':     
        for box in pieces:
            for part in current_piece:
                if box.colliderect(part):
                    cur_x += size
                    update_current(False)
                    return False
    
    elif direction == 'down':
        for box in pieces:
            for part in current_piece:
                if box.colliderect(part):
                    global cur_y
                    cur_y-=size
                    update_current(False)
                    new_piece()
                    return False

    elif direction == 'right': 
        for box in pieces:
            for part in current_piece:
                if box.colliderect(part):
                    cur_x -= size
                    update_current(False)
                    return False    

    elif direction == 'rotate':
        for box in pieces:
            for part in current_piece:
                if box.colliderect(part):
                    rotate(True)
                    update_current(False)
                    return False
                if part.x < 0 or part.x >= WIDTH:
                    rotate(True)
                    update_current(False)
                    return False

    else:
        for box in pieces:
            for part in current_piece:
                if box.colliderect(part):
                    return False
    return True
   
def new_piece():
    global pieces,cur_x,cur_y,num, rows
    for block in current_piece:
        pieces.append(block)

    update_rows()
    print("making new piece and rows are: " + str(rows))

    for i in range(0,len(rows)):
        if rows[i] >= 10:
            print("found a full row, row number: " + str(i))
            clear_row(i)
            print("cleared! ")
            print(rows)
            #cleared_rows +=1
            #print("cleared row count:" + str(cleared_rows))

        # determene which row the block is in
        # index = int(block.y / size) 
        # #update the count of filled blocks in the row
        # rows[index] += 1
        # print(rows)
        # if rows[index] == 10:
        #     clear_row (index)
        #     print("cleared row!")
        #     print(rows)

    cur_x = WIDTH/2
    cur_y = 0
    num = random.randint (1,8)
    #TODO added
    update_current(True)
    
def update_rows():
    reset_rows()
    global rows, pieces
    #TODO if the row has more than 10, we should do something about that
    for index in range(0,len(rows)):
        for piece in pieces:
            if piece.y == index * size:
                rows[index] += 1

    print("rows are now: ")
    print(rows)

def clear_row(index):
    global pieces, size
    y = index * size
    new_pieces= []    

    for b in pieces:
        if b.y < y:
            b.y += size
            new_pieces.append(b)
        elif b.y == y:
            continue
        else: 
            new_pieces.append(b)

    pieces = new_pieces

    update_rows()


def move_left():
    global cur_x
    cur_x -= size
    update_current(False)
    check_collision('left')
    

def move_right():
    global cur_x
    cur_x += size
    update_current(False)
    check_collision('right')

def move_down():
    global cur_y
    cur_y += size
    update_current(False)
    check_collision('down')

def rotate(option=False):
    global cur_x, cur_y
    for block in current_piece:
        #translate to 'origin'
        ox = block.x - cur_x
        oy = block.y - cur_y

        #mapping for clockwise rotation is (x,y) --> (y, -x)
        #but since we're in computer graphics land, should be flipped (x,y) --> (-y, x)
        if not option:
            block.x = -oy
            block.y = ox
        else:
            #if option, that means we want to rotate backwards
            block.x = oy
            block.y = -ox

        #now translate back to original position
        block.x = block.x + cur_x
        block.y = block.y + cur_y
    
    #all finished, so we can update
    update_current(False)
    check_collision('rotate')

def min_x():
    smallest = 1000
    for square in current_piece:
        if square.x < smallest:
            smallest = square.x
            #print (square.x)
    return smallest

def max_x():
    biggest = -1
    for square in current_piece:
        if square.x > biggest:
            biggest = square.x
            #print (square.x)
    return biggest

def max_y():
    biggest = -1
    for square in current_piece:
        if square.y > biggest:
            biggest = square.y
            #print (square.y)
    return biggest

def end_game():
    print("game has ended")
    global is_game_over, draw_game_over
    is_game_over = True
    draw_game_over = True
    

def update_current(isnew=True):
    global num, current_piece, box_len, box_width
    #TODO update_current will only allow pieces to be drawn in their default orientation.
    #we need to update this so that the current piece blocks are just shifted
    #TODO CHANGED the 'cur_x,cur_y' piece is now always first in the list
    if isnew:
        #tbox
        if num==1:
            current_piece = [
                Rect((cur_x,cur_y),(size,size)),
                Rect((cur_x - size,cur_y),(size,size)),
                Rect((cur_x,cur_y - size),(size,size)),
                Rect((cur_x + size,cur_y),(size,size))
            ]         

        elif num == 2:
            current_piece = [
                Rect((cur_x,cur_y),(size,size))
            ]  
        
        elif num == 3:
            current_piece = [
                Rect((cur_x,cur_y),(size,size)),
                Rect((cur_x + size,cur_y),(size,size)),
                Rect((cur_x + size,cur_y - size),(size,size)),
                Rect((cur_x,cur_y - size),(size,size))
            ]    
        
        elif num == 4:
            current_piece = [
                Rect((cur_x,cur_y),(size,size)),
                Rect((cur_x - size,cur_y),(size,size)),
                Rect((cur_x + size,cur_y),(size,size)),
                Rect((cur_x + size * 2,cur_y),(size,size))
            ]

        elif num == 5:
            current_piece = [
                Rect((cur_x,cur_y),(size,size)),
                Rect((cur_x + size,cur_y),(size,size)),
                Rect((cur_x + size * 2,cur_y),(size,size)),
                Rect((cur_x + size * 2,cur_y + size),(size,size))
            ]
        
        elif num == 6:
            current_piece = [
                Rect((cur_x,cur_y),(size,size)),
                Rect((cur_x - size,cur_y),(size,size)),
                Rect((cur_x + size,cur_y),(size,size)),
                Rect((cur_x - size ,cur_y + size),(size,size))
            ]

        elif num == 7:
            current_piece = [
                Rect((cur_x,cur_y),(size,size)),
                Rect((cur_x - size,cur_y),(size,size)),
                Rect((cur_x,cur_y + size),(size,size)),
                Rect((cur_x + size ,cur_y + size ),(size,size))
                
            ]

        elif num == 8:
            current_piece = [
                Rect((cur_x,cur_y),(size,size)),
                Rect((cur_x + size,cur_y  ),(size,size)),
                Rect((cur_x + size,cur_y - size),(size,size)),
                Rect((cur_x + size * 2 ,cur_y - size),(size,size))
            ]

    else:
        delta_x = cur_x - current_piece[0].x
        delta_y = cur_y - current_piece[0].y
        for box in current_piece:
            box.x += delta_x
            box.y += delta_y


update_current(True)

def update() :
    global size
    global pieces
    global current_piece
    global cur_x,cur_y
    global num
    global counter, fall_time
    global cleared_rows
    if not is_game_over:
        if max_y() < HEIGHT - size and check_collision('down'):
            counter += 1
            if counter > fall_time:
                move_down()
                check_collision('down')
                counter = 0

            if keyboard.down and max_y() < HEIGHT - size and check_collision('down'):
                #cur_x+= -size
                clock.schedule_unique(move_down,0.05)

            if keyboard.left and min_x() > 0 and check_collision("left"):
                #cur_x+= -size
                clock.schedule_unique(move_left,0.05)
                
            if keyboard.right and max_x() <WIDTH - size and check_collision("right"):
                #cur_x+= size
                clock.schedule_unique(move_right,0.05)

            #TODO changed:
            if keyboard.up and check_collision("rotate"):
                clock.schedule_unique(rotate,0.05)
        else:
            print("here")
            cur_y -= size
            new_piece()

        update_current(False)

        for piece in pieces:
            if piece.y < 0:
                end_game()


  
    
def draw():
    global is_game_over, draw_game_over
    screen.clear()
    screen.fill((128, 50, 100))

    if not is_game_over:
        for part in current_piece:
            screen.draw.filled_rect(part,"yellow")
            screen.draw.rect(part,(0,0,0))

        for box in pieces:
            screen.draw.filled_rect(box,"yellow")
            screen.draw.rect(box,(0,0,0))
    
    else:

        for part in current_piece:
            screen.draw.filled_rect(part,"red")
            screen.draw.rect(part,(0,0,0))

        for box in pieces:
            screen.draw.filled_rect(box,"red")
            screen.draw.rect(box,(0,0,0))
          
        screen.draw.text("GAME IS OVER", (WIDTH / 2, HEIGHT / 2))
       
pgzrun.go()