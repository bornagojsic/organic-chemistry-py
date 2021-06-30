import turtle
from setup import *


##############################################################


PERCENTAGE_OF_THE_SCREEN = 85 / 100
BTN_WIDTH = 40
plus_btn_x, plus_btn_y = PERCENTAGE_OF_THE_SCREEN * WIDTH / 2, PERCENTAGE_OF_THE_SCREEN * HEIGHT / 2
minus_btn_x, minus_btn_y = plus_btn_x + 3 * BTN_WIDTH / 2, plus_btn_y

MAX_LINE_LENGTH = 150
MIN_LINE_LENGTH = 20


##############################################################


def draw_zoom_btns():
	draw_a_zoom_btn('plus', plus_btn_x, plus_btn_y, BTN_WIDTH)
	draw_a_zoom_btn('minus', minus_btn_x, minus_btn_y, BTN_WIDTH)


def draw_a_zoom_btn(sign, x, y, width):
	if not sign in 'plus minus'.split() or not x or not y or not width:
		return

	jump_to_a_point(x, y)

	for i in range(4):
		turtle.fd(width)
		turtle.rt(90)

	draw_a_sign(sign, width)

	jump_to_a_point(0, 0)


def draw_a_sign(sign, width):
	if sign == 'plus':
		turtle.pu()
		turtle.fd(width/2)
		turtle.rt(90)
		turtle.fd(width/4)
		turtle.pd()
		turtle.fd(width/2)
		turtle.bk(width/4)
		turtle.rt(90)
		turtle.bk(width/4)
		turtle.fd(width/2)
		return

	turtle.pu()
	turtle.rt(90)
	turtle.fd(width/2)
	turtle.lt(90)
	turtle.fd(width/4)
	turtle.pd()
	turtle.fd(width/2)