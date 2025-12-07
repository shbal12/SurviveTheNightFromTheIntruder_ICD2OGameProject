#Shealteile B
#6/5/2024
#Final Project - Interactive Story - player tries to survive from the intruder that escaped from prison and is now breaking in their house
#======================ENHANCEMENTS=========================================
#included an ASCII graphic text - 0.5
#used a custom program icon - 0.5
#used timer - 0.5
#added a sound (using channel method + knowing how to add more channels) - 1
#mouse & keyboard input - 1
#used list (listing all the actions that the user does?) - 1
#functions - adding strings together? - 1
#custom fonts
#gave my story a visual aspects - 2




import pygame #importing pygame 
import random #for the luck and tracking the stats
pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("The Intruder") #the project name
clock = pygame.time.Clock() #setting time

#===========for the timer===========
#on 0 for default 
current_time = 0 
button_press_time = 0 

#icon of the game
icon = pygame.image.load("logo_icon.png") #(from karisha)
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
DESCP = (161, 44, 35)

#============luck for knife=============
luck = random.randrange(10)
#=======player don't have knife yet so variable is set to false=======
knife = False #this is to check the inventory of the player if they have knife
if luck == 5:
    knife = True

#===========fear stat=========
fear = 10 #fear starts on 10
fear_limit = 100 #the limit (player will go insane because of fear)

#luck for gun ending
luck_gun = random.randrange(1,10)


#================for rectangle==============
x = 0 #x-pos variable of the rectangles (for the animation of text disappearing and reappearing)
#===================================================================


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

font4 = pygame.font.Font('KenPixel Blocks.ttf', 100) #font for the game over/you win


#=================setting up the text=================
#===for the starting screen===
#title text
game_intro1 = font1.render("Survive the night from", False, DESCP)
game_intro2 = font1.render("the Intruder", True, DESCP)

#asking user to start
game_intro3 = font2.render("Press space to start", True, WHITE)

#===for the start of the story (pov of the user on their way home)===
pov_text1 = font3.render("- On the way home from work, listening to the news radio -", True, WHITE)
#asking user to press 'p' to listen to the news radio 
pov_text3 = font2.render("Press \"P\" to listen to the radio | ", True, WHITE)
pov_text4 = font2.render("Press \"S\" to stop | ", True, WHITE)

#text to tell the user pressing space allows them continue
space_text = font2.render("Press space to continue", True, WHITE)

#===for selecting an option for the first scene===
#text for narrating that the user have arrived home
first_text = font3.render("- You've arrived home -", True, WHITE)

#==========asking what option the user should do=============
choose_1 = font2.render("Choose what option to do:", True, WHITE)

#providing the options
opt1_1 = font2.render("A. Go to the bathroom", False, WHITE)
opt2_1 = font2.render("B. Relax & Watch television", False, WHITE)
#the toturial on the bottom of the screen so user would know what key to press + if thy want to eat 
tut1 = font2.render("Press A for option \"A.\" & B for option \"B.\" | Click screen to calm yourself.", True, WHITE)

#for the option A 1
#describing what the player is doing in the bathroom 
optA_1 = font3.render("- In the bathroom doing your business -", False, WHITE)


#for option B 1
#describing that the player is watching the television
optB_1 = font3.render("- Watching the telivision & relaxing -", False, WHITE)


#when the power goes out 
power_text = font3.render("- Power goes out -", True, WHITE)

#hear the glass break description
glass_text = font3.render("- You hear the window glass break -", True, WHITE)

#providing options for the user 
#both have same opt
optA_2 = font2.render("A. Grab your phone left in the car & call for help", False, WHITE)

#diff opt for A
optA_3 = font2.render("B. Stay where you are", False, WHITE)

#diff opt for B
optB_3 = font2.render("B. Go to the bathroom & hide as fast as you can", False, WHITE)

#the scene description for when (the player goes to the car to grab their device) (applys for optA & B 1)
car_text = font3.render("- On your way to your car to grab your phone -", False, WHITE)

#the text description that the player hear objects crashing coming inside from their house and that indicates that someone is in their house (applies for the scene where the player goes outside)
crash_noise = font3.render("- You hear noises coming from your house -", False, WHITE)
#the text for when the user thought that it's better to not come back inside 
text_noise = font3.render("\"It's better to not come back inside to be safe.\"", False, WHITE)
#text option of where the user would like to go now from car to...
optA_4 = font2.render("A. Run", False, WHITE)
optB_4 = font2.render("B. Get in your car and drive away", False, WHITE)

#text description (player chooses to stay in the bathroom)
noise2 = font3.render("- You hear someone walking & looking for you -", False, WHITE)
#user thinking its not safe to stay in the house (description)
text_noise2 = font3.render("\"It's not safe to stay in here.\"",False, WHITE)

#text option of where the user would like to go now from staying in the bathroom..(hunger would be consumed too so will add description about that later on)
optA_5 = font2.render("A. Go to the kitchen to find something that might be helpful", False, WHITE)
optB_5 = font2.render("B. Rummage through the drawers to find something that might help", False, WHITE)

#text description for when the user chooses to run scene and come across a police
run_text = font3.render("- Running -", False, WHITE)
police_text = font3.render("-You see an officer & approach them -", False, WHITE)
#text description of the player telling the officer that they need help because there's an intruder in the house 
help_text = font3.render("\"Officer someone is in my house\"", False, WHITE)

#text description for when the user chooses to drive their car
car_ending_text = font3.render("- Driving away thinking that you're safe -", False, WHITE)

#=============for string method==================================================
#will add a "game over" displaying string by string (if player loses)
#if player wins will add a "you win" also string by string
fear_text1 = ("-You need to calm yourself!"* 5).upper()


#=====description if the player's fear go up to 80 ==================
fear_opt = font2.render(fear_text1, False, YELLOW)
#================================================================================

#description if the player found knife (depends on luck if knife = True )
found_knife = font2.render("You found a knife. =={====- ", False, WHITE) #from ascii art
#description when (knife = False)
knife_text2 = font2.render("The knife is not here anymore.", False, WHITE)

#description telling the user if they choose to eat and don't have food 
no_food = font2.render("You don't have food.", False, WHITE)

#description saying that the player is rummaging through the drawer 
rummage = font3.render("- Rummaging through the drawers -", False, WHITE)
#description that the player found a gun 
gun_text1 = font3.render("- You found a gun -", False, WHITE)

#text description for when the fear reaches above 100 or more than(fear ending)
fear_ending = font2.render("Due to intense fear you had a panic attack.", False, DESCP)

#text description for police ending
police_ending1 = font2.render("The police team searched your house and found the killer.", False, GREEN)

#for car ending
car_ending1 = font2.render("The killer messed up with the brakes of your car.", False, DESCP)
car_ending2 = font3.render("- You crashed -", False, WHITE)

#for drawer ending 
drawer_ending1 = font2.render("You shot the killer first.", False, GREEN) #win
drawer_ending2 = font2.render("You were too slow the killer got you first.", False, DESCP) #lose

#for kitchen ending text
kitchen_ending1 = font2.render("You stabbed the killer to defend yourself.", False, GREEN)#win
kitchen_ending2 = font2.render("The killer have the knife & stabbed you with it.", False, DESCP)#lose

#for the end of the game description game over/ you win
game_over = font4.render("Game Over", False, DESCP)
you_win = font4.render("You  Win!!", False, GREEN)
#==============================================================

#===============loading the images==============================
#for the starting bg (might change later)
start_bgimg = pygame.image.load('start_bg.jfif')
start_bgimg = pygame.transform.scale(start_bgimg, (800,600))

#for the blood graphics on the intro screen
blood_img = pygame.image.load('blood_bg.png')
blood_img = pygame.transform.scale(blood_img, (150,150))


#for the start of the game (pov on the way home) 
pov_img = pygame.image.load('pov.jpg')
pov_img = pygame.transform.scale(pov_img, (800,600))

#bg for their first option on what to choose (inside of the house bg)
house_bg = pygame.image.load('bg_inside.jpg')
house_bg = pygame.transform.scale(house_bg, (800,600))

#bathroom image background 
bathroom_bg = pygame.image.load('bathroom.jpg')
bathroom_bg = pygame.transform.scale(bathroom_bg,(800,600))

#watching the tv image bg
tv_bg = pygame.image.load('watching_tv.jpg')
tv_bg = pygame.transform.scale(tv_bg, (800,600))

#bg image of car (for scene when the user needs to go grab their phone)
car_bg = pygame.image.load('car.png')
car_bg = pygame.transform.scale(car_bg, (800, 600))

#image of the bathroom  bg (darker this time because the power is out)
bathroom_bg2 = pygame.image.load('bathroom_dark.png')
bathroom_bg2 = pygame.transform.scale(bathroom_bg2,(800, 600))

#image for the one ending where the player comes across a police and seek for help
police_ending = pygame.image.load('police.jpg')
police_ending = pygame.transform.scale(police_ending, (800, 600))

#image for the run scene
run_image = pygame.image.load('run.webp')
run_image = pygame.transform.scale(run_image, (800, 600))

#image for the scene where user choose to get in their car
car2 = pygame.image.load('car2.jpg')
car2 = pygame.transform.scale(car2, (800, 600))

#ending scene for car
car3 = pygame.image.load('light_car.webp')
car3 = pygame.transform.scale(car3, (800, 600))

#kitchen scene image 
kitchen_img = pygame.image.load('kitchen.png')
kitchen_img = pygame.transform.scale(kitchen_img, (800, 600))

#drawer scene image
drawer_img = pygame.image.load('drawer.png')
drawer_img = pygame.transform.scale(drawer_img, (800, 600))
#adding more channels because the default is limited to only 8 (learned from a link from stackoverflow)
pygame.mixer.set_num_channels(20)


#===========variable for the channels of the audio========== (learned this method from stackoverflow, all sound methods are learned from the stackoverflow)
channel1 = pygame.mixer.Channel(0) #channel for the intro audio 
channel2 = pygame.mixer.Channel(1) #channel for the news audio
channel3 = pygame.mixer.Channel(2) #channel for the bg audio 
channel4 = pygame.mixer.Channel(3) #glass window shattering
channel5 = pygame.mixer.Channel(4) #for the object crash noises 
channel6 = pygame.mixer.Channel(5) #for the running sound audio 
channel7 = pygame.mixer.Channel(6) #for the someone walking audio
channel8 = pygame.mixer.Channel(7) #for where are you audio 
channel9 = pygame.mixer.Channel(8) #for the car driving audio
channel10 = pygame.mixer.Channel(9) #for the car crashing audio 
channel11 = pygame.mixer.Channel(10) #for game over audio 
channel12 = pygame.mixer.Channel(11) #for you win audio 


#============sounds to use==========
#====the news audio to use====
news = pygame.mixer.Sound('news.mp3') 

#====the audio to use for the intro====
intro_audio = pygame.mixer.Sound('bg_intro.wav')

#======bg audio===========
channel1.play(intro_audio, -1) #this bg audio will keep on playing 

#====the bg audio====
bg_audio = pygame.mixer.Sound('bg_music.wav')

#=====glass window shattering=======
window_break = pygame.mixer.Sound('glass_smash.mp3')

#=======the object crash noises 
obj_crash = pygame.mixer.Sound('crashing_objects.mp3')

#=========running sound audio=======
run_sound = pygame.mixer.Sound('run_sound.mp3')

#=====sound of someone walking======
walk_sound = pygame.mixer.Sound('walking.mp3')

#=====where are u audio=====
killer_talk = pygame.mixer.Sound('where_sound.mp3')

#======car driving audio=====
car_drive = pygame.mixer.Sound('car_driving.mp3')

#=======car crashing audio======
crash_audio = pygame.mixer.Sound('car_crash.mp3')

#=========game over audio===============
game_over_audio = pygame.mixer.Sound('game_over.mp3')

#===========you win audio==========
you_win_audio = pygame.mixer.Sound('you_win.mp3')



done = False #vcariable for controlling if the game is done 
while not done:
    for event in pygame.event.get(): #will keep track of the event that happened and store all of the events
        if event.type == pygame.QUIT: #if the user quits
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN: #reduces the player's fear everytime they press the mouse button
            fear = fear - reduce_fear
            if fear < 0: #so it won't show a negative number on the screen it will just show 0
                fear = 0            
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
                if not channel2.get_busy(): #will play the news audio 
                    channel2.play(news)
            if event.key == pygame.K_s or event.key == pygame.K_SPACE: #checks if the user press s or space (so audio will stop whenever they switch screen or press space or s)
                channel2.pause() #pauses the news 
                channel1.pause() #pauses the intro

                
                if not channel3.get_busy(): #will play the bg music 
                    channel3.play(bg_audio, -1) #will play in repeat                  
                
            #for controlling what option the user picks from the first scene taking to whatever option they pick 
            if event.key == pygame.K_a and game_state == "first_scene": #here included if the game state is on first scene so pressing the A or B key would only switch when its on the first scene
                button_press_time = pygame.time.get_ticks() #getting the time when the A button is pressed (for timer)                
                game_state = "second_scene_optA1" #setting the scene to optA1 (using washroom)
            elif event.key == pygame.K_b and game_state == "first_scene":
                button_press_time = pygame.time.get_ticks() #getting the time here too when the B button is pressed (for timer) (learned this from a youtube toturial provided on the google docs)              
                game_state = "second_scene_optB1" #setting the scene to optB1 (watching tv)

            #for controlling the scene from second_scence_optA1 to the next scene options
            #first option A scene(where the player grabs their phone from car)
            elif event.key == pygame.K_a and game_state == "second_scene_optA1":
                game_state = "third_scene_optA2"
                button_press_time = pygame.time.get_ticks() #getting the time when the A button is pressed (for timer)  
                if not channel5.get_busy(): #adding the crashing noises audio
                    channel5.play(obj_crash)                
                               
            #second option B scene(player staying where they are)
            elif event.key == pygame.K_b and game_state == "second_scene_optA1":
                game_state = "third_scene_optB2"    
                button_press_time = pygame.time.get_ticks() #getting the time when the B button is pressed (for timer)  
                if not channel7.get_busy(): #adding walking noise
                    channel7.play(walk_sound)  
              #adding the where are u audio
                    channel8.play(killer_talk)                 
              
            #for the ending where the player encounters a police and seeks help scene 
            elif event.key == pygame.K_a and game_state == "third_scene_optA2":
                game_state = "police ending"
                button_press_time = pygame.time.get_ticks() #getting the time when the A button is pressed (for timer)
                channel5.pause() #pauses the prev audio
                if not channel6.get_busy(): #adding run noises
                    channel6.play(run_sound)  
                            
                
            #for the ending where the player gets in their car
            elif event.key == pygame.K_b and game_state == "third_scene_optA2":
                game_state = "car ending"
                button_press_time = pygame.time.get_ticks() #getting the time when the A button is pressed (for timer)
                channel5.pause() #pauses the prev audio    
                if not channel9.get_busy(): #adding the driving sound
                    channel9.play(car_drive)
            
            #for controlling the options on the scene where the user chooses to watch the tv (switching scenes depends on what the option the user picks)
            elif event.key == pygame.K_a and game_state == "second_scene_optB1":
                game_state = "third_scene_optA2" #using the same variable here (because they have same ending)(run and start car ending)
                button_press_time = pygame.time.get_ticks() #getting the time when the A button is pressed (for timer)  
                if not channel5.get_busy(): #adding the crashing noises audio
                    channel5.play(obj_crash)                                
                
                
            elif event.key == pygame.K_b and game_state == "second_scene_optB1":
                game_state = "third_scene_optB2" #used sam variables since the same thing is happening here too   
                button_press_time = pygame.time.get_ticks() #getting the time when the B button is pressed (for timer)  
                if not channel7.get_busy(): #adding walking noise
                    channel7.play(walk_sound)  
              #adding the where are u audio
                    channel8.play(killer_talk)                
            
            #from player staying where they are to the scene option where the player goes to the kitchen (the other 2 ending)
            elif event.key == pygame.K_a and  game_state == "third_scene_optB2":
                game_state = "kitchen scene"
            elif event.key == pygame.K_b and  game_state == "third_scene_optB2":
                game_state = "drawer scene"
                button_press_time = pygame.time.get_ticks() #getting the time when the B button is pressed (for timer)        
            
            
    #for showing the stats on the screen                       
    fear_str = str(fear) #converting the fear amount into a string so i can display it to the screen
    fear_str2 = "Fear: " #descroiption on what the number is supposed to be
    fear_text = fear_str2 + fear_str #adding the two strings together 
    #=========showing the stats (fear)=============
    fear_stat = font2.render(fear_text, False, WHITE) #rendering the text 
    #for handling the stats (choosing random numbers on how much the fear should increase and decrease)
    add_fear = random.randrange(1, 20) #increase
    reduce_fear = random.randrange(15) #decrease
    fear = fear + add_fear #adding the random number to the fear
    fear_text = fear_str2 + fear_str #adding the two strings together 
    
    
    
    #filling the bg black 
    screen.fill(BLACK)
    #getting what milliseconds that i have right now (for timer)
    current_time = pygame.time.get_ticks()
    
    
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
        fear = 0 #so that fear would not start counting
        
        
        
        
        
        
        
        
    #for the pov on the way home 
    elif game_state == "pov":
        fear = 0 #so that fear would not start counting
        #the bg image 
        screen.blit(pov_img, [0,0])
        #the text saying the user is on their way home 
        screen.blit(pov_text1, (130, 500))
        #informations on what action the user can do 
        screen.blit(pov_text3, (5, 570))
        screen.blit(pov_text4, (300, 570))
        screen.blit(space_text, (470,570))
        screen.blit(fear_stat, (10, 0))
       
                     
        
    #for the first scene 
    elif game_state == "first_scene":
        fear = 0 #so that fear would not start counting        
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
        #displaying the stats at the top left of the screen (did this too for the other options)
        screen.blit(fear_stat, (10, 0))   
        if fear >= 80: #will remind the player that they need to calm
            screen.blit(fear_opt, (0, 400))
        
         
               
        
        
    #if the user chooses optA 1
    elif game_state == "second_scene_optA1":
        #bathroom bg image
        screen.blit(bathroom_bg, [0,0])
        #text description on what the user is doing 
        screen.blit(optA_1, (240,300))
        #to show the power going out randomly by using timer 
        screen.blit(fear_stat, (10, 0)) 
        if fear >= 80: #will remind the player that they need to calm
            screen.blit(fear_opt, (0, 400))      
        if current_time - button_press_time > 2500:#checking is the current time and time pressed for A subtracted is more than 2500 (checks the time for when the last time the button is pressed?)
            screen.fill(BLACK) #screen will be filled black (represents the power going out) 
            screen.blit(fear_stat, (10, 0)) 
            if fear >= 80: #will remind the player that they need to calm
                screen.blit(fear_opt, (0, 400))         
            #======will show text here about the power going out=======
            #text showing that the player hears the window breaks
            screen.blit(glass_text, (270, 100))
            clock.tick(15)#adding timer
            #text for saying that the power went out
            screen.blit(power_text, (340, 150))
            clock.tick(10) #adding a time on where to show the options
            #asking what the user wants to do
            screen.blit(choose_1, (300,200))            
            #providing the options
            screen.blit(optA_2, (200, 240))
            screen.blit(optA_3, (200,280))
            #providing tutorial on what the user should press
            screen.blit(tut1, (10,570)) 
            #window shattering audio 
            if not channel4.get_busy():             
                channel4.play(window_break)
                clock.tick(1)
                channel4.pause()  
                
                

               
            
         
        
    #if the user chooses optB 1
    elif game_state == "second_scene_optB1":
        #watching the tv bg image
        screen.blit(tv_bg, [0,0])
        #showing the text description of the user watching tv
        screen.blit(optB_1,(240, 280))
        screen.blit(fear_stat, (10, 0))
        if fear >= 80: #will remind the player that they need to calm
            screen.blit(fear_opt, (0, 400))          
        #to show the power going out randomly by using the timer
        if current_time - button_press_time > 2500: #checking is the current time and time pressed for B subtracted is more than 2500 (checks the time for when the last time the button is pressed?)
            #====text=====
            screen.fill(BLACK) #screen will be filled black (represents the power going out)       
            screen.blit(fear_stat, (10, 0))
            if fear >= 80: #will remind the player that they need to calm
                screen.blit(fear_opt, (0, 400))        
            #text showing that the player hears the window breaks
            screen.blit(glass_text, (270, 100))
            clock.tick(15)#adding timer            
            #======will show text here about the power going out=======
            screen.blit(power_text, (340, 150))
            clock.tick(10) #adding a time on where to show the options
            #asking what the user wants to do
            screen.blit(choose_1, (300,200))            
            #providing the options
            screen.blit(optA_2, (200, 240))
            screen.blit(optB_3, (200,280))
            #providing tutorial on what the user should press
            screen.blit(tut1, (10,570))    
            #window shattering audio 
            if not channel4.get_busy():             
                channel4.play(window_break)
                clock.tick(1) #adding time on when the audio should pause
                channel4.pause()  
                
                
                
    #for the next scene option A (where the player grabs their phone from car)
    elif game_state ==  "third_scene_optA2":
        #bg image of the car
        screen.blit(car_bg, [0, 0])
        screen.blit(car_text, (180, 100))
        #text description saying that the player is hearing some noises and its coming from their house and this indicates that there is someone inside 
        screen.blit(crash_noise, (200,150))
        screen.blit(fear_stat, (10, 0))
        if fear >= 80: #will remind the player that they need to calm
            screen.blit(fear_opt, (0, 400))        
        
        if current_time - button_press_time > 2500: #this overlaps the previous text in an amount of time
            screen.blit(car_bg, [0, 0])
            #adding the text that of player's thoughts that its not safe
            screen.blit(text_noise, (200, 100))
            #asking user what they want to do next 
            screen.blit(choose_1, (300,150))
            screen.blit(optA_4, (260, 180))
            screen.blit(optB_4, (320, 180))
            #providing tutorial on what the user should press
            screen.blit(tut1, (10,570))              
            screen.blit(fear_stat, (10, 0))
            if fear >= 80: #will remind the player that they need to calm
                screen.blit(fear_opt, (0, 400))            
            
            
            
        
    
    
    #for the next scene option B (player just stays where they are)
    elif game_state == "third_scene_optB2":
        #bathroom bg image (player staying where they are)
        screen.blit(bathroom_bg2, [0,0]) 
        #text description saying that the player is hearing some noises and its coming from their house and this indicates that there is someone inside 
        screen.blit(noise2, (200,150))  
        screen.blit(fear_stat, (10, 0))
        if fear >= 80: #will remind the player that they need to calm
            screen.blit(fear_opt, (0, 400))        
        
        if current_time - button_press_time > 2500: #this overlaps the previous text in an amount of time
            screen.blit(bathroom_bg2, [0, 0])
            #text (player thinks its not safe)
            screen.blit(text_noise2, (280, 100))
            #asking user what they want to do next 
            screen.blit(choose_1, (300,150))
            screen.blit(optA_5, (100, 180))
            screen.blit(optB_5, (100, 210))
            #providing tutorial on what the user should press
            screen.blit(tut1, (10,570))   
            screen.blit(fear_stat, (10, 0))
            if fear >= 80: #will remind the player that they need to calm
                screen.blit(fear_opt, (0, 400))            
            
        
    #for the ending where player encounters police scene 
    elif game_state == "police ending":
        fear = -100 #so the other ending wouldn't trigger
        #running scene image
        screen.blit(run_image, [0,0])
        #text description
        screen.blit(run_text, (370, 500))
        if current_time - button_press_time > 2500: #this overlaps the previous text/image in an amount of time
            #scene where the player sees a police image
            screen.blit(police_ending, [0,0])
            #text description 
            screen.blit(police_text, (230,200))
        if current_time - button_press_time > 10000:
            screen.fill(WHITE) 
            screen.blit(police_ending1, (105, 100))
            screen.blit(you_win, (100,200))
            pygame.draw.rect(screen, WHITE, [x, 200, 800, 600])
            x += 375 #x-pos of rect will move +375 every loop (game over text appearing & disappearing)
            if x > 900:#resets back the x- pos of rect when its more than 900
                x = 0        
            if not channel12.get_busy(): #plays the you win audio (it play over and over again)
                channel12.play(you_win_audio)               
            
            
    #for the scene where the player chooses to get in their car
    elif game_state == "car ending":
        fear = -100
        #image of driving car
        screen.blit(car2, [0,0])
        #text description
        screen.blit(car_ending_text, (230, 300))
        if current_time - button_press_time > 10000: #this overlaps the previous 
            #showing scene of crashing (made the time longer)
            #image of the scene
            screen.blit(car3, [0, 0])
            screen.blit(car_ending2, (330,300))
            channel9.pause()#pauses the audio when the crashing scene displays             
            if not channel10.get_busy(): #plays the crashing audio 
                channel10.play(crash_audio)
        if current_time - button_press_time > 16000: #pauses the audio and adding the ending scene saying that player loses
            channel10.pause() 
            screen.fill(BLACK) 
            screen.blit(car_ending1, (170, 100))
            screen.blit(game_over, (80, 200))
            pygame.draw.rect(screen, BLACK, [x, 200, 800, 600])
            x += 400 #x-pos of rect will move +400 every loop (game over text appearing & disappearing)
            if x > 900:#resets back the x- pos of rect when its more than 900
                x = 0 
            if not channel11.get_busy(): #plays the game over audio (it play over and over again)
                channel11.play(game_over_audio)               

            
            
     
    #user chooses to grab their phone from ther car (from watching tv scene)      
    elif game_state == "optA_sec":
        #bg image of the car
        screen.blit(car_bg, [0, 0])
        screen.blit(car_text, (180, 100))
        screen.blit(fear_stat, (10, 0))
        if fear >= 80: #will remind the player that they need to calm
            screen.blit(fear_opt, (0, 400))        
        
        #text description saying that the player is hearing some noises and its coming from their house and this indicates that there is someone inside 
        screen.blit(crash_noise, (200,150))
        if current_time - button_press_time > 2500: #this overlaps the previous text in an amount of time
            screen.blit(car_bg, [0, 0])
            #adding the text that of player's thoughts that its not safe
            screen.blit(text_noise, (200, 100))
            #asking user what they want to do next 
            screen.blit(choose_1, (300,150))
            screen.blit(optA_4, (260, 180))
            screen.blit(optB_4, (320, 180))
            #providing tutorial on what the user should press
            screen.blit(tut1, (10,570))   
            screen.blit(fear_stat, (10, 0))
            if fear >= 80: #will remind the player that they need to calm
                screen.blit(fear_opt, (0, 400))           
            

    #kitchen scene (ending)
    elif game_state == "kitchen scene":
        fear = -100
        #kitchen img
        screen.blit(kitchen_img, [0, 0])
        #will check if the player found a knife here and will display that they found a knife and add option that they can use knife however if they dont a description will be added that the knife is gone and the intruder might have already aquired it so therefore the player loses
        if knife == True: #if knife is true means that the user have luck (and have knife and will win)
            #will add text description
            screen.blit(found_knife, (300, 200))
            if current_time - button_press_time > 6500:
                screen.fill(WHITE)
                screen.blit(kitchen_ending1, (200,100))
                screen.blit(you_win, (100,200))
                pygame.draw.rect(screen, WHITE, [x, 200, 800, 600])
                x += 375 #x-pos of rect will move +375 every loop (game over text appearing & disappearing)
                if x > 900:#resets back the x- pos of rect when its more than 900
                    x = 0    
                if not channel12.get_busy(): #plays the you win audio (it play over and over again)
                    channel12.play(you_win_audio)                   
                
        elif knife == False:
            screen.blit(knife_text2, (300,200))
            if current_time - button_press_time > 6500:
                screen.fill(BLACK)
                screen.blit(kitchen_ending2, (200,100))
                screen.blit(game_over, (80, 200))
                pygame.draw.rect(screen, BLACK, [x, 200, 800, 600])
                x += 400 #x-pos of rect will move +400 every loop (game over text appearing & disappearing)
                if x > 900:#resets back the x- pos of rect when its more than 900
                    x = 0  
                if not channel11.get_busy(): #plays the game over audio (it play over and over again)
                    channel11.play(game_over_audio)                
        
        
    #drawer scene (ending)
    elif game_state == "drawer scene":
        fear = -100
        #filling the screen black (might change into an image later showing that the player is rummaging through the cabinets)
        screen.fill(BLACK)
        #displaying the text saying that the player is doing this
        screen.blit(rummage, (250, 250))
        if current_time - button_press_time > 2500: 
            #displaying the image of the drawer with a gun 
            screen.blit(drawer_img, [0, 0])
            #displaying text
            screen.blit(gun_text1, (330, 300))
            if current_time - button_press_time > 5000: 
                if luck_gun == 7: #depends on the luck of the player if they will win here or not
                    screen.fill(WHITE)
                    screen.blit(drawer_ending1, (300, 100)) 
                    screen.blit(you_win, (100,200))
                    pygame.draw.rect(screen, WHITE, [x, 200, 800, 600])
                    x += 375 #x-pos of rect will move +375 every loop (game over text appearing & disappearing)
                    if x > 900:#resets back the x- pos of rect when its more than 900
                        x = 0
                    if not channel12.get_busy(): #plays the you win audio (it play over and over again)
                        channel12.play(you_win_audio)                     
                        
                                        
                else:
                    screen.fill(BLACK)
                    screen.blit(drawer_ending2, (210, 100))
                    screen.blit(game_over, (80, 200))
                    pygame.draw.rect(screen, BLACK, [x, 200, 800, 600])
                    x += 400 #x-pos of rect will move +400 every loop (game over text appearing & disappearing)
                    if x > 900:#resets back the x- pos of rect when its more than 900
                        x = 0
                    if not channel11.get_busy(): #plays the game over audio (it play over and over again)
                        channel11.play(game_over_audio)                       
                    
                    
                   
                    
            
            
            
            
    #if the fear reached to 100 or more than player will lose
    if fear >= fear_limit: 
        screen.fill(BLACK)    
        screen.blit(fear_ending, (230, 100))
        screen.blit(game_over, (80, 200))
        pygame.draw.rect(screen, BLACK, [x, 200, 800, 600])
        x += 400 #x-pos of rect will move +400 every loop (game over text appearing & disappearing)
        if x > 900:#resets back the x- pos of rect when its more than 900
            x = 0     
        if not channel11.get_busy(): #plays the game over audio (it play over and over again)
            channel11.play(game_over_audio)    

       
    
    
    

    
    pygame.display.flip()
    clock.tick(1) #will play the game smoothly every 1
            
            
    
    

                        
pygame.quit()