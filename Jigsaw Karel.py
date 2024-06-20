from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""

def move_2_steps():
    for i in range(2):
        move()

def turn_right():
    for i in range(2):
        turn_left()

def move_2_wall():
    while front_is_clear():
        move()

def main():
    move_2_steps()
    pick_beeper()
    move()
    turn_left()
    move_2_steps()
    put_beeper()
    turn_right()
    move_2_wall()
    turn_left()
    turn_right()
    move_2_wall()
    turn_right()

    





# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()