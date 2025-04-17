import pygame 
pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # if event.type == pygame.KEYDOWN:
        #     print("A key was pressed")
        if event.key == pygame.K_UP:
            print("Up arrow key pressed")
        elif event.key == pygame.K_DOWN:
            print("down arrow key pressed")
        elif event.key == pygame.K_RIGHT:
            print("Right arrow key pressed")
        elif event.key == pygame.K_LEFT:
            print("Left arrow key pressed")
        # else:
        #     print("Other keys were pressed")
    pygame.display.flip()