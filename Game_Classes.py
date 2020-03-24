# This is it made with Classes and it works well

import pygame
pygame.mixer.music.load('audio\CarpenterBrut.mp3')
pygame.mixer.music.play(0)

pygame.init()
screen_width = 850
screen_height = 550


screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Collision Detection")

#Init variables for movement
moveX,moveY = 0,0
x,y = 0,0

# The collision detection stops working atm, won't take long to sort out
# Collision detection - takes two objects,(x,y), width and height
def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2): 
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
        return True

    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
        return True

    elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
        return True

    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
        return True

    else:
        return False

  
# Class 1
class Player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15

        # Player is now the medium sprite size to match the background size
        self.i1 = pygame.image.load("sprites/Sprite2.png")
        
        


    def draw(self,collision):
        
        if (collision == True):
            player.x -= moveX
            player.y -= moveY
            

        screen.blit(self.i1,(self.x,self.y))
      
#Class 1b:
class enemies:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20

        # Player is now the medium sprite size to match the background size
        self.i2 = pygame.image.load("Designs/zombie1.png")

    def draw(self,collision):
        if (collision == True):
            player.x -= moveX
            player.y -= moveY
            
        #render object to the screen
        screen.blit(self.i2,(self.x,self.y))
        

      
#Class 3
class Missile:
    #create missile
    def __init__(self,x,y,width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15
        speed = 0
        self.i3 = pygame.image.load('images/laser.png') 
 
    def draw(self,collision):
        
        speed +=10
        #updating position
        screen.blit(self.i3,(self.x,self.y))



bullet = Missile(5,5,moveX,moveY)   
white = (255,255,255)
black = (0,0,0)
player = Player(100,50,100,100)
#crate = draw_objects(800,100,50,50)
#jeep = draw_objects(800,350,130,120)
zombie = enemies(400,300,100,100)
points = 0
perks = []
powerups = []

    

game_state = True # inits the game state

while game_state:
    
    # inits the events the user could choose
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            game_state = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Missile(5,5,moveX,moveY)
            print ("fire.")
            pygame.mixer.music.load('audio/fire_noise.mp3')
            pygame.mixer.music.play(0)
            
        # if the user uses a keydown (presses a button) it
        # will go through this elif below:
        
        # Arrow keys or A,S,W,D first
        elif (event.type==pygame.KEYDOWN):
            
            
            
            if (event.key==pygame.K_LEFT or event.key== ord('a')):
                moveX = -30
                print ("player.x: ",player.x,"player.y:",player.y)
                
              
                
                
            elif (event.key==pygame.K_RIGHT or event.key== ord('d')):
                moveX = 30
                print ("player.x: ",player.x,"player.y:",player.y)
                
            elif (event.key==pygame.K_UP or event.key== ord('w')):
                moveY = -30
                print ("player.x: ",player.x,"player.y:",player.y)
                
                
            elif (event.key==pygame.K_DOWN or event.key== ord('s')):
                moveY = 30
                print ("player.x: ",player.x,"player.y:",player.y)
                
                
        
        # Checks to see if the user has let go of the key
        elif (event.type==pygame.KEYUP):
            if (event.key==pygame.K_LEFT or event.key== ord('a')):
                moveX = 0
            elif (event.key==pygame.K_RIGHT or event.key== ord('d')):
                moveX = 0
            elif (event.key==pygame.K_UP or event.key== ord('w')):
                moveY = 0
                
            elif (event.key==pygame.K_DOWN or event.key== ord('s')):
                moveY = 0              
    
    #loads background into memory and blits (renders) it to the screen
                
    # "Designs/setting_smaller1.png" was the original background, changed to setting2
    bg = pygame.image.load("Designs/setting2(features).png").convert()
    bg = pygame.transform.scale(bg, (screen_width, screen_height))
    screen.blit(bg, (0,0))
   
        
    pygame.display.update()
    
    # update players movement
    player.x += moveX
    player.y += moveY
    
    
    # Border Control
    if player.x > 790 or player.x < 0:
        player.x -= moveX
        
    elif player.y > 480 or player.y < 0:
        player.y -= moveY


#   Test for collisions
    collisions = detectCollisions(player.x,player.y,player.width,player.height,zombie.x,zombie.y,zombie.width,zombie.height)
    
    #parse values into the 'Player' and 'draw_objects' Class
    Player.draw(player,collisions)
    enemies.draw(zombie,collisions)
    zombie.draw(False)
    
    #The jeep
#    draw_objects.draw(jeep,collisions)
#    jeep.draw(False)
    
    

    #Inits the frame rate and the cycle clock
    FPS = 150
    clock = pygame.time.Clock()
    clock.tick(FPS)
            
    

    # Updates the screen while True in game_state
    pygame.display.flip()
pygame.quit()










