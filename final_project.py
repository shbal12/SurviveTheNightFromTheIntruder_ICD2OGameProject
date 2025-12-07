#Shealteile B
#Final Project - Interactive Story 
#6/5/2024

import pygame #importing pygame 
pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("The Intruder") #will come up with a better name later 
clock = pygame.time.Clock() #setting time

#will find a better icon later
icon = pygame.image.load("logo_icon.png")
pygame.display.set_icon(icon)

#setting up the colors 
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (138, 9, 189)
YELLOW = (252, 240, 3)
ORANGE = (247, 135, 15)
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
VIOLET = (100, 69, 255)
BROWN = (128, 95, 36)
GREY = (199, 196, 193)

#====game state variable (this will dictate which scene is to be shown)===== 
#will start as intro
game_state = "intro"

#========setting up the fonts to use (creating font)========== 
#for title on the introduction
font1 = pygame.font.Font('KenPixel Blocks.ttf', 40) 

#for asking the user to press keys 
font2 = pygame.font.Font('KenPixel Nova.ttf', 30)

#for narrating the story
font3 = pygame.font.Font('KenPixel High Square.ttf', 30)


#=================setting up the text=================
#===for the starting screen===
#title text
game_intro1 = font1.render("Survive the night from", True, RED)
game_intro2 = font1.render("the Intruder", True, RED)

#asking user to start
game_intro3 = font2.render("Press space to start", True, WHITE)

#===for the start of the story (pov of the user on their way home)===
pov_text1 = font3.render("- On the way home from work, listening to the news radio -", True, WHITE)
#asking user to press 'p' to listen to the news radio 
pov_text3 = font2.render("Press \"P\" to listen to the radio | ", True, WHITE)
pov_text4 = font2.render("Press \"S\" to stop | ", True, WHITE)
pov_text5 = font2.render("Press space to continue", True, WHITE)

#===for selecting an option for the first scene===
#text for narrating that the user have arrived home
first_text = font3.render("- You've arrived home -", True, WHITE)
#asking what option the user should do
choose_1 = font2.render("Choose what option to do:", True, WHITE)
#providing the options
opt1_1 = font3.render("A. Go to the bathroom", False, WHITE)
opt2_1 = font3.render("B. Relax & Watch television", False, WHITE)
#the toturial on the bottom of the screen so user would know what key to press 
tut1 = font2.render("Press A for option \"A.\" & B for option \"B.\"", True, WHITE)




#===============loading the images==============================
#for the starting bg (might change later)
start_bgimg = pygame.image.load('start_bg.jfif')
start_bgimg = pygame.transform.scale(start_bgimg, (800,600))

#for the blood graphics on the intro screen
blood_img = pygame.image.load('blood_bg.png')
blood_img = pygame.transform.scale(blood_img, (150,150))


#for the start of the game (pov on the way home) 
pov_img = pygame.image.load('pov_road.jpg')
pov_img = pygame.transform.scale(pov_img, (800,600))

#bg for their first option on what to choose (inside of the house bg)
house_bg = pygame.image.load('bg_inside.jpg')
house_bg = pygame.transform.scale(house_bg, (800,600))

#bathroom image background 
bathroom_bg = pygame.image.load('bathroom.jpg')
bathroom_bg = pygame.transform.scale(bathroom_bg,(800,600))

#watching the tv image bg
tv_bg = pygame.image.load('watching_tv.jpg')

#===========variable for the channels of the audio==========
channel1 = pygame.mixer.Channel(0) #channel for the intro audio 
channel2 = pygame.mixer.Channel(1) #channel for the news audio
channel3 = pygame.mixer.Channel(2) #channel for the bg audio 

#============sounds to use==========
#====the news audio to use====
news = pygame.mixer.Sound('news.mp3') 

#====the audio to use for the intro====
intro_audio = pygame.mixer.Sound('bg_intro.wav')
channel1.play(intro_audio, -1) #this audio will keep on playing 

#====the bg audio====
bg_audio = pygame.mixer.Sound('bg_music.wav')







done = False #vcariable for controlling if the game is done 
while not done:
    for event in pygame.event.get(): #will keep track of the event that happened and store all of the events
        if event.type == pygame.QUIT: #if the user quits
            done = True
        #handling switching screens from starting to the pov on the way home (checking if nany keys are pressed)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #will use space to control switching between screens 
                #====switch the screens (game_state) depending on the current state====
                if game_state == "intro": #switching from intro to the pov (player on the way home)
                    game_state = "pov"
                    
                elif game_state == "pov": #switching from pov to first scene 
                    game_state = "first_scene" #(where user have the opt to choose what to do) 
                
                    
            #for playing the news audio       
            if event.key == pygame.K_p and game_state == "pov": #checks if the user press p 
                if not channel2.get_busy():
                    channel2.play(news)
            if event.key == pygame.K_s or event.key == pygame.K_SPACE: #checks if the user press s or space (so audio will stop whenever they switch screen)
                pygame.mixer.pause()
                
            #for controlling what option the user picks from the first scene taking to whatever option they pick 
            if event.key == pygame.K_a and game_state == "first_scene": #here included if the game state is on first scene so pressing the A or B key would only switch when its on the first scene
                game_state = "second_scene_optA" 
            elif event.key == pygame.K_b and game_state == "first_scene":
                game_state = "second_scene_optB"            
                
                
            
                
            
    
    #filling the bg black 
    screen.fill(BLACK)
    
    #drawing scenes depending on what the condition is 
    #for starting screen 
    if game_state == "intro":
        #drawing image bg for the starting screen 
        screen.blit(start_bgimg, [0,0])
        #the title text (will change later)
        screen.blit(game_intro1, (100, 200))
        screen.blit(game_intro2, (100, 240))
        #image of blood 
        screen.blit(blood_img, [555,250])
        screen.blit(blood_img, [105,290])
        #asking user if they want to start the game 
        screen.blit(game_intro3, (340, 400))
       
        
        
        
        
        
        
        
    #for the pov on the way home 
    elif game_state == "pov":
        #the bg image 
        screen.blit(pov_img, [0,0])
        #the text saying the user is on their way home 
        screen.blit(pov_text1, (130, 500))
        #informations on what action the user can do 
        screen.blit(pov_text3, (5, 570))
        screen.blit(pov_text4, (300, 570))
        screen.blit(pov_text5, (470,570))
        
        
    #for the first scene 
    elif game_state == "first_scene":
        #the bg image
        screen.blit(house_bg, [0, 0])
        #narrating text that the player have arrived home
        screen.blit(first_text, (305,100))
        #asking what the user wants to do
        screen.blit(choose_1, (300,150))
        #providing options 
        screen.blit(opt1_1, (200,180))
        screen.blit(opt2_1, (410,180))
        #providing tutorial on what the user should press
        screen.blit(tut1, (10,570))
        
        
    #if the user chooses optA 1
    elif game_state == "second_scene_optA":
        #bathroom bg image
        screen.blit(bathroom_bg, [0,0])
        
        
    #if the user chooses optB 1
    elif game_state == "second_scene_optB":
        
        
        
        
        
        
        
               
        
    
    




    pygame.display.flip()
    clock.tick(1)
            
            
    
    

                        
pygame.quit()