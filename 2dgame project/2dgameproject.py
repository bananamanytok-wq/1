
import sys

import pygame


red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
rect2 = pygame.rect.Rect(100,0,100,100)
sum = ""
pygame.init()
screen = pygame.display.set_mode((1800,1000))
pygame.display.set_caption("2d game")
rect1 = pygame.rect.Rect(0,0,100,100)
text_font = pygame.font.SysFont("Arial", 20)
rect1color = white
close = text_font.render("X", True, black)
rect2color = white
clock = pygame.time.Clock()
changex = 0
changey = 0

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self,width,height,start_x,start_y,color):
        super().__init__()

        self.image = pygame.image.load("tyoma idle and movement1.jpg").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

    def update(self):
        self.rect.x += changex
        self.rect.y += changey

all_sprites = pygame.sprite.Group()
udin = PlayerSprite(200,200,900,500,(red))

all_sprites.add(udin)



while True:
    display =text_font.render(sum, True, white)
    screen.fill(black)
    keys = pygame.key.get_pressed()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if rect1.collidepoint(pygame.mouse.get_pos()):
            rect1color = gray
        else:
            rect1color = white
        if rect1.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()
        if rect2.collidepoint(pygame.mouse.get_pos()) and pygame.MOUSEBUTTONDOWN:
            sum += "1"
        if rect2.collidepoint(pygame.mouse.get_pos()) :
            rect2color = gray
        else:
            rect2color = white
    if keys[pygame.K_w]:
        changey = -5
    elif keys[pygame.K_s]:
        changey = 5
    else:
        changey = 0
    if keys[pygame.K_a]:
        changex = -5
    elif keys[pygame.K_d]:
        changex = 5
    else:
        changex = 0

    y = pygame.draw.rect(screen,(rect2color),rect2)
    x = pygame.draw.rect(screen, (rect1color), rect1)
    screen.blit(close, (50,50))

    all_sprites.update()
    all_sprites.draw(screen)
    screen.blit(display,(200,200))
    clock.tick(60)
    pygame.display.flip()
