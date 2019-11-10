import pygame as pg
import sys, time
from math import *
from pygame.locals import *
from random import randint






def main(recipe_object):
    
    screen = pg.display.set_mode((1000, 640))
    font = pg.font.Font(None, 24)
    clock = pg.time.Clock()



    
    #input_box3 = pg.Rect(430, 170, 80, 300)
    color_inactive = pg.Color(128,128,128)
    color_active = pg.Color(123, 209, 212)

    
    
    rec_box = pg.Rect(80, 1800, 800, 400)


    
    back_box = pg.Rect(650, 550, 100, 30)
    back_color = color_inactive
    
    
    
    done = False


    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            
            if event.type == pg.MOUSEBUTTONDOWN:
                if back_box.collidepoint(event.pos):
                    return

                      
                    
                    

        screen.fill((255,255,255))
        # Render the current text.

        
        
        
        diff = font.render(recipe_object.getName, True, (30,30,30))
        screen.blit(diff, (40,120))


        whatever = font.render(recipe_object.getName, True, (128,128,128))  
        screen.blit(whatever, (rec_box.x+5, rec_box.y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color_active, rec_box, 2)

        
        
        pg.draw.rect(screen, back_color, back_box, 2)
        bck = font.render('Back', True, (30,30,30))
        screen.blit(bck, (back_box.x+15, back_box.y+10))
        

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
