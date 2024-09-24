import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")#ウィンドウの名前的な
    screen = pg.display.set_mode((800, 600))#ウィンドウの大きさ
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#画像の読み込み
    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img2, True, False)
    kk_img = pg.image.load("fig/3.png")#練習2
    kk_img = pg.transform.flip(kk_img, True, False)#kk_imgを左右反転する（何を反転するか, 左右反転するか, 上下反転するか）
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -(tmr % 4800)
        screen.blit(bg_img, [x, 0])#スクリーンに画像を貼り付ける/練習６間延び解消背景動かす
        screen.blit(bg_img2, [x + 1600, 0])
        screen.blit(bg_img, [x + 3200, 0])
        screen.blit(bg_img2, [x + 4800, 0])
        screen.blit(kk_img, [300, 200])#練習4
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()