import pyglet
from pyglet.window import key

window = pyglet.window.Window(width=600, height=600)
megaman = pyglet.resource.image('mega_man.jpg')
megaman.anchor_x = megaman.width >> 1
megaman.anchor_y = megaman.height >> 1


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr

    return start


class GameState(object):
    def __init__(self):
        self.x = window.width >> 1
        self.y = window.height >> 1
        self.count = 0

        # instantiate coroutine
        self.tick = self.tick()
        self.walk = self.walk()

    def send(self, arg):
        self.tick.send(arg)

    @coroutine
    def tick(self):
        while True:
            symbol = yield
            self.walk.send(symbol)

    @coroutine
    def walk(self):
        step = 20
        while True:
            symbol = (yield)

            if symbol == key.RIGHT:
                self.x += step if self.x < window.width else 0
                self.count += 1
            elif symbol == key.LEFT:
                self.x -= step if self.x >= 0 else 0
                self.count += 1
            elif symbol == key.UP:
                self.y += step if self.y < window.height else 0
                self.count += 1
            elif symbol == key.DOWN:
                self.y -= step if self.y >= 0 else 0
                self.count += 1



gs = GameState()
walk_count = pyglet.text.Label(str(gs.count), x=0, y=0)


@window.event
def on_key_press(symbol, modifiers):
    gs.send(symbol)


@window.event
def on_draw():
    window.clear()
    megaman.blit(gs.x, gs.y)
    walk_count.text = str(gs.count)
    walk_count.draw()


pyglet.app.run()
