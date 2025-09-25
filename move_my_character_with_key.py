from pico2d import *
from enum import Enum

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')




while True:
   tuk_ground.draw_now(TUK_WIDTH // 2, TUK_HEIGHT // 2)
   pass


close_canvas()