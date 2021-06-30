import turtle
from win32api import GetSystemMetrics as get_system_metrics


##############################################################


WIDTH, HEIGHT = get_system_metrics(0), get_system_metrics(1)

window = turtle.Screen()
window.screensize(WIDTH, HEIGHT)
window.setup(width=1.0, height=1.0, startx=None, starty=None)


turtle.color("#000000")
turtle.speed(0)


##############################################################


def jump_to_a_point(x, y):
	turtle.seth(0)
	turtle.pu()

	try:
		turtle.goto(int(x), int(y))
	finally:
		turtle.pd()


def left(left_bool, angle):
	if left_bool:
		turtle.lt(angle)
		return

	turtle.rt(angle)


def right(right_bool, angle):
	left(not right_bool, angle)


def replace_last_n_occurences(s, old, new, number_of_occurences):
	rsplit_string = s.rsplit(old, number_of_occurences)
	return new.join(rsplit_string)