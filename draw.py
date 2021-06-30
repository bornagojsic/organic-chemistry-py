import turtle
from setup import *
from compound import *


##############################################################


elements_symbols = 'F Cl Br I At Ts S'.split()

elements_colors = '#cae85f #adf542 #e3591e #5f3269 #130117 #a200ff #e8de1c'.split()

substituent_quantity = 'metil etil propil butil pentil heksil heptil oktil nonil dekil undekil dodekil tridekil tetradekil pentadekil heksadekil heptadekil oktodekil nonadekil ikosil'.split()

cyclo_substituents = list(map(lambda s: 'ciklo' + s, substituent_quantity))


##############################################################


def draw_compound(compound):
	if compound.is_cyclic:
		draw_cyclic_compound(compound)
		return

	draw_regular_compound(compound)


def draw_regular_compound(compound):
	## the angle is -30° so that the compound is parallel to the edges of the window
	turtle.lt(30)

	for i, substituents in enumerate(compound.substituents_list):
		## because of the way the compound is supposed to look the turtle
		## needs to turn left on all even atoms and right on all odd atoms,
		## so the direction bool is 0 on all even and 1 on all odd atoms
		direction_bool = i % 2

		if substituents:
			left(direction_bool, 120)
			
			draw_substituents(substituents, compound, direction_bool)
			
			right(direction_bool, 120)

		## because every line contains 2 C atoms the number of lines needs
		## to be one less tha nthe number of atoms in the compound
		if i < compound.number_of_atoms - 1:
			turtle.fd(compound.line_length)
			left(direction_bool, 60)


def draw_cyclic_compound(compound):
	for substituents in compound.substituents_list:
		if substituents:
			turtle.rt(120)
			
			draw_substituents(substituents, compound)
			
			turtle.lt(120)

		turtle.fd(compound.line_length)
		turtle.lt(360 / compound.number_of_atoms)


def draw_substituents(substituents, compound, direction_bool=0):
	if not type(substituents) is list:
		return

	for substituent in substituents:
		if not substituent:
			return
		
		if substituent in 'en in'.split():
			## reverse the turtle if en or in is at an even
			## index of the substituents
			if substituents.index(substituent) % 2:
				turtle.rt(180)
			draw_en_in(substituent, compound, direction_bool)
			if substituents.index(substituent) % 2:
				turtle.rt(180)
			continue

		if compound.is_cyclic:
			turtle.lt(180 / compound.number_of_atoms)

		draw_a_whole_substituent(substituent, compound, direction_bool)

		if compound.is_cyclic:
			turtle.rt(180 / compound.number_of_atoms)
		
		turtle.rt(180)

	if len(substituents) == 1:
		turtle.lt(180)


def draw_en_in(substituent, compound, direction_bool):
	left(direction_bool, 60)
	
	turtle.rt(90)

	turtle.pu()
	turtle.fd(compound.line_length//10)
	turtle.lt(90)
	turtle.bk(compound.line_length//10)
	turtle.pd()

	turtle.bk(compound.line_length-compound.line_length//5)
	turtle.fd(compound.line_length-compound.line_length//5)

	turtle.pu()
	turtle.fd(compound.line_length//10)
	turtle.lt(90)
	turtle.fd(compound.line_length//10)
	turtle.pd()

	turtle.lt(90)

	if substituent == 'in':
		turtle.rt(90)

		turtle.pu()
		turtle.fd(compound.line_length//10)
		turtle.rt(90)
		turtle.bk(compound.line_length//10)
		turtle.pd()

		turtle.bk(compound.line_length-compound.line_length//5)
		turtle.fd(compound.line_length-compound.line_length//5)

		turtle.pu()
		turtle.fd(compound.line_length//10)
		turtle.rt(90)
		turtle.fd(compound.line_length//10)
		turtle.pd()
		
		turtle.rt(90)

	right(direction_bool, 60)


def draw_a_subcompound(substituent, compound):
	subcompound = Compound(replace_last_n_occurences(substituent[1:-1], 'il', '', 1), line_length=compound.line_length)
	postition = turtle.pos()
	direction = turtle.heading()
	
	if subcompound.is_cyclic:
		turtle.fd(subcompound.line_length)
		turtle.rt(45)
	
	draw_compound(subcompound)
	
	jump_to_a_point(*postition)
	turtle.seth(direction)


def draw_a_whole_substituent(substituent, compound, direction_bool):
	if not substituent:
		return

	if substituent.startswith('(') and substituent.endswith(')'):
		draw_a_subcompound(substituent, compound)
		return

	if substituent.endswith('il'):
		draw_a_substituent_base(substituent, compound, direction_bool)
		return
	
	draw_an_element_substituent(substituent, compound, direction_bool)


def draw_a_substituent_base(substituent, compound, direction_bool):
	postition = turtle.pos()
	direction = turtle.heading()

	turtle.fd(compound.line_length)

	if substituent == 'izopropil':
		draw_a_whole_substituent('(1-metiletil)', compound, direction_bool)
		turtle.bk(compound.line_length)
		return

	draw_a_substituent(substituent, compound, direction_bool)
		
	jump_to_a_point(*postition)
	turtle.seth(direction)


def draw_a_substituent(substituent, compound, direction_bool):
	if substituent in cyclo_substituents:
		number_of_atoms = cyclo_substituents.index(substituent) + 1

		turtle.rt(90)

		turtle.circle(compound.line_length // 2, 360, number_of_atoms)

		turtle.lt(90)

		return
	
	number_of_atoms = substituent_quantity.index(substituent)

	for i in range(number_of_atoms):
		left(direction_bool, 60)

		turtle.fd(compound.line_length)

		right(direction_bool, 60)
		
		direction_bool = not direction_bool


def draw_an_element_substituent(substituent, compound, direction_bool):
	turtle.fd(compound.line_length)

	turtle.pu()
	left(direction_bool, 90)
	turtle.fd(compound.line_length//10)
	right(direction_bool, 90)
	if not direction_bool:
		turtle.fd(2 * compound.line_length // 5)
	turtle.pd()

	if substituent in elements_symbols:
		turtle.color(elements_colors[elements_symbols.index(substituent)])
	turtle.write(substituent ,font=("Calibri", 3 * compound.line_length // 10, "bold"))
	turtle.color("#000000")
	
	turtle.pu()
	if not direction_bool:
		turtle.bk(2 * compound.line_length // 5)
	right(direction_bool, 90)
	turtle.fd(compound.line_length//10)
	left(direction_bool, 90)
	turtle.pd()

	turtle.bk(compound.line_length)