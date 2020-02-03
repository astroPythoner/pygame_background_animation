import pygame
from pygame_background import Background
from random import randrange

width = 960
height = 680

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("moving background")

# initialize background
b1 = Background(width,height,pygame.Color(0,255,0),pygame.Color(0,0,0),pygame.Color(255,0,0),max_speed=4,connection_distance=100,connection_line_width=2)

# loop pygame
clock = pygame.time.Clock()
done = False
i = 0
while not done:
    i += 1
    if i == 1000:
        i = 0
    print(i)
    clock.tick(200)

    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # change_background
    # anzahl knoten verändern
    if i%25 == 0 and i >= 500:
        b1.set_anz_knoten(b1.get_num_knoten()+1)
    elif i%25 == 0 and i < 500:
        b1.set_anz_knoten(b1.get_num_knoten()-1)
    # größe der Knoten verändern
    if i >= 500:
        b1.set_knoten_size(int((1000-i) / 50))
    else:
        b1.set_knoten_size(int(i / 50))
    # dicke der Linien verändern
    if i >= 500:
        b1.set_line_size(int((i-500) / 50)+1)
    else:
        b1.set_line_size(int((500-i) / 50)+1)
    # länge bis zu der sich Linien verbinden veröndern
    if i == 0:
        b1.set_connection_distance(randrange(50,140))
    # set colors
    make_to_color = lambda r,g,b: pygame.Color(min([max([r,0]),255]),min([max([g,0]),255]),min([max([b,0]),255]))
    calc_color_1 = lambda i: make_to_color(0,int((255/333)*i),int((-255/333)*i+255))
    calc_color_2 = lambda i: make_to_color(int((255/333)*i),int((-255/333)*i+255),0)
    calc_color_3 = lambda i: make_to_color(int((-255/333)*i+255),0,int((255/333)*i))
    if i < 333:
        b1.set_background_color(calc_color_1(i))
        b1.set_knoten_color    (calc_color_2(i))
        b1.set_linien_color    (calc_color_3(i))
    elif i < 666:
        b1.set_background_color(calc_color_2(i-333))
        b1.set_knoten_color    (calc_color_3(i-333))
        b1.set_linien_color    (calc_color_1(i-333))
    elif i < 999:
        b1.set_background_color(calc_color_3(i-666))
        b1.set_knoten_color    (calc_color_1(i-666))
        b1.set_linien_color    (calc_color_2(i-666))

    # update background
    b1.update()
    # blit image of background on screen
    screen.blit(b1.draw(),(0,0))

    pygame.display.flip()

# Quit pygame
pygame.quit()