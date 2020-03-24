import pygame
import time
pygame.init()

# Menu Music
pygame.mixer.music.load('audio\HeavenFalls.mp3')
pygame.mixer.music.play(0)


# Back button works but glithes the screen again

screen_width = 850
screen_height = 550

mouse_x,mouse_y = pygame.mouse.get_pos()

x,y = pygame.mouse.get_rel()
 
#Set Window dimensions and title
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("The Menu")

menu_state = True
choices = True
choices2 = True
black = (0,0,0)

def menu():
    bg = pygame.image.load("Designs/Menu_design.png").convert()
    bg = pygame.transform.scale(bg, (screen_width, screen_height))
    screen.blit(bg, (0,0))
    
def instructions():
    bg = pygame.image.load("Designs/peripheral1.png").convert()
    bg = pygame.transform.scale(bg, (screen_width, screen_height))
    screen.blit(bg, (0,0))
    
def help_page():
    bg = pygame.image.load("Designs/help_page.png").convert()
    bg = pygame.transform.scale(bg, (screen_width, screen_height))
    screen.blit(bg, (0,0))
    
def overview():
    bg = pygame.image.load("Designs/overview.png").convert()
    bg = pygame.transform.scale(bg, (screen_width, screen_height))
    screen.blit(bg, (0,0))


while menu_state:

    menu()    

    while choices:
        
        # Mouse coordinates
        event = pygame.event.poll()
        
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            print (x,y)
            

            # (x) top left, (x) top right, (y) top left, (y) bottom right
            if (x) > 186 and (x) < 373 and (y) > 158 and (y) < 230:
                print ("play game")
                import username_page
                
                
            elif (x) > 480 and (x) < 664 and (y) > 160 and (y) < 233:
                print ("Help")
                help_page()
            
            elif (x) > 186 and (x) < 371 and (y) > 284 and (y) < 356:
                print ("Instructions")
                screen.fill(black)
                instructions()
            
            elif (x) > 479 and (x) < 664 and (y) > 284 and (y) < 356:
                print ("Overview")
                overview()
                
            elif (x) > 698 and (x) < 839 and (y) > 462 and (y) < 520:
                print ("back")
                screen.fill(black)
                menu()

            elif (x) > 332 and (x) < 518 and (y) > 408 and (y) < 480:
                print ("Exit")
                exit()
            
        pygame.display.update()

    
    clock = pygame.time.Clock()
    clock.tick(70)
            
    


    pygame.display.flip()
pygame.quit()










