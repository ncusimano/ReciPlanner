import pygame as pg
import sys, time
from math import *
from pygame.locals import *
from random import randint






def main():
    screen = pg.display.set_mode((1000, 640))
    font = pg.font.Font(None, 24)
    clock = pg.time.Clock()
    input_box = pg.Rect(40, 110, 140, 32)
    input_box2 = pg.Rect(40, 170, 200, 300)
    input_box3 = pg.Rect(250, 170, 50, 300)
    color_inactive = pg.Color(128,128,128)
    color_active = pg.Color(123, 209, 212)
    color = color_inactive
    
    color_inactive2 = pg.Color(128,128,128)
    color_active2 = pg.Color(123, 209, 212)
    color2 = color_inactive
    
    color_inactive3 = pg.Color(128,128,128)
    color_active3 = pg.Color(123, 209, 212)
    color3 = color_inactive3
    
    #spacing_count1 = 0
    #spacing_count2 = 0
    
    
    active = False
    active2 = False
    active3 = False
    text = ''
    text2 = ''
    text3 = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                    active2 = False
                    active3 = False
                elif input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active2 = not active2
                    active = False
                    active3 = False
                elif input_box3.collidepoint(event.pos):
                    # Toggle the active variable.
                    active3 = not active3
                    active = False
                    active2 = False
                else:
                    active = False
                    active2 = False
                    active3 = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
                color2 = color_active2 if active2 else color_inactive2
                color3 = color_active3 if active3 else color_inactive3
                
                
            if event.type == pg.KEYDOWN:
                if active:
                    #if event.key == pg.K_RETURN:
                        #print(text)
                        #text = ''
                    if event.key == pg.K_BACKSPACE:
                        text = text[:-1]

                    else:
                        text += event.unicode
                            
                
                elif active2:
                    if event.key == pg.K_BACKSPACE:
                        text2 = text2[:-1]
                    else:
                        text2 += event.unicode
                        
                elif active3:
                    if event.key == pg.K_BACKSPACE:
                        text3 = text3[:-1]
                    else:
                        text3 += event.unicode
                    
                    
                    
                    
                    

        screen.fill((255,255,255))
        # Render the current text.
        txt_surface = font.render(text, True, (128,128,128))
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        
        
        txt_surface = font.render('Recipe Name', True, (30,30,30))
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y-18))
        
        
        
        #for len(text2)%
        txt_surface2 = font.render(text2, True, (128,128,128))
        
        
        # Resize the box if the text is too long.
        width2 = max(250, txt_surface2.get_width()+40)
        input_box2.w = width2
        # Blit the text.
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color2, input_box2, 2)
        
        
        txt_surface2 = font.render('Ingredients', True, (30,30,30))
        # Resize the box if the text is too long.
        width2 = max(200, txt_surface2.get_width()+10)
        input_box2.w = width2
        # Blit the text.
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y-18))


        #for len(text3)%
        txt_surface3 = font.render(text2, True, (128,128,128))
        
        
        # Resize the box if the text is too long.
        width3 = max(250, txt_surface3.get_width()+40)
        input_box3.w = width3
        # Blit the text.
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color3, input_box3, 2)
        
        
        txt_surface3 = font.render('Ingredients', True, (30,30,30))
        # Resize the box if the text is too long.
        width3 = max(200, txt_surface3.get_width()+10)
        input_box3.w = width3
        # Blit the text.
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y-18))




        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
