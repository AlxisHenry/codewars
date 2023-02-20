def do_poly_calc(elements, x):

	for el in elements:
		if len(el) == 0:
			elements.remove(el)

	print(elements)
	return eval(((" + ".join(elements)).replace('+ -', '- ')).replace('^', '**'))

def find_nth(string, substring, n): 
	if (n == 1): 
		return string.find(substring) 
	else: 
		return string.find(substring, find_nth(string, substring, n - 1) + 1)

def format_calc_string(list):

	#print('Liste de base: ', list)

	for i in list:
		if i.startswith('-') and len(i) > 1:
			if not list.index(i) == 0:
				list.insert(list.index(i),'-')
				list[list.index(i)] = list[list.index(i)].replace('-', '')

	#print('Liste modifiée: ', list)
	
	calc_str = ''

	for calc in list:
		if len(calc_str) == 0:
			calc_str += calc
		else:
			calc_str += ' + ' + calc

	calc_str = calc_str.replace(' + - + ', ' - ')

	#print('String du calcul', calc_str)

	return calc_str

def generate_calc_string(list, x: int):

	string_parts = []

	def check(el: int, index: int):
		#print('Liste : ', len(list))
		if el == 0:
			return ''
		elif el == 1:
			if index == 0:
				return str(el)
			elif index == 1:
				return '-x'
			elif index != 0:
				return 'x^' + str(index)
		elif el == -1:
			if index == 0:
				return str(el)
			elif index == 1:
				return '-x'
			elif index != 0:
				return '-x^' + str(index)
		else:
			if index == 1:
				return str(el) + '*x'
			elif index == 0:
				return str(el)
			else:
				return str(el) + '*x^' + str(index)

	for index, el in enumerate(list):
		string_parts.append("{}".format(check(el, index)))

	reverse_string_parts = string_parts[::-1]
	poly_result = do_poly_calc(reverse_string_parts, x)
	end_string = " with x = {} the value is {}".format(x, str(poly_result))
	return "For " + format_calc_string(reverse_string_parts) + end_string

def calc_poly(pol_list, x: int): 
	reverse_pol_list = pol_list[::-1]
	calc_string = generate_calc_string(reverse_pol_list, x)	
	#return 'String terminé : ' + calc_string
	return calc_string

def calculs():
	print(calc_poly([-1, -6, 28, 79], 35))
	print("-----------------------------------")
	print(calc_poly([6, 3, 5, -4], 4))
	print("-----------------------------------")
	print(calc_poly([2, 0, 5, -6, 4, 0], 2))
	print("-----------------------------------")
	print(calc_poly([-8, 32, -20], -22))
	print("-----------------------------------")
	print(calc_poly([-7, 38, 1], 21))
	print("-----------------------------------")
	print(calc_poly([6, -20, -26, 6], 76))
	print("-----------------------------------")
	print(calc_poly([-7, -16, 29, -14, -7, -38], 28))
	print("-----------------------------------")

calculs()