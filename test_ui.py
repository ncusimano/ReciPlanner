import pygame as pg
import sys, time
from math import *
from pygame.locals import *
from random import randint






def main():
    screen = pg.display.set_mode((1000, 640))
    font = pg.font.Font(None, 24)
    clock = pg.time.Clock()
    input_box = pg.Rect(40, 110, 250, 32)
    
    
    
    input_box2 = [input_box20,input_box21,input_box22,input_box23,input_box24,input_box25,input_box26,input_box27,input_box28,input_box29]
    
    yeehaw = 0
    for n in input_box2:
        n = pg.Rect(40, 170+yeehaw, 375, 300)
        yeehaw += 31
    
    
    input_box3 = pg.Rect(430, 170, 80, 300)
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
    
    active20 = False
    active21 = False
    active22 = False
    active23 = False
    active24 = False
    active25 = False
    active26 = False
    active27 = False
    active28 = False
    active29 = False
    
    
    active3 = False
    text = ''
    
    text20 = ''
    text21 = ''
    text22 = ''
    text23 = ''
    text24 = ''
    text25 = ''
    text26 = ''
    text27 = ''
    text28 = ''
    text29 = ''
    
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
                    active20 = False
                    active21 = False
                    active22 = False
                    active23 = False
                    active24 = False
                    active25 = False
                    active26 = False
                    active27 = False
                    active28 = False
                    active29 = False
                    active3 = False
                
                
                
                elif input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active20 = not active20
                    active21 = False
                    active22 = False
                    active23 = False
                    active24 = False
                    active25 = False
                    active26 = False
                    active27 = False
                    active28 = False
                    active29 = False
                
                elif input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active21 = not active21
                    active20 = False
                    active22 = False
                    active23 = False
                    active24 = False
                    active25 = False
                    active26 = False
                    active27 = False
                    active28 = False
                    active29 = False
                
                elif input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active22 = not active22
                    active20 = False
                    active21 = False
                    active23 = False
                    active24 = False
                    active25 = False
                    active26 = False
                    active27 = False
                    active28 = False
                    active29 = False
                
                elif input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active23 = not active23
                    active20 = False
                    active21 = False
                    active22 = False
                    active24 = False
                    active25 = False
                    active26 = False
                    active27 = False
                    active28 = False
                    active29 = False
                
                elif input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active24 = not active24
                    active20 = False
                    active21 = False
                    active22 = False
                    active23 = False
                    active25 = False
                    active26 = False
                    active27 = False
                    active28 = False
                    active29 = False
                
                elif input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active25 = not active25
                    active20 = False
                    active21 = False
                    active22 = False
                    active23 = False
                    active24 = False
                    active26 = False
                    active27 = False
                    active28 = False
                    active29 = False
                
                elif input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active26 = not active26
                    active20 = False
                    active21 = False
                    active22 = False
                    active23 = False
                    active24 = False
                    active25 = False
                    active27 = False
                    active28 = False
                    active29 = False
                
                elif input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active27 = not active27
                    active20 = False
                    active21 = False
                    active22 = False
                    active23 = False
                    active24 = False
                    active25 = False
                    active26 = False
                    active28 = False
                    active29 = False
                
                elif input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active28 = not active28
                    active20 = False
                    active21 = False
                    active22 = False
                    active23 = False
                    active24 = False
                    active25 = False
                    active26 = False
                    active27 = False
                    active29 = False
                
                elif input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active29 = not active29
                    active20 = False
                    active21 = False
                    active22 = False
                    active23 = False
                    active24 = False
                    active25 = False
                    active26 = False
                    active27 = False
                    active28 = False

                
                
                elif input_box3.collidepoint(event.pos):
                    # Toggle the active variable.
                    active3 = not active3
                    active = False
                    active20 = False
                    active21 = False
                    active22 = False
                    active23 = False
                    active24 = False
                    active25 = False
                    active26 = False
                    active27 = False
                    active28 = False
                    active29 = False
                
                else:
                    active = False
                    active20 = False
                    active21 = False
                    active22 = False
                    active23 = False
                    active24 = False
                    active25 = False
                    active26 = False
                    active27 = False
                    active28 = False
                    active29 = False
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
                            
                
                elif active20:
                    if event.key == pg.K_BACKSPACE:
                        text20 = text20[:-1]
                    else:
                        text20 += event.unicode
                
                elif active21:
                    if event.key == pg.K_BACKSPACE:
                        text21 = text21[:-1]
                    else:
                        text21 += event.unicode
                        
                elif active22:
                    if event.key == pg.K_BACKSPACE:
                        text22 = text22[:-1]
                    else:
                        text22 += event.unicode
                
                elif active23:
                    if event.key == pg.K_BACKSPACE:
                        text23 = text23[:-1]
                    else:
                        text23 += event.unicode
                
                elif active24:
                    if event.key == pg.K_BACKSPACE:
                        text24 = text24[:-1]
                    else:
                        text24 += event.unicode
                        
                elif active25:
                    if event.key == pg.K_BACKSPACE:
                        text25 = text25[:-1]
                    else:
                        text25 += event.unicode
                
                elif active26:
                    if event.key == pg.K_BACKSPACE:
                        text26 = text26[:-1]
                    else:
                        text26 += event.unicode
                        
                elif active27:
                    if event.key == pg.K_BACKSPACE:
                        text27 = text27[:-1]
                    else:
                        text27 += event.unicode
                
                elif active28:
                    if event.key == pg.K_BACKSPACE:
                        text28 = text28[:-1]
                    else:
                        text28 += event.unicode
                
                elif active29:
                    if event.key == pg.K_BACKSPACE:
                        text29 = text29[:-1]
                    else:
                        text29 += event.unicode
                
                
                
                
                
                
                elif active3:
                    if event.key == pg.K_BACKSPACE:
                        text3 = text3[:-1]
                    else:
                        text3 += event.unicode
                    
                    
                    
                    
                    

        screen.fill((255,255,255))
        # Render the current text.
        
        
        
        
        txt_surface = font.render(text, True, (128,128,128))
        
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        
        
        txt_surface = font.render('Recipe Name', True, (30,30,30))
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y-18))
        
        
        
        
        
        
        
        """
        try:
            curr_text = [text[i:i+10] for i in range(0, len(text), 10)]
        except:
            pass
        
        for l in curr_text:
        """
        
        
        
        #for len(text2)%
        txt_surface20 = font.render(text20, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface20, (input_box2[0].x+5, input_box2[0].y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2[0], 2)
        
        
        
        txt_surface20 = font.render('Ingredients', True, (30,30,30))
        # Blit the text.
        screen.blit(txt_surface20, (input_box2[0].x+5, input_box2[0].y-18))
        
        
        
        
        #for len(text2)%
        txt_surface21 = font.render(text21, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface21, (input_box2[1].x+5, input_box2[1].y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2[1], 2)
        
        
        
        #for len(text2)%
        txt_surface22 = font.render(text22, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface22, (input_box2[2].x+5, input_box2[2].y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2[2], 2)
        
        
        
        #for len(text2)%
        txt_surface23 = font.render(text23, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface23, (input_box2[3].x+5, input_box2[3].y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2[3], 2)



        #for len(text2)%
        txt_surface24 = font.render(text24, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface24, (input_box2[4].x+5, input_box2[4].y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2[4], 2)
        
        
        
        #for len(text2)%
        txt_surface25 = font.render(text25, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface25, (input_box2[5].x+5, input_box2[5].y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2, 2)
        
        
        
        #for len(text2)%
        txt_surface2 = font.render(text2, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2, 2)
        
        
        
        #for len(text2)%
        txt_surface2 = font.render(text2, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2, 2)

        
        
        #for len(text2)%
        txt_surface2 = font.render(text2, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2, 2)

        
        
        #for len(text2)%
        txt_surface2 = font.render(text2, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2, 2)

        
        
        
        
        
        
        





        #for len(text3)%
        txt_surface3 = font.render(text3, True, (128,128,128))
        
        # Blit the text.
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color3, input_box3, 2)
        
        
        txt_surface3 = font.render('Amount', True, (30,30,30))
        # Blit the text.
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y-18))





        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
