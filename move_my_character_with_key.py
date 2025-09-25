from pico2d import *
from enum import Enum


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')


class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3
    NONE = 4

class Character:
    def __init__(self):
        self.x, self.y = TUK_WIDTH // 2, TUK_HEIGHT // 2
        self.dir = Direction.NONE
        self.speed = 10
        self.animation_image = load_image('animation_sheet.png')
        self.frame = 8

player = Character()
running = True

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False



while True:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    update_canvas()

    handle_events()
    if not running:
        break


