import pygame
from sys import exit

pygame.init()

#variables:
screen = pygame.display.set_mode((626, 327))
pygame.display.set_caption('Meow Jump')
clock = pygame.time.Clock()
back_surf = pygame.image.load('FINAL PROJECT/background.png')

#Score Variables:
font_text = pygame.font.Font('FINAL PROJECT/slkscreb.ttf', 40)
score_text = font_text.render('0', False, 'white')
score_rect = score_text.get_rect(center = (313, 50))

#Player Variables:
player_surf = pygame.image.load('FINAL PROJECT/meow_run_frame_1_2x_nobg.png')
player_rect = player_surf.get_rect(midbottom = (100, 272),)

#Well Variable (enemy):
well_surf = pygame.image.load('FINAL PROJECT/15.png')
well_rect = well_surf.get_rect(midright = (626,229))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    
#Background:
    screen.blit(back_surf,(0,0))

#Score:
    screen.blit(score_text, score_rect)

#Player:
    screen.blit(player_surf, player_rect)
    
#Well:
    well_rect.x -= 3
    if well_rect.right <= 0: well_rect.left = 750
    screen.blit(well_surf, well_rect)

#Collision:
    if player_rect.colliderect(well_rect):
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)
