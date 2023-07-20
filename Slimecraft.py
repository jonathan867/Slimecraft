#Jonathan Feng, Dorian Chen
#June 19 2020
#Slimecraft: a dungeon crawler game

from graphics import *
import time
import threading
from random import randint

map1 = GraphWin("Map1",1200,800) #starts window

boundax=0 #dorian
bounday=345
boundbx=150
boundby=345
boundcx=150
boundcy=165
bounddx=1030
bounddy=165
boundex=1030
boundey=345
boundfx=1199
boundfy=345
boundgx=1199
boundgy=498
boundhx=1030
boundhy=498
boundix=1030
boundiy=670
boundjx=710
boundjy=670
boundkx=710
boundky=799
boundlx=460
boundly=799
boundmx=460
boundmy=670
boundnx=150
boundny=670
boundox=150
boundoy=498
boundpx=0
boundpy=498


#map
mapbackground = "1a" #variable that keeps track what room it is
map1a=Image(Point(-600,400),"MAPS/level 1/dungeon background level 1a.png") #draws all the rooms out of frame first
map1a.draw(map1)
map1b=Image(Point(-600,400),"MAPS/level 1/dungeon background level 1b.png")
map1b.draw(map1)
map1c=Image(Point(1800,400),"MAPS/level 1/dungeon background level 1c.png")
map1c.draw(map1)
map2a=Image(Point(-600,400),"MAPS/level 2/dungeon background level 2a.png")
map2a.draw(map1)
map2b=Image(Point(-600,400),"MAPS/level 2/dungeon background level 2b.png")
map2b.draw(map1)
map2c=Image(Point(1800,400),"MAPS/level 2/dungeon background level 2c.png")
map2c.draw(map1)
map3a=Image(Point(-600,400),"MAPS/level 3/dungeon background 3a.png")
map3a.draw(map1)
map3b=Image(Point(-600,400),"MAPS/level 3/dungeon background 3b.png")
map3b.draw(map1)
map3c=Image(Point(1800,400),"MAPS/level 3/dungeon background 3c.png")
map3c.draw(map1)

#character
sx = 100 #character location
sy = 400
slimeHp=5000#character Hp
slimeHpnew=5000 #variable to check if the Hp changed
#enemy
e1x = 800# enemy location
e1y = 600
e2x = 800
e2y = 200
e3x = 800
e3y = 200

#ranged enemy
r1x = 1000# enemy location
r1y = 400
r2x = 1000
r2y = 600
r3x = 200
r3y = 400
r2Hp=200#enemy health
r3Hp=200
r1Hp=200

#mortar
m1x = 960# enemy location
m1y = 200
m2x = 240
m2y = 200
m1Hp=600#enemy health
m2Hp=600
#Items
hx = 0# item location
hy = 0
ix = 0
iy = 0
lx = 0
ly = 0
e1Hp = 100#enemy health
e2Hp = 100
e3Hp = 100
frozen = False #checks if ice item is activated

enemy11a = "alive"#checks if the enemy is alive when entering or returning to a room
enemy11b = "alive"
enemy12a = "alive"
enemy12b = "alive"
enemy13a = "alive"
enemy13b = "alive"
enemy21a = "alive"
enemy21b = "alive"
enemy22a = "alive"
enemy22b = "alive"
enemy23a = "alive"
enemy23b = "alive"
enemy31b = "alive"
ranged12a = "alive"
ranged12b = "alive"
ranged13a = "alive"
ranged13b = "alive"
ranged22a = "alive"
ranged22b = "alive"
ranged23a = "alive"
ranged23b = "alive"
ranged32b = "alive"
mortar13a = "alive"
mortar13b = "alive"
mortar23b = "alive"

titlescreen1=Image(Point(600,400),"Images/title 1.png") #title screen
titlescreen2=Image(Point(600,400),"Images/title 2.png")
titlescreen3=Image(Point(600,400),"Images/title 3.png")
titlescreen4=Image(Point(600,400),"Images/title 4.png")
titlescreen5=Image(Point(600,400),"Images/title 5.png")#glitchy animation images
titlescreenbackground=Image(Point(600,400),"Images/screen background.png")
pressFtext=Image(Point(600,400),"Images/press f.png")
loadingtext1=Image(Point(600,400),"Images/loading 1.png")
loadingtext2=Image(Point(600,400),"Images/loading 2.png")
loadingtext3=Image(Point(600,400),"Images/loading 3.png")

slimesword1=Image(Point(sx,sy),"Images/slime sword 1.png")#swordslimeswing animation images
slimesword2=Image(Point(sx,sy),"Images/slime sword 2.png")
slimesword3=Image(Point(sx,sy),"Images/slime sword 3.png")
slimesword4=Image(Point(sx,sy),"Images/slime sword 4.png")
slimesword5=Image(Point(sx,sy),"Images/slime sword 5.png")
class TheActualGame (threading.Thread): #starts the game
    def _init_ (self):
        threading.Thread._init_(self)
    def run (self): 
        global winner
        winner=False#checks if the player won
        titlescreenbackground.draw(map1)
        titleclick=""
        titleclick1=""
        titleclick2=""
        titleclick3=""
        infotext = Text(Point(600,750),"By: Dorian Chen and Jonathan Feng, June 19 2020")
        infotext.setSize(20)
        infotext.draw(map1)
        infotext.setFill("white")
        while titleclick!="f" and titleclick!="F":#press f to start
            titlescreen1.draw(map1) #glitch animation
            time.sleep(0.2)
            titlescreen5.undraw()
            titlescreen2.draw(map1)
            time.sleep(0.2)
            titlescreen1.undraw()
            titlescreen3.draw(map1)
            time.sleep(0.2)
            titlescreen2.undraw()
            titlescreen4.draw(map1)
            time.sleep(0.2)
            pressFtext.undraw()
            titlescreen3.undraw()
            titlescreen5.draw(map1)
            time.sleep(0.2)
            titlescreen4.undraw()
            pressFtext.draw(map1)
            titleclick=map1.checkKey()
            if titleclick=="f"or titleclick=="F":
                infotext.undraw()
                for i in range (2):
                    pressFtext.undraw()
                    loadingtext1.draw(map1)#loading animation
                    time.sleep(0.3)
                    loadingtext1.undraw()
                    time.sleep(0.3)
                    loadingtext2.draw(map1)
                    time.sleep(0.3)
                    loadingtext2.undraw()
                    time.sleep(0.3)
                    loadingtext3.draw(map1)
                    time.sleep(1)
                    loadingtext3.undraw()
                pressFtext.undraw()
                titlescreen5.undraw()
                titlescreenbackground.undraw()
        instructions1=Image(Point(600,400),"Images/INSTRUCTIONS 1.png")#instructions
        instructions1.draw(map1)
        while titleclick1!="f" or titleclick1!="F":
            titleclick1=map1.getKey()
            if titleclick1=="f" or titleclick1=="F":#move on to next instructions
                break
            break
        instructions2=Image(Point(600,400),"Images/INSTRUCTIONS 2.png")
        instructions2.draw(map1)
        while titleclick3!="f" or titleclick3!="F":#move on to next instructions
            titleclick3=map1.getKey()
            if titleclick3=="f" or titleclick3=="F":
                break
            break
        instructions3=Image(Point(600,400),"Images/INSTRUCTIONS 3.png")
        instructions3.draw(map1)
        while titleclick2!="f" or titleclick2!="F":#move on from instructions
            titleclick2=map1.getKey()
            if titleclick2=="f" or titleclick2=="F":
                break
            break
        instructions1.undraw()
        instructions2.undraw()
        instructions3.undraw()
        map1a.move(1200,0) #moves map on screen
        thread1 = MoveSlime()
        thread1.start()#starts character thread

class MoveSlime (threading.Thread): #character movement and other functions
    def _init_ (self):
        threading.Thread._init_(self)
    def run (self):
        global slimeHp
        global slimeHpnew
        slimeHpnew=3000
        slimeHp = 3000
        slime = Image(Point(100,400),"Images/slime.png")# spawns slime
        slime.draw(map1)
        select = Rectangle(Point(360,5), Point(440,85))# shows selected inventory
        select.draw(map1)
        select.setFill("yellow")
        select.setOutline("yellow")
        
        boundax=0 #map bounderies
        bounday=345
        boundbx=155
        boundby=345
        boundcx=155
        boundcy=165
        bounddx=1030
        bounddy=165
        boundex=1030
        boundey=345
        boundfx=1199
        boundfy=345
        boundgx=1199
        boundgy=475
        boundhx=1030
        boundhy=475
        boundix=1030
        boundiy=655
        boundjx=705
        boundjy=655
        boundkx=705
        boundky=799
        boundlx=470
        boundly=799
        boundmx=470
        boundmy=655
        boundnx=155
        boundny=655
        boundox=155
        boundoy=475
        boundpx=0
        boundpy=475
        
        inv1 = Rectangle(Point(370,15), Point(430,75)) #draws inventory boxes
        inv1.draw(map1)
        inv1.setFill(color_rgb(138,138,138))
        inv1I = Rectangle(Point(375,20), Point(425,70))
        inv1I.draw(map1)
        inv1I.setFill(color_rgb(190,190,190))
        inv1I.setWidth(3)
        inv1I.setOutline(color_rgb(170,170,170))
        inv2 = Rectangle(Point(470,15), Point(530,75))
        inv2.draw(map1)
        inv2.setFill(color_rgb(138,138,138))
        inv2I = Rectangle(Point(475,20), Point(525,70))
        inv2I.draw(map1)
        inv2I.setFill(color_rgb(190,190,190))
        inv2I.setWidth(3)
        inv2I.setOutline(color_rgb(170,170,170))
        inv3 = Rectangle(Point(570,15), Point(630,75))
        inv3.draw(map1)
        inv3.setFill(color_rgb(138,138,138))
        inv3I = Rectangle(Point(575,20), Point(625,70))
        inv3I.draw(map1)
        inv3I.setFill(color_rgb(190,190,190))
        inv3I.setWidth(3)
        inv3I.setOutline(color_rgb(170,170,170))
        inv4 = Rectangle(Point(670,15), Point(730,75))
        inv4.draw(map1)
        inv4.setFill(color_rgb(138,138,138))
        inv4I = Rectangle(Point(675,20), Point(725,70))
        inv4I.draw(map1)
        inv4I.setFill(color_rgb(190,190,190))
        inv4I.setWidth(3)
        inv4I.setOutline(color_rgb(170,170,170))
        inv5 = Rectangle(Point(770,15), Point(830,75))
        inv5.draw(map1)
        inv5.setFill(color_rgb(138,138,138))
        inv5I = Rectangle(Point(775,20), Point(825,70))
        inv5I.draw(map1)
        inv5I.setFill(color_rgb(190,190,190))
        inv5I.setWidth(3)
        inv5I.setOutline(color_rgb(170,170,170))

        heart1 = Image(Point(400,45),"Images/heart.png") #items
        heart2 = Image(Point(500,45),"Images/heart.png")
        heart3 = Image(Point(600,45),"Images/heart.png")
        heart4 = Image(Point(700,45),"Images/heart.png")
        heart5 = Image(Point(800,45),"Images/heart.png")
        ice1 = Image(Point(400,45),"Images/freeze 1.png")
        ice2 = Image(Point(500,45),"Images/freeze 1.png")
        ice3 = Image(Point(600,45),"Images/freeze 1.png")
        ice4 = Image(Point(700,45),"Images/freeze 1.png")
        ice5 = Image(Point(800,45),"Images/freeze 1.png")
        lightning1 = Image(Point(400,45),"Images/lightning.png")
        lightning2 = Image(Point(500,45),"Images/lightning.png")
        lightning3 = Image(Point(600,45),"Images/lightning.png")
        lightning4 = Image(Point(700,45),"Images/lightning.png")
        lightning5 = Image(Point(800,45),"Images/lightning.png")

        drawnU = False#checks if the slime trail is already drawn
        drawnR = False
        drawnL = False
        drawnD = False
        previousKey = "1"#checks what inventory slot was previously chosen so that it knows to move the yellow part how much
        global mapbackground#checks what map it is
        mapbackground = "1a"
        global key
        
        in1 = False #false = empty (checks if the inventory slots are full)
        in2 = False
        in3 = False
        in4 = False
        in5 = False
        selection = 1
        i1 = ""#checks what is in the inventory
        i2 = ""
        i3 = ""
        i4 = ""
        i5 = ""
        global hx #checks where the items are
        global hy
        global ix
        global iy
        global lx
        global ly
        hTaken = False #checks if the items on the map are taken
        iTaken = False
        lTaken = False
        global frozen #checks if ice is activated
        frozen = False
        global e1Hp# checks enemy Hp
        global e2Hp
        global e3Hp
        global r1Hp
        global r2Hp
        global r3Hp
        global m1Hp
        global m2Hp
        global enemy11a#checks if the enemies are alive when entering or returning to a room
        global enemy11b
        global enemy12a
        global enemy12b
        global enemy13a
        global enemy13b
        global enemy21b
        global enemy21a
        global enemy22a
        global enemy22b
        global enemy23a
        global enemy23b
        global enemy31b
        global ranged12a
        global ranged12b
        global ranged13a
        global ranged13b
        global ranged22a
        global ranged22b
        global ranged23b
        global ranged32b
        global mortar13a
        global mortar13b
        global mortar23b
        global e1x#checks enemy locations
        global e1y
        global e2x
        global e2y
        global e3x
        global e3y
        global r1x
        global r1y
        global r2x
        global r2y
        global r3x
        global r3y
        global m1x
        global m1y
        global m2x
        global m2y
        global sx#checks where the character is
        global sy
        sx = 100
        sy = 400
        enemy11a = "alive"#checks if the enemy is alive when entering or returning to a room
        enemy11b = "alive"
        enemy12a = "alive"
        enemy12b = "alive"
        enemy13a = "alive"
        enemy13b = "alive"
        enemy21a = "alive"
        enemy21b = "alive"
        enemy22a = "alive"
        enemy22b = "alive"
        enemy23a = "alive"
        enemy23b = "alive"
        enemy31b = "alive"
        ranged12a = "alive"
        ranged12b = "alive"
        ranged13a = "alive"
        ranged13b = "alive"
        ranged22a = "alive"
        ranged22b = "alive"
        ranged23a = "alive"
        ranged23b = "alive"
        ranged32b = "alive"
        mortar13a = "alive"
        mortar13b = "alive"
        mortar23b = "alive"
        e1x = 800
        e1y = 600
        e2x = 800
        e2y = 200
        thread2 = MoveEnemy1()
        thread2.start() #starts enemy1
        thread3 = MoveEnemy2()
        thread3.start() #starts enemy2
        winner = False
        slimeHpbox=Image(Point(80,45),"Images/healthbar.png")#draws heathbar
        slimeHpbox.draw(map1)
        slimeHptext=Text(Point(80,45),slimeHp)
        slimeHptext.draw(map1)
        while slimeHp > 0:
            key = map1.checkKey()# gets key input
            clickposition=map1.checkMouse() #gets mouse input
            print("")
            if slimeHpnew!=slimeHp: #checks if the character's Hp changed
                slimeHptext.undraw()#if it did change, the hp is updated
                slimeHpnew=slimeHp
                slimeHptext=Text(Point(80,45),slimeHp)
                slimeHptext.draw(map1)
            if clickposition!=None: #attack function
                slimeswordswingx=clickposition.getX()
                if slimeswordswingx>sx:#checks which side the player is aiming at
                    slimesword1=Image(Point(sx,sy-38),"Images/slime sword 1.png") #attack to the right animation
                    slimesword1.draw(map1)
                    time.sleep(0.5)
                    slimesword2=Image(Point(sx+30,sy-39),"Images/slime sword 2.png")
                    slimesword2.draw(map1)
                    slimesword1.undraw()
                    slimesword3=Image(Point(sx+38,sy-19),"Images/slime sword 3.png")
                    slimesword3.draw(map1)
                    slimesword2.undraw()
                    slimesword4=Image(Point(sx+35,sy-1),"Images/slime sword 4.png")
                    slimesword4.draw(map1)
                    slimesword3.undraw()
                    slimesword5=Image(Point(sx,sy+38),"Images/slime sword 5.png")
                    slimesword5.draw(map1)
                    slimesword4.undraw()
                    slimesword5.undraw()
                    if (0<(e2x-sx)<100) and ((sy-e2y<100)and(sy-e2y>-100)):#checks if any enemies were hit
                        e2Hp=e2Hp-20
                    if (0<(e3x-sx)<100) and ((sy-e3y<100)and(sy-e3y>-100)):#first 3 enemies
                        e3Hp=e3Hp-20
                    if (0<(e1x-sx)<100) and ((sy-e1y<100)and(sy-e1y>-100)):
                        e1Hp=e1Hp-20
                    if (0<(r2x-sx)<100) and ((sy-r2y<100)and(sy-r2y>-100)):#first ranged
                        r2Hp=r2Hp-20
                    if (0<(r3x-sx)<100) and ((sy-r3y<100)and(sy-r3y>-100)):
                        r3Hp=r3Hp-20
                    if (0<(r1x-sx)<100) and ((sy-r1y<100)and(sy-r1y>-100)):
                        r1Hp=r1Hp-20
                    if (0<(m1x-sx)<100) and ((sy-m1y<100)and(sy-m1y>-100)):#mortar
                        m1Hp=m1Hp-20
                    if (0<(m2x-sx)<100) and ((sy-m2y<100)and(sy-m2y>-100)):
                        m2Hp=m2Hp-20
                elif slimeswordswingx<sx: #dorian
                    slimesword1=Image(Point(sx,sy-38),"Images/slime sword 1.png") #attack to the left animation
                    slimesword1.draw(map1)
                    time.sleep(0.5)
                    slimesword2flip=Image(Point(sx-29,sy-38),"Images/slime sword 2 flipped.png")
                    slimesword2flip.draw(map1)
                    slimesword1.undraw()
                    slimesword3flip=Image(Point(sx-38,sy-19),"Images/slime sword 3 flipped.png")
                    slimesword3flip.draw(map1)
                    slimesword2flip.undraw()
                    slimesword4flip=Image(Point(sx-35,sy-1),"Images/slime sword 4 flipped.png")
                    slimesword4flip.draw(map1)
                    slimesword3flip.undraw()
                    slimesword5=Image(Point(sx,sy+38),"Images/slime sword 5.png")
                    slimesword5.draw(map1)
                    slimesword4flip.undraw()
                    slimesword5.undraw()
                    if (0>(e2x-sx)>-100) and ((sy-e2y<100)and(sy-e2y>-100)):#checks if any enemies were hit
                        e2Hp=e2Hp-20
                    if (0>(e3x-sx)>-100) and ((sy-e3y<100)and(sy-e3y>-100)):#attack melee
                        e3Hp=e3Hp-20
                    if (0>(e1x-sx)>-100) and ((sy-e1y<100)and(sy-e1y>-100)):
                        e1Hp=e1Hp-20
                    if (0>(r2x-sx)>-100) and ((sy-r2y<100)and(sy-r2y>-100)):#attack ranged
                        r2Hp=r2Hp-20
                    if (0>(r3x-sx)>-100) and ((sy-r3y<100)and(sy-r3y>-100)):
                        r3Hp=r3Hp-20
                    if (0>(r1x-sx)>-100) and ((sy-r1y<100)and(sy-r1y>-100)):
                        r1Hp=r1Hp-20
                    if (0>(m1x-sx)>-100) and ((sy-m1y<100)and(sy-m1y>-100)):#mortar
                        m1Hp=m1Hp-20
                    if (0>(m2x-sx)>-100) and ((sy-m2y<100)and(sy-m2y>-100)):
                        m2Hp=m2Hp-20
            if key == "Up" and ((boundax<=sx<=boundbx and sy-10>boundby) or (boundex<=sx<=boundfx and sy-10>boundey) or (boundbx<=sx<=boundex and sy-10>bounddy)): #checks which direction and if slime is within the bounderies
                if drawnR == True: #checks if it is moving the same direction as last time. If it is, it undraws old trail and draws new trail. If not, it moves old trail with slime
                    trailR.undraw()
                    drawnR = False
                if drawnL == True:
                    trailL.undraw()
                    drawnL = False
                slime.move(0,-10)#moves the character
                sy = sy - 10
                if drawnU == False:
                    trailU = Image(Point(sx,sy + 34),"Images/slime moving up trail.png")
                    trailU.draw(map1)
                    drawnU = True
                else:
                    trailU.move(0,-10)
                    
            elif key == "Right" and ((boundcy<=sy<=boundby and sx+10<boundix) or (bounday<=sy<=boundpy and sx+10<boundfx) or (boundpy<=sy<=boundny and sx+10<boundix) or (boundly>=sy>=boundmy and sx+10<boundkx)): #dorian
                if drawnU == True: #checks if it is moving the same direction as last time. If it is, it undraws old trail and draws new trail. If not, it moves old trail with slime
                    trailU.undraw()
                    drawnU = False
                if drawnL == True:
                    trailL.undraw()
                    drawnL = False
                slime.move(10,0)#moves the character
                sx = sx + 10
                if drawnR == False:
                    trailR = Image(Point(sx - 30,sy + 18),"Images/slime moving right trail.png")
                    trailR.draw(map1)
                    drawnR = True
                else:
                    trailR.move(10,0)
                    
            elif key == "Left" and ((boundcy<=sy<=boundby and sx-10>boundcx) or (bounday<=sy<=boundpy and sx-10>boundax) or (boundpy<=sy<=boundny and sx-10>boundox) or (boundly>=sy>boundmy and sx-10>boundmx)): #dorian
                if drawnU == True: #checks if it is moving the same direction as last time. If it is, it undraws old trail and draws new trail. If not, it moves old trail with slime
                    trailU.undraw()
                    drawnU = False
                if drawnR == True:
                    trailR.undraw()
                    drawnR = False
                slime.move(-10,0)#moves the character
                sx = sx - 10
                if drawnL == False:
                    trailL = Image(Point(sx + 30,sy + 18),"Images/slime moving left trail.png")
                    trailL.draw(map1)
                    drawnL = True
                else:
                    trailL.move(-10,0)

            elif key == "Down" and ((boundax<=sx<boundbx and sy+10<=boundoy) or (boundcx<=sx<=boundmx and sy+10<boundmy) or (boundmx<sx<=boundjx and sy+10<boundky) or (boundex<=sx<=boundfx and sy+10<boundgy)or (boundjx<=sx<boundix and sy+10<boundjy)): #dorian
                if drawnU == True: #checks if it is moving the same direction as last time. If it is, it undraws old trail and draws new trail. If not, it moves old trail with slime
                    trailU.undraw()
                    drawnU = False
                if drawnR == True:
                    trailR.undraw()
                    drawnR = False
                if drawnL == True:
                    trailL.undraw()
                    drawnL = False  
                slime.move(0,10) #moves the character
                sy = sy + 10

            elif key == "1" or key == "2" or key == "3" or key == "4" or key == "5": #inventory selection (moving the yellow thing)
                selection = int(key)
                if int(key) - int(previousKey) == 1:#compares previous selection with current selection to see how much it should move the yellow select box
                    select.move(100,0)
                    previousKey = key
                elif int(key) - int(previousKey) == -1:
                    select.move(-100,0)
                    previousKey = key
                elif int(key) - int(previousKey) == 2:
                    select.move(200,0)
                    previousKey = key
                elif int(key) - int(previousKey) == -2:
                    select.move(-200,0)
                    previousKey = key
                elif int(key) - int(previousKey) == 3:
                    select.move(300,0)
                    previousKey = key
                elif int(key) - int(previousKey) == -3:
                    select.move(-300,0)
                    previousKey = key
                elif int(key) - int(previousKey) == 4:
                    select.move(400,0)
                    previousKey = key
                elif int(key) - int(previousKey) == -4:
                    select.move(-400,0)
                    previousKey = key
            #pick up items
            elif key == "c" and (in1 == False or in2 == False or in3 == False or in4 == False or in5 == False): #checks that there is an empty spot left
                if hTaken == False and ((sx - hx > -50 and sx - hx < 50) and (sy - hy > -50 and sy - hy < 50)): #checks that the item is not already taken and is close enough
                    if in1 == False:
                        heart1 = Image(Point(400,45),"Images/heart.png") #puts heart in inventory 1
                        heart1.draw(map1)
                        in1 = True #makes this inventory slot filled
                        i1 = "heart"
                    elif in2 == False:
                        heart2 = Image(Point(500,45),"Images/heart.png") #puts heart in inventory 2
                        heart2.draw(map1)
                        in2 = True #makes this inventory slot filled
                        i2 = "heart"
                    elif in3 == False:
                        heart3 = Image(Point(600,45),"Images/heart.png") #puts heart in inventory 3
                        heart3.draw(map1)
                        in3 = True #makes this inventory slot filled
                        i3 = "heart"
                    elif in4 == False:
                        heart4 = Image(Point(700,45),"Images/heart.png") #puts heart in inventory 4
                        heart4.draw(map1)
                        in4 = True #makes this inventory slot filled
                        i4 = "heart"
                    elif in5 == False:
                        heart5 = Image(Point(800,45),"Images/heart.png") #puts heart in inventory 5
                        heart5.draw(map1)
                        in5 = True #makes this inventory slot filled
                        i5 = "heart"
                    hTaken = True #makes the heart taken
                    heart.undraw()

                if  (sx - ix > -50 and sx - ix < 50) and (sy - iy > -50 and sy - iy < 50) and iTaken == False:
                    if in1 == False:
                        ice1 = Image(Point(400,45),"Images/freeze 1.png") #puts ice in inventory 1
                        ice1.draw(map1)
                        in1 = True #makes this inventory slot filled
                        i1 = "ice"
                    elif in2 == False:
                        ice2 = Image(Point(500,45),"Images/freeze 1.png")#puts ice in inventory 2
                        ice2.draw(map1)
                        in2 = True #makes this inventory slot filled
                        i2 = "ice"
                    elif in3 == False:
                        ice3 = Image(Point(600,45),"Images/freeze 1.png")#puts ice in inventory 3
                        ice3.draw(map1)
                        in3 = True #makes this inventory slot filled
                        i3 = "ice"
                    elif in4 == False:
                        ice4 = Image(Point(700,45),"Images/freeze 1.png")#puts ice in inventory 4
                        ice4.draw(map1)
                        in4 = True #makes this inventory slot filled
                        i4 = "ice"
                    elif in5 == False:
                        ice5 = Image(Point(800,45),"Images/freeze 1.png")#puts ice in inventory 5
                        ice5.draw(map1)
                        in5 = True #makes this inventory slot filled
                        i5 = "ice"
                    iTaken = True #maeks the ice taken
                    ice.undraw()

                if (sx - lx > -50 and sx - lx < 50) and (sy - ly > -50 and sy - ly < 50): #and lTaken == False:
                    if in1 == False:
                        lightning1 = Image(Point(400,45),"Images/lightning.png") #puts lightning in inventory 1
                        lightning1.draw(map1)
                        in1 = True #makes this inventory slot filled
                        i1 = "lightning"
                    elif in2 == False:
                        lightning2 = Image(Point(500,45),"Images/lightning.png") #puts lightning in inventory 2
                        lightning2.draw(map1)
                        in2 = True #makes this inventory slot filled
                        i2 = "lightning"
                    elif in3 == False:
                        lightning3 = Image(Point(600,45),"Images/lightning.png") #puts lightning in inventory 3
                        lightning3.draw(map1)
                        in3 = True #makes this inventory slot filled
                        i3 = "lightning"
                    elif in4 == False:
                        lightning4 = Image(Point(700,45),"Images/lightning.png") #puts lightning in inventory 4
                        lightning4.draw(map1)
                        in4 = True #makes this inventory slot filled
                        i4 = "lightning"
                    elif in5 == False:
                        lightning5 = Image(Point(800,45),"Images/lightning.png") #puts lightning in inventory 5
                        lightning5.draw(map1)
                        in5 = True #makes this inventory slot filled
                        i5 = "lightning"
                    lTaken = True #makes the lightning taken
                    lightning.undraw()
                              
            elif key == "v": #use items
                
                def speed(): #effect of lightning item
                    global sx
                    global sy
                    linex = sx
                    liney = sy
                    if sx < 600 and sy < 400: #moves the character to the opposite corner of the room
                        slime.move(900 - sx, 600 - sy)
                        sx = 900
                        sy = 600
                    elif sx < 600 and sy > 400:
                        slime.move(900 - sx, 200 - sy)
                        sx = 900
                        sy = 200
                    elif sx > 600 and sy < 400:
                        slime.move(200 - sx, 600 - sy)
                        sx = 200
                        sy = 600
                    else:
                        slime.move(200 - sx, 200 - sy)
                        sx = 200
                        sy = 200
                    line = Line(Point(linex,liney), Point(sx,sy)) #lightning animation
                    line.draw(map1)
                    line.setWidth(20)
                    line.setFill("yellow")
                    cloud = Circle(Point(linex,liney),50)
                    cloud.draw(map1)
                    cloud.setFill("gray")
                    cloud.setOutline("gray")
                    cloud1 = Circle(Point(linex - 50,liney + 20),30)
                    cloud1.draw(map1)
                    cloud1.setFill("gray")
                    cloud1.setOutline("gray")
                    cloud2 = Circle(Point(linex + 50,liney + 10),40)
                    cloud2.draw(map1)
                    cloud2.setFill("gray")
                    cloud2.setOutline("gray")
                    time.sleep(0.5)
                    line.undraw()
                    cloud.undraw()
                    cloud1.undraw()
                    cloud2.undraw()
                    
                if mapbackground != "1c" and mapbackground != "2c" and mapbackground != "3c":   #checks that character is not in a portal room
                    if selection == 1: #checks that something is in the box
                        if i1 == "heart":
                            slimeHp = slimeHp + 500 #starts effect of the selected item
                            heart1.undraw()
                        elif i1 == "ice":
                            frozen = True
                            ice1.undraw()
                        elif i1 == "lightning":
                            speed()
                            lightning1.undraw()
                        i1 = ""
                        in1 = False
                    elif selection == 2:
                        if i2 == "heart":
                            slimeHp = slimeHp + 500 #starts effect of the selected item
                            heart2.undraw()
                        elif i2 == "ice":
                            frozen = True
                            ice2.undraw()
                        elif i2 == "lightning":
                            speed()
                            lightning2.undraw()
                        i2 = ""
                        in2 = False
                    elif selection == 3:
                        if i3 == "heart":
                            slimeHp = slimeHp + 500 #starts effect of the selected item
                            heart3.undraw()
                        elif i3 == "ice":
                            frozen = True
                            ice3.undraw()
                        elif i3 == "lightning":
                            speed()
                            lightning3.undraw()
                        i3 = ""
                        in3 = False
                    elif selection == 4:
                        if i4 == "heart":
                            slimeHp = slimeHp + 500 #starts effect of the selected item
                            heart4.undraw()
                        elif i4 == "ice":
                            frozen = True
                            ice4.undraw()
                        elif i4 == "lightning":
                            speed()
                            lightning4.undraw()
                        i4 = ""
                        in4 = False
                    elif selection == 5:
                        if i5 == "heart":
                            slimeHp = slimeHp + 500 #starts effect of the selected item
                            heart5.undraw()
                        elif i5 == "ice":
                            frozen = True
                            ice5.undraw()
                        elif i5 == "lightning":
                            speed()
                            lightning5.undraw()
                        i5 = ""
                        in5 = False

            if key == "f":#takes you to another map
                if mapbackground == "1a" and (sx <  50) and enemy11a == "dead" and enemy21a == "dead": #checks which map to take you to according to what map you are on and your position, and checks if all enemies are defeated
                    map1b.move(1200,0) #moves maps onscreen/offscreen
                    map1a.move(-1200,0)
                    mapbackground = "1b"
                    thread2 = MoveEnemy1()
                    thread2.start() #starts enemy1
                    thread4 = MoveEnemy3()
                    thread4.start() #starts enemy3
                    thread3 = MoveEnemy2()
                    thread3.start()#starts enemy 2
                    slime.undraw()
                    sx = 1150
                    slime = Image(Point(1150,sy),"Images/slime.png")
                    slime.draw(map1)
                    boundax=155#dorian
                    boundky=655
                    boundly=655
                    boundpx=155
                elif mapbackground == "1b" and (sx > 1150) and enemy11b == "dead" and enemy21b == "dead" and enemy31b == "dead":
                    map1a.move(1200,0)#moves maps onscreen/offscreen
                    map1b.move(-1200,0)
                    mapbackground = "1a"
                    slime.undraw()
                    sx = 50
                    slime = Image(Point(50,sy),"Images/slime.png")
                    slime.draw(map1)
                    boundax=0 #new boundaries
                    boundky=799
                    boundly=799
                    boundpx=0
                elif mapbackground == "1a" and (sx > 1150) and enemy11b == "dead" and enemy21b == "dead" and enemy31b == "dead": #checks if left room enemies are killed
                    map1c.move(-1200,0)#moves maps onscreen/offscreen
                    map1a.move(-1200,0)
                    mapbackground = "1c"
                    slime.undraw()
                    sx = 50
                    slime = Image(Point(50,sy),"Images/slime.png")
                    slime.draw(map1)
                    heart = Image(Point(300,400), "Images/heart.png")# draw items
                    if hTaken == False:
                        heart.draw(map1)
                        hx = 300
                        hy = 400
                    ice = Image(Point(300,600), "Images/freeze 1.png")
                    if iTaken == False:
                        ice.draw(map1)
                        ix = 300
                        iy = 600
                    lightning = Image(Point(300,200), "Images/lightning.png")
                    if lTaken == False:
                        lightning.draw(map1)
                        lx = 300
                        ly = 200
                    boundax=0  #new boundaries
                    bounday=345
                    boundbx=155
                    boundby=345
                    boundcx=155
                    boundcy=165
                    bounddx=530
                    bounddy=165
                    boundex=530
                    boundey=345
                    boundfx=530
                    boundfy=345
                    boundgx=530
                    boundgy=475
                    boundhx=530
                    boundhy=475
                    boundix=530
                    boundiy=655
                    boundjx=530
                    boundjy=655
                    boundkx=530
                    boundky=799
                    boundlx=155
                    boundly=655
                    boundmx=530
                    boundmy=655
                    boundnx=155
                    boundny=655
                    boundox=155
                    boundoy=475
                    boundpx=0
                    boundpy=475
                elif mapbackground == "1c" and (sx < 50):
                    map1a.move(1200,0)#moves maps onscreen/offscreen
                    map1c.move(1200,0)
                    mapbackground = "1a"
                    slime.undraw()
                    sx = 1150
                    heart.undraw()
                    ice.undraw()
                    lightning.undraw()
                    hx = 0
                    hy = 0
                    ix = 0
                    iy = 0
                    lx = 0
                    ly = 0
                    slime = Image(Point(1150,sy),"Images/slime.png")
                    slime.draw(map1)
                    boundax=0 #dorian
                    bounday=345
                    boundbx=155
                    boundby=345
                    boundcx=155
                    boundcy=165
                    bounddx=1030
                    bounddy=165
                    boundex=1030
                    boundey=345
                    boundfx=1199
                    boundfy=345
                    boundgx=1199
                    boundgy=475
                    boundhx=1030
                    boundhy=475
                    boundix=1030
                    boundiy=655
                    boundjx=705
                    boundjy=655
                    boundkx=705
                    boundky=799
                    boundlx=470
                    boundly=799
                    boundmx=470
                    boundmy=655
                    boundnx=155
                    boundny=655
                    boundox=155
                    boundoy=475
                    boundpx=0
                    boundpy=475
                elif mapbackground == "1c" and (sx > 350 and sx < 450) and (sy > 300 and sy < 500):
                    map2a.move(1200,0)#moves maps onscreen/offscreen
                    map1c.move(1200,0)
                    mapbackground = "2a"
                    heart.undraw()
                    ice.undraw()
                    lightning.undraw()
                    hx = 0
                    hy = 0
                    ix = 0
                    iy = 0
                    lx = 0
                    ly = 0
                    thread2 = MoveEnemy1()
                    thread2.start() #starts enemy1
                    thread5 = MoveRanged1()
                    thread5.start() #start the ranged 1 enemy
                    thread6 = MoveRanged2()
                    thread6.start()#starts ranged 2 enemy
                    slime.undraw()
                    sx = 600
                    sy = 400
                    slime = Image(Point(600,400),"Images/slime.png")
                    slime.draw(map1)
                    boundax=0 #new boundaries
                    bounday=345
                    boundbx=155
                    boundby=345
                    boundcx=155
                    boundcy=165
                    bounddx=1030
                    bounddy=165
                    boundex=1030
                    boundey=345
                    boundfx=1199
                    boundfy=345
                    boundgx=1199
                    boundgy=475
                    boundhx=1030
                    boundhy=475
                    boundix=1030
                    boundiy=655
                    boundjx=705
                    boundjy=655
                    boundkx=705
                    boundky=799
                    boundlx=470
                    boundly=799
                    boundmx=470
                    boundmy=655
                    boundnx=155
                    boundny=655
                    boundox=155
                    boundoy=475
                    boundpx=0
                    boundpy=475
                elif mapbackground == "2a" and (sx < 50) and enemy12a == "dead" and ranged12a == "dead" and ranged22a == "dead":
                    map2b.move(1200,0)#moves maps onscreen/offscreen
                    map2a.move(-1200,0)
                    mapbackground = "2b"
                    thread2 = MoveEnemy1()
                    thread2.start() #starts enemy1
                    thread5 = MoveRanged1()
                    thread5.start() #start the ranged 1 enemy
                    thread6 = MoveRanged2()
                    thread6.start()#starts ranged 2 enemy
                    thread7 = MoveRanged3()
                    thread7.start()#starts ranged enemy 3
                    slime.undraw()
                    sx = 1150
                    slime = Image(Point(1150,sy),"Images/slime.png")
                    slime.draw(map1)
                    boundax=0#new boundaries 
                    boundky=799
                    boundly=799
                    boundpx=0
                elif mapbackground == "2b" and (sx > 1150) and enemy12b == "dead" and ranged12b == "dead" and ranged22b == "dead" and ranged32b == "dead":
                    map2a.move(1200,0)
                    map2b.move(-1200,0)
                    mapbackground = "2a"
                    slime.undraw()
                    sx = 50
                    slime = Image(Point(50,sy),"Images/slime.png")
                    slime.draw(map1)
                    boundax=0  #new boundaries
                    bounday=345
                    boundbx=155
                    boundby=345
                    boundcx=155
                    boundcy=165
                    bounddx=1030
                    bounddy=165
                    boundex=1030
                    boundey=345
                    boundfx=1199
                    boundfy=345
                    boundgx=1199
                    boundgy=475
                    boundhx=1030
                    boundhy=475
                    boundix=1030
                    boundiy=655
                    boundjx=705
                    boundjy=655
                    boundkx=705
                    boundky=799
                    boundlx=470
                    boundly=799
                    boundmx=470
                    boundmy=655
                    boundnx=155
                    boundny=655
                    boundox=155
                    boundoy=475
                    boundpx=0
                    boundpy=475
                    hTaken = False
                    iTaken = False
                    lTaken = False
                elif mapbackground == "2a" and (sx > 1150) and enemy12b == "dead" and ranged12b == "dead" and ranged22b == "dead" and ranged32b == "dead":
                    map2c.move(-1200,0)#moves maps onscreen/offscreen
                    map2a.move(-1200,0)
                    mapbackground = "2c"
                    slime.undraw()
                    sx = 50
                    slime = Image(Point(50,sy),"Images/slime.png")
                    slime.draw(map1)
                    heart = Image(Point(300,400), "Images/heart.png")# draw items
                    if hTaken == False:
                        heart.draw(map1)
                        hx = 300
                        hy = 400
                    ice = Image(Point(300,600), "Images/freeze 1.png")
                    if hTaken == False:
                        ice.draw(map1)
                        ix = 300
                        iy = 600
                    lightning = Image(Point(300,200), "Images/lightning.png")
                    if hTaken == False:
                        lightning.draw(map1)
                        lx = 300
                        ly = 200
                    boundax=0  #new boundaries
                    bounday=345
                    boundbx=155
                    boundby=345
                    boundcx=155
                    boundcy=165
                    bounddx=530
                    bounddy=165
                    boundex=530
                    boundey=345
                    boundfx=530
                    boundfy=345
                    boundgx=530
                    boundgy=475
                    boundhx=530
                    boundhy=475
                    boundix=530
                    boundiy=655
                    boundjx=530
                    boundjy=655
                    boundkx=530
                    boundky=799
                    boundlx=155
                    boundly=655
                    boundmx=530
                    boundmy=655
                    boundnx=155
                    boundny=655
                    boundox=155
                    boundoy=475
                    boundpx=0
                    boundpy=475
                elif mapbackground == "2c" and (sx < 50):
                    map2a.move(1200,0)#moves maps onscreen/offscreen
                    map2c.move(1200,0)
                    mapbackground = "2a"
                    slime.undraw()
                    sx = 1150
                    heart.undraw()
                    ice.undraw()
                    lightning.undraw()
                    hx = 0
                    hy = 0
                    ix = 0
                    iy = 0
                    lx = 0
                    ly = 0
                    slime = Image(Point(1150,sy),"Images/slime.png")
                    slime.draw(map1)
                    boundax=0  #new boundaries
                    bounday=345
                    boundbx=155
                    boundby=345
                    boundcx=155
                    boundcy=165
                    bounddx=1030
                    bounddy=165
                    boundex=1030
                    boundey=345
                    boundfx=1199
                    boundfy=345
                    boundgx=1199
                    boundgy=475
                    boundhx=1030
                    boundhy=475
                    boundix=1030
                    boundiy=655
                    boundjx=705
                    boundjy=655
                    boundkx=705
                    boundky=799
                    boundlx=470
                    boundly=799
                    boundmx=470
                    boundmy=655
                    boundnx=155
                    boundny=655
                    boundox=155
                    boundoy=475
                    boundpx=0
                    boundpy=475
                elif mapbackground == "2c" and (sx > 350 and sx < 450) and (sy > 300 and sy < 500):
                    map3a.move(1200,0)#moves maps onscreen/offscreen
                    map2c.move(1200,0)
                    mapbackground = "3a"
                    thread2 = MoveEnemy1()
                    heart.undraw()
                    ice.undraw()
                    lightning.undraw()
                    hx = 0
                    hy = 0
                    ix = 0
                    iy = 0
                    lx = 0
                    ly = 0
                    thread2.start() #starts enemy1
                    thread3 = MoveEnemy2()
                    thread3.start()#starts enemy 2
                    thread5 = MoveRanged1()
                    thread5.start() #start the ranged 1 enemy
                    thread8 = MoveMortar1() 
                    thread8.start()#starts eye enemy 1
                    slime.undraw()
                    sx = 600
                    sy = 400
                    slime = Image(Point(600,400),"Images/slime.png")
                    slime.draw(map1)
                    boundax=0  #new boundaries
                    bounday=345
                    boundbx=155
                    boundby=345
                    boundcx=155
                    boundcy=165
                    bounddx=1030
                    bounddy=165
                    boundex=1030
                    boundey=345
                    boundfx=1199
                    boundfy=345
                    boundgx=1199
                    boundgy=475
                    boundhx=1030
                    boundhy=475
                    boundix=1030
                    boundiy=655
                    boundjx=705
                    boundjy=655
                    boundkx=705
                    boundky=799
                    boundlx=470
                    boundly=799
                    boundmx=470
                    boundmy=655
                    boundnx=155
                    boundny=655
                    boundox=155
                    boundoy=475
                    boundpx=0
                    boundpy=475
                elif mapbackground == "3a" and (sx < 50) and enemy13a == "dead" and enemy23a == "dead" and ranged13a == "dead" and mortar13a == "dead":
                    map3b.move(1200,0)#moves maps onscreen/offscreen
                    map3a.move(-1200,0)
                    mapbackground = "3b"
                    thread3 = MoveEnemy2()
                    thread3.start()#starts enemy 2
                    thread5 = MoveRanged1()
                    thread5.start()#start the ranged 1 enemy
                    thread6 = MoveRanged2()
                    thread6.start()#starts ranged 2 enemy
                    thread8 = MoveMortar1() 
                    thread8.start()#starts eye enemy 1
                    thread9 = MoveMortar2() #starts eye enemy 2
                    thread9.start()
                    slime.undraw()
                    sx = 1150
                    slime = Image(Point(1150,sy),"Images/slime.png")
                    slime.draw(map1)
                    boundax=0#new boundaries dorian
                    boundky=799
                    boundly=799
                    boundpx=0
                elif mapbackground == "3b" and (sx > 1150) and enemy23b == "dead" and ranged13b == "dead" and ranged23b == "dead" and mortar13b == "dead" and mortar23b == "dead":
                    map3a.move(1200,0)#moves maps onscreen/offscreen
                    map3b.move(-1200,0)
                    mapbackground = "3a"
                    slime.undraw()
                    sx = 50
                    slime = Image(Point(50,sy),"Images/slime.png")
                    slime.draw(map1)
                    boundax=0  #new boundaries
                    bounday=345
                    boundbx=155
                    boundby=345
                    boundcx=155
                    boundcy=165
                    bounddx=1030
                    bounddy=165
                    boundex=1030
                    boundey=345
                    boundfx=1199
                    boundfy=345
                    boundgx=1199
                    boundgy=475
                    boundhx=1030
                    boundhy=475
                    boundix=1030
                    boundiy=655
                    boundjx=705
                    boundjy=655
                    boundkx=705
                    boundky=799
                    boundlx=470
                    boundly=799
                    boundmx=470
                    boundmy=655
                    boundnx=155
                    boundny=655
                    boundox=155
                    boundoy=475
                    boundpx=0
                    boundpy=475
                elif mapbackground == "3a" and (sx > 1150) and enemy23b == "dead" and ranged13b == "dead" and ranged23b == "dead" and mortar13b == "dead" and mortar23b == "dead":
                    map3c.move(-1200,0)#moves maps onscreen/offscreen
                    map3a.move(-1200,0)
                    mapbackground = "3c"
                    slime.undraw()
                    sx = 50
                    slime = Image(Point(50,sy),"Images/slime.png")
                    slime.draw(map1)
                    boundax=0  #new boundaries
                    bounday=345
                    boundbx=155
                    boundby=345
                    boundcx=155
                    boundcy=165
                    bounddx=530
                    bounddy=165
                    boundex=530
                    boundey=345
                    boundfx=530
                    boundfy=345
                    boundgx=530
                    boundgy=475
                    boundhx=530
                    boundhy=475
                    boundix=530
                    boundiy=655
                    boundjx=530
                    boundjy=655
                    boundkx=530
                    boundky=799
                    boundlx=155
                    boundly=655
                    boundmx=530
                    boundmy=655
                    boundnx=155
                    boundny=655
                    boundox=155
                    boundoy=475
                    boundpx=0
                    boundpy=475
                elif mapbackground == "3c" and (sx < 50):
                    map3a.move(1200,0)#moves maps onscreen/offscreen
                    map3c.move(1200,0)
                    mapbackground = "3a"
                    slime.undraw()
                    sx = 1150
                    slime = Image(Point(1150,sy),"Images/slime.png")
                    slime.draw(map1)
                    boundax=0  #new boundaries
                    bounday=345
                    boundbx=155
                    boundby=345
                    boundcx=155
                    boundcy=165
                    bounddx=1030
                    bounddy=165
                    boundex=1030
                    boundey=345
                    boundfx=1199
                    boundfy=345
                    boundgx=1199
                    boundgy=475
                    boundhx=1030
                    boundhy=475
                    boundix=1030
                    boundiy=655
                    boundjx=705
                    boundjy=655
                    boundkx=705
                    boundky=799
                    boundlx=470
                    boundly=799
                    boundmx=470
                    boundmy=655
                    boundnx=155
                    boundny=655
                    boundox=155
                    boundoy=475
                    boundpx=0
                    boundpy=475
                elif mapbackground == "3c" and (sx > 350 and sx < 450) and (sy > 300 and sy < 500):
                    map3c.move(1200,0)#moves maps onscreen/offscreen
                    win = Rectangle(Point(0,0), Point(1200,800))
                    win.setFill("green")
                    win.draw(map1)
                    slime.undraw()
                    sx = 600
                    sy = 400
                    winmenu=Image(Point(600,400),"Images/gamewinscreenbackground.png")#dorian
                    winmenu.draw(map1)
                    slimewin = Image(Point(600,400),"Images/slimecrown.png")
                    slimewin.draw(map1)
                    gameendtext=Image(Point(600,400),"Images/game end.png")
                    gameendtext.draw(map1)
                    winner = True
            elif key == "x" and winner == True:    
                exit()
        lose = Image(Point(600,400),"Images/YOULOSESCREEN.png")#dorian
        lose.draw(map1)
        block = Rectangle(Point(0,700), Point(1200,800))
        block.setFill("red")
        block.draw(map1)
        time.sleep(5)
        exit()

class MoveEnemy1 (threading.Thread): #enemy movement
    def _init_ (self):
        threading.Thread._init_(self)
    def run (self):
        global e1Hp
        e1Hp = 100
        global sx
        global sy
        global e1x
        global e1y
        global frozen
        global enemy11a#checks if the enemy is alive when entering or returning to a room
        global enemy11b
        global enemy12a
        global enemy12b
        global enemy13a
        global enemy13b
        def enemy1_attack():#check for character and attack animation
            global slimeHp
            if (sx - e1x > -70 and sx - e1x < 70) and (sy - e1y > -70 and sy - e1y < 70): #checks if slime is in range
                if sx < e1x: #checks what side to attack
                    swordU = Image(Point(e1x,e1y - 38),"Images/sword swing up.png")#attack animation
                    swordU.draw(map1)
                    time.sleep(0.5)
                    slimeHp=slimeHp-10 #hurts the slime if hit
                    swordL1 = Image(Point(e1x - 29,e1y - 38),"Images/small quatre swing flipped.png")
                    swordL1.draw(map1)
                    swordU.undraw()
                    swordL2 = Image(Point(e1x - 38,e1y - 19),"Images/quatre swing flipped copy.png")
                    swordL2.draw(map1)
                    swordL1.undraw()
                    swordL3 = Image(Point(e1x - 35,e1y - 1),"Images/swing down flipped.png")
                    swordL3.draw(map1)
                    swordL2.undraw()
                    swordD = Image(Point(e1x,e1y + 38),"Images/sword swing bottom.png")
                    swordD.draw(map1)
                    swordL3.undraw()
                    time.sleep(1.5)
                    swordD.undraw()
                else:#checks what side to attack
                    swordU = Image(Point(e1x,e1y - 38),"Images/sword swing up.png")#attack animation
                    swordU.draw(map1)
                    time.sleep(0.5)
                    slimeHp=slimeHp-10  #hurts the slime if hit
                    swordR1 = Image(Point(e1x + 30,e1y - 39),"Images/small quatre swing.png")
                    swordR1.draw(map1)
                    swordU.undraw()
                    swordR2 = Image(Point(e1x + 38,e1y - 19),"Images/quatre swing.png")
                    swordR2.draw(map1)
                    swordR1.undraw()
                    swordR3 = Image(Point(e1x + 35,e1y - 1),"Images/swing down.png")
                    swordR3.draw(map1)
                    swordR2.undraw()
                    swordD = Image(Point(e1x,e1y + 38),"Images/sword swing bottom.png")
                    swordD.draw(map1)
                    swordR3.undraw()
                    time.sleep(1.5)
                    swordD.undraw()
        if mapbackground == "1a" and enemy11a == "alive": #spawns enemy at a certain position according to the room
            enemy1 = Image(Point(800,600),"Images/enemy.png")
            enemy1.draw(map1)
        elif mapbackground == "1b" and enemy11b == "alive":
            enemy1 = Image(Point(400,600),"Images/enemy.png")
            enemy1.draw(map1)
            e1Hp = 100
            e1x = 400
            e1y = 600
        elif mapbackground == "2a" and enemy12a == "alive":
            enemy1 = Image(Point(200,400),"Images/enemy.png")
            enemy1.draw(map1)
            e1Hp = 100
            e1x = 200
            e1y = 400
        elif mapbackground == "2b" and enemy12b == "alive":
            enemy1 = Image(Point(600,400),"Images/enemy.png")
            enemy1.draw(map1)
            e1Hp = 100
            e1x = 600
            e1y = 400
        elif mapbackground == "3a" and enemy13a == "alive":
            enemy1 = Image(Point(200,200),"Images/enemy.png")
            enemy1.draw(map1)
            e1Hp = 100
            e1x = 200
            e1y = 200
                
        while e1Hp > 0:#checks if enemy is alive
            if sx > e1x:#moves enemy towards the character
                enemy1.move(40,0)
                e1x = e1x + 40
            else:
                enemy1.move(-40,0)
                e1x = e1x - 40
            enemy1Hp = Text(Point(e1x,e1y - 35),e1Hp)# draws the Hp
            enemy1Hp.setFill("red")
            enemy1Hp.draw(map1)
            enemy1_attack()# function
            time.sleep(0.5)
            enemy1Hp.undraw()
            if frozen == True:# checks if the ice cube item is activated
                freeze = Image(Point(e1x,e1y),"Images/freeze 2.png")
                freeze.draw(map1)
                time.sleep(15)
                frozen = False
                freeze.undraw()
            if sy > e1y:
                enemy1.move(0,40)
                e1y = e1y + 40
            else:
                enemy1.move(0,-40)
                e1y = e1y - 40
            enemy1Hp = Text(Point(e1x,e1y - 35),e1Hp) #updates the enemy Hp
            enemy1Hp.draw(map1)
            enemy1Hp.setFill("red")
            enemy1_attack()#function
            time.sleep(0.5)
            enemy1Hp.undraw()
        enemy1.undraw()#undraws enemy when it is dead
        if mapbackground == "1a": #keeps track of death so that enemy does not respawn when re-entering a room
            enemy11a = "dead"
        elif mapbackground == "1b":
            enemy11b = "dead"
        elif mapbackground == "2a":
            enemy12a = "dead"
        elif mapbackground == "2b":
            enemy12b = "dead"
        elif mapbackground == "3a":
            enemy13a = "dead"
  
class MoveEnemy2 (threading.Thread): #exact same as MoveEnemy1, but with different variable names
    def _init_ (self):
        threading.Thread._init_(self)
    def run (self):
        global e2Hp
        e2Hp = 100
        global sx
        global sy
        global e2x
        global e2y
        global frozen
        global enemy21a #checks if the enemy is alive when entering or returning to a room
        global enemy21b
        global enemy23a
        global enemy23b
        def enemy2_attack():#check for character and attack animation
            global slimeHp
            if (sx - e2x > -70 and sx - e2x < 70) and (sy - e2y > -70 and sy - e2y < 70): #checks if the slime is in range
                if sx < e2x:#checks what side to attack
                    swordU = Image(Point(e2x,e2y - 38),"Images/sword swing up.png")#attack animation
                    swordU.draw(map1)
                    time.sleep(0.5)
                    slimeHp=slimeHp-10
                    swordL1 = Image(Point(e2x - 29,e2y - 38),"Images/small quatre swing flipped.png")
                    swordL1.draw(map1)
                    swordU.undraw()
                    swordL2 = Image(Point(e2x - 38,e2y - 19),"Images/quatre swing flipped copy.png")
                    swordL2.draw(map1)
                    swordL1.undraw()
                    swordL3 = Image(Point(e2x - 35,e2y - 1),"Images/swing down flipped.png")
                    swordL3.draw(map1)
                    swordL2.undraw()
                    swordD = Image(Point(e2x,e2y + 38),"Images/sword swing bottom.png")
                    swordD.draw(map1)
                    swordL3.undraw()
                    time.sleep(1.5)
                    swordD.undraw()
                else:
                    swordU = Image(Point(e2x,e2y - 38),"Images/sword swing up.png")#attack animation
                    swordU.draw(map1)
                    time.sleep(0.5)
                    slimeHp=slimeHp-10
                    swordR1 = Image(Point(e2x + 30,e2y - 39),"Images/small quatre swing.png")
                    swordR1.draw(map1)
                    swordU.undraw()
                    swordR2 = Image(Point(e2x + 38,e2y - 19),"Images/quatre swing.png")
                    swordR2.draw(map1)
                    swordR1.undraw()
                    swordR3 = Image(Point(e2x + 35,e2y - 1),"Images/swing down.png")
                    swordR3.draw(map1)
                    swordR2.undraw()
                    swordD = Image(Point(e2x,e2y + 38),"Images/sword swing bottom.png")
                    swordD.draw(map1)
                    swordR3.undraw()
                    time.sleep(1.5)
                    swordD.undraw()

        if mapbackground == "1a" and enemy21a == "alive": #spawns enemy at a certain position according to the room
            enemy2 = Image(Point(800,200),"Images/enemy.png")
            enemy2.draw(map1)
        elif mapbackground == "1b" and enemy21b == "alive":
            enemy2 = Image(Point(400,200),"Images/enemy.png")
            enemy2.draw(map1)
            e2Hp = 100
            e2x = 400
            e2y = 200
        elif mapbackground == "3a" and enemy23a == "alive":
            enemy2 = Image(Point(200,600),"Images/enemy.png")
            enemy2.draw(map1)
            e2Hp = 100
            e2x = 200
            e2y = 600
        elif mapbackground == "3b" and enemy23b == "alive":
            enemy2 = Image(Point(800,600),"Images/enemy.png")
            enemy2.draw(map1)
            e2Hp = 100
            e2x = 800
            e2y = 600
                
        while e2Hp > 0:# checks that enemy is alive
            if sy > e2y:
                enemy2.move(0,40)
                e2y = e2y + 40
            else:
                enemy2.move(0,-40)
                e2y = e2y - 40
            enemy2Hp = Text(Point(e2x,e2y - 35),e2Hp) #draws enemy Hp
            enemy2Hp.setFill("red")
            enemy2Hp.draw(map1)
            enemy2_attack()#function
            time.sleep(0.5)
            enemy2Hp.undraw()
            if frozen == True:
                freeze = Image(Point(e2x,e2y),"Images/freeze 2.png")#checks if ice is activated
                freeze.draw(map1)
                time.sleep(15)
                frozen = False
                freeze.undraw()
            if sx > e2x: #moves enemy towards the player
                enemy2.move(40,0)
                e2x = e2x + 40
            else:
                enemy2.move(-40,0)
                e2x = e2x - 40
            enemy2Hp = Text(Point(e2x,e2y - 35),e2Hp)#updates the Hp
            enemy2Hp.setFill("red")
            enemy2Hp.draw(map1)
            enemy2_attack()# function
            time.sleep(0.5)
            enemy2Hp.undraw()
        enemy2.undraw()# undraws enemy when it is dead
        if mapbackground == "1a": #keeps track of death so that enemy does not respawn when re-entering a room
            enemy21a = "dead"
        elif mapbackground == "1b":
            enemy21b = "dead"
        elif mapbackground == "3a":
            enemy23a = "dead"
        elif mapbackground == "3b":
            enemy23b = "dead"

class MoveEnemy3 (threading.Thread): #exact same as MoveEnemy1, but with different variable names
    def _init_ (self):
        threading.Thread._init_(self)
    def run (self):
        global e3Hp
        e3Hp = 0
        enemy3 = Image(Point(360,400),"Images/enemy.png")
        global sx
        global sy
        global e3x
        global e3y
        global frozen
        global enemy31a#checks if the enemy is alive when entering or reaaaturning to a room
        global enemy31b
        def enemy3_attack():#check for character and attack animation
            global slimeHp
            if (sx - e3x > -70 and sx - e3x < 70) and (sy - e3y > -70 and sy - e3y < 70):
                if sx < e1x:
                    swordU = Image(Point(e3x,e3y - 38),"Images/sword swing up.png")
                    swordU.draw(map1)
                    time.sleep(0.5)
                    slimeHp=slimeHp-10 #dorian
                    swordL1 = Image(Point(e3x - 29,e3y - 38),"Images/small quatre swing flipped.png")
                    swordL1.draw(map1)
                    swordU.undraw()
                    swordL2 = Image(Point(e3x - 38,e3y - 19),"Images/quatre swing flipped copy.png")
                    swordL2.draw(map1)
                    swordL1.undraw()
                    swordL3 = Image(Point(e3x - 35,e3y - 1),"Images/swing down flipped.png")
                    swordL3.draw(map1)
                    swordL2.undraw()
                    swordD = Image(Point(e3x,e3y + 38),"Images/sword swing bottom.png")
                    swordD.draw(map1)
                    swordL3.undraw()
                    time.sleep(1.5)
                    swordD.undraw()
                else:
                    swordU = Image(Point(e3x,e3y - 38),"Images/sword swing up.png")
                    swordU.draw(map1)
                    time.sleep(0.5)
                    slimeHp=slimeHp-10
                    swordR1 = Image(Point(e3x + 30,e3y - 39),"Images/small quatre swing.png")
                    swordR1.draw(map1)
                    swordU.undraw()
                    swordR2 = Image(Point(e3x + 38,e3y - 19),"Images/quatre swing.png")
                    swordR2.draw(map1)
                    swordR1.undraw()
                    swordR3 = Image(Point(e3x + 35,e3y - 1),"Images/swing down.png")
                    swordR3.draw(map1)
                    swordR2.undraw()
                    swordD = Image(Point(e3x,e3y + 38),"Images/sword swing bottom.png")
                    swordD.draw(map1)
                    swordR3.undraw()
                    time.sleep(1.5)
                    swordD.undraw()

        if mapbackground == "1b" and enemy31b == "alive":
            enemy3 = Image(Point(360,400),"Images/enemy.png")
            enemy3.draw(map1)
            e3Hp = 100
            e3x = 360
            e3y = 400
                
        while e3Hp > 0 :
            if sx > e3x:
                enemy3.move(40,0)
                e3x = e3x + 40
            else:
                enemy3.move(-40,0)
                e3x = e3x - 40
            enemy3Hp = Text(Point(e3x,e3y - 35),e3Hp)# moves towards the character
            enemy3Hp.setFill("red")
            enemy3Hp.draw(map1)
            enemy3_attack()# function
            time.sleep(0.5)
            enemy3Hp.undraw()
            if frozen == True:# checks if the ice cube item is activated
                freeze = Image(Point(e3x,e3y),"Images/freeze 2.png")
                freeze.draw(map1)
                time.sleep(15)
                frozen = False
                freeze.undraw()
            if sy > e3y:
                enemy3.move(0,40)
                e3y = e3y + 40
            else:
                enemy3.move(0,-40)
                e3y = e3y - 40
            enemy3Hp = Text(Point(e3x,e3y - 35),e3Hp) #draws the enemy Hp
            enemy3Hp.draw(map1)
            enemy3Hp.setFill("red")
            enemy3_attack()#function
            time.sleep(0.5)
            enemy3Hp.undraw()
        enemy3.undraw()
        if mapbackground == "1b":#keeps track of death so that enemy does not respawn when re-entering a room
            enemy31b = "dead"
            
class MoveRanged1 (threading.Thread): #ranged enemy movement
    def _init_ (self):
        threading.Thread._init_(self)
    def run (self):
        ranged1 = Image(Point(1000,400),"Images/ranged.png")
        global r1Hp
        r1Hpnew = 200# ranged Hp
        r1Hp = 0
        global sx
        global sy
        global r1x
        global r1y
        global frozen
        global ranged12a
        global ranged12b
        global ranged13a
        global ranged13b
        bx1 = r1x
        by1 = r1y
        global slimeHp

        if mapbackground == "2a" and ranged12a == "alive":#spawns enemy at a certain position according to the room
            ranged1 = Image(Point(1000,200),"Images/ranged.png")
            ranged1.draw(map1)
            r1Hp = 200
            r1x = 1000
            r1y = 200
        elif mapbackground == "2b" and ranged12b == "alive":
            ranged1 = Image(Point(300,200),"Images/ranged.png")
            ranged1.draw(map1)
            r1Hp = 200
            r1x = 300
            r1y = 200
        elif mapbackground == "3a" and ranged13a == "alive":
            ranged1 = Image(Point(200,400),"Images/ranged.png")
            ranged1.draw(map1)
            r1Hp = 200
            r1x = 200
            r1y = 400
        elif mapbackground == "3b" and ranged13b == "alive":
            ranged1 = Image(Point(200,300),"Images/ranged.png")
            ranged1.draw(map1)
            r1Hp = 200
            r1x = 200
            r1y = 300

        ranged1Hp = Text(Point(r1x,r1y - 35),r1Hp) #draws the enemy Hp
        ranged1Hp.draw(map1)
        ranged1Hp.setFill("red")
        while r1Hp > 0:#checks that ranged enemy is alive
            for i in range(3):#fires normal shot 3 times
                if frozen == True:#checks if ice is activated
                    freeze = Image(Point(r1x,r1y),"Images/freeze 2.png")
                    freeze.draw(map1)
                    time.sleep(15)
                    freeze.undraw()
                    frozen = False
                time.sleep(3)
                enemyR1 = Image(Point(r1x,r1y),"Images/ranged 1.png")#attack animation
                enemyR1.draw(map1)
                bx1 = r1x
                by1 = r1y
                bullet1 = Circle(Point(bx1,by1 + 10), 10)
                bullet1.draw(map1)
                bullet1.setFill("cyan")
                bMoveX1 = int((sx - r1x) / 5)#finds rise and run of the line between slime and enemy
                bMoveY1 = int((sy - r1y - 5) / 5)
                if bMoveX1 >= 100 or bMoveY1 >= 100 or bMoveX1 <= -100 or bMoveY1 <= -100: #reduces slope's x and y to smaller number around 20 - 40
                    bMoveX1 = int(round(bMoveX1 / 5))
                    bMoveY1 = int(round(bMoveY1 / 5))                
                elif bMoveX1 >= 50 or bMoveY1 >= 50 or bMoveX1 <= -50 or bMoveY1 <= -50:
                    bMoveX1 = int(round(bMoveX1 / 2.5))
                    bMoveY1 = int(round(bMoveY1 / 2.5))
                elif bMoveX1 >= 20 or bMoveY1 >= 20 or bMoveX1 <= -20 or bMoveY1 <= -20:
                    bMoveX1 = int(round(bMoveX1 * 2))
                    bMoveY1 = int(round(bMoveY1 * 2))
                else:
                    bMoveX1 = bMoveX1 * 5
                    bMoveY1 = bMoveY1 * 5
                if bMoveX1 == 0 and bMoveY1 == 0:# if slime is directly on top of enemy
                    bMoveX1 = -60
                    bMoveY1 = 0
                while (bx1 < 1200) and (bx1 > 0) and (by1 < 800) and (by1 > 0):# the bullet continues moving until it goes off screen or hits the enemy
                    bullet1.move(bMoveX1,bMoveY1)#moves bullet
                    time.sleep(0.1)
                    bx1 = bx1 + bMoveX1 #tracks where the bullets are
                    by1 = by1 + bMoveY1
                    if (sx - bx1 > -30 and sx - bx1 < 30) and (sy - by1 > -30 and sy - by1 < 30):# hurts the slime it hit
                        slimeHp=slimeHp-10 
                        break
                bullet1.undraw()
                enemyR1.undraw()
                if r1Hpnew!=r1Hp:#checks if the enemy Hp changed
                    ranged1Hp.undraw() #if it did, it updates the Hp
                    r1Hpnew=r1Hp
                    ranged1Hp = Text(Point(r1x,r1y - 35),r1Hp)
                    ranged1Hp.setFill("red")
                    ranged1Hp.draw(map1)
                if r1Hp < 1:#breaks out of loop if the enemy is dead
                    break
            if r1Hp < 1:
                break
            time.sleep(4)
            if frozen == True:# checks if ice is activated
                freeze = Image(Point(r1x,r1y),"Images/freeze 2.png")
                freeze.draw(map1)
                time.sleep(15)
                frozen = False
                freeze.undraw()
            enemyR11 = Image(Point(r1x,r1y),"Images/ranged 1.png")#animation of getting big to shoot three bullets
            enemyR11.draw(map1)
            time.sleep(0.1)
            enemyR21 = Image(Point(r1x,r1y),"Images/ranged 2.png")
            enemyR21.draw(map1)
            time.sleep(0.1)
            enemyR31 = Image(Point(r1x,r1y),"Images/ranged 3.png")
            enemyR31.draw(map1)
            time.sleep(0.5)
            bx1 = r1x
            by1 = r1y
            bulletA1 = Circle(Point(bx1,by1 - 20), 10)#draws three bullets
            bulletA1.draw(map1)
            bulletA1.setFill("cyan")
            b1x1 = r1x
            b1y1 = r1y - 20
            bullet1 = Circle(Point(bx1,by1 + 10), 10)
            bullet1.draw(map1)
            bullet1.setFill("cyan")
            bulletB1 = Circle(Point(bx1,by1 + 40), 10)
            bulletB1.draw(map1)
            bulletB1.setFill("cyan")
            b2x1 = r1x
            b2y1 = r1y + 40
            time.sleep(0.5)
               
            bMoveX1 = int((sx - r1x) / 5) #same targeting code as above
            bMoveY1 = int((sy - r1y - 5) / 5)
            if bMoveX1 >= 100 or bMoveY1 >= 100 or bMoveX1 <= -100 or bMoveY1 <= -100: #reduces slope's x and y to smaller number around 20 - 40
                bMoveX1 = int(round(bMoveX1 / 5))
                bMoveY1 = int(round(bMoveY1 / 5))                
            elif bMoveX1 >= 50 or bMoveY1 >= 50 or bMoveX1 <= -50 or bMoveY1 <= -50:
                bMoveX1 = int(round(bMoveX1 / 2.5))
                bMoveY1 = int(round(bMoveY1 / 2.5))
            elif bMoveX1 >= 20 or bMoveY1 >= 20 or bMoveX1 <= -20 or bMoveY1 <= -20:
                bMoveX1 = int(round(bMoveX1 * 2))
                bMoveY1 = int(round(bMoveY1 * 2))
            else:
                bMoveX1 = bMoveX1 * 5
                bMoveY1 = bMoveY1 * 5
            if bMoveX1 == 0 and bMoveY1 == 0:
                bMoveX1 = -60
                bMoveY1 = 0
                
            while (bx1 < 1200) and (bx1 > 0) and (by1 < 800) and (by1 > 0): #checks that the bullets are still on screen
                bulletA1.move(bMoveX1,bMoveY1 - 5)#causes the bullets to spread out when they move
                bullet1.move(bMoveX1,bMoveY1)
                bulletB1.move(bMoveX1,bMoveY1 + 5)
                time.sleep(0.1)
                
                bx1 = bx1 + bMoveX1 #tracks where the bullets are
                by1 = by1 + bMoveY1
                b1x1 = b1x1 + bMoveX1
                b1y1 = b1y1 + bMoveY1 - 5
                b2x1 = b2x1 + bMoveX1
                b2y1 = b2y1 + bMoveY1 + 5
                    
                if (sx - bx1 > -35 and sx - bx1 < 35) and (sy - by1 > -35 and sy - by1 < 35): #checks if it hits the slime
                    bullet1.undraw()
                    slimeHp=slimeHp-10# hurts the enemy if they are hit
                if (sx - b1x1 > -35 and sx - b1x1 < 35) and (sy - b1y1 > -35 and sy - b1y1 < 35):
                    bulletA1.undraw()
                    slimeHp=slimeHp-10#dorian
                if (sx - b2x1 > -35 and sx - b2x1 < 35) and (sy - b2y1 > -35 and sy - b2y1 < 35):
                    bulletB1.undraw()
                    slimeHp=slimeHp-10#dorian
            if r1Hpnew!=r1Hp:#checks if the health changes
                ranged1Hp.undraw()
                r1Hpnew=r1Hp
                ranged1Hp = Text(Point(r1x,r1y - 35),r1Hp)
                ranged1Hp.setFill("red")
                ranged1Hp.draw(map1)
            bullet1.undraw()
            bulletA1.undraw()
            bulletB1.undraw()
            enemyR31.undraw()
            time.sleep(0.2)
            enemyR21.undraw()
            time.sleep(0.2)
            enemyR11.undraw()
        ranged1Hp.undraw() #undraws the enemy when it is dead
        ranged1.undraw()
        if mapbackground == "2a":#keeps track of death so that enemy does not respawn when re-entering a room
            ranged12a = "dead"
        elif mapbackground == "2b":
            ranged12b = "dead"
        elif mapbackground == "3a":
            ranged13a = "dead"
        elif mapbackground == "3b":
            ranged13b = "dead"

class MoveRanged2 (threading.Thread): #exact same as MoveRanged1, but with different variable names
    def _init_ (self):
        threading.Thread._init_(self)
    def run (self):
        ranged2 = Image(Point(1000,400),"Images/ranged.png")
        global r2Hp
        r2Hpnew = 200
        r2Hp = 0
        global sx
        global sy
        global r2x
        global r2y
        global frozen
        global ranged22a
        global ranged22b
        global ranged23a
        global ranged23b
        bx2 = r2x
        by2 = r2y
        global slimeHp

        if mapbackground == "2a" and ranged22a == "alive":
            ranged2 = Image(Point(1000,600),"Images/ranged.png")
            ranged2.draw(map1)
            r2Hp = 200
            r2x = 1000
            r2y = 600
        elif mapbackground == "2b" and ranged22b == "alive":
            ranged2 = Image(Point(300,600),"Images/ranged.png")
            ranged2.draw(map1)
            r2Hp = 200
            r2x = 300
            r2y = 600
        elif mapbackground == "3b" and ranged23b == "alive":
            ranged2 = Image(Point(200,500),"Images/ranged.png")
            ranged2.draw(map1)
            r2Hp = 200
            r2x = 200
            r2y = 500

        ranged2Hp = Text(Point(r2x,r2y - 35),r2Hp) #draws the enemy Hp
        ranged2Hp.draw(map1)
        ranged2Hp.setFill("red")
        while r2Hp > 0:
            for i in range(3):
                if frozen == True:
                    freeze = Image(Point(r2x,r2y),"Images/freeze 2.png")
                    freeze.draw(map1)
                    time.sleep(15)
                    freeze.undraw()
                    frozen = False
                time.sleep(3)
                enemyR2 = Image(Point(r2x,r2y),"Images/ranged 1.png")
                enemyR2.draw(map1)
                bx2 = r2x
                by2 = r2y
                bullet2 = Circle(Point(bx2,by2 + 10), 10)
                bullet2.draw(map1)
                bullet2.setFill("cyan")
                bMoveX2 = int((sx - r2x) / 5)
                bMoveY2 = int((sy - r2y - 5) / 5)
                if bMoveX2 >= 100 or bMoveY2 >= 100 or bMoveX2 <= -100 or bMoveY2 <= -100: #reduces slope's x and y to smaller number around 20 - 40
                    bMoveX2 = int(round(bMoveX2 / 5))
                    bMoveY2 = int(round(bMoveY2 / 5))                
                elif bMoveX2 >= 50 or bMoveY2 >= 50 or bMoveX2 <= -50 or bMoveY2 <= -50:
                    bMoveX2 = int(round(bMoveX2 / 2.5))
                    bMoveY2 = int(round(bMoveY2 / 2.5))
                elif bMoveX2 >= 20 or bMoveY2 >= 20 or bMoveX2 <= -20 or bMoveY2 <= -20:
                    bMoveX2 = int(round(bMoveX2 * 2))
                    bMoveY2 = int(round(bMoveY2 * 2))
                else:
                    bMoveX2 = bMoveX2 * 5
                    bMoveY2 = bMoveY2 * 5
                if bMoveX2 == 0 and bMoveY2 == 0:
                    bMoveX2 = -60
                    bMoveY2 = 0
                while (bx2 < 1200) and (bx2 > 0) and (by2 < 800) and (by2 > 0):
                    bullet2.move(bMoveX2,bMoveY2)
                    time.sleep(0.1)
                    bx2 = bx2 + bMoveX2 #tracks where the bullets are
                    by2 = by2 + bMoveY2
                    if (sx - bx2 > -30 and sx - bx2 < 30) and (sy - by2 > -30 and sy - by2 < 30):
                        slimeHp=slimeHp-10 #dorian
                        break 
                bullet2.undraw()
                enemyR2.undraw()
                if r2Hpnew!=r2Hp:
                    ranged2Hp.undraw()
                    r2Hpnew=r1Hp
                    ranged2Hp = Text(Point(r2x,r2y - 35),r2Hp)
                    ranged2Hp.setFill("red")
                    ranged2Hp.draw(map1)
                if r2Hp < 1:
                    break
            if r2Hp < 1:
                break
            time.sleep(4)
            if frozen == True:
                freeze = Image(Point(r2x,r2y),"Images/freeze 2.png")
                freeze.draw(map1)
                time.sleep(15)
                frozen = False
                freeze.undraw()
            enemyR12 = Image(Point(r2x,r2y),"Images/ranged 1.png")
            enemyR12.draw(map1)
            time.sleep(0.1)
            enemyR22 = Image(Point(r2x,r2y),"Images/ranged 2.png")
            enemyR22.draw(map1)
            time.sleep(0.1)
            enemyR32 = Image(Point(r2x,r2y),"Images/ranged 3.png")
            enemyR32.draw(map1)
            time.sleep(0.5)
            bx2 = r2x
            by2 = r2y
            bulletA2 = Circle(Point(bx2,by2 - 20), 10)
            bulletA2.draw(map1)
            bulletA2.setFill("cyan")
            b1x2 = r2x
            b1y2 = r2y - 20
            bullet2 = Circle(Point(bx2,by2 + 10), 10)
            bullet2.draw(map1)
            bullet2.setFill("cyan")
            bulletB2 = Circle(Point(bx2,by2 + 40), 10)
            bulletB2.draw(map1)
            bulletB2.setFill("cyan")
            b2x2 = r2x
            b2y2 = r2y + 40
            time.sleep(0.5)
               
            bMoveX2 = int((sx - r2x) / 5)
            bMoveY2 = int((sy - r2y - 5) / 5)
            if bMoveX2 >= 100 or bMoveY2 >= 100 or bMoveX2 <= -100 or bMoveY2 <= -100: #reduces slope's x and y to smaller number around 20 - 40
                bMoveX2 = int(round(bMoveX2 / 5))
                bMoveY2 = int(round(bMoveY2 / 5))                
            elif bMoveX2 >= 50 or bMoveY2 >= 50 or bMoveX2 <= -50 or bMoveY2 <= -50:
                bMoveX2 = int(round(bMoveX2 / 2.5))
                bMoveY2 = int(round(bMoveY2 / 2.5))
            elif bMoveX2 >= 20 or bMoveY2 >= 20 or bMoveX2 <= -20 or bMoveY2 <= -20:
                bMoveX2 = int(round(bMoveX2 * 2))
                bMoveY2 = int(round(bMoveY2 * 2))
            else:
                bMoveX2 = bMoveX2 * 5
                bMoveY2 = bMoveY2 * 5
            if bMoveX2 == 0 and bMoveY2 == 0:
                bMoveX2 = -60
                bMoveY2 = 0
                
            while (bx2 < 1200) and (bx2 > 0) and (by2 < 800) and (by2 > 0):
                bulletA2.move(bMoveX2,bMoveY2 - 5)
                bullet2.move(bMoveX2,bMoveY2)
                bulletB2.move(bMoveX2,bMoveY2 + 5)
                time.sleep(0.1)
                
                bx2 = bx2 + bMoveX2 #tracks where the bullets are
                by2 = by2 + bMoveY2
                b1x2 = b1x2 + bMoveX2
                b1y2 = b1y2 + bMoveY2 - 5
                b2x2 = b2x2 + bMoveX2
                b2y2 = b2y2 + bMoveY2 + 5
                    
                if (sx - bx2 > -35 and sx - bx2 < 35) and (sy - by2 > -35 and sy - by2 < 35):
                    bullet2.undraw()
                    slimeHp=slimeHp-10 #dorian
                if (sx - b1x2 > -35 and sx - b1x2 < 35) and (sy - b1y2 > -35 and sy - b1y2 < 35):
                    bulletA2.undraw()
                    slimeHp=slimeHp-10 #dorian
                if (sx - b2x2 > -35 and sx - b2x2 < 35) and (sy - b2y2 > -35 and sy - b2y2 < 35):
                    bulletB2.undraw()
                    slimeHp=slimeHp-10 #dorian
            if r2Hpnew!=r2Hp:
                ranged2Hp.undraw()
                r2Hpnew=r2Hp
                ranged2Hp = Text(Point(r2x,r2y - 35),r2Hp)
                ranged2Hp.setFill("red")
                ranged2Hp.draw(map1) 
            bullet2.undraw()
            bulletA2.undraw()
            bulletB2.undraw()
            enemyR32.undraw()
            time.sleep(0.2)
            enemyR22.undraw()
            time.sleep(0.2)
            enemyR12.undraw()
        ranged2Hp.undraw()
        ranged2.undraw()
        if mapbackground == "2a":
            ranged22a = "dead"
        elif mapbackground == "2b":
            ranged22b = "dead"
        elif mapbackground == "3b":
            ranged23b = "dead"
            
class MoveRanged3 (threading.Thread): #exact same as MoveRanged1, but with different variable names
    def _init_ (self):
        threading.Thread._init_(self)
    def run (self):
        ranged3 = Image(Point(200,400),"Images/ranged.png")
        global r3Hp
        r3Hpnew=200
        r3Hp = 0
        global sx
        global sy
        global r3x
        global r3y
        global frozen
        global ranged32b
        bx3 = r3x
        by3 = r3y
        global slimeHp
        if mapbackground == "2b" and ranged12b == "alive":
            ranged3 = Image(Point(200,400),"Images/ranged.png")
            ranged3.draw(map1)
            r3Hp = 200
            r3x = 200
            r3y = 400
        ranged3Hp = Text(Point(r3x,r3y - 35),r3Hp) #draws the enemy Hp
        ranged3Hp.draw(map1)
        ranged3Hp.setFill("red")
        while r3Hp > 0:
            for i in range(3):
                if frozen == True:
                    freeze = Image(Point(r3x,r3y),"Images/freeze 2.png")
                    freeze.draw(map1)
                    time.sleep(15)
                    freeze.undraw()
                    frozen = False
                time.sleep(3)
                enemyR3 = Image(Point(r3x,r3y),"Images/ranged 1.png")
                enemyR3.draw(map1)
                bx3 = r3x
                by3 = r3y
                bullet3 = Circle(Point(bx3,by3 + 10), 10)
                bullet3.draw(map1)
                bullet3.setFill("cyan")
                bMoveX3 = int((sx - r3x) / 5)
                bMoveY3 = int((sy - r3y - 5) / 5)
                if bMoveX3 >= 100 or bMoveY3 >= 100 or bMoveX3 <= -100 or bMoveY3 <= -100: #reduces slope's x and y to smaller number around 20 - 40
                    bMoveX3 = int(round(bMoveX3 / 5))
                    bMoveY3 = int(round(bMoveY3 / 5))                
                elif bMoveX3 >= 50 or bMoveY3 >= 50 or bMoveX3 <= -50 or bMoveY3 <= -50:
                    bMoveX3 = int(round(bMoveX3 / 2.5))
                    bMoveY3 = int(round(bMoveY3 / 2.5))
                elif bMoveX3 >= 20 or bMoveY3 >= 20 or bMoveX3 <= -20 or bMoveY3 <= -20:
                    bMoveX3 = int(round(bMoveX3 * 2))
                    bMoveY3 = int(round(bMoveY3 * 2))
                else:
                    bMoveX3 = bMoveX3 * 5
                    bMoveY3 = bMoveY3 * 5
                if bMoveX3 == 0 and bMoveY3 == 0:
                    bMoveX3 = -60
                    bMoveY3 = 0
                while (bx3 < 1200) and (bx3 > 0) and (by3 < 800) and (by3 > 0):
                    bullet3.move(bMoveX3,bMoveY3)
                    time.sleep(0.1)
                    bx3 = bx3 + bMoveX3 #tracks where the bullets are
                    by3 = by3 + bMoveY3
                    if (sx - bx3 > -30 and sx - bx3 < 30) and (sy - by3 > -30 and sy - by3 < 30):
                        slimeHp=slimeHp-10 #dorian
                        break
                bullet3.undraw()
                enemyR3.undraw()
                if r3Hpnew!=r3Hp:
                    ranged3Hp.undraw()
                    r3Hpnew=r3Hp
                    ranged3Hp = Text(Point(r3x,r3y - 35),r3Hp)
                    ranged3Hp.setFill("red")
                    ranged3Hp.draw(map1)
                if r3Hp < 1:
                    break
            if r3Hp < 1:
                break
            time.sleep(4)
            if frozen == True:
                freeze = Image(Point(r3x,r3y),"Images/freeze 2.png")
                freeze.draw(map1)
                time.sleep(15)
                frozen = False
                freeze.undraw()
            enemyR13 = Image(Point(r3x,r3y),"Images/ranged 1.png")
            enemyR13.draw(map1)
            time.sleep(0.1)
            enemyR23 = Image(Point(r3x,r3y),"Images/ranged 2.png")
            enemyR23.draw(map1)
            time.sleep(0.1)
            enemyR33 = Image(Point(r3x,r3y),"Images/ranged 3.png")
            enemyR33.draw(map1)
            time.sleep(0.5)
            bx3 = r3x
            by3 = r3y
            bulletA3 = Circle(Point(bx3,by3 - 20), 10)
            bulletA3.draw(map1)
            bulletA3.setFill("cyan")
            b1x3 = r3x
            b1y3 = r3y - 20
            bullet3 = Circle(Point(bx3,by3 + 10), 10)
            bullet3.draw(map1)
            bullet3.setFill("cyan")
            bulletB3 = Circle(Point(bx3,by3 + 40), 10)
            bulletB3.draw(map1)
            bulletB3.setFill("cyan")
            b2x3 = r3x
            b2y3 = r3y + 40
            time.sleep(0.5) 
            bMoveX3 = int((sx - r3x) / 5)
            bMoveY3 = int((sy - r3y - 5) / 5)
            if bMoveX3 >= 100 or bMoveY3 >= 100 or bMoveX3 <= -100 or bMoveY3 <= -100: #reduces slope's x and y to smaller number around 20 - 40
                bMoveX3 = int(round(bMoveX3 / 5))
                bMoveY3 = int(round(bMoveY3 / 5))                
            elif bMoveX3 >= 50 or bMoveY3 >= 50 or bMoveX3 <= -50 or bMoveY3 <= -50:
                bMoveX3 = int(round(bMoveX3 / 2.5))
                bMoveY3 = int(round(bMoveY3 / 2.5))
            elif bMoveX3 >= 20 or bMoveY3 >= 20 or bMoveX3 <= -20 or bMoveY3 <= -20:
                bMoveX3 = int(round(bMoveX3 * 2))
                bMoveY3 = int(round(bMoveY3 * 2))
            else:
                bMoveX3 = bMoveX3 * 5
                bMoveY3 = bMoveY3 * 5
            if bMoveX3 == 0 and bMoveY3 == 0:
                bMoveX3 = -60
                bMoveY3 = 0
                    
            while (bx3 < 1200) and (bx3 > 0) and (by3 < 800) and (by3 > 0):
                bulletA3.move(bMoveX3,bMoveY3 - 5)
                bullet3.move(bMoveX3,bMoveY3)
                bulletB3.move(bMoveX3,bMoveY3 + 5)
                time.sleep(0.1)
                    
                bx3 = bx3 + bMoveX3 #tracks where the bullets are
                by3 = by3 + bMoveY3
                b1x3 = b1x3 + bMoveX3
                b1y3 = b1y3 + bMoveY3 - 5
                b2x3 = b2x3 + bMoveX3
                b2y3 = b2y3 + bMoveY3 + 5
                    
                if (sx - bx3 > -35 and sx - bx3 < 35) and (sy - by3 > -35 and sy - by3 < 35):
                    bullet3.undraw()
                    slimeHp=slimeHp-10 #dorian
                if (sx - b1x3 > -35 and sx - b1x3 < 35) and (sy - b1y3 > -35 and sy - b1y3 < 35):
                    bulletA3.undraw()
                    slimeHp=slimeHp-10 #dorian
                if (sx - b2x3 > -35 and sx - b2x3 < 35) and (sy - b2y3 > -35 and sy - b2y3 < 35):
                    bulletB3.undraw()
                    slimeHp=slimeHp-10 #dorian
            if r3Hpnew!=r3Hp:
                ranged3Hp.undraw()
                r3Hpnew=r3Hp
                ranged3Hp = Text(Point(r3x,r3y - 35),r3Hp)
                ranged3Hp.setFill("red")
                ranged3Hp.draw(map1)   
            bullet3.undraw()
            bulletA3.undraw()
            bulletB3.undraw()
            enemyR33.undraw()
            time.sleep(0.2)
            enemyR23.undraw()
            time.sleep(0.2)
            enemyR13.undraw()
        ranged3Hp.undraw()
        ranged3.undraw()
        if mapbackground == "2b":
            ranged32b = "dead"
        
class MoveMortar1 (threading.Thread): #eye enemy movement
    def _init_ (self):
        threading.Thread._init_(self)
    def run (self):
        global m1Hp #dorian
        m1Hpnew = 300 #dorian
        m1Hp = 300 #dorian
        m1Portal1 = Oval(Point(960,160), Point(1000,240))# sets the portals
        m1Portal1.setFill("cyan")
        m1Portal1.setOutline("blue")
        m1Portal2 = Oval(Point(960,560), Point(1000,640))
        m1Portal2.setFill("cyan")
        m1Portal2.setOutline("blue")
        global sx
        global sy
        global m1x
        global m1y
        global frozen
        global mortar13a
        global mortar13b
        global slimeHp
        global tx1
        global ty1
        
        if mapbackground == "3a" and mortar13a == "alive":#spawns enemy at a certain position according to the room
            mortar1 = Image(Point(960,200),"Images/eye.png")
            mortar1.draw(map1)
            m1Hp = 300
            m1x = 960
            m1y = 200
        elif mapbackground == "3b" and mortar13b == "alive":
            mortar1 = Image(Point(960,200),"Images/eye.png")
            mortar1.draw(map1)
            m1Hp = 300
            m1x = 960
            m1y = 200

        mortar1Hp = Text(Point(m1x,m1y - 35),m1Hp)# draws enemy Hp
        mortar1Hp.setFill("red")
        mortar1Hp.draw(map1)
        
        while m1Hp > 0:#Checks that it is alive
            mortar1Hp.undraw()
            m1Hpnew=m1Hp
            mortar1Hp = Text(Point(m1x,m1y - 35),m1Hp)#draws enemy Hp
            mortar1Hp.setFill("red")
            mortar1Hp.draw(map1)    
            time.sleep(5) #attack
            if m1Hpnew!=m1Hp: #dorian
                mortar1Hp.undraw()
                m1Hpnew=m1Hp
                mortar1Hp = Text(Point(m1x,m1y - 35),m1Hp)
                mortar1Hp.setFill("red")
                mortar1Hp.draw(map1)
            if frozen == True:#checks if ice is activated
                freeze = Image(Point(m1x,m1y),"Images/freeze 2.png")
                freeze.draw(map1)
                time.sleep(15)
                frozen = False
                freeze.undraw()
            eyeBlink1 = Image(Point(m1x,m1y),"Images/eye blink.png")#attack animation
            eyeBlink1.draw(map1)
            time.sleep(0.5)
            eyeAttack1 = Image(Point(m1x,m1y),"Images/eye attack.png")
            eyeAttack1.draw(map1)
            tx1 = sx
            ty1 = sy
            target1 = Oval(Point(tx1 - 50,ty1 - 30), Point(tx1 + 50,ty1 + 30))#draws target on ground
            target1.draw(map1)
            target1.setWidth(10)
            target1.setOutline("red")
            line1 = Rectangle(Point(tx1 - 6,ty1 - 70), Point(tx1 + 6,ty1 - 15))
            line1.draw(map1)
            line1.setFill("cyan")
            point1 = Oval(Point(tx1 - 10,ty1 - 6), Point(tx1 + 10, ty1 + 6))
            point1.draw(map1)
            point1.setFill("cyan")
            time.sleep(1.5)
            eyeGlow1 = Circle(Point(m1x,m1y), 8)#Lazer animation
            eyeGlow1.draw(map1)
            eyeGlow1.setFill("white")
            eyeGlow1.setWidth(6)
            eyeGlow1.setOutline("cyan")
            lazerA1 = Line(Point(m1x,m1y), Point(tx1,ty1))
            lazerA1.draw(map1)
            lazerA1.setWidth(14)
            lazerA1.setFill("cyan")
            point1.setOutline("cyan")
            lazerB1 = Line(Point(m1x,m1y), Point(tx1,ty1))
            lazerB1.draw(map1)
            lazerB1.setWidth(6)
            lazerB1.setFill("white")
            time.sleep(0.2)
            lazerA1.undraw()
            lazerB1.undraw()
            target1.undraw()
            point1.undraw()
            line1.undraw()
            eyeGlow1.undraw()
            explosionA1 = Circle(Point(tx1,ty1),20)#explosion animation
            explosionA1.draw(map1)
            explosionA1.setFill("white")
            explosionA1.setOutline("white")
            explosionB1 = Circle(Point(tx1,ty1),30)
            explosionB1.draw(map1)
            explosionB1.setFill("yellow")
            explosionB1.setOutline("yellow")
            explosionC1 = Circle(Point(tx1,ty1),40)
            explosionC1.draw(map1)
            explosionC1.setFill("orange")
            explosionC1.setOutline("orange")
            explosionD1 = Circle(Point(tx1,ty1),50)
            explosionD1.draw(map1)
            explosionD1.setFill("red")
            explosionD1.setOutline("red")
            if (sx - tx1 > -60 and sx - tx1 < 60) and (sy - ty1 > -40 and sy - ty1 < 40):#checks if the enemy was in range
                slimeHp=slimeHp-100 #hurts enemy if hit
            flash1 = Rectangle(Point(0,0), Point(1200,800))
            flash1.setFill("white")
            flash1.draw(map1)       
            explosionD1.undraw()
            explosionC1.undraw()
            explosionB1.undraw()
            explosionA1.undraw()
            time.sleep(0.1)
            flash1.undraw()
            time.sleep(1)
            if frozen == True:# checks for frozen
                freeze = Image(Point(m1x,m1y),"Images/freeze 2.png")
                freeze.draw(map1)
                time.sleep(15)
                frozen = False
                freeze.undraw()    
            eyeAttack1.undraw()
            time.sleep(0.5)
            eyeTeleport1 = Image(Point(m1x,m1y),"Images/eye teleport.png")
            eyeTeleport1.draw(map1)
            time.sleep(1)  
            eyeBlink1.undraw()
            eyeTeleport1.undraw()
            m1Portal1.draw(map1)
            m1Portal2.draw(map1)
            eyeTeleport1.draw(map1)
            mortar1.move(20,0)
            time.sleep(1)
            if m1y == 200: #teleport animation
                eyeTeleport1.undraw()
                eyeA1 = Image(Point(m1x + 5,m1y),"Images/eye 1.png")
                eyeA1.draw(map1)
                eyeD1 = Image(Point(m1x + 15,m1y + 400),"Images/eye 3.png")
                eyeD1.draw(map1)
                time.sleep(0.1)
                eyeA1.undraw()
                eyeB1 = Image(Point(m1x + 10,m1y),"Images/eye 2.png")
                eyeB1.draw(map1)
                eyeD1.undraw()
                eyeE1 = Image(Point(m1x + 10,m1y + 400),"Images/eye 2.png")
                eyeE1.draw(map1)
                time.sleep(0.1)
                eyeB1.undraw()
                eyeC1 = Image(Point(m1x + 15,m1y),"Images/eye 3.png")
                eyeC1.draw(map1)
                eyeE1.undraw()
                eyeF1 = Image(Point(m1x + 5,m1y + 400),"Images/eye 1.png")
                eyeF1.draw(map1)
                time.sleep(0.1)
                eyeC1.undraw()
                eyeF1.undraw()
                mortar1.move(0,400)
                m1y = m1y + 400
                mortar1.move(-20,0)
                eyeTeleport1 = Image(Point(m1x,m1y),"Images/eye teleport.png")
                eyeTeleport1.draw(map1)
                time.sleep(1)
                m1Portal1.undraw()
                m1Portal2.undraw()
                eyeBlink1 = Image(Point(m1x,m1y),"Images/eye blink.png")
                eyeBlink1.draw(map1)
                eyeTeleport1.undraw()
                time.sleep(0.5)
                eyeBlink1.undraw()
            else:
                eyeTeleport1.undraw()#teleport animation
                eyeF1 = Image(Point(m1x + 5,m1y),"Images/eye 1.png")
                eyeF1.draw(map1)
                eyeC1 = Image(Point(m1x + 15,m1y - 400),"Images/eye 3.png")
                eyeC1.draw(map1)
                time.sleep(0.1)
                eyeF1.undraw()
                eyeE1 = Image(Point(m1x + 10,m1y),"Images/eye 2.png")
                eyeE1.draw(map1)
                eyeC1.undraw()
                eyeB1 = Image(Point(m1x + 10,m1y - 400),"Images/eye 2.png")
                eyeB1.draw(map1)
                time.sleep(0.1)
                eyeE1.undraw()
                eyeD1 = Image(Point(m1x + 15,m1y),"Images/eye 3.png")
                eyeD1.draw(map1)
                eyeB1.undraw()
                eyeA1 = Image(Point(m1x + 5,m1y - 400),"Images/eye 1.png")
                eyeA1.draw(map1)
                time.sleep(0.1)
                eyeD1.undraw()
                eyeA1.undraw()
                mortar1.move(0,-400)
                m1y = m1y - 400
                mortar1.move(-20,0)
                eyeTeleport1 = Image(Point(m1x,m1y),"Images/eye teleport.png")
                eyeTeleport1.draw(map1)
                time.sleep(1)
                m1Portal1.undraw()
                m1Portal2.undraw()
                eyeBlink1 = Image(Point(m1x,m1y),"Images/eye blink.png")
                eyeBlink1.draw(map1)
                eyeTeleport1.undraw()
                time.sleep(0.5)
                eyeBlink1.undraw()
        mortar1Hp.undraw()# undraws if enemy is dead
        mortar1.undraw()
        if mapbackground == "3a":#keeps track of death so that enemy does not respawn when re-entering a room
            mortar13a = "dead"
        elif mapbackground == "3b":
            mortar13b = "dead"

class MoveMortar2 (threading.Thread): #exact same as MoveMortar1, but with different variable names
    def _init_ (self):
        threading.Thread._init_(self)
    def run (self):
        global m2Hp #dorian
        m2Hpnew = 300 #dorian
        m2Hp = 300 #dorian
        mortar2 = Image(Point(240,200),"Images/eye.png")
        mortar2.draw(map1)
        m2Portal1 = Oval(Point(240,160), Point(280,240))
        m2Portal1.setFill("cyan")
        m2Portal1.setOutline("blue")
        m2Portal2 = Oval(Point(240,560), Point(280,640))
        m2Portal2.setFill("cyan")
        m2Portal2.setOutline("blue")
        global sx
        global sy
        global m2x
        global m2y
        global frozen
        global mortar23b
        time.sleep(7)
        mortar2.undraw()
        global ty2
        global tx2
        global slimeHp

        if mapbackground == "3b" and mortar23b == "alive":#spawns enemy at a certain position according to the room
            mortar2 = Image(Point(240,200),"Images/eye.png")
            mortar2.draw(map1)
            m2Hp = 300
            m2x = 240
            m2y = 200

        mortar2Hp = Text(Point(m2x,m2y - 35),m2Hp)# moves towards the character
        mortar2Hp.setFill("red")
        mortar2Hp.draw(map1)
            
        while m2Hp > 0: #dorian
            #if m2Hpnew!=m2Hp:
            mortar2Hp.undraw()
            m2Hpnew=m2Hp
            mortar2Hp = Text(Point(m2x,m2y - 35),m2Hp)
            mortar2Hp.setFill("red")
            mortar2Hp.draw(map1)    
            time.sleep(5) #attack
            if m2Hpnew!=m2Hp:
                mortar2Hp.undraw()
                m2Hpnew=m2Hp
                mortar2Hp = Text(Point(m2x,m2y - 35),m2Hp)
                mortar2Hp.setFill("red")
                mortar2Hp.draw(map1) 
            if frozen == True:
                freeze = Image(Point(m2x,m2y),"Images/freeze 2.png")
                freeze.draw(map1)
                time.sleep(15)
                frozen = False
                freeze.undraw()
            eyeBlink2 = Image(Point(m2x,m2y),"Images/eye blink.png")
            eyeBlink2.draw(map1)
            time.sleep(0.5)
            eyeAttack2 = Image(Point(m2x,m2y),"Images/eye attack.png")
            eyeAttack2.draw(map1)
            tx2 = sx
            ty2 = sy
            target2 = Oval(Point(tx2 - 50,ty2 - 30), Point(tx2 + 50,ty2 + 30))
            target2.draw(map1)
            target2.setWidth(10)
            target2.setOutline("red")
            line2 = Rectangle(Point(tx2 - 6,ty2 - 70), Point(tx2 + 6,ty2 - 15))
            line2.draw(map1)
            line2.setFill("cyan")
            point2 = Oval(Point(tx2 - 10,ty2 - 6), Point(tx2 + 10, ty2 + 6))
            point2.draw(map1)
            point2.setFill("cyan")
            time.sleep(1.5)
            eyeGlow2 = Circle(Point(m2x,m2y), 8)
            eyeGlow2.draw(map1)
            eyeGlow2.setFill("white")
            eyeGlow2.setWidth(6)
            eyeGlow2.setOutline("cyan")
            lazerA2 = Line(Point(m2x,m2y), Point(tx2,ty2))
            lazerA2.draw(map1)
            lazerA2.setWidth(14)
            lazerA2.setFill("cyan")
            point2.setOutline("cyan")
            lazerB2 = Line(Point(m2x,m2y), Point(tx2,ty2))
            lazerB2.draw(map1)
            lazerB2.setWidth(6)
            lazerB2.setFill("white")
            time.sleep(0.2)
            lazerA2.undraw()
            lazerB2.undraw()
            target2.undraw()
            point2.undraw()
            line2.undraw()
            eyeGlow2.undraw()
            explosionA2 = Circle(Point(tx2,ty2),20)
            explosionA2.draw(map1)
            explosionA2.setFill("white")
            explosionA2.setOutline("white")
            explosionB2 = Circle(Point(tx2,ty2),30)
            explosionB2.draw(map1)
            explosionB2.setFill("yellow")
            explosionB2.setOutline("yellow")
            explosionC2 = Circle(Point(tx2,ty2),40)
            explosionC2.draw(map1)
            explosionC2.setFill("orange")
            explosionC2.setOutline("orange")
            explosionD2 = Circle(Point(tx2,ty2),50)
            explosionD2.draw(map1)
            explosionD2.setFill("red")
            explosionD2.setOutline("red")
            if (sx - tx2 > -60 and sx - tx2 < 60) and (sy - ty2 > -40 and sy - ty2 < 40):
                slimeHp=slimeHp-100 #dorian
            flash2 = Rectangle(Point(0,0), Point(1200,800))
            flash2.setFill("white")
            flash2.draw(map1)       
            explosionD2.undraw()
            explosionC2.undraw()
            explosionB2.undraw()
            explosionA2.undraw()
            time.sleep(0.1)
            flash2.undraw()
            time.sleep(1)
            if frozen == True:
                freeze = Image(Point(m2x,m2y),"Images/freeze 2.png")
                freeze.draw(map1)
                time.sleep(15)
                frozen = False
                freeze.undraw()    
            eyeAttack2.undraw()
            time.sleep(0.5)
            eyeTeleport2 = Image(Point(m2x,m2y),"Images/eye teleport.png")
            eyeTeleport2.draw(map1)
            time.sleep(1)  
            eyeBlink2.undraw()
            eyeTeleport2.undraw()
            m2Portal1.draw(map1)
            m2Portal2.draw(map1)
            eyeTeleport2.draw(map1)
            mortar2.move(20,0)
            time.sleep(1)
            if m2y == 200: #teleport animation
                eyeTeleport2.undraw()
                eyeA2 = Image(Point(m2x + 5,m2y),"Images/eye 1.png")
                eyeA2.draw(map1)
                eyeD2 = Image(Point(m2x + 15,m2y + 400),"Images/eye 3.png")
                eyeD2.draw(map1)
                time.sleep(0.1)
                eyeA2.undraw()
                eyeB2 = Image(Point(m2x + 10,m2y),"Images/eye 2.png")
                eyeB2.draw(map1)
                eyeD2.undraw()
                eyeE2 = Image(Point(m2x + 10,m2y + 400),"Images/eye 2.png")
                eyeE2.draw(map1)
                time.sleep(0.1)
                eyeB2.undraw()
                eyeC2 = Image(Point(m2x + 15,m2y),"Images/eye 3.png")
                eyeC2.draw(map1)
                eyeE2.undraw()
                eyeF2 = Image(Point(m2x + 5,m2y + 400),"Images/eye 1.png")
                eyeF2.draw(map1)
                time.sleep(0.1)
                eyeC2.undraw()
                eyeF2.undraw()
                mortar2.move(0,400)
                m2y = m2y + 400
                mortar2.move(-20,0)
                eyeTeleport2 = Image(Point(m2x,m2y),"Images/eye teleport.png")
                eyeTeleport2.draw(map1)
                time.sleep(1)
                m2Portal1.undraw()
                m2Portal2.undraw()
                eyeBlink2 = Image(Point(m2x,m2y),"Images/eye blink.png")
                eyeBlink2.draw(map1)
                eyeTeleport2.undraw()
                time.sleep(0.5)
                eyeBlink2.undraw()
            else:
                eyeTeleport2.undraw()
                eyeF2 = Image(Point(m2x + 5,m2y),"Images/eye 1.png")
                eyeF2.draw(map1)
                eyeC2 = Image(Point(m2x + 15,m2y - 400),"Images/eye 3.png")
                eyeC2.draw(map1)
                time.sleep(0.1)
                eyeF2.undraw()
                eyeE2 = Image(Point(m2x + 10,m2y),"Images/eye 2.png")
                eyeE2.draw(map1)
                eyeC2.undraw()
                eyeB2 = Image(Point(m2x + 10,m2y - 400),"Images/eye 2.png")
                eyeB2.draw(map1)
                time.sleep(0.1)
                eyeE2.undraw()
                eyeD2 = Image(Point(m2x + 15,m2y),"Images/eye 3.png")
                eyeD2.draw(map1)
                eyeB2.undraw()
                eyeA2 = Image(Point(m2x + 5,m2y - 400),"Images/eye 1.png")
                eyeA2.draw(map1)
                time.sleep(0.1)
                eyeD2.undraw()
                eyeA2.undraw()
                mortar2.move(0,-400)
                m2y = m2y - 400
                mortar2.move(-20,0)
                eyeTeleport2 = Image(Point(m2x,m2y),"Images/eye teleport.png")
                eyeTeleport2.draw(map1)
                time.sleep(1)
                m2Portal1.undraw()
                m2Portal2.undraw()
                eyeBlink2 = Image(Point(m2x,m2y),"Images/eye blink.png")
                eyeBlink2.draw(map1)
                eyeTeleport2.undraw()
                time.sleep(0.5)
                eyeBlink2.undraw()
        mortar2Hp.undraw()
        mortar2.undraw()
        if mapbackground == "3b":
            mortar23b = "dead"
                
thread10 = TheActualGame()#starts the game thread
thread10.start()
map1.mainloop()


