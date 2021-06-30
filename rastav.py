import re


def prevedi(spoj):
	ciklo = False

	elementi = 'fluor klor brom jod astat tenesin sumpor ol'.split()

	elementi_kratice = 'F Cl Br I At Ts S OH'.split()

	nastavci_za_broj_s_n = 'metan etan propan butan pentan heksan heptan oktan nonan dekan undekan dodekan tridekan tetradekan pentadekan heksadekan heptadekan oktodekan nonadekan ikosan'.split()
	nastavci_za_broj_bez_a = list(map(lambda nastavak: nastavak[:-2], nastavci_za_broj_s_n))

	nastavci_za_kolicinu = 'di tri tetra'.split() + list(map(lambda nastavak: nastavak[:-1], nastavci_za_broj_s_n))[4:]

	print(spoj, type(spoj))

	if spoj.count('-') == 0:
		for i, nastavak in enumerate(nastavci_za_kolicinu):
			if spoj.startswith(nastavak):
				spoj = f'{"1," * (i + 1)}1-' + spoj
				break
		else:
			spoj = '1-' + spoj

	string = f'-{spoj.replace(" ", "")}-'

	dijelovi = []

	maks = 0
	for i in range(len(string)):
		if string[i] == '(' and i > maks:
			n = 1
			for j in range(i + 1, len(string)):
				n += 1 if string[j] == '(' else -1 if string[j] == ')' else 0

				# if string[j] == '(':
				# 	n += 1

				# if string[j] == ')':
				# 	n -= 1

				if n == 0:
					maks = j
					dijelovi.append('-' + string[i:j+1])
					break


	print(f"{dijelovi=}, {string=}")

	# string2 = string

	# for i in range(1, len(string)):
	# 	if string[i].isdigit() and string[i-1] == '-':
	# 		j = i
	# 		while string[j].isdigit() or string[j] == ',':
	# 			j += 1
	# 		string2 = string2[:i] + string2[j+1:]

	# print(string2) 
	# -\(.+\)-?

	#dijelovi = re.findall('-\(.*?\)', string)
	brojevi = []
	for dio in dijelovi:
		for i in range(string.index(dio)-2,-1,-1):
			if string[i] == '-':
				brojevi.append(string[i:string.index(dio)+1])
				string = string[:i] + string[string.index(dio)+len(dio):] ## + ('-' if string[:i][:-1] != '-' else '')
				print(dio, string)
				break

	dijelovi = list(map(lambda s: s + '-' if s[-1] != '-' else s, dijelovi))

	string = '-' + string if string[0] != '-' else string

	print(f"{dijelovi=}, {brojevi=}, {string=}")

	dijelovi += re.findall('-[A-z]+-', string)
	brojevi += re.findall('-[0-9\,]+-', string)

	dijelovi = [ dio[1:-1] for dio in dijelovi ]
	brojevi = [ broj[1:-1].split(',') for broj in brojevi ]

	print(f"{dijelovi=}, {brojevi=}, {string=}")

	## supstituenti moraju biti prije nastavka en

	n = 0

	for i in range(1, len(dijelovi)+1):
		if dijelovi[-i][::-1][:2][::-1] in 'en in ol'.split():
			continue
		
		for index, nastavak in enumerate('an a'.split()):
			
			if dijelovi[-i].endswith(nastavak):
				dijelovi[-i] = dijelovi[-i][:-(2-index)]

		for j in range(len(nastavci_za_broj_bez_a)-1,-1,-1): ## DODAJ ENUMERATE

			if dijelovi[-i].endswith(nastavci_za_broj_bez_a[j]):
				n = j + 1
				dijelovi[-i] = dijelovi[-i][:-len(nastavci_za_broj_bez_a[j])]
				break

		if dijelovi[-i].endswith('ciklo'):
			dijelovi[-i] = dijelovi[-i][:-(len('ciklo'))]
			ciklo = True
		break

	#dijelovi = [dio.replace(nastavak, '') if dio.startswith(nastavak) else dio for nastavak in nastavci_za_kolicinu for dio in dijelovi]

	print(f"{dijelovi=}, {brojevi=}, {ciklo=}")

	for i, dio in enumerate(dijelovi):
		
		for nastavak in nastavci_za_kolicinu[::-1]:
		
			if dio.startswith(nastavak):
				dijelovi[i] = dio.replace(nastavak, '')

		if dijelovi[i] in elementi:
			dijelovi[i] = elementi_kratice[elementi.index(dijelovi[i])]

	dijelovi = [dio for dio in dijelovi if dio]

	print(f"{dijelovi=}, {brojevi=}, {n=}, {string=}")

	# print(n)

	molekula = dict(zip(dijelovi, brojevi))

	# print(molekula)

	supstituenti = [''] * n

	for dio in molekula:

		print(dio, molekula[dio])

		for broj in molekula[dio]:

			ostatak = 1 if dio in 'en in'.split() else 1

			if supstituenti[int(broj)-ostatak] != '':
				supstituenti[int(broj)-ostatak] = [supstituenti[int(broj)-ostatak], dio]
				continue

			supstituenti[int(broj)-ostatak] = dio

	for supstituent in supstituenti:
		
		print(type(supstituent), supstituent)
		
		if type(supstituent) is list and any(supstituent[0].startswith(nastavak) for nastavak in 'en in'.split()):
		
			supstituenti[supstituenti.index(supstituent)] = supstituent[::-1]

	supstituenti = [[s] if not type(s) is list else s for s in supstituenti]

	return n, supstituenti, ciklo