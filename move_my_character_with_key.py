from pico2d import *
from enum import Enum


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')


#방향 enum 클래스
class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3
    LEFT_to_NONE = 4
    RIGHT_to_NONE = 5

class Character:
    def __init__(self):
        self.x, self.y = TUK_WIDTH // 2, TUK_HEIGHT // 2
        self.dir = Direction.RIGHT_to_NONE
        self.speed = 10
        self.animation_image = load_image('animation_sheet.png')
        self.frame = 8
        self.image_size = 150
    def update(self):
        print('update')
        self.frame = (self.frame + 1) % 8
    def render(self):
        self.animation_image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y, self.image_size, self.image_size)
        delay(0.016)


player = Character()
running = True

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        #key down 처리
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                player.dir = Direction.RIGHT
            elif event.key == SDLK_LEFT:
                player.dir = Direction.LEFT
            elif event.key == SDLK_UP:
                player.dir = Direction.UP
            elif event.key == SDLK_DOWN:
                player.dir = Direction.DOWN
        #key up 처리
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT and player.dir == Direction.RIGHT:
                player.dir = Direction.RIGHT_to_NONE
            elif event.key == SDLK_LEFT and player.dir == Direction.LEFT:
                player.dir = Direction.LEFT_to_NONE
            elif event.key == SDLK_UP and player.dir == Direction.UP:
                player.dir = Direction.RIGHT_to_NONE
            elif event.key == SDLK_DOWN and player.dir == Direction.DOWN:
                player.dir = Direction.LEFT_to_NONE






while True:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    player.update()
    player.render()
    update_canvas()

    handle_events()
    if not running:
        break
