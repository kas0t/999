from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load("background.png"), (700, 500))

x1 = 100
y2 = 300

x2 = 300
y2 = 300    

sp1 = transform.scale(image.load('sprite1.png'), (100, 100))
sp1 = transform.scale(image.load('sprite2.png'), (100, 100))
speed = 10

game = True
clock = time.Clock()
FPS = 60

while game:
    window.blit(background, (0,0))
    window.blit(sp1, (x1, y2))
    window.blit(sp2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_LEFT] and x1 < 5:
        y1 += speed

    
    
    display.update()
