#!/usr/bin/env python3

import pygame as pg

from cube import RubicsCube
import translate as tr
#from playground import playground


# Klasy
# Klasa reprezentujaca przycisk
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self, color):
        pg.draw.rect(screen, color, self.rect)
        font = pg.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()


# Funkcje
def draw_side(index, x, y):
    for l in range(3):
        for p in range(3):
            pg.draw.rect(
                screen,
                cube.state[index][l][p],
                (
                    int(p * rect_size * 1.1 + rect_size * 3.3 * x),
                    int(l * rect_size * 1.1 + rect_size * 3.3 * y),
                    rect_size,
                    rect_size
                )
            )

def draw_cube():
    draw_side(0, 1, 0)
    draw_side(4, 0, 1)
    draw_side(1, 1, 1)
    draw_side(2, 2, 1)
    draw_side(3, 3, 1)
    draw_side(5, 1, 2)
    pg.display.update()

def scramble():
    cube.scramble()
    draw_cube()

def newCube():
    cube.reset()
    draw_cube()

def playground():
    btn_u = Button(10, 600, 50, 50, "U", (128, 128, 128), (0, 128, 128), cube.U)
    btn_up = Button(70, 600, 50, 50, "U'", (128, 128, 128), (0, 128, 128), cube.Up)
    btn_e = Button(130, 600, 50, 50, "E", (128, 128, 128), (0, 128, 128), cube.E)
    btn_ep = Button(190, 600, 50, 50, "E'", (128, 128, 128), (0, 128, 128), cube.Ep)
    btn_d = Button(250, 600, 50, 50, "D", (128, 128, 128), (0, 128, 128), cube.D)
    btn_dp = Button(310, 600, 50, 50, "D'", (128, 128, 128), (0, 128, 128), cube.Dp)
    btn_l = Button(370, 600, 50, 50, "L", (128, 128, 128), (0, 128, 128), cube.L)
    btn_lp = Button(430, 600, 50, 50, "L'", (128, 128, 128), (0, 128, 128), cube.Lp)
    btn_m = Button(490, 600, 50, 50, "M", (128, 128, 128), (0, 128, 128), cube.M)
    btn_mp = Button(10, 700, 50, 50, "M'", (128, 128, 128), (0, 128, 128), cube.Mp)
    btn_r = Button(70, 700, 50, 50, "R", (128, 128, 128), (0, 128, 128), cube.R)
    btn_rp = Button(130, 700, 50, 50, "R'", (128, 128, 128), (0, 128, 128), cube.Rp)
    btn_f = Button(190, 700, 50, 50, "F", (128, 128, 128), (0, 128, 128), cube.F)
    btn_fp = Button(250, 700, 50, 50, "F'", (128, 128, 128), (0, 128, 128), cube.Fp)
    btn_s = Button(310, 700, 50, 50, "S", (128, 128, 128), (0, 128, 128), cube.S)
    btn_sp = Button(370, 700, 50, 50, "S'", (128, 128, 128), (0, 128, 128), cube.Sp)
    btn_b = Button(430, 700, 50, 50, "B", (128, 128, 128), (0, 128, 128), cube.B)
    btn_bp = Button(490, 700, 50, 50, "B'", (128, 128, 128), (0, 128, 128), cube.Bp)
    btn_back = Button(550, 650, 100, 50, "Back", (128, 128, 128), (0, 128, 128), back)

    global buttons
    buttons = [btn_u, btn_up, btn_e, btn_ep, btn_d, btn_dp, btn_l, btn_lp, btn_m, btn_mp, btn_r, btn_rp, btn_f, btn_fp, btn_s, btn_sp, btn_b, btn_bp, btn_back]

    screen.fill(background_color)
    draw_cube()

    pg.display.update()

def back():
    global buttons
    buttons = [btn_scramble, btn_solve, btn_playground, btn_exit]

    screen.fill(background_color)
    draw_cube()

    pg.display.update()

def ext():
    global running
    running = False


# Zmienne
size = width, height = (800, 800)
rect_size = int(width / 15)

background_color = (50, 50, 50)

cube = RubicsCube()

btn_scramble = Button(width / 4 - width / 8, height * .8, width / 2, 50, "Wymieszaj kostkę", (128, 128, 128), (0, 128, 128), scramble)
btn_solve = Button(width / 2 + width / 8, height * .8, width / 2, 50, "Ułóż kostkę", (128, 128, 128), (0, 128, 128), newCube)
btn_playground = Button(width / 4 - width / 8, height * .9, width / 2, 50, "Playground", (128, 128, 128), (0, 128, 128), playground)
btn_exit = Button(width / 2 + width / 8, height * .9, width / 2, 50, "Wyjście", (128, 128, 128), (0, 128, 128), ext)

buttons = [btn_scramble, btn_solve, btn_playground, btn_exit]


# Startowy kod
pg.init()
running = True

screen = pg.display.set_mode(size, pg.RESIZABLE)
pg.display.set_caption("Rubics Cube Lerner")
screen.fill(background_color)

draw_cube()


# Glowna petla
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.VIDEORESIZE:
            if width > height:
                rect_size = int(height / 15)
            else:
                rect_size = int(width / 15)

        for button in buttons:
            button.handle_event(event)

    # Rysowanie przycisków
    for button in buttons:
        if button.rect.collidepoint(pg.mouse.get_pos()):
            button.draw(button.hover_color)
        else:
            button.draw(button.color)

    draw_cube()
    pg.display.flip()


# Zakonczenie
pg.quit()