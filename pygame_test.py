# Example file showing a basic pygame "game loop"
import os
import pygame

#Disables audio
#os.environ["SDL_AUDIODRIVER"] = "dummy"

#Disables render
#os.environ["SDL_VIDEODRIVER"] = "dummy"

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:

    #print("test")

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(pygame.Color(100,200,200))

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, pygame.Color(0,0,0), pygame.Rect((640-(500/2)), (320-(500/2)), 500, 500), 6)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()