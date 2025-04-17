import pygame 
pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.circle(screen,(255,255,0),[100,100],30)
    pygame.draw.circle(screen,(255,255,0),[200,200],30,3)
    pygame.display.flip()