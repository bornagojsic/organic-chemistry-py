from zoom import *
from compound import *
from math import pi as PI
from draw import draw_compound


##############################################################


def draw(compound):
	global drawn

	drawn = False

	turtle.clear()
	turtle.seth(0)
	center(compound)

	turtle.pensize(compound.line_length / 20)

	draw_compound(compound)

	draw_zoom_btns()

	drawn = True


def center(compound):
	if compound.is_cyclic:
		turtle.rt(90)
		turtle.fd((compound.number_of_atoms + 0.5) * compound.line_length / (2 * PI))
		turtle.lt(90)
		return

	turtle.lt(180)
	turtle.fd(3 * compound.number_of_atoms * compound.line_length / 8)
	turtle.rt(180)


def on_btn_click(compound, x, y):
	global drawn

	if not drawn:
		return

	plus_btn_clicked = plus_btn_x < x < plus_btn_x + BTN_WIDTH and plus_btn_y - BTN_WIDTH < y < plus_btn_y
	minus_btn_clicked = minus_btn_x < x < minus_btn_x + BTN_WIDTH and minus_btn_y - BTN_WIDTH < y < minus_btn_y
	line_length_too_long = compound.line_length >= MAX_LINE_LENGTH
	line_length_too_short = compound.line_length <= MIN_LINE_LENGTH

	if plus_btn_clicked and not line_length_too_long:
		compound.line_length += 10
		draw(compound)
		return

	if minus_btn_clicked and not line_length_too_short:
		compound.line_length -= 10
		draw(compound)


def main():
	compound_name = turtle.textinput('Organic compound', 'Enter the name of an organic compound:')

	compound = Compound(compound_name)

	draw(compound)

	## 1 -> left click
	turtle.onscreenclick(lambda x,y: on_btn_click(compound, x, y), 1)

	turtle.ht()

	turtle.mainloop()


##############################################################


if __name__ == '__main__':
	main()