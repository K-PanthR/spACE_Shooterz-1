import pgzrun
import random

WIDTH=500
HEIGHT=500
TITLE="SpACE_Shooterz"
alien=Actor("alien")
message=""
def draw():
    screen.clear()
    screen.fill(color=(146,81,81))
    alien.draw()
    screen.draw.text(message, center=(250,270), fontsize=30)

def place_alien():
    alien.x=random.randint(50,WIDTH-50)
    alien.y=random.randint(50,WIDTH-50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message="Good Shot!"
        place_alien()
    else:
        message="You Missed."

pgzrun.go()