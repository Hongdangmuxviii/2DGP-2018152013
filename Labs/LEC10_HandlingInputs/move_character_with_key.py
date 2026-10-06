from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


running = True
frame = 0


close_canvas()
