import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")#ウィンドウの名前的な
    screen = pg.display.set_mode((800, 600))#ウィンドウの大きさ
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#画像の読み込み
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)#kk_imgを左右反転する（何を反転するか, 左右反転するか, 上下反転するか）
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])#スクリーン（左上を）に画像を貼り付ける
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()