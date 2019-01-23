import pygame
from random import randrange
 
MAX_STARS  = 500
STAR_SPEED = 1
 
def init_stars(screen):
  """ Create the starfield """
  global stars
  stars = []
  for i in range(MAX_STARS):
    # A star is represented as a list with this format: [X,Y]
    star = [randrange(0,screen.get_width() - 1),
            randrange(0,screen.get_height() - 1)]
    stars.append(star)
 
def move_and_draw_stars(screen):
  """ Move and draw the stars in the given screen """
  global stars
  for star in stars:
    star[1] += STAR_SPEED
    # If the star hit the bottom border then we reposition
    # it in the top of the screen with a random X coordinate.
    if star[1] >= screen.get_height():
      star[1] = 0
      star[0] = randrange(0,639)
 
    screen.set_at(star,(255,255,255))
 
def main():
  # Pygame stuff
  pygame.init()
  screen = pygame.display.set_mode((640,480))
  pygame.display.set_caption("Starfield Simulation")
  pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
  myfont = pygame.font.SysFont('Comic Sans MS', 30)
  textsurface = myfont.render('stars', False, (0, 0, 255))  
  screen.blit(textsurface,(250,250))
  pygame.display.flip()      
  clock = pygame.time.Clock()
 
  init_stars(screen)
 
  while True:
    # Lock the framerate at 50 FPS
    clock.tick(25)
 
    # Handle events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
 
    screen.fill((0,0,0))
    move_and_draw_stars(screen)
    pygame.display.flip()
 
if __name__ == "__main__":
  main()