from pico2d import *

open_canvas(800, 600)
charactor = load_image('character.png')


def move_circle (): 
    print('CIRCLE')
    clear_canvas()
    charactor.draw(400,300)
    update_canvas()
    pass

def move_rectangle():
    print('RECTANGLE')
    pass

def move_triangle():
    print('TRIANGLE')
    pass
while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass


close_canvas()