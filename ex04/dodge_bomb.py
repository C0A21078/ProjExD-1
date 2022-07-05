import random
import pygame as pg
import sys

def main():

    clock= pg.time.Clock()

    pg.display.set_caption("Run away! KouKaTon !!!")
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc  = pg.image.load("pg_bg.jpg")
    bgimg_rct  = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)
    
    # practice 3
    kkimg_sfc = pg.image.load("fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900,400

    #practice 5
    bmimg_sfc = pg.Surface((20,20))
    bmimg_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc,(255,0,0), (10,10), 10)
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    vx, vy = +1, +1


    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        
        #practice 2
        for event in pg.event.get():
            if event.type == pg.QUIT: return
       
        #practice 4
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]    == True: kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN]  == True: kkimg_rct.centery += 1
        if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        bmimg_rct.move_ip(vx,vy)
        screen_sfc.blit(bmimg_sfc, bmimg_rct)

        pg.display.update()
        clock.tick(1000)
if __name__ == '__main__':  
    pg.init()
    main()
    pg.quit()
    sys.exit()