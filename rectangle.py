import pygame 
pygame.init()

white = (255,255,255)
screen = pygame.display.set_mode((640,480))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen,(255,255,0),pygame.Rect(240,240,80,60))
    pygame.display.flip()