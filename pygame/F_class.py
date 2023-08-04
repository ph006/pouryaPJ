import pygame

class Fighter():
    def __init__(self,x,y):
        self.rect=pygame.Rect((x,y,80,180))
        self.jump=False
        self.vel_y=0
        self.attacking=0
        self.percentage=100


    def draw(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)
    def attack(self,surface,opp):
        attack_proj=pygame.Rect(self.rect.centerx,self.rect.y,2* self.rect.width,self.rect.height)
        if attack_proj.colliderect(opp):
            opp.percentage -= 10

        pygame.draw.rect(surface,(0,255,0),attack_proj)

    def movement(self,screen_width, screen_height,surface,opp):
        speed=10
        dx=0
        dy=0
        gravity=1
        key=pygame.key.get_pressed()
        if key[pygame.K_w] and self.jump==False:
            self.vel_y= -18
            self.jump=True
        self.vel_y +=gravity
        dy += self.vel_y

        if key[pygame.K_a]:
            dx = -speed
        if key[pygame.K_d]:
            dx = speed
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 20:
            self.jump=False
            self.vel_y=0
            dy = screen_height -20 - self.rect.bottom

        #colision
        if key[pygame.K_f]:
            self.attack(surface,opp)



        self.rect.x += dx
        self.rect.y += dy


