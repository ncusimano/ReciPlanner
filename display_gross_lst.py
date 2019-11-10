import pygame as pg
import sys, time
from math import *
from pygame.locals import *
from random import randint






def main(gross_object):
    
    screen = pg.display.set_mode((1000, 640))
    font = pg.font.Font(None, 28)
    clock = pg.time.Clock()



    
    #input_box3 = pg.Rect(430, 170, 80, 300)
    color_inactive = pg.Color(128,128,128)
    color_active = pg.Color(123, 209, 212)

    
    
    rec_box = pg.Rect(80, 180, 800, 350)


    
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

        
        
        
        diff = font.render("Grocery List", True, (30,30,30))
        screen.blit(diff, (40,120))


        dict_gross = gross_object.getDict()

        for i in dict_gross:
            
            whatever = font.render(i, True,  (40,40,40))  
            screen.blit(whatever, (rec_box.x+5, rec_box.y+5+30*i))
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
