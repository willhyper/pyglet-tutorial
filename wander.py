import pyglet
from pyglet.window import key

window = pyglet.window.Window(width=600, height=600)
megaman = pyglet.resource.image('mega_man.jpg')
megaman.anchor_x = megaman.width >> 1
megaman.anchor_y = megaman.height >> 1


class GameState(object):
    def __init__(self):
        self.x = window.width >> 1
        self.y = window.height >> 1
        self.walk_count = 0

gs = GameState()
score_label = pyglet.text.Label(str(gs.walk_count),x=0,y=0)

@window.event
def on_key_press(symbol, modifiers):
    step = 20

    if symbol == key.RIGHT:
        gs.x += step if gs.x < window.width else 0
    elif symbol == key.LEFT:
        gs.x -= step if gs.x >= 0 else 0
    elif symbol == key.UP:
        gs.y += step if gs.y < window.height else 0
    elif symbol == key.DOWN:
        gs.y -= step if gs.y >= 0 else 0

    gs.walk_count += 1

@window.event
def on_draw():
    window.clear()
    megaman.blit(gs.x, gs.y)
    score_label.text = str(gs.walk_count)
    score_label.draw()

pyglet.app.run()
