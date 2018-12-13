#Emilio Leion F. Tamayo
#2018-05042
#Harvey S. Samson
#2018-00542
#Trisha Mae N. Cua
#2018-02553


import pygame
import os
import datetime

def draw_box(screenname,x,y,width,height,color1=(255,255,255),color2 = (0,0,0)):
    pygame.draw.rect(screenname,(color1),(x-1,y-1,width+2,height+2),0)
    pygame.draw.rect(screenname,(color2),(x,y,width,height),0)

def draw_button(screenname,x,y,width,height,color1=(255,255,255),color2 = (0,0,0)):
    pygame.draw.rect(screenname,(color1),(x-10,y-10,width+20,height+20),0)
    pygame.draw.rect(screenname,(color2),(x,y,width,height),0)

def textbox (screenname,fontname,fontsize,text,colors,x,y):
    default_font = pygame.font.Font(fontname,fontsize)
    screenname.blit(default_font.render(text,1,colors),(x,y))

def start_shop():
    global rope_purchased
    global dagger_purchased
    global doll_purchased
    global info_purchased
    global game_currency
    img = pygame.image.load('the_armor_shop_by_sweetmoon-d622tbg.jpg')
    img = pygame.transform.scale(img, (1280, 720))
    rope_img = pygame.image.load('rope-clipart-png-5.png')
    rope_img = pygame.transform.scale(rope_img, (200, 150))
    dagger_img = pygame.image.load('Equips_Poisoned_Dagger.png')
    dagger_img = pygame.transform.scale(dagger_img, (200, 160))
    doll_img = pygame.image.load('88537ac8bd13a8eff684c2405db55e05.png')
    doll_img = pygame.transform.scale(doll_img, (165, 200))
    info_img = pygame.image.load('information-icon-5.png')
    info_img = pygame.transform.scale(info_img, (190, 190))
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode([screen_width,screen_height])
    done = False
    rope_buy = rope_purchased[0]
    dagger_buy = dagger_purchased
    doll_buy = doll_purchased
    info_buy = info_purchased
    rope_quantity = rope_purchased[1]
    rope_buyagain = 0
    error_msg = 0
    cost = 0
    pygame.mixer.music.load('Spells-a-Brewin_Looping.mp3')
    pygame.mixer.music.play(-1)
    while not done:
        mouse_position = pygame.mouse.get_pos()
        pygame.event.get()
        pygame.display.flip()
        screen.blit(img,(0,0))
        if rope_purchased[1]<2:
            draw_box(screen,190,60,220,40)
            textbox(screen,'BEBAS.ttf',20,'70 rupees',[255,255,255],250,70)
            draw_box(screen,190,120,220,220,color1 = (0,0,0),color2 = (60,30,0))#rope
            screen.blit(rope_img,(200,150))
        if not dagger_purchased:
            draw_box(screen,520,60,220,40)
            textbox(screen,'BEBAS.ttf',20,'410 rupees',[255,255,255],580,70)
            draw_box(screen,520,120,220,220,color1 = (0,0,0),color2 = (60,30,0))#dagger
            screen.blit(dagger_img,(530,150))
        if not doll_purchased:
            draw_box(screen,190,640,220,40)
            textbox(screen,'BEBAS.ttf',20,'50 rupees',[255,255,255],250,650)
            draw_box(screen,190,400,220,220,color1 = (0,0,0),color2 = (60,30,0))#doll
            screen.blit(doll_img,(200,410))
        if not info_purchased:
            draw_box(screen,520,640,220,40)
            textbox(screen,'BEBAS.ttf',20,'400 rupees',[255,255,255],580,650)
            draw_box(screen,520,400,220,220)#info
            screen.blit(info_img,(535,415))
        draw_button(screen,1100,30,120,40) #currency
        draw_button(screen,1100,650,120,40) #return
        draw_button(screen,800,100,250,40) #items to be purchased
        draw_button(screen,800,420,120,40) #purchase button
        draw_button(screen,1100,100,120,40) #cost button
        textbox(screen,'BEBAS.ttf',22,str(game_currency),(255,255,255),1110,40)
        textbox(screen,'BEBAS.ttf',22,'PURCHASE',(255,255,255),810,430)
        textbox(screen,'BEBAS.ttf',22,'ITEMS TO BE PURCHASED',(255,255,255),820,110)
        textbox(screen,'BEBAS.ttf',22,'RETURN',(255,255,255),1120,660)
        textbox(screen,'BEBAS.ttf',22,'COST: '+str(cost),(255,255,255),1110,110)
        if rope_buy and rope_purchased[1] < 2:
            draw_box(screen,800,180,200,40)
            textbox(screen,'BEBAS.ttf',20,'ROPE x'+str(rope_quantity),(255,255,255),810,190)
        if rope_buyagain:
            draw_box(screen,800,180,200,40)
            draw_box(screen,920,185,30,30)
            draw_box(screen,960,185,30,30)
            textbox(screen,'BEBAS.ttf',20,'QUANTITY',(255,255,255),810,190)
            textbox(screen,'BEBAS.ttf',20,'1',(255,255,255),930,190)
            textbox(screen,'BEBAS.ttf',20,'2',(255,255,255),970,190)
        if dagger_buy and not dagger_purchased:
            draw_box(screen,800,240,200,40)
            textbox(screen,'BEBAS.ttf',20,'POISON DAGGER',(255,255,255),810,250)
        if doll_buy and not doll_purchased:
            draw_box(screen,800,300,200,40)
            textbox(screen,'BEBAS.ttf',20,'DOLL',(255,255,255),810,310)
        if info_buy and not info_purchased:
            draw_box(screen,800,360,200,40)
            textbox(screen,'BEBAS.ttf',20,'INFORMATION',(255,255,255),810,370)
        if mouse_position[0]>190 and mouse_position[0]<410 and mouse_position[1]>120 and mouse_position[1]<340 and rope_purchased[1]<2:
            draw_box(screen,800,550,320,60)
            draw_box(screen,800,500,200,38)
            textbox(screen,'Futura Book font.ttf',20,'Useful for tying up your enemies',(255,255,255),810,560)
            textbox(screen,'Futura Book font.ttf',20,'ROPE',(255,255,255),810,505)
        elif mouse_position[0]>520 and mouse_position[0]<740 and mouse_position[1]>120 and mouse_position[1]<340 and not dagger_purchased:
            draw_box(screen,800,550,320,60)
            draw_box(screen,800,500,200,38)
            textbox(screen,'Futura Book font.ttf',20,'Kills opponents swiftly',(255,255,255),810,560)
            textbox(screen,'Futura Book font.ttf',20,'POISON DAGGER',(255,255,255),810,505)
        elif mouse_position[0]>190 and mouse_position[0]<410 and mouse_position[1]>400 and mouse_position[1]<620 and not doll_purchased:
            draw_box(screen,800,550,320,60)
            draw_box(screen,800,500,200,38)
            textbox(screen,'Futura Book font.ttf',20,'Something nostalgic.',(255,255,255),810,560)
            textbox(screen,'Futura Book font.ttf',20,'DOLL',(255,255,255),810,505)
        elif mouse_position[0]>520 and mouse_position[0]<740 and mouse_position[1]>400 and mouse_position[1]<620 and not info_purchased:
            draw_box(screen,800,550,320,60)
            draw_box(screen,800,500,200,38)
            textbox(screen,'Futura Book font.ttf',20,'Get some top-secret info',(255,255,255),810,560)
            textbox(screen,'Futura Book font.ttf',20,'INFORMATION',(255,255,255),810,505)
        if error_msg:
            draw_box(screen,800,500,300,60)
            draw_box(screen,1030,510,40,40)
            textbox(screen,'BEBAS.ttf',20,'Insufficient funds!',(255,255,255),820,520)
            textbox(screen,'BEBAS.ttf',20,'OK',(255,255,255),1040,520)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and (mouse_position[0]>1100 and mouse_position[0]<1220) and (mouse_position[1]>650 and mouse_position[1]<690):
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and rope_buyagain == 0 and int(rope_purchased[1]) <2 and mouse_position[0]>190 and mouse_position[0]<410 and mouse_position[1]>120 and mouse_position[1]<340:
                rope_buyagain = 1
                rope_buy = 0
                rope_quantity = 0
            elif event.type == pygame.MOUSEBUTTONDOWN and rope_buyagain == 0 and rope_buy == 1 and int(rope_purchased[1]) == 2 and mouse_position[0]>190 and mouse_position[0]<410 and mouse_position[1]>120 and mouse_position[1]<340:
                rope_buy = 0
                cost -= rope_quantity*70
                rope_quantity = 0
            elif event.type == pygame.MOUSEBUTTONDOWN and rope_buyagain == 1 and mouse_position[0]>920 and mouse_position[0]<950 and mouse_position[1]>185 and mouse_position[1]<215:
                rope_quantity += 1
                cost+=70
                rope_buyagain = 0
                rope_buy = 1
            elif event.type == pygame.MOUSEBUTTONDOWN and rope_buyagain == 1 and rope_quantity <1 and mouse_position[0]>960 and mouse_position[0]<990 and mouse_position[1]>185 and mouse_position[1]<215:
                rope_quantity += 2
                cost+=140
                rope_buyagain = 0
                rope_buy = 1
            elif event.type == pygame.MOUSEBUTTONDOWN and rope_buyagain == 1 and rope_quantity==1 and mouse_position[0]>960 and mouse_position[0]<990 and mouse_position[1]>185 and mouse_position[1]<215:
                rope_buyagain = 0
                rope_buy = 1
                cost-=70
            elif event.type == pygame.MOUSEBUTTONDOWN and rope_buyagain == 1 and rope_quantity>2 and ((mouse_position[0]>960 and mouse_position[0]<990) or (mouse_position[0]>920 and mouse_position[0]<950)) and mouse_position[1]>185 and mouse_position[1]<215:
                rope_buyagain = 0
                rope_buy = 1
                cost-=140
            
            elif event.type == pygame.MOUSEBUTTONDOWN and dagger_buy == 0 and mouse_position[0]>520 and mouse_position[0]<740 and mouse_position[1]>120 and mouse_position[1]<340:
                dagger_buy = 1
                cost+=410
            elif event.type == pygame.MOUSEBUTTONDOWN and dagger_buy == 1 and mouse_position[0]>520 and mouse_position[0]<740 and mouse_position[1]>120 and mouse_position[1]<340:
                dagger_buy = 0
                cost-=410
            elif event.type == pygame.MOUSEBUTTONDOWN and doll_buy == 0 and mouse_position[0]>190 and mouse_position[0]<410 and mouse_position[1]>400 and mouse_position[1]<620:
                doll_buy = 1
                cost+=50
            elif event.type == pygame.MOUSEBUTTONDOWN and doll_buy == 1 and mouse_position[0]>190 and mouse_position[0]<410 and mouse_position[1]>400 and mouse_position[1]<620:
                doll_buy = 0
                cost-=50
            elif event.type == pygame.MOUSEBUTTONDOWN and info_buy == 0 and mouse_position[0]>520 and mouse_position[0]<740 and mouse_position[1]>400 and mouse_position[1]<620:
                info_buy = 1
                cost+=400
            elif event.type == pygame.MOUSEBUTTONDOWN and info_buy == 1 and mouse_position[0]>520 and mouse_position[0]<740 and mouse_position[1]>400 and mouse_position[1]<620:
                info_buy = 0
                cost-=400
            elif event.type == pygame.MOUSEBUTTONDOWN and mouse_position[0]>800 and mouse_position[0]<920 and mouse_position[1]>420 and mouse_position[1]<460 and game_currency>=cost:
                rope_purchased[0] = rope_buy
                rope_purchased[1] += rope_quantity
                doll_purchased = doll_buy
                dagger_purchased = dagger_buy
                info_purchased = info_buy
                game_currency -= cost
                cost = 0
                error_msg = 0
                rope_buy = 0
            elif event.type == pygame.MOUSEBUTTONDOWN and mouse_position[0]>800 and mouse_position[0]<920 and mouse_position[1]>420 and mouse_position[1]<460 and game_currency<=cost:
                error_msg = 1
                rope_buy = 0
                doll_buy = 0
                dagger_buy = 0
                info_buy = 0
                cost = 0
            elif event.type == pygame.MOUSEBUTTONDOWN and error_msg and mouse_position[0]>1030 and mouse_position[0]<1070 and mouse_position[1]>510 and mouse_position[1]<550:
                error_msg = 0
def start_menu():
    global shop_access
    global lanaya_chosen
    global yorjan_chosen
    global what_scene
    global current_line
    global finallist1
    global finallist2
    global finallist3
    global finallist4
    global finallist5
    global finallist6
    global finallist7
    global finallist8
    global finallist9
    global finallist10
    global rope_purchased
    global dagger_purchased
    global doll_purchased
    global info_purchased
    global game_currency
    global currency_1
    img = pygame.image.load('719788-cool-fantasy-wallpapers-2560x1600-picture.jpg')
    img = pygame.transform.scale(img, (1280, 720))
    screen_width = 1280
    screen_height = 720
    load_on = 0
    screen = pygame.display.set_mode([screen_width,screen_height])
    done = False
    pygame.mixer.music.load('Celtic Fantasy Music - Hymn to Annûmara.mp3')
    pygame.mixer.music.play(-1)
    while not done:
        tempstring = ''
        fh1 = open(save_file_list[0],'r',encoding = 'utf-8')
        fh2 = open(save_file_list[1],'r',encoding = 'utf-8')
        fh3 = open(save_file_list[2],'r',encoding = 'utf-8')
        fh4 = open(save_file_list[3],'r',encoding = 'utf-8')
        fh5 = open(save_file_list[4],'r',encoding = 'utf-8')
        fh6 = open(save_file_list[5],'r',encoding = 'utf-8')
        fh7 = open(save_file_list[6],'r',encoding = 'utf-8')
        fh8 = open(save_file_list[7],'r',encoding = 'utf-8')
        fh9 = open(save_file_list[8],'r',encoding = 'utf-8')
        fh10 = open(save_file_list[9],'r',encoding = 'utf-8')
        templist1 = ''
        templist2 = ''
        templist3 = ''
        templist4 = ''
        templist5 = ''
        templist6 = ''
        templist7 = ''
        templist8 = ''
        templist9 = ''
        templist10 = ''
        finallist1 = []
        finallist2 = []
        finallist3 = []
        finallist4 = []
        finallist5 = []
        finallist6 = []
        finallist7 = []
        finallist8 = []
        finallist9 = []
        finallist10 = []
        for i in fh1:
            templist1 += i
        finallist1 = templist1.split('\n')
        for i in fh2:
            templist2 += i
        finallist2 = templist2.split('\n')
        for i in fh3:
            templist3 += i
        finallist3 = templist3.split('\n')
        for i in fh4:
            templist4 += i
        finallist4 = templist4.split('\n')
        for i in fh5:
            templist5 += i
        finallist5 = templist5.split('\n')
        for i in fh6:
            templist6 += i
        finallist6 = templist6.split('\n')
        for i in fh7:
            templist7 += i
        finallist7 = templist7.split('\n')
        for i in fh8:
            templist8 += i
        finallist8 = templist8.split('\n')
        for i in fh9:
            templist9 += i
        finallist9 = templist9.split('\n')
        for i in fh10:
            templist10 += i
        finallist10 = templist10.split('\n')
        mouse_position = pygame.mouse.get_pos()
        pygame.event.get()
        pygame.display.flip()
        screen.blit(img,(0,0))
        textbox(screen,'BLKCHCRY.ttf',100,'Missiletainn',(255,255,255),420,100)
        if load_on == 0:
            draw_button(screen,500,250,300,60)
            draw_button(screen,500,380,300,60)
            draw_button(screen,500,510,300,60)
            textbox(screen,'BLKCHCRY.ttf',45,'New Game',(255,255,255),550,251)
            textbox(screen,'BLKCHCRY.ttf',45,'Load Game',(255,255,255),550,381)
            textbox(screen,'BLKCHCRY.ttf',45,'Quit',(255,255,255),600,511)
        elif load_on == 1:
            draw_button(screen,250,250,300,40)
            draw_button(screen,250,330,300,40)
            draw_button(screen,250,410,300,40)
            draw_button(screen,250,490,300,40)
            draw_button(screen,250,570,300,40)
            draw_button(screen,750,250,300,40)
            draw_button(screen,750,330,300,40)
            draw_button(screen,750,410,300,40)
            draw_button(screen,750,490,300,40)
            draw_button(screen,750,570,300,40)
            draw_button(screen,1100,650,120,40)
            if len (finallist1) == 11:
                textbox(screen,'BEBAS.ttf',27,'SLOT 1',(255,255,255),365,258)
            elif len (finallist1) == 12:
                textbox(screen,'BEBAS.ttf',27,finallist1[11],(255,255,255),300,258)
            if len (finallist2) == 11:
                textbox(screen,'BEBAS.ttf',27,'SLOT 2',(255,255,255),365,338)
            elif len (finallist2) == 12:
                textbox(screen,'BEBAS.ttf',27,finallist2[11],(255,255,255),300,338)
            if len (finallist3) == 11:
                textbox(screen,'BEBAS.ttf',27,'SLOT 3',(255,255,255),365,418)
            elif len (finallist3) == 12:
                textbox(screen,'BEBAS.ttf',27,finallist3[11],(255,255,255),300,418)
            if len (finallist4) == 11:
                textbox(screen,'BEBAS.ttf',27,'SLOT 4',(255,255,255),365,498)
            elif len (finallist4) == 12:
                textbox(screen,'BEBAS.ttf',27,finallist4[11],(255,255,255),300,498)
            if len (finallist5) == 11:
                textbox(screen,'BEBAS.ttf',27,'SLOT 5',(255,255,255),365,578)
            elif len (finallist5) == 12:
                textbox(screen,'BEBAS.ttf',27,finallist5[11],(255,255,255),300,578)
            if len (finallist6) == 11:
                textbox(screen,'BEBAS.ttf',27,'SLOT 6',(255,255,255),865,258)
            elif len (finallist6) == 12:
                textbox(screen,'BEBAS.ttf',27,finallist6[11],(255,255,255),800,258)
            if len (finallist7) == 11:
                textbox(screen,'BEBAS.ttf',27,'SLOT 7',(255,255,255),865,338)
            elif len (finallist7) == 12:
                textbox(screen,'BEBAS.ttf',27,finallist7[11],(255,255,255),800,338)
            if len (finallist8) == 11:
                textbox(screen,'BEBAS.ttf',27,'SLOT 8',(255,255,255),865,418)
            elif len (finallist8) == 12:
                textbox(screen,'BEBAS.ttf',27,finallist8[11],(255,255,255),800,418)
            if len (finallist9) == 11:
                textbox(screen,'BEBAS.ttf',27,'SLOT 9',(255,255,255),865,498)
            elif len (finallist9) == 12:
                textbox(screen,'BEBAS.ttf',27,finallist9[11],(255,255,255),800,498)
            if len (finallist10) == 11:
                textbox(screen,'BEBAS.ttf',27,'SLOT 10',(255,255,255),865,578)
            elif len (finallist10) == 12:
                textbox(screen,'BEBAS.ttf',27,finallist10[11],(255,255,255),800,578)
            textbox(screen,'BEBAS.ttf',25,'RETURN',(255,255,255),1120,660)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and load_on == 0 and (mouse_position[0]>500 and mouse_position[0]<800) and (mouse_position[1]>510 and mouse_position[1]<570):
                done = True
                what_scene = '1'
            elif event.type == pygame.MOUSEBUTTONDOWN and load_on == 0 and (mouse_position[0]>500 and mouse_position[0]<800) and (mouse_position[1]>250 and mouse_position[1]<310):
                rope_purchased = [0,0]
                doll_purchased = 0
                dagger_purchased = 0
                info_purchased = 0
                game_currency = 0
                currency_1 = 0
                what_scene = '2'
                current_line = 1
                shop_access = 0
                lanaya_chosen = 0
                yorjan_chosen = 0
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and load_on == 0 and (mouse_position[0]>500 and mouse_position[0]<800) and (mouse_position[1]>380 and mouse_position[1]<440):
                load_on = 1
            elif event.type == pygame.MOUSEBUTTONDOWN and load_on == 1 and (mouse_position[0]>1100 and mouse_position[0]<1220) and (mouse_position[1]>650 and mouse_position[1]<690):
                load_on = 0
            elif event.type == pygame.MOUSEBUTTONDOWN and load_on == 1 and (mouse_position[0]>250 and mouse_position[0]<550) and (mouse_position[1]>250 and mouse_position[1]<290):
                open_file = open('savefile1.txt','r',encoding = 'utf-8')
                for i in open_file:
                    tempstring+=i
                file_details = tempstring.split('\n')
                what_scene = file_details[0]
                current_line = int(file_details[1])
                rope_purchased = [int(file_details[2]),int(file_details[3])]
                dagger_purchased = int(file_details[4])
                doll_purchased = int(file_details[5])
                info_purchased = int(file_details[6])
                game_currency = int(file_details[7])
                shop_access = int(file_details[8])
                lanaya_chosen = int(file_details[9])
                yorjan_chosen = int(file_details[10])
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and load_on == 1 and (mouse_position[0]>250 and mouse_position[0]<550) and (mouse_position[1]>330 and mouse_position[1]<370):
                open_file = open('savefile2.txt','r',encoding = 'utf-8')
                for i in open_file:
                    tempstring+=i
                file_details = tempstring.split('\n')
                what_scene = file_details[0]
                current_line = int(file_details[1])
                rope_purchased = [int(file_details[2]),int(file_details[3])]
                dagger_purchased = int(file_details[4])
                doll_purchased = int(file_details[5])
                info_purchased = int(file_details[6])
                game_currency = int(file_details[7])
                shop_access = int(file_details[8])
                lanaya_chosen = int(file_details[9])
                yorjan_chosen = int(file_details[10])
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and load_on == 1 and (mouse_position[0]>250 and mouse_position[0]<550) and (mouse_position[1]>410 and mouse_position[1]<450):
                open_file = open('savefile3.txt','r',encoding = 'utf-8')
                for i in open_file:
                    tempstring+=i
                file_details = tempstring.split('\n')
                what_scene = file_details[0]
                current_line = int(file_details[1])
                rope_purchased = [int(file_details[2]),int(file_details[3])]
                dagger_purchased = int(file_details[4])
                doll_purchased = int(file_details[5])
                info_purchased = int(file_details[6])
                game_currency = int(file_details[7])
                shop_access = int(file_details[8])
                lanaya_chosen = int(file_details[9])
                yorjan_chosen = int(file_details[10])
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and load_on == 1 and (mouse_position[0]>250 and mouse_position[0]<550) and (mouse_position[1]>490 and mouse_position[1]<540):
                open_file = open('savefile4.txt','r',encoding = 'utf-8')
                for i in open_file:
                    tempstring+=i
                file_details = tempstring.split('\n')
                what_scene = file_details[0]
                current_line = int(file_details[1])
                rope_purchased = [int(file_details[2]),int(file_details[3])]
                dagger_purchased = int(file_details[4])
                doll_purchased = int(file_details[5])
                info_purchased = int(file_details[6])
                game_currency = int(file_details[7])
                shop_access = int(file_details[8])
                lanaya_chosen = int(file_details[9])
                yorjan_chosen = int(file_details[10])
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and load_on == 1 and (mouse_position[0]>250 and mouse_position[0]<550) and (mouse_position[1]>570 and mouse_position[1]<610):
                open_file = open('savefile5.txt','r',encoding = 'utf-8')
                for i in open_file:
                    tempstring+=i
                file_details = tempstring.split('\n')
                what_scene = file_details[0]
                current_line = int(file_details[1])
                rope_purchased = [int(file_details[2]),int(file_details[3])]
                dagger_purchased = int(file_details[4])
                doll_purchased = int(file_details[5])
                info_purchased = int(file_details[6])
                game_currency = int(file_details[7])
                shop_access = int(file_details[8])
                lanaya_chosen = int(file_details[9])
                yorjan_chosen = int(file_details[10])
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and load_on == 1 and (mouse_position[0]>750 and mouse_position[0]<1050) and (mouse_position[1]>250 and mouse_position[1]<290):
                open_file = open('savefile6.txt','r',encoding = 'utf-8')
                for i in open_file:
                    tempstring+=i
                file_details = tempstring.split('\n')
                what_scene = file_details[0]
                current_line = int(file_details[1])
                rope_purchased = [int(file_details[2]),int(file_details[3])]
                dagger_purchased = int(file_details[4])
                doll_purchased = int(file_details[5])
                info_purchased = int(file_details[6])
                game_currency = int(file_details[7])
                shop_access = int(file_details[8])
                lanaya_chosen = int(file_details[9])
                yorjan_chosen = int(file_details[10])
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and load_on == 1 and (mouse_position[0]>750 and mouse_position[0]<1050) and (mouse_position[1]>330 and mouse_position[1]<370):
                open_file = open('savefile7.txt','r',encoding = 'utf-8')
                for i in open_file:
                    tempstring+=i
                file_details = tempstring.split('\n')
                what_scene = file_details[0]
                current_line = int(file_details[1])
                rope_purchased = [int(file_details[2]),int(file_details[3])]
                dagger_purchased = int(file_details[4])
                doll_purchased = int(file_details[5])
                info_purchased = int(file_details[6])
                game_currency = int(file_details[7])
                shop_access = int(file_details[8])
                lanaya_chosen = int(file_details[9])
                yorjan_chosen = int(file_details[10])
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and load_on == 1 and (mouse_position[0]>750 and mouse_position[0]<1050) and (mouse_position[1]>410 and mouse_position[1]<450):
                open_file = open('savefile8.txt','r',encoding = 'utf-8')
                for i in open_file:
                    tempstring+=i
                file_details = tempstring.split('\n')
                what_scene = file_details[0]
                current_line = int(file_details[1])
                rope_purchased = [int(file_details[2]),int(file_details[3])]
                dagger_purchased = int(file_details[4])
                doll_purchased = int(file_details[5])
                info_purchased = int(file_details[6])
                game_currency = int(file_details[7])
                shop_access = int(file_details[8])
                lanaya_chosen = int(file_details[9])
                yorjan_chosen = int(file_details[10])
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and load_on == 1 and (mouse_position[0]>750 and mouse_position[0]<1050) and (mouse_position[1]>490 and mouse_position[1]<530):
                open_file = open('savefile9.txt','r',encoding = 'utf-8')
                for i in open_file:
                    tempstring+=i
                file_details = tempstring.split('\n')
                what_scene = file_details[0]
                current_line = int(file_details[1])
                rope_purchased = [int(file_details[2]),int(file_details[3])]
                dagger_purchased = int(file_details[4])
                doll_purchased = int(file_details[5])
                info_purchased = int(file_details[6])
                game_currency = int(file_details[7])
                shop_access = int(file_details[8])
                lanaya_chosen = int(file_details[9])
                yorjan_chosen = int(file_details[10])
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and load_on == 1 and (mouse_position[0]>750 and mouse_position[0]<1050) and (mouse_position[1]>570 and mouse_position[1]<610):
                open_file = open('savefile10.txt','r',encoding = 'utf-8')
                for i in open_file:
                    tempstring+=i
                file_details = tempstring.split('\n')
                what_scene = file_details[0]
                current_line = int(file_details[1])
                rope_purchased = [int(file_details[2]),int(file_details[3])]
                dagger_purchased = int(file_details[4])
                doll_purchased = int(file_details[5])
                info_purchased = int(file_details[6])
                game_currency = int(file_details[7])
                shop_access = int(file_details[8])
                lanaya_chosen = int(file_details[9])
                yorjan_chosen = int(file_details[10])
                done = True
class scene():
    def __init__(self):
        global current_line
        self.screen_width = 1280
        self.screen_height = 720
        self.script = []
        self.bg = ''
        self.line_no = current_line
        self.screen = pygame.display.set_mode([self.screen_width,self.screen_height])
        self.sprites = []
        self.bgm = ''
        self.choices = []
        self.decision_on = 0
        self.decision_number = 0
        self.save_on = 0
        self.load_on = 0
        self.inventory_on = 0
    def ins_decision(self,line,choices,fontsize,xcoordinate):
        self.choices.append([line,choices,fontsize,xcoordinate])
    def bg_img(self,filename):
        self.bg = filename
    def ins_script(self,filename):
        fh = open(filename,'r',encoding = 'utf-8')
        textlist = ''
        templist = []
        finallist = []
        for i in fh:
            textlist += i
        templist = textlist.split('\n')
        for i in templist:
            text = i.split(':')
            finallist.append(text)
        self.script = finallist
    def ins_sprite(self, filename, firstline, lastline,x,y,width,height):
        sprite_info = [filename,firstline,lastline,x,y,width,height]
        self.sprites.append(sprite_info)
    def ins_audio(self,filename):
        self.bgm = filename
    def run_scene(self,font,fontsize):
        global what_scene
        global current_line
        global rope_purchased
        global dagger_purchased
        global doll_purchased
        global info_purchased
        global game_currency
        global shop_access
        global yorjan_chosen
        global lanaya_chosen
        done = False
        img = pygame.image.load(self.bg)
        img = pygame.transform.scale(img, (1280, 720))
        menu_on = 0
        pygame.mixer.music.load(self.bgm)
        pygame.mixer.music.play(-1)
        while not done:
            tempstring = ''
            fh1 = open(save_file_list[0],'r',encoding = 'utf-8')
            fh2 = open(save_file_list[1],'r',encoding = 'utf-8')
            fh3 = open(save_file_list[2],'r',encoding = 'utf-8')
            fh4 = open(save_file_list[3],'r',encoding = 'utf-8')
            fh5 = open(save_file_list[4],'r',encoding = 'utf-8')
            fh6 = open(save_file_list[5],'r',encoding = 'utf-8')
            fh7 = open(save_file_list[6],'r',encoding = 'utf-8')
            fh8 = open(save_file_list[7],'r',encoding = 'utf-8')
            fh9 = open(save_file_list[8],'r',encoding = 'utf-8')
            fh10 = open(save_file_list[9],'r',encoding = 'utf-8')
            templist1 = ''
            templist2 = ''
            templist3 = ''
            templist4 = ''
            templist5 = ''
            templist6 = ''
            templist7 = ''
            templist8 = ''
            templist9 = ''
            templist10 = ''
            finallist1 = []
            finallist2 = []
            finallist3 = []
            finallist4 = []
            finallist5 = []
            finallist6 = []
            finallist7 = []
            finallist8 = []
            finallist9 = []
            finallist10 = []
            for i in fh1:
                templist1 += i
            finallist1 = templist1.split('\n')
            for i in fh2:
                templist2 += i
            finallist2 = templist2.split('\n')
            for i in fh3:
                templist3 += i
            finallist3 = templist3.split('\n')
            for i in fh4:
                templist4 += i
            finallist4 = templist4.split('\n')
            for i in fh5:
                templist5 += i
            finallist5 = templist5.split('\n')
            for i in fh6:
                templist6 += i
            finallist6 = templist6.split('\n')
            for i in fh7:
                templist7 += i
            finallist7 = templist7.split('\n')
            for i in fh8:
                templist8 += i
            finallist8 = templist8.split('\n')
            for i in fh9:
                templist9 += i
            finallist9 = templist9.split('\n')
            for i in fh10:
                templist10 += i
            finallist10 = templist10.split('\n')
            mouse_position = pygame.mouse.get_pos()
            pygame.event.get()
            pygame.display.flip()
            self.screen.blit(img,(0,0))
            for sprite in self.sprites:
                if self.line_no>=(sprite[1]) and self.line_no<=(sprite[2]):
                    sprited = pygame.image.load(sprite[0])
                    sprited = pygame.transform.scale(sprited, (sprite[5], sprite[6]))
                    self.screen.blit(sprited,(sprite[3],sprite[4]))
                else:
                    pass
            draw_box(self.screen,35,550,1200,120,color2=(0,0,0))
            draw_box(self.screen,40,550,1190,120,color2=(0,0,0))
            draw_box(self.screen,30,540,170,30,color2=(159,139,0))
            draw_button(self.screen,1050,40,180,40)
            textbox(self.screen,'DaysOne-Regular.ttf',fontsize+2,'Menu',(255,255,255),1100,40)
            if self.script[self.line_no][0] != 'Monologue':
                textbox(self.screen,font,fontsize+2,self.script[self.line_no][0],(0,0,0),35,540)
            else:
                pass
            if len (self.script[self.line_no][1]) < 100:
                textbox(self.screen,font,fontsize,self.script[self.line_no][1],(255,255,255),50,573)
            elif len(self.script[self.line_no][1]) < 200:
                first = ''
                second = ''
                for i in range(100):
                    first += self.script[self.line_no][1][i]
                for i in range(100,len(self.script[self.line_no][1])):
                    second += self.script[self.line_no][1][i]
                textbox(self.screen,font,fontsize,first,(255,255,255),50,573)
                textbox(self.screen,font,fontsize,second,(255,255,255),50,603)
            else:
                first = ''
                second = ''
                third = ''
                for i in range(100):
                    first += self.script[self.line_no][1][i]
                for i in range(100,200):
                    second += self.script[self.line_no][1][i]
                for i in range(200, len(self.script[self.line_no][1])):
                    third += self.script[self.line_no][1][i]
                textbox(self.screen,font,fontsize,first,(255,255,255),50,573)
                textbox(self.screen,font,fontsize,second,(255,255,255),50,603)
                textbox(self.screen,font,fontsize,third,(255,255,255),50,633)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and self.decision_on == 0 and (mouse_position[0]>=40 and mouse_position[0]<=1230) and (mouse_position[1]>=550 and mouse_position[1]<=670):
                    self.line_no+=1
                    current_line = self.line_no
                elif event.type == pygame.MOUSEBUTTONDOWN and menu_on == 0 and (mouse_position[0]>=1050 and mouse_position[0]<=1230) and (mouse_position[1]>=40 and mouse_position[1]<=80):
                    menu_on = 1
                    self.save_on = 0
                    self.load_on = 0
                    self.inventory_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and menu_on == 1 and (mouse_position[0]>=1050 and mouse_position[0]<=1230) and (mouse_position[1]>=40 and mouse_position[1]<=80):
                    menu_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and menu_on == 1 and (mouse_position[0]>=1070 and mouse_position[0]<=1210) and (mouse_position[1]>=110 and mouse_position[1]<=150):
                    done = True 
                    pygame.mixer.music.stop()
                    start_menu()
                elif event.type == pygame.MOUSEBUTTONDOWN and shop_access == 1 and menu_on == 1 and (mouse_position[0]>=1070 and mouse_position[0]<=1210) and (mouse_position[1]>=170 and mouse_position[1]<=210):
                    done = True 
                    pygame.mixer.music.stop()
                    start_shop()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.decision_on == 1 and len(self.choices[self.decision_number][1]) == 2 and ((mouse_position[0]>=400 and mouse_position[0]<=900) and (mouse_position[1]>=100 and mouse_position[1]<=180)):
                    done = True
                    if not str(what_scene[1]).isdigit():
                        what_scene = str(int(what_scene[0])+1) + what_scene[1:] + 'a'
                    elif str(what_scene[1]).isdigit():
                        what_scene = str(int(what_scene[0:2])+1) + what_scene[2:] + 'a'
                    current_line = 1
                elif event.type == pygame.MOUSEBUTTONDOWN and self.decision_on == 1 and len(self.choices[self.decision_number][1]) == 2 and ((mouse_position[0]>=400 and mouse_position[0]<=900) and (mouse_position[1]>=300 and mouse_position[1]<=380)):
                    done = True
                    if not str(what_scene[1]).isdigit():
                        what_scene = str(int(what_scene[0])+1) + what_scene[1:] + 'b'
                    elif str(what_scene[1]).isdigit():
                        what_scene = str(int(what_scene[0:2])+1) + what_scene[2:] + 'b'
                    current_line = 1
                elif event.type == pygame.MOUSEBUTTONDOWN and self.decision_on == 1 and len(self.choices[self.decision_number][1]) == 3 and ((mouse_position[0]>=400 and mouse_position[0]<=900) and (mouse_position[1]>=100 and mouse_position[1]<=180)):
                    done = True
                    if not str(what_scene[1]).isdigit():
                        what_scene = str(int(what_scene[0])+1) + what_scene[1:] + 'a'
                    elif str(what_scene[1]).isdigit():
                        what_scene = str(int(what_scene[0:2])+1) + what_scene[2:] + 'a'
                    current_line = 1
                elif event.type == pygame.MOUSEBUTTONDOWN and self.decision_on == 1 and len(self.choices[self.decision_number][1]) == 3 and ((mouse_position[0]>=400 and mouse_position[0]<=900) and (mouse_position[1]>=250 and mouse_position[1]<=330)):
                    done = True
                    if not str(what_scene[1]).isdigit():
                        what_scene = str(int(what_scene[0])+1) + what_scene[1:] + 'b'
                    elif str(what_scene[1]).isdigit():
                        what_scene = str(int(what_scene[0:2])+1) + what_scene[2:] + 'b'
                    current_line = 1
                elif event.type == pygame.MOUSEBUTTONDOWN and self.decision_on == 1 and len(self.choices[self.decision_number][1]) == 3 and ((mouse_position[0]>=400 and mouse_position[0]<=900) and (mouse_position[1]>=400 and mouse_position[1]<=480)):
                    done = True
                    if not str(what_scene[1]).isdigit():
                        what_scene = str(int(what_scene[0])+1) + what_scene[1:] + 'c'
                    elif str(what_scene[1]).isdigit():
                        what_scene = str(int(what_scene[0:2])+1) + what_scene[2:] + 'c'
                    current_line = 1
                elif event.type == pygame.MOUSEBUTTONDOWN and menu_on and self.save_on == 0 and ((mouse_position[0]>=1070 and mouse_position[0]<=1210) and (mouse_position[1]>=230 and mouse_position[1]<=270)):
                    self.save_on = 1
                    menu_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and menu_on and self.load_on == 0 and ((mouse_position[0]>=1070 and mouse_position[0]<=1210) and (mouse_position[1]>=290 and mouse_position[1]<=330)):
                    self.load_on = 1
                    menu_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and menu_on and self.load_on == 0 and ((mouse_position[0]>=1070 and mouse_position[0]<=1210) and (mouse_position[1]>=350 and mouse_position[1]<=390)):
                    self.inventory_on = 1
                    menu_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and self.save_on == 1 and ((mouse_position[0]>=970 and mouse_position[0]<=1230) and (mouse_position[1]>=110 and mouse_position[1]<=140)):
                    savefile = open('savefile1.txt','w',encoding = 'utf-8')
                    savefile.write(str(what_scene)+'\n')
                    savefile.write(str(self.line_no)+'\n')
                    savefile.write(str(rope_purchased[0])+'\n')
                    savefile.write(str(rope_purchased[1])+'\n')
                    savefile.write(str(dagger_purchased)+'\n')
                    savefile.write(str(doll_purchased)+'\n')
                    savefile.write(str(info_purchased)+'\n')
                    savefile.write(str(game_currency)+'\n')
                    savefile.write(str(shop_access)+'\n')
                    savefile.write(str(lanaya_chosen)+'\n')
                    savefile.write(str(yorjan_chosen)+'\n')
                    savefile.write(str(now.year)+':'+str(now.month)+':'+str(now.day)+':'+str(now.hour)+':'+str(now.minute)+':'+str(now.second))
                    savefile.close()
                    self.save_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and self.save_on == 1 and ((mouse_position[0]>=970 and mouse_position[0]<=1230) and (mouse_position[1]>=150 and mouse_position[1]<=180)):
                    savefile = open('savefile2.txt','w',encoding = 'utf-8')
                    savefile.write(str(what_scene)+'\n')
                    savefile.write(str(self.line_no)+'\n')
                    savefile.write(str(rope_purchased[0])+'\n')
                    savefile.write(str(rope_purchased[1])+'\n')
                    savefile.write(str(dagger_purchased)+'\n')
                    savefile.write(str(doll_purchased)+'\n')
                    savefile.write(str(info_purchased)+'\n')
                    savefile.write(str(game_currency)+'\n')
                    savefile.write(str(shop_access)+'\n')
                    savefile.write(str(lanaya_chosen)+'\n')
                    savefile.write(str(yorjan_chosen)+'\n')
                    savefile.write(str(now.year)+':'+str(now.month)+':'+str(now.day)+':'+str(now.hour)+':'+str(now.minute)+':'+str(now.second))
                    savefile.close()
                    self.save_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and self.save_on == 1 and ((mouse_position[0]>=970 and mouse_position[0]<=1230) and (mouse_position[1]>=190 and mouse_position[1]<=220)):
                    savefile = open('savefile3.txt','w',encoding = 'utf-8')
                    savefile.write(str(what_scene)+'\n')
                    savefile.write(str(self.line_no)+'\n')
                    savefile.write(str(rope_purchased[0])+'\n')
                    savefile.write(str(rope_purchased[1])+'\n')
                    savefile.write(str(dagger_purchased)+'\n')
                    savefile.write(str(doll_purchased)+'\n')
                    savefile.write(str(info_purchased)+'\n')
                    savefile.write(str(game_currency)+'\n')
                    savefile.write(str(shop_access)+'\n')
                    savefile.write(str(lanaya_chosen)+'\n')
                    savefile.write(str(yorjan_chosen)+'\n')
                    savefile.write(str(now.year)+':'+str(now.month)+':'+str(now.day)+':'+str(now.hour)+':'+str(now.minute)+':'+str(now.second))
                    savefile.close()
                    self.save_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and self.save_on == 1 and ((mouse_position[0]>=970 and mouse_position[0]<=1230) and (mouse_position[1]>=230 and mouse_position[1]<=260)):
                    savefile = open('savefile4.txt','w',encoding = 'utf-8')
                    savefile.write(str(what_scene)+'\n')
                    savefile.write(str(self.line_no)+'\n')
                    savefile.write(str(rope_purchased[0])+'\n')
                    savefile.write(str(rope_purchased[1])+'\n')
                    savefile.write(str(dagger_purchased)+'\n')
                    savefile.write(str(doll_purchased)+'\n')
                    savefile.write(str(info_purchased)+'\n')
                    savefile.write(str(game_currency)+'\n')
                    savefile.write(str(shop_access)+'\n')
                    savefile.write(str(lanaya_chosen)+'\n')
                    savefile.write(str(yorjan_chosen)+'\n')
                    savefile.write(str(now.year)+':'+str(now.month)+':'+str(now.day)+':'+str(now.hour)+':'+str(now.minute)+':'+str(now.second))
                    savefile.close()
                    self.save_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and self.save_on == 1 and ((mouse_position[0]>=970 and mouse_position[0]<=1230) and (mouse_position[1]>=270 and mouse_position[1]<=310)):
                    savefile = open('savefile5.txt','w',encoding = 'utf-8')
                    savefile.write(str(what_scene)+'\n')
                    savefile.write(str(self.line_no)+'\n')
                    savefile.write(str(rope_purchased[0])+'\n')
                    savefile.write(str(rope_purchased[1])+'\n')
                    savefile.write(str(dagger_purchased)+'\n')
                    savefile.write(str(doll_purchased)+'\n')
                    savefile.write(str(info_purchased)+'\n')
                    savefile.write(str(game_currency)+'\n')
                    savefile.write(str(shop_access)+'\n')
                    savefile.write(str(lanaya_chosen)+'\n')
                    savefile.write(str(yorjan_chosen)+'\n')
                    savefile.write(str(now.year)+':'+str(now.month)+':'+str(now.day)+':'+str(now.hour)+':'+str(now.minute)+':'+str(now.second))
                    savefile.close()
                    self.save_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and self.save_on == 1 and ((mouse_position[0]>=970 and mouse_position[0]<=1230) and (mouse_position[1]>=310 and mouse_position[1]<=340)):
                    savefile = open('savefile6.txt','w',encoding = 'utf-8')
                    savefile.write(str(what_scene)+'\n')
                    savefile.write(str(self.line_no)+'\n')
                    savefile.write(str(rope_purchased[0])+'\n')
                    savefile.write(str(rope_purchased[1])+'\n')
                    savefile.write(str(dagger_purchased)+'\n')
                    savefile.write(str(doll_purchased)+'\n')
                    savefile.write(str(info_purchased)+'\n')
                    savefile.write(str(game_currency)+'\n')
                    savefile.write(str(shop_access)+'\n')
                    savefile.write(str(lanaya_chosen)+'\n')
                    savefile.write(str(yorjan_chosen)+'\n')
                    savefile.write(str(now.year)+':'+str(now.month)+':'+str(now.day)+':'+str(now.hour)+':'+str(now.minute)+':'+str(now.second))
                    savefile.close()
                    self.save_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and self.save_on == 1 and ((mouse_position[0]>=970 and mouse_position[0]<=1230) and (mouse_position[1]>=350 and mouse_position[1]<=380)):
                    savefile = open('savefile7.txt','w',encoding = 'utf-8')
                    savefile.write(str(what_scene)+'\n')
                    savefile.write(str(self.line_no)+'\n')
                    savefile.write(str(rope_purchased[0])+'\n')
                    savefile.write(str(rope_purchased[1])+'\n')
                    savefile.write(str(dagger_purchased)+'\n')
                    savefile.write(str(doll_purchased)+'\n')
                    savefile.write(str(info_purchased)+'\n')
                    savefile.write(str(game_currency)+'\n')
                    savefile.write(str(shop_access)+'\n')
                    savefile.write(str(lanaya_chosen)+'\n')
                    savefile.write(str(yorjan_chosen)+'\n')
                    savefile.write(str(now.year)+':'+str(now.month)+':'+str(now.day)+':'+str(now.hour)+':'+str(now.minute)+':'+str(now.second))
                    savefile.close()
                    self.save_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and self.save_on == 1 and ((mouse_position[0]>=970 and mouse_position[0]<=1230) and (mouse_position[1]>=390 and mouse_position[1]<=420)):
                    savefile = open('savefile8.txt','w',encoding = 'utf-8')
                    savefile.write(str(what_scene)+'\n')
                    savefile.write(str(self.line_no)+'\n')
                    savefile.write(str(rope_purchased[0])+'\n')
                    savefile.write(str(rope_purchased[1])+'\n')
                    savefile.write(str(dagger_purchased)+'\n')
                    savefile.write(str(doll_purchased)+'\n')
                    savefile.write(str(info_purchased)+'\n')
                    savefile.write(str(game_currency)+'\n')
                    savefile.write(str(shop_access)+'\n')
                    savefile.write(str(lanaya_chosen)+'\n')
                    savefile.write(str(yorjan_chosen)+'\n')
                    savefile.write(str(now.year)+':'+str(now.month)+':'+str(now.day)+':'+str(now.hour)+':'+str(now.minute)+':'+str(now.second))
                    savefile.close()
                    self.save_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and self.save_on == 1 and ((mouse_position[0]>=970 and mouse_position[0]<=1230) and (mouse_position[1]>=430 and mouse_position[1]<=450)):
                    savefile = open('savefile9.txt','w',encoding = 'utf-8')
                    savefile.write(str(what_scene)+'\n')
                    savefile.write(str(self.line_no)+'\n')
                    savefile.write(str(rope_purchased[0])+'\n')
                    savefile.write(str(rope_purchased[1])+'\n')
                    savefile.write(str(dagger_purchased)+'\n')
                    savefile.write(str(doll_purchased)+'\n')
                    savefile.write(str(info_purchased)+'\n')
                    savefile.write(str(game_currency)+'\n')
                    savefile.write(str(shop_access)+'\n')
                    savefile.write(str(lanaya_chosen)+'\n')
                    savefile.write(str(yorjan_chosen)+'\n')
                    savefile.write(str(now.year)+':'+str(now.month)+':'+str(now.day)+':'+str(now.hour)+':'+str(now.minute)+':'+str(now.second))
                    savefile.close()
                    self.save_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and self.save_on == 1 and ((mouse_position[0]>=970 and mouse_position[0]<=1230) and (mouse_position[1]>=470 and mouse_position[1]<=500)):
                    savefile = open('savefile10.txt','w',encoding = 'utf-8')
                    savefile.write(str(what_scene)+'\n')
                    savefile.write(str(self.line_no)+'\n')
                    savefile.write(str(rope_purchased[0])+'\n')
                    savefile.write(str(rope_purchased[1])+'\n')
                    savefile.write(str(dagger_purchased)+'\n')
                    savefile.write(str(doll_purchased)+'\n')
                    savefile.write(str(info_purchased)+'\n')
                    savefile.write(str(game_currency)+'\n')
                    savefile.write(str(shop_access)+'\n')
                    savefile.write(str(lanaya_chosen)+'\n')
                    savefile.write(str(yorjan_chosen)+'\n')
                    savefile.write(str(now.year)+':'+str(now.month)+':'+str(now.day)+':'+str(now.hour)+':'+str(now.minute)+':'+str(now.second))
                    savefile.close()
                    self.save_on = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and self.load_on == 1 and (mouse_position[0]>970 and mouse_position[0]<1230) and (mouse_position[1]>110 and mouse_position[1]<140):
                    open_file = open('savefile1.txt','r',encoding = 'utf-8')
                    for i in open_file:
                        tempstring+=i
                    file_details = tempstring.split('\n')
                    what_scene = file_details[0]
                    current_line = int(file_details[1])
                    rope_purchased = [int(file_details[2]),int(file_details[3])]
                    dagger_purchased = int(file_details[4])
                    doll_purchased = int(file_details[5])
                    info_purchased = int(file_details[6])
                    game_currency = int(file_details[7])
                    shop_access = int(file_details[8])
                    lanaya_chosen = int(file_details[9])
                    yorjan_chosen = int(file_details[10])
                    self.load_on = 0
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self.load_on == 1 and (mouse_position[0]>970 and mouse_position[0]<1230) and (mouse_position[1]>150 and mouse_position[1]<180):
                    open_file = open('savefile2.txt','r',encoding = 'utf-8')
                    for i in open_file:
                        tempstring+=i
                    file_details = tempstring.split('\n')
                    what_scene = file_details[0]
                    current_line = int(file_details[1])
                    rope_purchased = [int(file_details[2]),int(file_details[3])]
                    dagger_purchased = int(file_details[4])
                    doll_purchased = int(file_details[5])
                    info_purchased = int(file_details[6])
                    game_currency = int(file_details[7])
                    shop_access = int(file_details[8])
                    lanaya_chosen = int(file_details[9])
                    yorjan_chosen = int(file_details[10])
                    self.load_on = 0
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self.load_on == 1 and (mouse_position[0]>970 and mouse_position[0]<1230) and (mouse_position[1]>190 and mouse_position[1]<220):
                    open_file = open('savefile3.txt','r',encoding = 'utf-8')
                    for i in open_file:
                        tempstring+=i
                    file_details = tempstring.split('\n')
                    what_scene = file_details[0]
                    current_line = int(file_details[1])
                    rope_purchased = [int(file_details[2]),int(file_details[3])]
                    dagger_purchased = int(file_details[4])
                    doll_purchased = int(file_details[5])
                    info_purchased = int(file_details[6])
                    game_currency = int(file_details[7])
                    shop_access = int(file_details[8])
                    lanaya_chosen = int(file_details[9])
                    yorjan_chosen = int(file_details[10])
                    self.load_on = 0
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self.load_on == 1 and (mouse_position[0]>970 and mouse_position[0]<1230) and (mouse_position[1]>230 and mouse_position[1]<260):
                    open_file = open('savefile4.txt','r',encoding = 'utf-8')
                    for i in open_file:
                        tempstring+=i
                    file_details = tempstring.split('\n')
                    what_scene = file_details[0]
                    current_line = int(file_details[1])
                    rope_purchased = [int(file_details[2]),int(file_details[3])]
                    dagger_purchased = int(file_details[4])
                    doll_purchased = int(file_details[5])
                    info_purchased = int(file_details[6])
                    game_currency = int(file_details[7])
                    shop_access = int(file_details[8])
                    lanaya_chosen = int(file_details[9])
                    yorjan_chosen = int(file_details[10])
                    self.load_on = 0
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self.load_on == 1 and (mouse_position[0]>970 and mouse_position[0]<1230) and (mouse_position[1]>270 and mouse_position[1]<300):
                    open_file = open('savefile5.txt','r',encoding = 'utf-8')
                    for i in open_file:
                        tempstring+=i
                    file_details = tempstring.split('\n')
                    what_scene = file_details[0]
                    current_line = int(file_details[1])
                    rope_purchased = [int(file_details[2]),int(file_details[3])]
                    dagger_purchased = int(file_details[4])
                    doll_purchased = int(file_details[5])
                    info_purchased = int(file_details[6])
                    game_currency = int(file_details[7])
                    shop_access = int(file_details[8])
                    lanaya_chosen = int(file_details[9])
                    yorjan_chosen = int(file_details[10])
                    self.load_on = 0
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self.load_on == 1 and (mouse_position[0]>970 and mouse_position[0]<1230) and (mouse_position[1]>310 and mouse_position[1]<340):
                    open_file = open('savefile6.txt','r',encoding = 'utf-8')
                    for i in open_file:
                        tempstring+=i
                    file_details = tempstring.split('\n')
                    what_scene = file_details[0]
                    current_line = int(file_details[1])
                    rope_purchased = [int(file_details[2]),int(file_details[3])]
                    dagger_purchased = int(file_details[4])
                    doll_purchased = int(file_details[5])
                    info_purchased = int(file_details[6])
                    game_currency = int(file_details[7])
                    shop_access = int(file_details[8])
                    lanaya_chosen = int(file_details[9])
                    yorjan_chosen = int(file_details[10])
                    self.load_on = 0
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self.load_on == 1 and (mouse_position[0]>970 and mouse_position[0]<1230) and (mouse_position[1]>350 and mouse_position[1]<380):
                    open_file = open('savefile7.txt','r',encoding = 'utf-8')
                    for i in open_file:
                        tempstring+=i
                    file_details = tempstring.split('\n')
                    what_scene = file_details[0]
                    current_line = int(file_details[1])
                    rope_purchased = [int(file_details[2]),int(file_details[3])]
                    dagger_purchased = int(file_details[4])
                    doll_purchased = int(file_details[5])
                    info_purchased = int(file_details[6])
                    game_currency = int(file_details[7])
                    shop_access = int(file_details[8])
                    lanaya_chosen = int(file_details[9])
                    yorjan_chosen = int(file_details[10])
                    self.load_on = 0
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self.load_on == 1 and (mouse_position[0]>970 and mouse_position[0]<1230) and (mouse_position[1]>390 and mouse_position[1]<420):
                    open_file = open('savefile8.txt','r',encoding = 'utf-8')
                    for i in open_file:
                        tempstring+=i
                    file_details = tempstring.split('\n')
                    what_scene = file_details[0]
                    current_line = int(file_details[1])
                    rope_purchased = [int(file_details[2]),int(file_details[3])]
                    dagger_purchased = int(file_details[4])
                    doll_purchased = int(file_details[5])
                    info_purchased = int(file_details[6])
                    game_currency = int(file_details[7])
                    shop_access = int(file_details[8])
                    lanaya_chosen = int(file_details[9])
                    yorjan_chosen = int(file_details[10])
                    self.load_on = 0
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self.load_on == 1 and (mouse_position[0]>970 and mouse_position[0]<1230) and (mouse_position[1]>430 and mouse_position[1]<470):
                    open_file = open('savefile9.txt','r',encoding = 'utf-8')
                    for i in open_file:
                        tempstring+=i
                    file_details = tempstring.split('\n')
                    what_scene = file_details[0]
                    current_line = int(file_details[1])
                    rope_purchased = [int(file_details[2]),int(file_details[3])]
                    dagger_purchased = int(file_details[4])
                    doll_purchased = int(file_details[5])
                    info_purchased = int(file_details[6])
                    game_currency = int(file_details[7])
                    shop_access = int(file_details[8])
                    lanaya_chosen = int(file_details[9])
                    yorjan_chosen = int(file_details[10])
                    self.load_on = 0
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self.load_on == 1 and (mouse_position[0]>970 and mouse_position[0]<1230) and (mouse_position[1]>470 and mouse_position[1]<510):
                    open_file = open('savefile10.txt','r',encoding = 'utf-8')
                    for i in open_file:
                        tempstring+=i
                    file_details = tempstring.split('\n')
                    what_scene = file_details[0]
                    current_line = int(file_details[1])
                    rope_purchased = [int(file_details[2]),int(file_details[3])]
                    dagger_purchased = int(file_details[4])
                    doll_purchased = int(file_details[5])
                    info_purchased = int(file_details[6])
                    game_currency = int(file_details[7])
                    shop_access = int(file_details[8])
                    lanaya_chosen = int(file_details[9])
                    yorjan_chosen = int(file_details[10])
                    self.load_on = 0
                    done = True
            if menu_on: #opens the menu box
                draw_box(self.screen,1050,90,180,330)
                draw_box(self.screen,1070,110,140,40,color2 = (117,100,0))
                draw_box(self.screen,1070,170,140,40,color2 = (117,100,0))
                draw_box(self.screen,1070,230,140,40,color2 = (117,100,0))
                draw_box(self.screen,1070,290,140,40,color2 = (117,100,0))
                draw_box(self.screen,1070,350,140,40,color2 = (117,100,0))
                textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'MAIN MENU',(255,255,255),1075,120)
                textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'SHOP',(255,255,255),1110,180)
                textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'SAVE',(255,255,255),1110,240)
                textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'LOAD',(255,255,255),1110,300)
                textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'INVENTORY',(255,255,255),1075,360)
            if self.inventory_on: #opens the inventory box
                draw_box(self.screen,1050,90,180,200)
                draw_box(self.screen,1070,110,140,40,color2 = (117,100,0))
                draw_box(self.screen,1070,170,140,40,color2 = (117,100,0))
                draw_box(self.screen,1070,230,140,40,color2 = (117,100,0))
                textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'ROPE x'+str(rope_purchased[1]),(255,255,255),1090,120)
                textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'DOLL x'+str(doll_purchased),(255,255,255),1090,180)
                textbox(self.screen,'DaysOne-Regular.ttf',fontsize-6,'P.DAGGER x' + str(dagger_purchased),(255,255,255),1075,240)
            if self.save_on or self.load_on:
                draw_box(self.screen,950,90,300,430)
                draw_box(self.screen,970,110,260,30,color2 = (117,100,0))
                draw_box(self.screen,970,150,260,30,color2 = (117,100,0))
                draw_box(self.screen,970,190,260,30,color2 = (117,100,0))
                draw_box(self.screen,970,230,260,30,color2 = (117,100,0))
                draw_box(self.screen,970,270,260,30,color2 = (117,100,0))
                draw_box(self.screen,970,310,260,30,color2 = (117,100,0))
                draw_box(self.screen,970,350,260,30,color2 = (117,100,0))
                draw_box(self.screen,970,390,260,30,color2 = (117,100,0))
                draw_box(self.screen,970,430,260,30,color2 = (117,100,0))
                draw_box(self.screen,970,470,260,30,color2 = (117,100,0))
                if len (finallist1) == 11:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'SLOT 1',(255,255,255),1070,115)
                elif len (finallist1) == 12:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,finallist1[11],(255,255,255),1010,115)
                if len (finallist2) == 11:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'SLOT 2',(255,255,255),1070,155)
                elif len (finallist2) == 12:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,finallist2[11],(255,255,255),1010,155)
                if len (finallist3) == 11:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'SLOT 3',(255,255,255),1070,195)
                elif len (finallist3) == 12:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,finallist3[11],(255,255,255),1010,195)
                if len (finallist4) == 11:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'SLOT 4',(255,255,255),1070,235)
                elif len (finallist4) == 12:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,finallist4[11],(255,255,255),1010,235)
                if len (finallist5) == 11:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'SLOT 5',(255,255,255),1070,275)
                elif len (finallist5) == 12:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,finallist5[11],(255,255,255),1010,275)
                if len (finallist6) == 11:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'SLOT 6',(255,255,255),1070,315)
                elif len (finallist6) == 12:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,finallist6[11],(255,255,255),1010,315)
                if len (finallist7) == 11:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'SLOT 7',(255,255,255),1070,355)
                elif len (finallist7) == 12:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,finallist7[11],(255,255,255),1010,355)
                if len (finallist8) == 11:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'SLOT 8',(255,255,255),1070,395)
                elif len (finallist8) == 12:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,finallist8[11],(255,255,255),1010,395)
                if len (finallist9) == 11:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'SLOT 9',(255,255,255),1070,435)
                elif len (finallist9) == 12:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,finallist9[11],(255,255,255),1010,435)
                if len (finallist10) == 11:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,'SLOT 10',(255,255,255),1070,475)
                elif len (finallist10) == 12:
                    textbox(self.screen,'DaysOne-Regular.ttf',fontsize-4,finallist10[11],(255,255,255),1010,475)
            for decision in self.choices:
                if decision[0] == self.line_no and len(decision[1]) == 2:
                    draw_button(self.screen,400,100,500,80,color2 = (3,0,70))
                    draw_button(self.screen,400,300,500,80,color2 = (3,0,70))
                    textbox(self.screen,'BEBAS.ttf',decision[2],decision[1][0],(255,255,255),decision[3][0],120)
                    textbox(self.screen,'BEBAS.ttf',decision[2],decision[1][1],(255,255,255),decision[3][1],320)
                    self.decision_on = 1
                elif decision[0] == self.line_no and len(decision[1]) == 3:
                    draw_button(self.screen,400,100,500,80,color2 = (3,0,70))
                    draw_button(self.screen,400,250,500,80,color2 = (3,0,70))
                    draw_button(self.screen,400,400,500,80,color2 = (3,0,70))
                    textbox(self.screen,'BEBAS.ttf',decision[2],decision[1][0],(255,255,255),decision[3][0],120)
                    textbox(self.screen,'BEBAS.ttf',decision[2],decision[1][1],(255,255,255),decision[3][1],270)
                    textbox(self.screen,'BEBAS.ttf',decision[2],decision[1][2],(255,255,255),decision[3][2],420)
                    self.decision_on = 1
            if self.line_no == len(self.script):
                done = True
                pygame.mixer.music.stop()
                if str(what_scene[1]).isdigit():
                    what_scene = str(int(what_scene[0:2])+1)
                else:
                    what_scene = str(int(what_scene[0])+1)
                current_line = 1
def main():
    global what_scene
    global current_line
    global now
    global save_file_list
    global clock
    global rope_purchased
    global dagger_purchased
    global doll_purchased
    global info_purchased
    global game_currency
    global currency_1
    global shop_access
    global lanaya_chosen
    global yorjan_chosen
    pygame.init()
    pygame.font.init()
    save_file_list = ['savefile1.txt','savefile2.txt','savefile3.txt','savefile4.txt','savefile5.txt','savefile6.txt','savefile7.txt','savefile8.txt','savefile9.txt','savefile10.txt']
    what_scene = '0'
    current_line = 0
    rope_purchased = [0,0]
    doll_purchased = 0
    dagger_purchased = 0
    info_purchased = 0
    game_currency = 0
    currency1 = 0
    shop_access = 0
    lanaya_chosen = 0
    yorjan_chosen = 0
    clock = pygame.time.Clock()
    start_menu()
    while what_scene != '1':
        now = datetime.datetime.now()
        if what_scene == '2':
            scene1 = scene()
            scene1.line_no = current_line
            scene1.bg_img('red-and-black-background-picture-17-free-wallpaper.png')
            scene1.ins_audio('ProductionMusic__Instrumental_Version__-_Cinematic_Dark_Suspense_Mystic_Thriller_Background_Music_Film_Atmosphere_Theme_001.mp3')
            scene1.ins_script('scene1.txt')
            scene1.ins_sprite('Dark_Dementor.png',5,5,400,80,650,660)
            scene1.ins_sprite('Dark_Dementor.png',9,9,400,80,650,660)
            scene1.ins_sprite('Dark_Dementor.png',11,11,400,80,650,660)
            scene1.ins_sprite('Dark_Dementor.png',16,16,400,80,650,660)
            scene1.ins_sprite('Dark_Dementor.png',24,24,400,80,650,660)
            scene1.ins_sprite('Dark_Dementor.png',26,26,400,80,650,660)
            scene1.ins_sprite('Dark_Dementor.png',28,28,400,80,650,660)
            scene1.ins_sprite('Dark_Dementor.png',33,33,400,80,650,660)
            scene1.ins_sprite('Dark_Dementor.png',37,37,400,80,650,660)
            scene1.ins_sprite('Dark_Dementor.png',52,52,400,80,650,660)
            scene1.ins_sprite('Dark_Dementor.png',57,57,400,80,650,660)
            scene1.ins_sprite('Dark_Dementor.png',59,59,400,80,650,660)
            scene1.ins_sprite('Dark_Dementor.png',65,65,400,80,650,660)
            scene1.ins_sprite('Dark_Dementor.png',68,68,400,80,650,660)
            scene1.ins_sprite('Yorjan Sad.png.png',30,30,380,60,690,680)
            scene1.ins_sprite('Lanaya Sad.png.png',45,45,400,80,552,560)
            scene1.ins_sprite('Lanaya Sad.png.png',47,48,400,80,552,560)
            scene1.run_scene('Futura Book font.ttf',23)
        elif what_scene == '3':
            scene2 = scene()
            scene2.bg_img('underground_by_jordangrimmer_d9uj0ml-pre.jpg')
            scene2.ins_audio('Violet Evergarden OST - Rust.mp3')
            scene2.ins_script('scene2.txt')
            scene2.ins_sprite('Yorjan Talking.png.png',10,10,380,60,690,680)
            scene2.ins_sprite('Lanaya Angry.png.png',12,12,400,80,552,560)
            scene2.ins_sprite('Lanaya Angry.png.png',14,14,400,80,552,560)
            scene2.ins_sprite('Lanaya Talking.png.png',17,17,400,80,552,560)
            scene2.ins_sprite('Lanaya Angry.png.png',19,19,400,80,552,560)
            scene2.ins_sprite('Yorjan Angry.png.png',22,22,380,60,690,680)
            scene2.ins_sprite('Yorjan Normal.png.png',24,24,380,60,690,680)
            scene2.ins_sprite('Lanaya Talking.png.png',26,26,400,80,552,560)
            scene2.ins_sprite('Yorjan Talking.png.png',27,27,380,60,690,680)
            scene2.run_scene('Futura Book font.ttf',23)
        elif what_scene == '4':
            scene3 = scene()
            scene3.bg_img('jungle_path_by_ljfhutch_d4yoj5u-fullview.jpg')
            scene3.ins_audio('Made in Abyss   - OST -Rafters.mp3')
            scene3.ins_script('scene3.txt')
            scene3.ins_sprite('Claude Normal.png.png',4,4,320,60,750,660)
            scene3.ins_sprite('Yorjan Talking.png.png',5,5,380,60,690,680)
            scene3.ins_sprite('Lanaya Happy.png.png',7,8,50,80,552,560)#for Lanaya on the left side
            scene3.ins_sprite('Yorjan Angry.png.png',7,9,600,60,690,680)#for yorjan on the right side
            scene3.ins_sprite('Lanaya Angry.png.png',9,9,50,80,552,560)
            scene3.ins_sprite('Claude Normal.png.png',10,10,320,60,750,660)
            scene3.ins_sprite('Claude Normal.png.png',13,13,320,60,750,660)
            scene3.ins_sprite('Claude Normal.png.png',18,18,320,60,750,660)
            scene3.ins_sprite('Lanaya Angry.png.png',19,20,50,80,552,560)
            scene3.ins_sprite('Claude Normal.png.png',20,20,500,60,750,660)
            scene3.ins_sprite('Claude Normal.png.png',22,22,320,60,750,660)
            scene3.ins_sprite('Claude Talking.png.png',23,23,320,60,750,660)
            scene3.ins_sprite('Claude Normal.png.png',24,24,320,60,750,660)
            scene3.ins_sprite('Claude Normal.png.png',26,26,320,60,750,660)
            scene3.run_scene('Futura Book font.ttf',23)
        elif what_scene == '5':
            scene4 = scene()
            scene4.bg_img('forgotten_forest_by_mirojohannes_d4whsx1-fullview.jpg')
            scene4.ins_audio('Made in Abyss OST 13. Relinquish.mp3')
            scene4.ins_script('scene4.txt')
            scene4.ins_sprite('Claude Talking.png.png',3,3,320,60,750,660)
            scene4.ins_sprite('Claude Talking.png.png',7,7,320,60,750,660)
            scene4.ins_sprite('Lanaya Angry.png.png',10,10,400,80,552,560)
            scene4.ins_sprite('Claude Talking.png.png',11,11,320,60,750,660)
            scene4.ins_sprite('Yorjan Talking.png.png',12,12,380,60,690,680)
            scene4.ins_sprite('Claude Talking.png.png',14,14,320,60,750,660)
            scene4.ins_sprite('Yorjan Angry.png.png',21,21,380,60,690,680)
            scene4.ins_sprite('Lanaya Angry.png.png',23,23,400,80,552,560)
            scene4.ins_sprite('Claude Talking.png.png',25,25,320,60,750,660)
            scene4.ins_sprite('Lanaya Angry.png.png',28,28,400,80,552,560)
            scene4.ins_sprite('Lanaya Angry.png.png',33,33,400,80,552,560)
            scene4.ins_sprite('Claude Talking.png.png',36,36,320,60,750,660)
            scene4.ins_sprite('Claude Talking.png.png',38,38,320,60,750,660)
            scene4.ins_sprite('Claude Sad.png.png',39,39,320,60,750,660)
            scene4.ins_sprite('Lanaya Angry.png.png',43,44,400,80,552,560)
            scene4.ins_sprite('Yorjan Talking.png.png',48,48,380,60,690,680)
            scene4.ins_sprite('Claude Sad.png.png',49,49,320,60,750,660)
            scene4.ins_sprite('Claude Sad.png.png',51,51,320,60,750,660)
            scene4.ins_sprite('Lanaya Angry.png.png',52,53,50,80,552,560)
            scene4.ins_sprite('Yorjan Angry.png.png',53,53,600,60,690,680)
            scene4.run_scene('Futura Book font.ttf',23)
        elif what_scene == '6':
            scene5 = scene()
            scene5.bg_img('village_by_vityar83_d8f9uxv-pre.jpg')
            scene5.ins_audio('Violet Evergarden - The Ultimate Price.mp3')
            scene5.ins_script('scene5.txt')
            scene5.ins_sprite('Lanaya Angry.png.png',3,3,400,80,552,560)
            scene5.ins_sprite('Claude Sad.png.png',7,7,320,60,750,660)#claude in middle
            scene5.ins_sprite('Lanaya Angry.png.png',9,9,50,80,552,560)#lanaya in the left
            scene5.ins_sprite('Yorjan Angry.png.png',8,9,600,60,690,680)#yorjan in the right
            scene5.ins_sprite('Claude Sad.png.png',11,11,320,60,750,660)
            scene5.ins_sprite('Lanaya Angry.png.png',12,12,400,80,552,560)#lanaya in the middle
            scene5.ins_sprite('Claude Sad.png.png',14,15,50,60,750,660)#claude in the left
            scene5.ins_sprite('Yorjan Angry.png.png',15,15,600,60,690,680)
            scene5.ins_sprite('Claude Normal.png.png',17,17,320,60,750,660)
            scene5.ins_sprite('Claude Normal.png.png',19,19,320,60,750,660)
            scene5.ins_sprite('Lanaya Talking.png.png',20,20,400,80,552,560)
            scene5.ins_sprite('Claude Normal.png.png',22,22,320,60,750,660)
            scene5.ins_sprite('Claude Normal.png.png',24,24,320,60,750,660)
            scene5.ins_sprite('Claude Sad.png.png',25,25,320,60,750,660)
            scene5.run_scene('Futura Book font.ttf',23)
        elif what_scene == '7':
            scene6 = scene()
            scene6.bg_img('old_town_by_kotnonekot_d55s99y-fullview.jpg')
            scene6.ins_audio('Violet Evergarden OST - Never Coming Back.mp3')
            scene6.ins_script('scene6.txt')
            scene6.ins_sprite('Lanaya Normal.png.png',7,7,400,80,552,560)
            scene6.ins_sprite('Yorjan Talking.png.png',8,8,380,60,690,680)
            scene6.ins_sprite('Lanaya Talking.png.png',13,13,400,80,552,560)
            scene6.ins_sprite('Yorjan Talking.png.png',16,16,380,60,690,680)
            scene6.ins_sprite('Lanaya Talking.png.png',18,18,400,80,552,560)
            scene6.run_scene('Futura Book font.ttf',23)
        elif what_scene == '8': #insert sprites starting here
            scene7 = scene()
            scene7.bg_img('underground_by_jordangrimmer_d9uj0ml-pre.jpg')
            scene7.ins_audio('Violet Evergarden OST - Rust.mp3')
            scene7.ins_script('scene7.txt')
            scene7.ins_decision(14,['Look around for possible items','Leave right away'],35,[400,520])
            scene7.run_scene('Futura Book font.ttf',23)
        elif what_scene == '9a':
            lanaya_chosen+=1
            scene7a = scene()
            scene7a.bg_img('underground_by_jordangrimmer_d9uj0ml-pre.jpg')
            scene7a.ins_audio('Violet Evergarden OST - Rust.mp3')
            scene7a.ins_script('scene7a.txt')
            scene7a.run_scene('Futura Book font.ttf',23)
        elif what_scene == '9b':
            yorjan_chosen.append('7')
            scene7b = scene()
            scene7b.bg_img('underground_by_jordangrimmer_d9uj0ml-pre.jpg')
            scene7b.ins_audio('Violet Evergarden OST - Rust.mp3')
            scene7b.ins_script('scene7b.txt')
            scene7b.run_scene('Futura Book font.ttf',23)
        elif what_scene == '10':
            scene8 = scene()
            scene8.bg_img('Mystery_Sanctuary.jpg')
            scene8.ins_audio('INTENSE SUSPENSE BACKGROUND MUSIC.mp3')
            scene8.ins_script('scene8.txt')
            scene8.ins_sprite('Yorjan Angry.png.png',7,7,600,60,690,680)
            scene8.ins_sprite('Yorjan Talking.png.png',13,13,600,60,690,680)
            scene8.ins_sprite('')
            scene8.run_scene('Futura Book font.ttf',23)
        elif what_scene == '11':
            scene9 = scene()
            scene9.bg_img('Mystery_Sanctuary.jpg')
            scene9.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene9.ins_script('scene9.txt')
            scene9.ins_decision(24,['Left Path','Right Path'],35,[540,538])
            scene9.run_scene('Futura Book font.ttf',23)
        elif what_scene == '12a':
            lanaya_chosen+=1
            scene9a = scene()
            scene9a.bg_img('Mystery_Sanctuary.jpg')
            scene9a.ins_audio('Made in Abyss OST - Tomorrow (メイドインアビス OST).mp3')
            scene9a.ins_script('scene9a.txt')
            scene9a.run_scene('Futura Book font.ttf',23)
        elif what_scene == '12b':
            yorjan_chosen+=1
            scene9a = scene()
            scene9a.bg_img('Mystery_Sanctuary.jpg')
            scene9a.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene9a.ins_script('scene9b.txt')
            scene9a.run_scene('Futura Book font.ttf',23)
        elif what_scene == '13':
            scene10 = scene()
            scene10.bg_img('Mystery_Sanctuary.jpg')
            scene10.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene10.ins_script('scene10.txt')
            scene10.ins_sprite('Yorjan Talking.png.png',3,3,600,60,690,680)
            scene10.ins_sprite('Yorjan Talking.png.png',7,7,600,60,690,680)
            scene10.ins_sprite('Lanaya Talking.png.png',8,8,400,80,552,560)
            scene10.ins_decision(9,['Attack the Monster','Ignore and walk away'],35,[510,510])
            scene10.run_scene('Futura Book font.ttf',23)
        elif what_scene == '14a':
            scene10a = scene()
            scene10a.bg_img('Mystery_Sanctuary.jpg')
            scene10a.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            if lanaya_chosen>0:
                if dagger_purchased:
                    scene10a.ins_script('scene10aa.txt')
                    scene10a.ins_sprite('Lanaya Normal.png.png',5,5,400,80,552,560)
                    scene10a.ins_sprite('Yorjan Sad.png.png',6,6,600,60,690,680)
                    scene10a.ins_sprite('Yorjan Talking.png.png',13,13,600,60,690,680)
                    scene10a.ins_sprite('Lanaya Talking.png.png',14,14,400,80,552,560)
                    scene10a.ins_sprite('Lanaya Talking.png.png',21,21,400,80,552,560)
                    scene10a.ins_sprite('Yorjan Sad.png.png',23,23,600,60,690,680)
                    scene10a.ins_sprite('Lanaya Happy.png.png',26,26,50,80,552,560)
                    scene10a.ins_sprite('Lanaya Happy.png.png',27,27,50,80,552,560)
                    scene10a.ins_sprite('Yorjan Angry.png.png',27,27,600,60,690,680)
                    scene10a.ins_sprite('Lanaya Happy.png.png',28,28,400,80,552,560)
                    scene10a.ins_sprite('Yorjan Talking.png.png',30,30,600,60,690,680)

                else:
                    scene10a.ins_script('scene10ab.txt')
                    scene10a.ins_sprite('Lanaya Normal.png.png',5,5,400,80,552,560)
                    scene10a.ins_sprite('Yorjan Sad.png.png',6,6,600,60,690,680)
                    scene10a.ins_sprite('Yorjan Talking.png.png',13,13,600,60,690,680)
                    scene10a.ins_sprite('Lanaya Talking.png.png',14,14,400,80,552,560)
                    scene10a.ins_sprite('Lanaya Happy.png.png',21,21,400,80,552,560)
                    scene10a.ins_sprite('Yorjan Sad.png.png',23,23,600,60,690,680)
                    scene10a.ins_sprite('Lanaya Happy.png.png', 26, 26, 50, 80, 552, 560)
                    scene10a.ins_sprite('Lanaya Happy.png.png', 27, 27, 50, 80, 552, 560)
                    scene10a.ins_sprite('Yorjan Angry.png.png', 27, 27, 600, 60, 690, 680)
                    scene10a.ins_sprite('Lanaya Happy.png.png', 28, 28, 400, 80, 552, 560)
                    scene10a.ins_sprite('Yorjan Talking.png.png',30,30,600,60,690,680)

            else:
                if dagger_purchased:
                    scene10a.ins_script('scene10ac.txt')
                    scene10a.ins_sprite('Lanaya Angry.png.png',0,0,400,80,552,560)
                    scene10a.ins_sprite('Lanaya Angry.png.png',1,1,400,80,552,560)
                    scene10a.ins_sprite('Yorjan Angry.png.png', 1, 1, 600, 60, 690, 680)
                    scene10a.ins_sprite('Yorjan Talking.png.png',3,3,600,60,690,680)
                    scene10a.ins_sprite('Yorjan Talking.png.png',10,10,600,60,690,680)
                    scene10a.ins_sprite('Lanaya Talking.png.png',11,11,400,80,552,560)
                    scene10a.ins_sprite('Lanaya Angry.png.png',18,18,400,80,552,560)
                    scene10a.ins_sprite('Yorjan Talking.png.png',19,19,600,60,690,680)
                    scene10a.ins_sprite('Yorjan Sad.png.png',21,21,600,60,690,680)
                    scene10a.ins_sprite('Lanaya Sad.png.png',24,24,400,80,552,560)
                    scene10a.ins_sprite('Yorjan Angry.png.png', 25, 25, 600, 60, 690, 680)
                    scene10a.ins_sprite('Yorjan Talking.png.png',27,27,600,60,690,680)




                else:
                    scene10a.ins_script('scene10ad.txt')
                    scene10a.ins_sprite('Lanaya Angry.png.png',0,0,400,80,552,560)
                    scene10a.ins_sprite('Lanaya Angry.png.png',1,1,400,80,552,560)
                    scene10a.ins_sprite('Yorjan Angry.png.png', 1, 1, 600, 60, 690, 680)
                    scene10a.ins_sprite('Yorjan Talking.png.png',3,3,600,60,690,680)
                    scene10a.ins_sprite('Yorjan Talking.png.png',10,10,600,60,690,680)
                    scene10a.ins_sprite('Lanaya Talking.png.png',11,11,400,80,552,560)
                    scene10a.ins_sprite('Lanaya Angry.png.png',18,18,400,80,552,560)
                    scene10a.ins_sprite('Yorjan Talking.png.png',19,19,600,60,690,680)
                    scene10a.ins_sprite('Yorjan Sad.png.png',21,21,600,60,690,680)
                    scene10a.ins_sprite('Lanaya Sad.png.png',24,24,400,80,552,560)
                    scene10a.ins_sprite('Yorjan Angry.png.png', 25, 25, 600, 60, 690, 680)
                    scene10a.ins_sprite('Yorjan Talking.png.png',27,27,600,60,690,680)
            scene10a.run_scene('Futura Book font.ttf',23)

        elif what_scene == '14b':
            scene10b = scene()
            scene10b.bg_img('Mystery_Sanctuary.jpg')
            scene10b.ins_script('scene10b.txt')
            scene10b.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene10b.ins_sprite('Yorjan Talking.png.png', 1, 1, 600, 60, 690, 680)
            scene10b.ins_sprite('Lanaya Talking.png.png', 3, 3, 400, 80, 552, 560)
            scene10b.ins_sprite('Lanaya Talking.png.png', 3, 3, 400, 80, 552, 560)
            scene10b.run_scene('Futura Book font.ttf',23)

        elif what_scene == '15':
            scene11 = scene()
            scene11.bg_img('Mystery_Sanctuary.jpg')
            if lanaya_chosen>0:    
                scene11.ins_script('scene11a.txt')
            else:
                scene11.ins_script('scene11b.txt')
            scene11.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene11.run_scene('Futura Book font.ttf',23)
        elif what_scene == '16':
            scene12 = scene()
            scene12.bg_img('Mystery_Sanctuary.jpg')
            if doll_purchased:    
                scene12.ins_script('scene12a.txt')
                scene12.ins_sprite('Claude Talking.png.png',2,2,320,60,750,660)
                scene12.ins_sprite('Yorjan Talking.png.png', 3, 3, 600, 60, 690, 680)
                scene12.ins_sprite('Lanaya Happy.png.png', 5, 5, 400, 80, 552, 560)
                scene12.ins_sprite('Claude Talking.png.png',7,7,320,60,750,660)
                scene12.ins_sprite('Claude Talking.png.png',9,9,320,60,750,660)
                scene12.ins_sprite('Claude Talking.png.png',11,11,320,60,750,660)
                scene12.ins_sprite('Lanaya Sad.png.png', 12, 12, 50, 80, 552, 560)
                scene12.ins_sprite('Lanaya Sad.png.png', 13, 13, 50, 80, 552, 560)
                scene12.ins_sprite('Yorjan Normal.png.png', 13, 13, 600, 60, 690, 680)
                scene12.ins_sprite('Yorjan Angry.png.png', 16, 16, 600, 60, 690, 680)
                scene12.ins_sprite('Claude Talking.png.png',23,23,320,60,750,660)
                scene12.ins_decision(25,['Follow the Chupacabras','Listen to Claude'],30,[510,520])

            else:
                scene12.ins_script('scene12b.txt')
                what_scene = str(int(what_scene)+1)
                scene12.ins_audio('Made in Abyss OST - Tomorrow.mp3')
                scene12.ins_sprite('Claude Talking.png.png',2,2,320,60,750,660)
                scene12.ins_sprite('Yorjan Talking.png.png', 3, 3, 600, 60, 690, 680)
                scene12.ins_sprite('Lanaya Happy.png.png', 5, 5, 400, 80, 552, 560)
                scene12.ins_sprite('Claude Talking.png.png',7,7,320,60,750,660)
                scene12.ins_sprite('Claude Talking.png.png',9,9,320,60,750,660)
                scene12.ins_sprite('Claude Talking.png.png',11,11,320,60,750,660)
                scene12.ins_sprite('Lanaya Sad.png.png', 12, 12, 50, 80, 552, 560)
                scene12.ins_sprite('Lanaya Sad.png.png', 13, 13, 50, 80, 552, 560)
                scene12.ins_sprite('Yorjan Normal.png.png', 13, 13, 600, 60, 690, 680)
                scene12.ins_sprite('Yorjan Angry.png.png', 16, 16, 600, 60, 690, 680)
                scene12.ins_sprite('Claude Talking.png.png',23,23,320,60,750,660)
                scene12.ins_sprite('Yorjan Sad.png.png', 29, 29, 600, 60, 690, 680)
                scene12.ins_sprite('Lanaya Normal.png.png',30,30, 400, 80, 552, 560)
                scene12.run_scene('Futura Book font.ttf',23)

        elif what_scene == '17a':
            scene12a = scene()
            scene12a.bg_img('Mystery_Sanctuary.jpg')
            scene12a.ins_script('scene12aa.txt')
            scene12a.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene12a.ins_sprite('Claude Talking.png.png', 2, 2, 320, 60, 750, 660)
            scene12a.ins_sprite('Yorjan Sad.png.png', 6, 6, 600, 60, 690, 680)
            scene12a.ins_sprite('Lanaya Normal.png.png', 7, 7, 400, 80, 552, 560)
            scene12a.run_scene('Futura Book font.ttf',23)

        elif what_scene == '17b':
            scene12b = scene()
            scene12b.bg_img('Mystery_Sanctuary.jpg')
            scene12b.ins_script('scene12ab.txt')
            scene12b.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene12b.ins_sprite('Yorjan Sad.png.png', 6, 6, 600, 60, 690, 680)
            scene12b.ins_sprite('Lanaya Normal.png.png', 7, 7, 400, 80, 552, 560)
            scene12b.run_scene('Futura Book font.ttf',23)
        elif what_scene == '18':
            scene13 = scene()
            scene13.bg_img('Mystery_Sanctuary.jpg')
            scene13.ins_script('scene13.txt')
            scene13.ins_decision(5,["Call Lanaya's attention","Attack it myself"],30,[500,510])
            scene13.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene13.run_scene('Futura Book font.ttf',23)
        elif what_scene == '19a':
            scene13a = scene()
            lanaya_chosen+=1
            scene13a.bg_img('Mystery_Sanctuary.jpg')
            if lanaya_chosen>0:
                scene13a.ins_script('scene13aa.txt')
            else:
                scene13a.ins_script('scene13ab.txt')
            scene13a.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene13a.run_scene('Futura Book font.ttf',23)
        elif what_scene == '19b':
            scene13b = scene()
            yorjan_chosen+=1
            scene13b.bg_img('Mystery_Sanctuary.jpg')
            if lanaya_chosen>0:
                scene13b.ins_script('scene13ac.txt')
            else:
                scene13b.ins_script('scene13ad.txt')
            scene13b.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene13b.run_scene('Futura Book font.ttf',23)
        elif what_scene == '20':
            scene14 = scene()
            scene14.bg_img('Mystery_Sanctuary.jpg')
            scene14.ins_script('scene14.txt')
            scene14.ins_sprite('Yorjan Talking.png.png', 1, 1, 600, 60, 690, 680)
            scene14.ins_sprite('Lanaya Sad.png.png', 2, 2, 400, 80, 552, 560)
            scene14.ins_sprite('Yorjan Sad.png.png', 4, 4, 600, 60, 690, 680)
            scene14.ins_sprite('Lanaya Talking.png.png', 6, 6, 400, 80, 552, 560)
            scene14.ins_sprite('Yorjan Talking.png.png', 14, 14, 600, 60, 690, 680)
            scene14.ins_sprite('Yorjan Talking.png.png', 15, 15, 600, 60, 690, 680)
            scene14.ins_sprite('Lanaya Sad.png.png', 15, 15, 400, 80, 552, 560)
            scene14.ins_sprite('Lanaya Talking.png.png', 18, 18, 50, 80, 552, 560)
            scene14.ins_sprite('Lanaya Talking.png.png', 19, 19, 50, 80, 552, 560)
            scene14.ins_sprite('Yorjan Talking.png.png', 19, 19, 600, 60, 690, 680)
            scene14.ins_sprite('Lanaya Talking.png.png', 20, 20, 50, 80, 552, 560)
            scene14.ins_sprite('Yorjan Talking.png.png', 20, 20, 600, 60, 690, 680)
            scene14.ins_sprite('Yorjan Talking.png.png', 21, 21, 600, 60, 690, 680)
            scene14.ins_sprite('Lanaya Talking.png.png', 21, 21, 50, 80, 552, 560)
            scene14.ins_sprite('Lanaya Talking.png.png', 22, 22, 50, 80, 552, 560)
            scene14.ins_sprite('Yorjan Talking.png.png', 22, 22, 600, 60, 690, 680)

            scene14.ins_decision(24,['Go with Yorjan (Left)','Go with Lanaya (Right)'],30,[490,490])
            scene14.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene14.run_scene('Futura Book font.ttf',23)

        elif what_scene == '21a':
            scene14a = scene()
            yorjan_chosen+=1
            scene14a.bg_img('Mystery_Sanctuary.jpg')
            if lanaya_chosen>0:
                scene14a.ins_script('scene14aa.txt')
                scene14a.ins_sprite('Yorjan Normal.png.png', 2, 2, 600, 60, 690, 680)
                scene14a.ins_sprite('Lanaya Angry.png.png', 3, 3, 50, 80, 552, 560)
                scene14a.ins_sprite('Lanaya Normal.png.png', 8, 8, 400, 80, 552, 560)
                scene14a.ins_sprite('Yorjan Talking.png.png', 10, 10, 600, 60, 690, 680)
                scene14a.ins_sprite('Yorjan Talking.png.png', 14, 14, 600, 60, 690, 680)
                scene14a.ins_sprite('Yorjan Happy.png.png', 16, 16, 600, 60, 690, 680)
                scene14a.ins_sprite('Yorjan Talking.png.png',18, 18, 600, 60, 690, 680)
                scene14a.ins_sprite('Yorjan Happy.png.png',20, 20, 600, 60, 690, 680)


            else:
                scene14a.ins_script('scene14ab.txt')
                scene14a.ins_sprite('Yorjan Talking.png.png', 2, 2, 600, 60, 690, 680)
                scene14a.ins_sprite('Yorjan Normal.png.png', 3, 3, 600, 60, 690, 680)
                scene14a.ins_sprite('Lanaya Angry.png.png', 3, 3, 50, 80, 552, 560)
                scene14a.ins_sprite('Lanaya Angry.png.png', 5, 5, 400, 80, 552, 560)
                scene14a.ins_sprite('Lanaya Angry.png.png', 7, 7, 400, 80, 552, 560)
                scene14a.ins_sprite('Yorjan Talking.png.png', 13, 13, 600, 60, 690, 680)
                scene14a.ins_sprite('Lanaya Talking.png.png', 15, 15, 400, 80, 552, 560)
                scene14a.ins_sprite('Yorjan Talking.png.png', 19, 19, 600, 60, 690, 680)
                scene14a.ins_sprite('Yorjan Happy.png.png',21, 21, 600, 60, 690, 680)
                scene14a.ins_sprite('Yorjan Talking.png.png',23, 23, 600, 60, 690, 680)
                scene14a.ins_sprite('Yorjan Happy.png.png',25, 25, 600, 60, 690, 680)

            scene14a.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene14a.run_scene('Futura Book font.ttf',23)
        elif what_scene == '21b':
            scene14b = scene()
            lanaya_chosen+=1
            scene14b.bg_img('Mystery_Sanctuary.jpg')
            if lanaya_chosen>=2:
                scene14b.ins_script('scene14ac.txt')
                scene14b.ins_sprite('Lanaya Talking.png.png', 2, 2, 400, 80, 552, 560)
                scene14b.ins_sprite('Yorjan Talking.png.png', 3, 3, 600, 60, 690, 680)
                scene14b.ins_sprite('Lanaya Talking.png.png', 5, 5, 400, 80, 552, 560)
                scene14b.ins_sprite('Lanaya Talking.png.png', 9, 9, 400, 80, 552, 560)
                scene14b.ins_sprite('Lanaya Happy.png.png', 10, 10, 50, 80, 552, 560)
                scene14b.ins_sprite('Yorjan Happy.png.png', 10, 10, 600, 60, 690, 680)
                scene14b.ins_sprite('Lanaya Talking.png.png', 11, 11, 50, 80, 552, 560)
                scene14b.ins_sprite('Lanaya Talking.png.png', 13, 13, 400, 80, 552, 560)
                scene14b.ins_sprite('Lanaya Talking.png.png', 14, 14, 400, 80, 552, 560)
                scene14b.ins_sprite('Yorjan Talking.png.png', 18, 18, 600, 60, 690, 680)
                scene14b.ins_sprite('Yorjan Talking.png.png', 20, 20, 600, 60, 690, 680)
                scene14b.ins_sprite('Lanaya Happy.png.png', 22, 22, 400, 80, 552, 560)
                scene14b.ins_sprite('Yorjan Talking.png.png', 24, 24, 600, 60, 690, 680)
                scene14b.ins_sprite('Lanaya Happy.png.png', 26, 26, 400, 80, 552, 560)
                scene14b.ins_sprite('Yorjan Happy.png.png', 27, 27, 600, 60, 690, 680)

            else:
                scene14b.ins_script('scene14ad.txt')
                scene14b.ins_sprite('Lanaya Talking.png.png', 2, 2, 400, 80, 552, 560)
                scene14b.ins_sprite('Yorjan Talking.png.png', 3, 3, 600, 60, 690, 680)
                ene14b.ins_sprite('Lanaya Talking.png.png', 5, 5, 400, 80, 552, 560)
                scene14b.ins_sprite('Lanaya Talking.png.png', 9, 9, 400, 80, 552, 560)
                scene14b.ins_sprite('Lanaya Happy.png.png', 10, 10, 50, 80, 552, 560)
                scene14b.ins_sprite('Yorjan Happy.png.png', 10, 10, 600, 60, 690, 680)
                scene14b.ins_sprite('Lanaya Talking.png.png', 11, 11, 50, 80, 552, 560)
                scene14b.ins_sprite('Lanaya Talking.png.png', 13, 13, 400, 80, 552, 560)
                scene14b.ins_sprite('Lanaya Normal.png.png', 15, 15, 400, 80, 552, 560)
                scene14b.ins_sprite('Yorjan Talking.png.png', 20, 20, 600, 60, 690, 680)
                scene14b.ins_sprite('Yorjan Talking.png.png', 22, 22, 600, 60, 690, 680)
                scene14b.ins_sprite('Lanaya Happy.png.png', 24, 24, 400, 80, 552, 560)
                scene14b.ins_sprite('Yorjan Talking.png.png', 26, 26, 600, 60, 690, 680)
                scene14b.ins_sprite('Lanaya Happy.png.png', 28, 28, 400, 80, 552, 560)
                scene14b.ins_sprite('Yorjan Happy.png.png', 29, 29, 600, 60, 690, 680)

            scene14b.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene14b.run_scene('Futura Book font.ttf',23)
        elif what_scene == '22':
            scene15 = scene()
            scene15.bg_img('Mystery_Sanctuary.jpg')
            if rope_purchased:
                rope_purchased = str(int(rope_purchased)-1)
                scene15.ins_script('scene15a.txt')
            else:
                scene15.ins_script('scene15b.txt')
            scene15.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene15.ins_decision(34,['Kill Asterios','Let him live'],30,[530,530])
            scene15.run_scene('Futura Book font.ttf',23)
        elif what_scene == '23a':
            scene15a = scene()
            scene15a.bg_img('Mystery_Sanctuary.jpg')
            if lanaya_chosen>=2:
                scene15a.ins_script('scene15aa.txt')
            else:
                scene15a.ins_script('scene15ab.txt')
            scene15a.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene15a.run_scene('Futura Book font.ttf',23)
        elif what_scene == '23b':
            scene15b = scene()
            scene15b.bg_img('Mystery_Sanctuary.jpg')
            if lanaya_chosen>=3:
                scene15b.ins_script('scene15ac.txt')
            else:
                scene15b.ins_script('scene15ad.txt')
            scene15b.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene15b.run_scene('Futura Book font.ttf',23)
        elif what_scene == '24':
            scene16 = scene()
            scene16.bg_img('Mystery_Sanctuary.jpg')
            scene16.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            if lanaya_chosen < 2:
                scene16.ins_script('scene16a.txt')
                scene16.ins_sprite('Yorjan Talking.png.png', 2, 2, 600, 60, 690, 680)
                scene16.ins_sprite('Yorjan Talking.png.png', 5, 5, 600, 60, 690, 680)
                scene16.ins_sprite('Yorjan Talking.png.png', 9, 9, 600, 60, 690, 680)
                what_scene = str(int(what_scene)+1)

            else:
                scene16.ins_script('scene16b.txt')
                scene16.ins_sprite('Lanaya Talking.png.png', 2, 2, 400, 80, 552, 560)
                scene16.ins_sprite('Yorjan Talking.png.png', 4, 4, 600, 60, 690, 680)
                scene16.ins_sprite('Lanaya Talking.png.png', 5, 5, 400, 80, 552, 560)
                scene16.ins_sprite('Yorjan Talking.png.png', 8, 8, 600, 60, 690, 680)
                scene16.ins_sprite('Lanaya Talking.png.png', 10, 10, 400, 80, 552, 560)
                scene16.ins_sprite('Yorjan Talking.png.png', 11, 11, 600, 60, 690, 680)

                scene16.ins_decision(12,['Follow Yorjan','Follow Lanaya'],30,[520,520])
            scene16.run_scene('Futura Book font.ttf',23)
        elif what_scene == '25a':
            scene16a = scene()
            scene16a.bg_img('Mystery_Sanctuary.jpg')
            scene16a.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene16a.ins_script('scene16aa.txt')
            scene16a.ins_sprite('Lanaya Talking.png.png', 2, 2, 400, 80, 552, 560)
            scene16a.run_scene('Futura Book font.ttf',23)
        elif what_scene == '25b':
            scene16b = scene()
            scene16b.bg_img('Mystery_Sanctuary.jpg')
            scene16b.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            if yorjan_chosen <1:
                scene16b.ins_script('scene16ab.txt')
                scene16b.ins_sprite('Yorjan Angry.png.png', 2, 2, 600, 60, 690, 680)
                scene16b.ins_sprite('Yorjan Angry.png.png', 4, 4, 600, 60, 690, 680)
                scene16b.ins_sprite('Yorjan Angry.png.png', 5, 5, 600, 60, 690, 680)
                scene16b.ins_sprite('Yorjan Angry.png.png', 6, 6, 600, 60, 690, 680)
                scene16b.ins_sprite('Yorjan Angry.png.png', 8, 8, 600, 60, 690, 680)

            else:
                scene16b.ins_script('scene16ac.txt')
                scene16b.ins_sprite('Yorjan Sad.png.png', 2, 2, 600, 60, 690, 680)

            scene16b.run_scene('Futura Book font.ttf',23)
        elif what_scene == '26':
            scene17 = scene()
            scene17.bg_img('Mystery_Sanctuary.jpg')
            if lanaya_chosen <2 and info_purchased:
                scene17.ins_script('scene17a.txt')  
            elif lanaya_chosen <2 and not info_purchased:
                scene17.ins_script('scene17b.txt')
            elif lanaya_chosen >=2 and lanaya_chosen > yorjan_chosen and yorjan_chosen > 0:
                scene17.ins_script('scene17c.txt')
            elif lanaya_chosen >=2 and yorjan_chosen <1:
                scene17.ins_script('scene17d.txt')
            elif lanaya_chosen == yorjan_chosen:
                scene17.ins_script('scene17e.txt')
            scene17.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene17.run_scene('Futura Book font.ttf',23)
        elif what_scene == '27':
            scene18 = scene()
            scene18.bg_img('Mystery_Sanctuary.jpg')
            scene18.ins_script('scene18.txt')
            scene18.ins_sprite('Klaus.png.png',1,1,250,80,900,1160)
            scene18.ins_sprite('Klaus.png.png',4,4,250,80,900,1160)
            scene18.ins_sprite('Klaus.png.png',7,7,250,80,900,1160)
            scene18.ins_sprite('Klaus.png.png',8,8,250,80,900,1160)

            scene18.ins_audio('Made in Abyss OST - Tomorrow.mp3')
            scene18.run_scene('Futura Book font.ttf',23)

        elif what_scene == '28':
            if lanaya_chosen < 2 and info_purchased:
                scene20 = scene()
                scene20.bg_img('Mystery_Sanctuary.jpg')
                scene20.ins_script('scene20.txt')
                scene20.ins_sprite('Klaus.png.png',2,2,250,80,900,1160)
                scene20.ins_sprite('Klaus.png.png',2,2,250,80,900,1160)
                scene20.ins_audio('Made in Abyss OST - Tomorrow.mp3')
                scene20.run_scene('Futura Book font.ttf', 23)
            elif lanaya_chosen < 2 and not info_purchased:
                scene19 = scene()
                scene19.bg_img('Mystery_Sanctuary.jpg')
                scene19.ins_script('scene19.txt')
                scene19.ins_audio('Made in Abyss OST - Tomorrow.mp3')
                scene19.run_scene('Futura Book font.ttf', 23)
            elif yorjan_chosen < 1:
                scene21 = scene()
                scene21.bg_img('Mystery_Sanctuary.jpg')
                scene21.ins_script('scene21.txt')
                scene21.ins_audio('Made in Abyss OST - Tomorrow.mp3')
                scene21.run_scene('Futura Book font.ttf', 23)
            elif yorjan_chosen == lanaya_chosen:
                scene22 = scene()
                scene22.bg_img('Mystery_Sanctuary.jpg')
                scene22.ins_script('scene22.txt')
                scene22.ins_audio('Made in Abyss OST - Tomorrow.mp3')
                scene22.ins_sprite('Klaus.png.png',3,3,250,80,900,1160)
                scene22.ins_sprite('Klaus.png.png',5,5,250,80,900,1160)
                scene22.ins_sprite('Lanaya Angry.png.png', 6, 6, 400, 80, 552, 560)
                scene22.ins_sprite('Yorjan Talking.png.png', 7, 7, 600, 60, 690, 680)
                scene22.ins_sprite('Lanaya Talking.png.png', 11, 11, 400, 80, 552, 560)
                scene22.ins_sprite('Lanaya Talking.png.png', 13, 13, 400, 80, 552, 560)
                scene22.ins_sprite('Yorjan Talking.png.png', 15, 15, 600, 60, 690, 680)
                scene22.ins_sprite('Klaus.png.png',18,18,250,80,900,1160)
                scene22.ins_sprite('Klaus.png.png',20,20,250,80,900,1160)
                scene22.ins_sprite('Klaus.png.png',24,24,250,80,900,1160)
                scene22.ins_sprite('Lanaya Talking.png.png', 26, 26, 400, 80, 552, 560)
                scene22.ins_sprite('Yorjan Talking.png.png', 28, 28, 600, 60, 690, 680)
                scene22.run_scene('Futura Book font.ttf', 23)
            elif yorjan_chosen == 1 and final_yorjan_chosen:
                scene24 = scene()
                scene24.bg_img('Mystery_Sanctuary.jpg')
                scene24.ins_script('scene24.txt')
                scene24.ins_audio('Made in Abyss OST - Tomorrow.mp3')
                scene24.ins_sprite('Klaus.png.png',2,2,250,80,900,1160)
                scene24.ins_sprite('Yorjan Talking.png.png', 4, 4, 600, 60, 690, 680)
                scene24.ins_sprite('Klaus.png.png',5,5,250,80,900,1160)
                scene24.ins_sprite('Lanaya Talking.png.png', 6, 6, 400, 80, 552, 560)
                scene24.ins_sprite('Yorjan Talking.png.png', 7, 7, 600, 60, 690, 680)
                scene24.ins_sprite('Klaus.png.png',8,8,250,80,900,1160)
                scene24.ins_sprite('Klaus.png.png',12,12,250,80,900,1160)
                scene24.ins_sprite('Claude Resurrected Angry.png.png',13,13,320,60,750,660)
                scene24.ins_sprite('Claude Resurrected.png.png',15,15,320,60,750,660)
                scene24.ins_sprite('Yorjan Talking.png.png', 16, 16, 600, 60, 690, 680)
                scene24.ins_sprite('Lanaya Talking.png.png', 18, 18, 400, 80, 552, 560)
                scene24.ins_sprite('Klaus.png.png',19,19,250,80,900,1160)
                scene24.ins_sprite('Claude Resurrected.png.png',20,20,320,60,750,660)
                scene24.ins_sprite('Lanaya Angry.png.png', 22, 22, 400, 80, 552, 560)
                scene24.ins_sprite('Klaus.png.png',25,25,250,80,900,1160)
                scene24.ins_sprite('Lanaya Angry.png.png', 26, 26, 400, 80, 552, 560)
                scene24.ins_sprite('Klaus.png.png',27,27,250,80,900,1160)
                scene24.ins_sprite('Klaus.png.png',28,28,250,80,900,1160)
                scene24.ins_sprite('Yorjan Talking.png.png', 30, 30, 600, 60, 690, 680)
                scene24.ins_sprite('Lanaya Talking.png.png', 31, 31, 400, 80, 552, 560)
                scene24.ins_sprite('Klaus.png.png',34,34,250,80,900,1160)
                scene24.ins_sprite('Klaus.png.png',36,36,250,80,900,1160)
                scene24.ins_sprite('Lanaya Talking.png.png', 37, 37, 400, 80, 552, 560)
                scene24.ins_sprite('Yorjan Talking.png.png', 38, 38, 600, 60, 690, 680)
                scene24.ins_sprite('Yorjan Talking.png.png', 42, 42, 600, 60, 690, 680)
                scene24.ins_sprite('Lanaya Talking.png.png', 43, 43, 400, 80, 552, 560)
                scene24.ins_sprite('Claude Resurrected.png.png',44,44,320,60,750,660)
                scene24.ins_sprite('Claude Resurrected.png.png',45,45,320,60,750,660)
                scene24.ins_sprite('Claude Resurrected.png.png',46,46,320,60,750,660)
                scene24.ins_sprite('Claude Resurrected.png.png',48,48,320,60,750,660)
                scene24.ins_sprite('Lanaya Talking.png.png', 49, 49, 400, 80, 552, 560)
                scene24.ins_sprite('Yorjan Talking.png.png', 50, 50, 600, 60, 690, 680)
                scene24.ins_sprite('Claude Resurrected.png.png',51,51,320,60,750,660)
                scene24.ins_sprite('Claude Resurrected.png.png',52,52,320,60,750,660)
                scene24.ins_sprite('Lanaya Sad.png.png', 53, 53, 400, 80, 552, 560)
                scene24.ins_sprite('Yorjan Sad.png.png', 54, 54, 600, 60, 690, 680)


                scene24.run_scene('Futura Book font.ttf', 23)
            elif doll_purchased:
                scene25 = scene()
                scene25.bg_img('Mystery_Sanctuary.jpg')
                scene25.ins_script('scene25.txt')
                scene25.ins_audio('Made in Abyss OST - Tomorrow.mp3')
                scene25.run_scene('Futura Book font.ttf', 23)
            else:
                scene23 = scene()
                scene23.bg_img('Mystery_Sanctuary.jpg')
                scene23.ins_script('scene23.txt')
                scene23.ins_audio('Made in Abyss OST - Tomorrow.mp3')
                scene23.run_scene('Futura Book font.ttf', 23)

            what_scene = '0'
            start_ending()
        pygame.quit()

        if __name__ == '__main__':
            main()


