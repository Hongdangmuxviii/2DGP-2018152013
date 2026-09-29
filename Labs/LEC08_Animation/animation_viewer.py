from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BASE_DIR = Path(__file__).resolve().parent


def asset_path(relative_path):
    return str(BASE_DIR / relative_path)


RUN_SHEET = asset_path('assets/fox_swordswoman_run_12f.png')


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
grass = load_image(asset_path('grass.png'))
run_sheet = load_image(RUN_SHEET)
grass.draw(CANVAS_WIDTH // 2, 30)
update_canvas()
delay(1)
close_canvas()
