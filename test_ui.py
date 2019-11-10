import pygame as pg
import sys, time
from math import *
from pygame.locals import *
from random import randint






def main(recipe_planner):
    screen = pg.display.set_mode((1000, 640))
    font = pg.font.Font(None, 24)
    clock = pg.time.Clock()
    input_box = pg.Rect(40, 110, 250, 32)
    
    
    
    input_box2 = []
    
    yeehaw = 0
    for n in range(10):
        input_box2.append(pg.Rect(40, 170+yeehaw, 375, 30))
        yeehaw += 30
        
        
    yeehaw2 = 0
    input_box3 = {}
    active3 = {}
    text3 = {}
    for n in range(10):
        input_box3[n] = pg.Rect(420, 170+yeehaw2, 90, 30)
        active3[n] = False
        text3[n] = ''
        yeehaw2 += 30


    break_box = pg.Rect(40, 515, 220, 30)
    lunch_box = pg.Rect(40, 550, 220, 30)
    dinn_box = pg.Rect(290, 515, 220, 30)
    snak_box = pg.Rect(290, 550, 220, 30)


    
    #input_box3 = pg.Rect(430, 170, 80, 300)
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
    
    active_butt1 = True
    active_butt2 = False
    active_butt3 = False
    active_butt4 = False
    
    col_butt1 = color_active
    col_butt2 = color_inactive
    col_butt3 = color_inactive
    col_butt4 = color_inactive
    
    
    
    diff_col_butt1 = color_inactive
    diff_col_butt2 = color_inactive
    diff_col_butt3 = color_inactive
    diff_col_butt4 = color_inactive
    diff_col_butt5 = color_inactive
    
    
    diff_box1 = pg.Rect(650, 120, 30, 30)
    diff_box2 = pg.Rect(700, 120, 30, 30)
    diff_box3 = pg.Rect(750, 120, 30, 30)
    diff_box4 = pg.Rect(800, 120, 30, 30)
    diff_box5 = pg.Rect(850, 120, 30, 30)
    
    
    
    active_diff1 = False
    active_diff2 = False
    active_diff3 = False
    active_diff4 = False
    active_diff5 = False
    
    
    
    instr_box = pg.Rect(560, 210, 385, 300)
    instr_color = color_inactive
    
    instr_text = ''
    active_instr = False
    
    
    
    submit_box = pg.Rect(850, 550, 100, 30)
    submit_color = color_active
    
    active_submit = False
    
    
    done = False
    condition_final = False

    while not done:
        for event in pg.event.get():
            if (event.type == pg.QUIT or condition_final == True):
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
                    for z in range(10):
                        active3[z] = False
                    active_instr = False
                
                
                
                elif input_box2[0].collidepoint(event.pos):
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
                    active = False
                    for z in range(10):
                        active3[z] = False
                    active_instr = False
                
                elif input_box2[1].collidepoint(event.pos):
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
                    active = False
                    for z in range(10):
                        active3[z] = False
                    active_instr = False
                
                elif input_box2[2].collidepoint(event.pos):
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
                    active = False
                    for z in range(10):
                        active3[z] = False
                    active_instr = False
                
                elif input_box2[3].collidepoint(event.pos):
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
                    active = False
                    for z in range(10):
                        active3[z] = False
                    active_instr = False
                
                elif input_box2[4].collidepoint(event.pos):
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
                    active = False
                    for z in range(10):
                        active3[z] = False
                    active_instr = False
                
                elif input_box2[5].collidepoint(event.pos):
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
                    active = False
                    for z in range(10):
                        active3[z] = False
                    active_instr = False
                
                elif input_box2[6].collidepoint(event.pos):
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
                    active = False
                    for z in range(10):
                        active3[z] = False
                    active_instr = False
                
                elif input_box2[7].collidepoint(event.pos):
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
                    active = False
                    for z in range(10):
                        active3[z] = False
                    active_instr = False
                
                elif input_box2[8].collidepoint(event.pos):
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
                    active = False
                    for z in range(10):
                        active3[z] = False
                    active_instr = False
                
                elif input_box2[9].collidepoint(event.pos):
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
                    active = False
                    for z in range(10):
                        active3[z] = False
                    active_instr = False



                elif break_box.collidepoint(event.pos):
                    active_butt1 = not active_butt1
                    active_butt2 = False
                    active_butt3 = False
                    active_butt4 = False
                    time = "Breakfast"

                elif lunch_box.collidepoint(event.pos):
                    active_butt1 = False
                    active_butt2 = not active_butt2
                    active_butt3 = False
                    active_butt4 = False
                    time = "Lunch"

                elif dinn_box.collidepoint(event.pos):
                    active_butt1 = False
                    active_butt2 = False
                    active_butt3 = not active_butt3
                    active_butt4 = False
                    time = "Dinner"

                elif snak_box.collidepoint(event.pos):
                    active_butt1 = False
                    active_butt2 = False
                    active_butt3 = False
                    active_butt4 = not active_butt4
                    time = "Snack"
                    
                    
                elif diff_box1.collidepoint(event.pos):
                    print('yeehaw')
                    active_diff1 = True
                    active_diff2 = False
                    active_diff3 = False
                    active_diff4 = False
                    active_diff5 = False
                    active_instr = False
                    score = 1
                    
                elif diff_box2.collidepoint(event.pos):
                    active_diff1 = True
                    active_diff2 = True
                    active_diff3 = False
                    active_diff4 = False
                    active_diff5 = False
                    active_instr = False
                    score = 2
                    
                elif diff_box3.collidepoint(event.pos):
                    active_diff1 = True
                    active_diff2 = True
                    active_diff3 = True
                    active_diff4 = False
                    active_diff5 = False
                    active_instr = False
                    score = 3
                
                elif diff_box4.collidepoint(event.pos):
                    active_diff1 = True
                    active_diff2 = True
                    active_diff3 = True
                    active_diff4 = True
                    active_diff5 = False
                    active_instr = False
                    score = 4
                    
                elif diff_box5.collidepoint(event.pos):
                    active_diff1 = True
                    active_diff2 = True
                    active_diff3 = True
                    active_diff4 = True
                    active_diff5 = True
                    active_instr = False
                    score = 5


                elif instr_box.collidepoint(event.pos):
                    active_instr = True
                    
                
                
                elif submit_box.collidepoint(event.pos):
                    active_submit = True


                    rec_obj = recipe_planner.makeRecipe(text, [text20,text21,text22,text23,text24,text25,text26,text27,text28,text28,text29], [text3[0],text3[1],text3[2],text3[3],text3[4],text3[5],text3[6],text3[7],text3[8],text3[9]], time, score, instr_text)




                    done = True
                    condition_final = True

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                

                else:
                    q = 0
                    condition = True
                    while condition == True:
                        if input_box3[q].collidepoint(event.pos):
                            # Toggle the active variable.
                            active3[q] = not active3[q]
                            
                            print(q)
                            
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
                            active_instr = False
                            condition = False
                    
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
                            for z in range(10):
                                active3[z] = False
                            active_instr = False
                
    
                        q += 1
                        if q == 10:
                            condition = False
                
                
                
                
                
                # Change the current color of the input box.
                color = color_active if active else color_inactive
                color2 = color_active2 if (active20 or active21 or active22 or active23 or active24 or active25 or active26 or active27 or active28 or active29) else color_inactive2
                color3 = color_active3 if (active3[0] or active3[1] or active3[2] or active3[3] or active3[4] or active3[5] or active3[6] or active3[7] or active3[8] or active3[9]) else color_inactive3
                
                col_butt1 = color_active if active_butt1 else color_inactive
                col_butt2 = color_active if active_butt2 else color_inactive
                col_butt3 = color_active if active_butt3 else color_inactive
                col_butt4 = color_active if active_butt4 else color_inactive
                
                diff_col_butt1 = color_active if active_diff1 else color_inactive
                diff_col_butt2 = color_active if active_diff2 else color_inactive
                diff_col_butt3 = color_active if active_diff3 else color_inactive
                diff_col_butt4 = color_active if active_diff4 else color_inactive
                diff_col_butt5 = color_active if active_diff5 else color_inactive
                
                instr_color = color_active if active_instr else color_inactive
                
                #print(active3)
                #print(color3)
                
                
                
            if event.type == pg.KEYDOWN:
                
                
                """
                elif active_submit:
                    done = True
                    condition_final = True
                    print('done')
                    exit()
                    
                    #
                    #
                    #
                    #
                    #
                    #
                    #
                """
                
                
                
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
                
                elif active_instr:
                    if event.key == pg.K_BACKSPACE:
                        instr_text = instr_text[:-1]
                    else:
                        instr_text += event.unicode
            
                
                
                
                
                
                else:
                    for t in range(10):

                        
                        if active3[t]:
                            if event.key == pg.K_BACKSPACE:
                                text3[t] = text3[t][:-1]
                            else:
                                text3[t] += event.unicode
                            
                      
                    
                    

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
        pg.draw.rect(screen, color2, input_box2[5], 2)
        
        
        
        #for len(text2)%
        txt_surface26 = font.render(text26, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface26, (input_box2[6].x+5, input_box2[6].y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2[6], 2)
        
        
        
        #for len(text2)%
        txt_surface27 = font.render(text27, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface27, (input_box2[7].x+5, input_box2[7].y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2[7], 2)

        
        
        #for len(text2)%
        txt_surface28 = font.render(text28, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface28, (input_box2[8].x+5, input_box2[8].y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2[8], 2)

        
        
        #for len(text2)%
        txt_surface29 = font.render(text29, True, (128,128,128))  
        
        # Blit the text.
        screen.blit(txt_surface29, (input_box2[9].x+5, input_box2[9].y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, color2, input_box2[9], 2)

        
        
        
        
        
        
        




        for u in range(10):
            #for len(text3)%
            txt_surface3 = font.render(text3[u], True, (128,128,128))
            
            
            
            # Blit the text.
            x1 = input_box3[u].x+5
            y1 = input_box3[u].y+5
            screen.blit(txt_surface3, (x1, y1))
            # Blit the input_box rect.
            pg.draw.rect(screen, color3, input_box3[u], 2)
            
        
        txt_surface3 = font.render('Amount', True, (30,30,30))
        # Blit the text.
        screen.blit(txt_surface3, (input_box3[0].x+5, input_box3[0].y-18))
        
        
        
        txt_surface4 = font.render('Time', True, (30,30,30))
        # Blit the text.
        screen.blit(txt_surface4, (40, 485))

        
        
        
        
        # buttons for time of meals
        pg.draw.rect(screen, col_butt1, break_box, 2)
        pg.draw.rect(screen, col_butt2, lunch_box, 2)
        pg.draw.rect(screen, col_butt3, dinn_box, 2)
        pg.draw.rect(screen, col_butt4, snak_box, 2)
        
        # labels for buttons
        txt_break = font.render('Breakfast', True, (30,30,30))
        screen.blit(txt_break, (break_box.x+74, break_box.y+10))
        
        txt_lunch = font.render('Lunch', True, (30,30,30))
        screen.blit(txt_lunch, (lunch_box.x+83, lunch_box.y+10))
        
        txt_dinner = font.render('Dinner', True, (30,30,30))
        screen.blit(txt_dinner, (dinn_box.x+83, dinn_box.y+10))
        
        txt_snak = font.render('Snack', True, (30,30,30))
        screen.blit(txt_snak, (snak_box.x+83, snak_box.y+10))
        
    

        diff = font.render('Difficulty', True, (30,30,30))
        screen.blit(diff, (560,80))



        # buttons for difficulty
        pg.draw.rect(screen, diff_col_butt1, diff_box1, 2)
        pg.draw.rect(screen, diff_col_butt2, diff_box2, 2)
        pg.draw.rect(screen, diff_col_butt3, diff_box3, 2)
        pg.draw.rect(screen, diff_col_butt4, diff_box4, 2)
        pg.draw.rect(screen, diff_col_butt5, diff_box5, 2)


        
        
        
        diff = font.render('Instructions', True, (30,30,30))
        screen.blit(diff, (560,180))


        whatever = font.render(instr_text, True, (128,128,128))  
        screen.blit(whatever, (instr_box.x+5, instr_box.y+5))
        # Blit the input_box rect.      
        pg.draw.rect(screen, instr_color, instr_box, 2)


        pg.draw.rect(screen, submit_color, submit_box, 2)
        sub = font.render('Submit', True, (30,30,30))
        screen.blit(sub, (submit_box.x+15, submit_box.y+10))

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
