import pygame
from sys import exit
from F_class import Fighter


pygame.init()
clock=pygame.time.Clock()

screen_width=1000
screen_height=600


def health_bars(player,x,y):
    percent= player/100
    pygame.draw.rect(screen,(0,255,0),(x,y,percent*300,20))


screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('pixel fighter')

b_image= pygame.image.load('b_image/origbig.png').convert_alpha()
b_image_o= pygame.transform.scale(b_image,(screen_width,screen_height)).convert_alpha()

player=Fighter(200,400)
enemy= Fighter(700,400)
#Game loop

run= True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(b_image_o,(0,0))
    player.draw(screen)
    enemy.draw(screen)
    health_bars(player.percentage,20,20)
    health_bars(enemy.percentage,680,20)

    player.movement(screen_width,screen_height,screen,enemy)





    pygame.display.update()




