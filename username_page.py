import pygame
import time
pygame.init()

screen_width = 850
screen_height = 550

mouse_x,mouse_y = pygame.mouse.get_pos()

x,y = pygame.mouse.get_rel()
 
#Set Window dimensions and title
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Username Input")

#Variables for while loops
user = True
username_screen = True

def usr_scrn():
    #loads bg onto window screen
    bg = pygame.image.load("Designs/username_screen.png").convert()
    bg = pygame.transform.scale(bg, (screen_width, screen_height))
    screen.blit(bg, (0,0))
        
# Enters a loop for module of username page
while user:

    usr_scrn()    

    while username_screen:
        
        # Mouse coordinates
        event = pygame.event.poll()
        
        
        #exit game
        if event.type == pygame.QUIT:
            exit()
        
        # debugging test
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            
            
            
            #Username input field clicked - enter username in terminal.
            
            # (x) top left, (x) top right, (y) top left, (y) bottom right
            if (x) > 245 and (x) < 600 and (y) > 238 and (y) < 262:
                
                valid = False
                
                while valid == False:
 
                    username = input("Username: ")
                    
                    #array stores invalid chars
                    array = ["@","#","|","<",">","?","[","]"]
                    
                    #length check
                    if len(username) > 1 and len(username) <15:
                        
                        #takes each letter in turn - checks if invalid
                        for i in array:
                            if i in username:
                                print ("invalid username - must be a string.")
                                valid = False
                                break
                    
                            if i not in username:
                                print ("Valid Username.")
                                valid = True
                                break
                            break
                        
                 
     
                    else:
                        print ("Username must be between 1 and 15 chars.")

                
            # if 'Play' button is pressed
            elif (x) > 359 and (x) < 489 and (y) > 318 and (y) < 365:
                print ("play")
                pygame.mixer.music.fadeout(1500)
              
                import Game_Classes

            
            
                
            
        pygame.display.update()

    
    clock = pygame.time.Clock()
    clock.tick(70)
            

    pygame.display.flip()
pygame.quit()
