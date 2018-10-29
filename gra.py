import pygame, sys, time, random, math
pygame.init()
font1 = pygame.font.SysFont(None,40)
font2 = pygame.font.Font("Xefus.ttf",100)
font3 = pygame.font.SysFont(None,10)
font4 = pygame.font.Font("Xefus.ttf",40)
font5 = pygame.font.SysFont(None,100)
move = 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,800))
hiscore = open("hiscore.txt").read()
def wypis_na_ekran(txt, kolor, X, Y,font):
    text = font.render(str(txt), True, kolor)
    screen.blit(text, [X, Y])
tlo = pygame.image.load("space.png")
ship = pygame.image.load("statek.png")
boom = pygame.image.load("boom.png")
stdbullet = pygame.image.load("bullet.png")
menu = pygame.image.load("menu.png")
bullet = stdbullet
bullet1 = pygame.image.load("bullet1.png")
bullet2 = pygame.image.load("bullet2.png")
boss1 =  pygame.image.load("boss1.png")
bossbroke = pygame.image.load("bossbroke.png")
boss = boss1
boss1hit = pygame.image.load("boss1hit.png")
bosslaser = pygame.image.load("bosslaser.png")
bosslaserhit = pygame.image.load("bosslaserhit.png")
invader1 = pygame.image.load("invader.png")
invader2 = pygame.image.load("invader1.png")
invader = invader1
bosstime = 0
anim = time.clock()
actv = 0
invbullet = pygame.image.load("enemybullet.png")
atkup = pygame.image.load("atkup.png")
speedup = pygame.image.load("speedup.png")
superup = pygame.image.load("superup.png")
frqup = pygame.image.load("frqup.png")
heart = pygame.image.load("heart.png")
lazer = pygame.image.load("laser.png")
prelaser = pygame.image.load("prelaser.png")
laser = 0
upgr = pygame.mixer.Sound("upgr.wav")
invdestr = pygame.mixer.Sound("invdestr.wav")
dead = pygame.mixer.Sound("dead.wav")
lazersound = pygame.mixer.Sound("weaponfire11.wav")
sound1 = pygame.mixer.Sound("laser1.wav")
sound = sound1
sound2 = pygame.mixer.Sound("laser2.wav")
sound3 = pygame.mixer.Sound("laser3.wav")
sound4 = pygame.mixer.Sound("laser4.wav")
invader_height = invader.get_height()
invader_width = invader.get_width()
ship_top = screen.get_height() - ship.get_height()
ship_left = (screen.get_width() /2) - (ship.get_width() /2)
bullet_width = bullet.get_width()
game = 0
help = 0
lasertimer = 0
credits = 0
invaders_x = []
invaders_y = []
invaders_hp = []
invbullet_x = []
invbullet_y = []
invbullet_time = []
bullet_y = []
bullet_x = []
bullet_time = []
powerups_x = []
powerups_y = []
powerups_type = []
boom_x = []
boom_y = []
boom_time = []
liczbainv=30
invhp = 1
dmg=1
k=1
for i in range(100):
    if(i<liczbainv):
            invaders_x.append((invader_width+10)*(i%10)+0.5)
            invaders_y.append(10+(i//10)*invader_height)
            invaders_hp.append(invhp)
            boom_x.append(0)
            boom_y.append(0)
            boom_time.append(0)
    powerups_x.append(0)
    powerups_y.append(0)
    powerups_type.append(4)
    bullet_x.append(0)
    invbullet_x.append(0)
    bullet_y.append(0)
    invbullet_y.append(0)
    bullet_time.append(0)
    invbullet_time.append(0)
pygame.display.set_caption('Space Pew Pew')
pygame.display.set_icon(invader)
while True:
    if(game==0):
        clock.tick(60)
        x, y = pygame.mouse.get_pos()
        screen.blit(menu,(0,0))
        if (help == 1):
            tekst1 = "In this game your objective is to survive as long as you can."
            tekst2 = "Controls: Click LPM to shoot, use your mouse to move."
            tekst3 = "While you will be playing, there is a chance that your enemy "
            tekst4 = "will drop power-ups, here is a list of them:"
            tekst5 = "- increases your damage."
            tekst6 = "- increases the speed of your bullets."
            tekst7 = "- decreases the time between your shots"
            tekst8 = "- increases players health "
            tekst9 = "<--- Go back"
            if (x >= 40 and x <= 200 and y>=50 and y<=75):
                wypis_na_ekran(tekst9, (255, 0, 0),40,50 , font1)
            else:
                wypis_na_ekran(tekst9, (0, 0, 0),40 ,50 , font1)
            wypis_na_ekran(tekst1, (0, 0, 0), 100, 100, font1)
            wypis_na_ekran(tekst2, (0, 0, 0), 100, 150, font1)
            wypis_na_ekran(tekst3, (0, 0, 0), 100, 200, font1)
            wypis_na_ekran(tekst4, (0, 0, 0), 100, 250, font1)
            screen.blit(atkup,(100, 300))
            wypis_na_ekran(tekst5, (0, 0, 0), 140, 315, font1)
            screen.blit(speedup, (100, 350))
            wypis_na_ekran(tekst6, (0, 0, 0), 140, 365, font1)
            screen.blit(frqup, (100, 400))
            wypis_na_ekran(tekst7, (0, 0, 0), 140, 415, font1)
            screen.blit(heart, (100, 450))
            wypis_na_ekran(tekst8, (0, 0, 0), 140, 465, font1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif(x >= 40 and x <= 200 and y>=50 and y<=75 and event.type == pygame.MOUSEBUTTONDOWN ):
                    help = 0
        elif(credits==1):
            tekst1 = "<--- Go back"
            tekst2 = "Main and only creator: Olaf Boczarski"
            tekst3 = "Sound provider: Bartosz Kunat"
            tekst4 = "Zrobiłem creditsy bo taka była umowa z Bartkiem :)"
            wypis_na_ekran(tekst2, (0, 0, 0), 100, 300, font1)
            wypis_na_ekran(tekst3, (255, 215, 0), 100, 350, font1)
            wypis_na_ekran(tekst4, (0, 0, 0), 100, 400, font3)
            if (x >= 40 and x <= 200 and y>=50 and y<=75):
                wypis_na_ekran(tekst1, (255, 0, 0),40,50 , font1)
            else:
                wypis_na_ekran(tekst1, (0, 0, 0),40 ,50 , font1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif(x >= 40 and x <= 200 and y>=50 and y<=75 and event.type == pygame.MOUSEBUTTONDOWN ):
                    credits = 0
        else:
            tekst1 = "Start"
            tekst2 = "Help"
            tekst3 = "Credits"
            if(x>=screen.get_width() / 2 -100 and x<=screen.get_width()/2 + 145 and y>=100 and y<=190 ):
                wypis_na_ekran(tekst1, (255, 0, 0), screen.get_width() / 2 - 100, 100, font2)
            else:
                wypis_na_ekran(tekst1, (0, 0, 0), screen.get_width() / 2 -100, 100,font2)
            if(x>=screen.get_width() / 2 -100 and x<=screen.get_width()/2 + 60 and y>=200 and y<=290):
                wypis_na_ekran(tekst2, (255, 0, 0), screen.get_width() / 2 -100, 200,font2)
            else:
                wypis_na_ekran(tekst2, (0, 0, 0), screen.get_width() / 2 - 100, 200, font2)
            if(x>=screen.get_width() / 2 -100 and x<=screen.get_width()/2 + 185 and y>=300 and y<=390):
                wypis_na_ekran(tekst3, (255, 0, 0), screen.get_width() / 2 - 100, 300, font2)
            else:
                wypis_na_ekran(tekst3, (0, 0, 0), screen.get_width() / 2 - 100, 300, font2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if(x>=screen.get_width() / 2 -100 and x<=screen.get_width()/2 + 145 and y>=100 and y<=190 and event.type == pygame.MOUSEBUTTONDOWN ):
                    lose = 0
                    sound = sound1
                    bullet = stdbullet
                    boss = boss1
                    lose = 0
                    score = 0
                    block = 0
                    nextlvl = 0
                    start = 1
                    atkchng = 0
                    lvl = 1
                    bosslvl = 0
                    bosstart = 1
                    boss_x = 0
                    boss_y = 0
                    boss_hp = 100
                    speed = 10
                    frq = 0.25
                    hpplayer = 3
                    invhp = 1
                    chance = 1
                    liczbainv = 30
                    speedinv = 0.5
                    block = 0
                    dmg=1
                    game = 1
                    for i in range(liczbainv):
                        invaders_x.insert(i, (invader_width + 10) * (i % 10) + 0.5)
                        invaders_y.insert(i, 10 + (i // 10) * invader_height)
                        invaders_hp.insert(i, invhp)
                    for i in range(100):
                        bullet_x[i] = 0
                        bullet_y[i] = 0
                        bullet_time[i] = 0
                        invbullet_x[i] = 0
                        invbullet_y[i] = 0
                        invbullet_time[i] = 0
                        powerups_x[i] = 0
                        powerups_y[i] = 0
                        powerups_type[i] = 4
                elif(x>=screen.get_width() / 2 -100 and x<=screen.get_width()/2 + 60 and y>=200 and y<=290 and event.type == pygame.MOUSEBUTTONDOWN ):
                    help = 1
                elif(x>=screen.get_width() / 2 -100 and x<=screen.get_width()/2 + 185 and y>=300 and y<=390 and event.type == pygame.MOUSEBUTTONDOWN ):
                    credits = 1
        pygame.display.update()
    elif(game==1):
        if(start==1):
            screen.blit(tlo, (0, 0))
            screen.blit(ship, (ship_left, ship_top))
            start = 0
            pygame.mouse.set_visible(0)
        if(lose==1):
            tekst1 = "You lost."
            tekst2 = "Press Q to quit, C to play again or M to get to the main menu."
            tekst3 = "Highscore : "
            wypis_na_ekran("Score: " + str(score), (255, 0, 255), 0, 0,font1)
            wypis_na_ekran("Level: " + str(lvl), (255, 0, 255), 0, 30,font1)
            if(score>=int(hiscore)):
                open("hiscore.txt","w").write(str(score))
            screen.blit(heart, (screen.get_width() - 100, screen.get_height() - 100))
            wypis_na_ekran(str(hpplayer), (255, 255, 255), screen.get_width() - 87, screen.get_height() - 93,font1)
            wypis_na_ekran(tekst1, (255, 0, 0), screen.get_width() / 2 - 150, screen.get_height() / 2 - 100,font5)
            wypis_na_ekran(tekst2, (255, 255, 0), screen.get_width() / 2 - 430, screen.get_height() / 2 + 40,font1)
            wypis_na_ekran(tekst3 + hiscore, (255, 255, 255), screen.get_width() / 2 - 140, screen.get_height() / 2 + 70, font1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    elif event.key == pygame.K_c:
                        lose = 0
                        sound = sound1
                        bullet = stdbullet
                        boss = boss1
                        lose = 0
                        score = 0
                        block = 0
                        nextlvl = 0
                        start = 1
                        atkchng = 0
                        lvl = 1
                        bosslvl = 0
                        bosstart = 1
                        boss_x = 0
                        boss_y = 0
                        boss_hp = 100
                        speed = 10
                        frq = 0.25
                        hpplayer = 3
                        invhp = 1
                        chance = 1
                        liczbainv = 30
                        speedinv = 0.5
                        block = 0
                        dmg=1
                        liczbainv = 30
                        for i in range(liczbainv):
                            invaders_x.insert(i,(invader_width + 10) * (i % 10) + 0.5)
                            invaders_y.insert(i,10 + (i // 10) * invader_height)
                            invaders_hp.insert(i,invhp)
                        for i in range(100):
                            bullet_x[i] = 0
                            bullet_y[i] = 0
                            bullet_time[i] = 0
                            invbullet_x[i] = 0
                            invbullet_y[i] = 0
                            invbullet_time[i] = 0
                            powerups_x[i] = 0
                            powerups_y[i] = 0
                            powerups_type[i] = 4
                    elif event.key == pygame.K_m:
                        pygame.mouse.set_visible(1)
                        game=0
        elif(lose==0):
            clock.tick(60)
            if (nextlvl == 1):
                liczbainv = 30
                speedinv = math.fabs(speedinv) + 0.5
                invhp += 1
                hpplayer += 1
                chance += 1
                block = 0
                lvl += 1
                nextlvl = 0
                for i in range(liczbainv):
                    invaders_x.append((invader_width + 10) * (i % 10) + speedinv)
                    invaders_y.append(10 + (i // 10) * invader_height)
                    invaders_hp.append(invhp)
                if (lvl % 10 == 0):
                    speedinv = math.fabs(speedinv) - 3.5
                    invhp -= 7
                    chance -= 7
                    bosslvl = 1
                    bosstart = 1
                    lasertimer = time.clock()
                    boss_hp=lvl*10+ 60*dmg
                    tmp = boss_hp
            screen.blit(tlo, (0, 0))
            wypis_na_ekran("Score: "+str(score),(255,0,255),0,0,font1)
            wypis_na_ekran("Level: " + str(lvl), (255, 0, 255), 0, 30,font1)
            screen.blit(heart, (screen.get_width()-100, screen.get_height()-100))
            if(time.clock()- anim >=1):
                if(actv==0):
                    invader=invader1
                    actv=1
                else:
                    invader=invader2
                    actv=0
                anim = time.clock()
            if(hpplayer<10):
                wypis_na_ekran(str(hpplayer), (255, 255, 255), screen.get_width() + heart.get_width() / 2 - 107, screen.get_height() + heart.get_height() / 2 - 111,font1)
            elif(hpplayer>=10):
                wypis_na_ekran(str(hpplayer), (255, 255, 255), screen.get_width() + heart.get_width() / 2 - 115,screen.get_height() + heart.get_height() / 2 - 111,font1)
            wypis_na_ekran("DMG:"+str(dmg), (255, 0, 0), screen.get_width() - 120, screen.get_height() - 150,font1)
            wypis_na_ekran("SPD:"+str(speed), (255, 0, 0), screen.get_width() - 120, screen.get_height() - 200,font1)
            wypis_na_ekran("FRQ:" + str(1/frq), (255, 0, 0), screen.get_width() - 120, screen.get_height() - 250,font1)
            x,y = pygame.mouse.get_pos()
            screen.blit(ship, (x-ship.get_width()/2,ship_top))
            if(dmg>=5 and dmg <10 and atkchng == 0):
                bullet = bullet1
                sound = sound1
                atkchng = 1
            elif(dmg==10):
                bullet = bullet2
                sound = sound2
                atkchng = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif(event.type == pygame.MOUSEBUTTONDOWN and time.clock() - bullet_time[0] >= frq):
                    sound.play()
                    bullet_y.insert(0,ship_top)
                    bullet_y.pop(100)
                    bullet_x.insert(0, x-7)
                    bullet_x.pop(100)
                    bullet_time.insert(0,time.clock())
                    bullet_time.pop(100)
            if(pygame.mouse.get_pressed()[0] == 1 and time.clock() - bullet_time[0] >= frq):
                sound.play()
                bullet_y.insert(0, ship_top)
                bullet_y.pop(100)
                bullet_x.insert(0, x - 7)
                bullet_x.pop(100)
                bullet_time.insert(0, time.clock())
                bullet_time.pop(100)
            specialone = random.randint(0, liczbainv - 1)
            chancetoshoot = random.randint(0, 300)
            if(chancetoshoot<=chance and bosslvl == 0):
                sound4.play()
                invbullet_y.insert(0,invaders_y[specialone])
                invbullet_y.pop(100)
                invbullet_x.insert(0, invaders_x[specialone]+ 20)
                invbullet_x.pop(100)
                invbullet_time.insert(0, time.clock())
                invbullet_time.pop(100)
            elif(2>=random.randint(1,100) and bosslvl == 1):
                sound4.play()
                invbullet_y.insert(0, boss_y + boss.get_width()/2 - 100)
                invbullet_y.insert(0, boss_y + boss.get_width() / 2 - 100)
                invbullet_y.insert(0, boss_y + boss.get_width() / 2 - 100)
                invbullet_y.insert(0, boss_y + boss.get_width() / 2 - 100)
                invbullet_y.pop(100)
                invbullet_y.pop(100)
                invbullet_y.pop(100)
                invbullet_y.pop(100)
                invbullet_x.insert(0, boss_x + 190)
                invbullet_x.insert(0, boss_x + 190)
                invbullet_x.insert(0, boss_x + 190)
                invbullet_x.insert(0, boss_x + 190)
                invbullet_x.pop(100)
                invbullet_x.pop(100)
                invbullet_x.pop(100)
                invbullet_x.pop(100)
                invbullet_time.insert(0, time.clock())
                invbullet_time.insert(0, time.clock())
                invbullet_time.insert(0, time.clock())
                invbullet_time.insert(0, time.clock())
                invbullet_time.pop(100)
                invbullet_time.pop(100)
                invbullet_time.pop(100)
                invbullet_time.pop(100)
            for i in range(len(bullet_x)):
                if(invbullet_x[i]<= x + ship.get_width()/2 and invbullet_x[i] + invbullet.get_width() >= x - ship.get_width()/2 and invbullet_y[i] >= ship_top  and invbullet_y[i]<=ship_top + ship.get_height()):
                    hpplayer-=1
                    invbullet_y.pop(i)
                    invbullet_y.insert(i,0)
                    invbullet_x.pop(i)
                    invbullet_x.insert(i,0)
                    invbullet_time.pop(i)
                    invbullet_time.insert(i,0)
                    if(hpplayer==0):
                        dead.play()
                        screen.blit(boom,(x-20,ship_top+15))
                        lose = 1
                if (powerups_x[i] <= x + ship.get_width()/2  and powerups_x[i] + atkup.get_width() >= x - ship.get_width()/2   and powerups_y[i] >= ship_top and powerups_y[i]<=ship_top + ship.get_height()):
                    upgr.play()
                    powerups_y.pop(i)
                    powerups_y.insert(i,0)
                    powerups_x.pop(i)
                    powerups_x.insert(i,0)
                    if(powerups_type[i]==0):
                        hpplayer+=1
                    elif(powerups_type[i] == 1):
                        if(speed<=80):
                            speed+=2.5
                        else:
                            score+=20
                    elif(powerups_type[i] == 2):
                        dmg+=1
                    elif(powerups_type[i] == 3):
                        if(frq>=0.1):
                            frq-=0.005
                        else:
                            score+=20
                    powerups_type.pop(i)
                    powerups_type.insert(i,4)
                j=0
                while(j<liczbainv):
                    if(bullet_x[i] <= invaders_x[j] + invader_width and bullet_x[i]>= invaders_x[j] and bullet_y[i] <= invaders_y[j] + invader_height and bullet_y[i]>=invaders_y[j] and bosslvl ==0):
                        bullet_y.pop(i)
                        bullet_y.insert(i,0)
                        bullet_x.pop(i)
                        bullet_x.insert(i,0)
                        bullet_time.pop(i)
                        bullet_time.insert(i,0)
                        invaders_hp[j]-=dmg
                        if(invaders_hp[j]<0):
                            invdestr.play()
                            if(random.randint(0,100)<=10):
                                a = invaders_x.pop(j)
                                b = invaders_y.pop(j)
                                invaders_hp.pop(j)
                                liczbainv -= 1
                                score += lvl * 10
                                powerups_x.insert(0,a+10)
                                boom_x.insert(0,a+10)
                                powerups_x.pop()
                                boom_x.pop()
                                powerups_y.insert(0,b)
                                boom_y.insert(0,b)
                                boom_y.pop()
                                boom_time.insert(0,time.clock())
                                boom_time.pop()
                                powerups_type.insert(0,random.randint(0,3))
                                powerups_type.pop()
                                if (liczbainv <= 0):
                                    nextlvl = 1
                                    break
                            else:
                                a = invaders_x.pop(j)
                                b = invaders_y.pop(j)
                                boom_x.insert(0, a + 10)
                                boom_x.pop()
                                boom_y.insert(0, b)
                                boom_y.pop()
                                boom_time.insert(0, time.clock())
                                boom_time.pop()
                                invaders_hp.pop(j)
                                liczbainv -= 1
                                score += lvl * 10
                                if (liczbainv <= 0):
                                    nextlvl = 1
                                    break
                    j+=1
                if(bosslvl==1 and bullet_x[i] <= boss_x + boss.get_width() - 60 and bullet_x[i] >= boss_x +60 and bullet_y[i] <=boss_y + boss.get_height()/2 - 40 and bullet_y[i] >= boss_y):
                        bosstime = time.clock()
                        if(laser == 1):
                            boss = bosslaserhit
                        else:
                            boss = boss1hit
                        bullet_y.pop(i)
                        bullet_y.insert(i, 0)
                        bullet_x.pop(i)
                        bullet_x.insert(i, 0)
                        bullet_time.pop(i)
                        bullet_time.insert(i, 0)
                        boss_hp-=dmg
                        if(boss_hp<=0):
                            dead.play()
                            nextlvl = 1
                            bosslvl = 0
                            bosstart = 1
                            boss = boss1
                            score+=lvl*100
            if(nextlvl==1):
                continue
            if(bosslvl==0):
                for i in range(liczbainv):
                    invaders_x[i] += speedinv
                    if (invaders_x[i] + invader_width >= screen.get_width()):
                        invaders_x[i] = screen.get_width() - invader_width
                        speedinv = -speedinv
                        if (move == 0 and block ==0):
                            for j in range(liczbainv):
                                invaders_y[j] += invader_height - 20
                                if (invaders_y[j] == ship_top - 200):
                                    block=1
                            move = 1
                    elif (invaders_x[i] <= 0):
                        invaders_x[i] = 0
                        speedinv = -speedinv
                        if (move == 0 and block==0):
                            for j in range(liczbainv):
                                invaders_y[j] += invader_height - 20
                                if(invaders_y[j]==ship_top-200):
                                    block=1
                            move = 1
                    move = 0
                    screen.blit(invader, (invaders_x[i], invaders_y[i]))
            elif( bosslvl== 1 and bosstart==1):
                screen.blit(boss,( 300, 100))
                boss_x=300
                boss_y = 100
                bosstart=0
                lasertimer = time.clock()
            elif( bosslvl==1 and bosstart==0):
                if (time.clock() - bosstime >= 0.05):
                    if(laser == 1):
                        if(boss_hp<=50):
                            boss = bossbroke
                        else:
                            boss = bosslaser
                    else:
                        if (boss_hp <= tmp/2):
                            boss = bossbroke
                        else:
                            boss = boss1
                    bosstime = 0
                screen.blit(boss,(boss_x,boss_y))
                if(boss_x+boss.get_width()>=screen.get_width()):
                    boss_x = screen.get_width() - boss.get_width()
                    speedinv=-speedinv
                elif(boss_x<=0):
                    boss_x=0
                    speedinv=-speedinv
                boss_x+=speedinv
            if (time.clock() - lasertimer >= 7):
                laser = 1
                if(time.clock()-lasertimer>=8):
                    laser = 0
                    if(time.clock()-lasertimer>=8.5):
                        laser = 1
                        if(time.clock()-lasertimer>=9):
                            laser = 0
                            if(time.clock()-lasertimer>=10):
                                laser=1
                                if(time.clock()-lasertimer >=14):
                                    k=1
                                    laser = 0
                                    lasertimer = time.clock()
            for i in range(30):
                if(time.clock()- boom_time[i]<=0.3 and time.clock()- boom_time[i]>0):
                    screen.blit(boom, (boom_x[i], boom_y[i]))
                elif(time.clock()-boom_time[i]>0.3):
                    boom_time.pop(i)
                    boom_time.append(0)
                    boom_x.pop()
                    boom_x.append(0)
                    boom_y.pop(i)
                    boom_y.append(0)
            for i in range(100):
                if bullet_y[i] > 0:
                        screen.blit(bullet,(bullet_x[i],bullet_y[i]))
                        bullet_y[i] -= speed
                if invbullet_y[i] > 0 and bosslvl ==0 :
                        screen.blit(invbullet,(invbullet_x[i],invbullet_y[i]))
                        invbullet_y[i] += 10
                elif invbullet_y[i] > 0 and bosslvl==1 :
                        screen.blit(invbullet, (invbullet_x[i], invbullet_y[i]))
                        if(i%4==0):
                            invbullet_y[i] += 7
                            invbullet_x[i] -= 3
                        elif(i%4==1):
                            invbullet_y[i] += 7
                            invbullet_x[i] -= 1.5
                        elif (i % 4 == 2):
                            invbullet_y[i] += 7
                            invbullet_x[i] += 1.5
                        elif (i % 4 == 3):
                            invbullet_y[i] += 7
                            invbullet_x[i] += 3
                        if invbullet_y[i]>800:
                            invbullet_y.pop(i)
                            invbullet_y.insert(i,0)
                            invbullet_x.pop(i)
                            invbullet_x.insert(i, 0)
                            invbullet_time.pop(i)
                            invbullet_time.insert(i, 0)
                if powerups_y[i] > 0:
                    if powerups_type[i]==0:
                        screen.blit(heart ,(powerups_x[i],powerups_y[i]))
                        powerups_y[i] += 5
                    elif powerups_type[i]==1:
                        screen.blit(speedup ,(powerups_x[i],powerups_y[i]))
                        powerups_y[i] += 5
                    elif powerups_type[i]==2:
                        screen.blit(atkup ,(powerups_x[i],powerups_y[i]))
                        powerups_y[i] += 5
                    elif powerups_type[i]==3:
                        screen.blit(frqup, (powerups_x[i], powerups_y[i]))
                        powerups_y[i] += 5
                    if powerups_y[i] >= 800:
                        powerups_y.pop(i)
                        powerups_y.insert(i,0)
                        powerups_x.pop(i)
                        powerups_x.insert(i, 0)
                        powerups_type.pop(i)
                        powerups_type.insert(i, 4)
            if(time.clock()-lasertimer>=7 and time.clock()-lasertimer < 10 and bosslvl==1):
                screen.blit(prelaser,(boss_x + 145,boss_y + boss.get_width()/2 - 80))
            if(time.clock()-lasertimer >=10 and  time.clock()-lasertimer and bosslvl==1 ):
                screen.blit(lazer,(boss_x + 147,boss_y + boss.get_width()/2 - 80))
                if(k==1):
                    lazersound.play()
                    k=0
                if( boss_x + boss.get_width()/2 + lazer.get_width()/2  >= x - ship.get_width()/2 and x + ship.get_width()/2 >= boss_x + boss.get_width()/2 - lazer.get_width()/2 ):
                    lose=1
                    hpplayer=0
            pygame.display.update()