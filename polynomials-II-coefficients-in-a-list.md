# **Instructions**

You will be given a list with the coefficients of a polynomial. Look the following order in both:

>P(x) =       6x³ + 3x² + 5x -4 <br>
coefficients =  [ 6,   3,    5, -4]

Your task is to express the polynomial like a string with its value for a certain determinate ``x``:

> [6, 3, 5, -4], 4 returns "For 6*x^3 + 3*x^2 + 5*x - 4 with x = 4 the value is 448"

If we have some coefficients equals to ``0``, its corresponding term will not be seen.

> [2, 0, 5, -6, 4, 0], 2 returns "For 2*x^5 + 5*x^3 - 6*x^2 + 4*x with x = 2 the value is 88"

An interesting case will be when the first coefficient is equal to ``-1``

> [-1, -6, 28, 79], 35 returns "For -x^3 - 6*x^2 + 28*x + 79 with x = 35 the value is -49166"

The following answer will be considered incorrect:

> "For -1x^3 - 6*x^2 + 28*x + 79 with x = 35 the value is -49166"

You will not receive an empty list and the values for the variable ``x`` will be valid for all the cases.

# **Sample Tests**

```py
from solution import calc_poly


def dotest(L, x, expected):
    actual = calc_poly(L[:], x)
    test.assert_equals(actual, expected, f"Test failed with pol_list = {L}, x = {x}")


@test.describe("Tests")
def test_group():
    @test.it("Example tests")
    def test_case():
        for (p, x, expected) in [
            ([6, 3, 5, -4], 4, "For 6*x^3 + 3*x^2 + 5*x - 4 with x = 4 the value is 448"),
            ([2, 0, 5, -6, 4, 0], 2, "For 2*x^5 + 5*x^3 - 6*x^2 + 4*x with x = 2 the value is 88"),
        ]:
            dotest(p, x, expected)
```

# **Solution**

```py
def do_poly_calc(elements, x):

	for el in elements:
		if len(el) == 0:
			elements.remove(el)

	return eval(((" + ".join(elements)).replace('+ -', '- ')).replace('^', '**'))

def find_nth(string, substring, n): 
	if (n == 1): 
		return string.find(substring) 
	else: 
		return string.find(substring, find_nth(string, substring, n - 1) + 1)

def format_calc_string(list):

	for i in list:
		if i.startswith('-') and len(i) > 1:
			if not list.index(i) == 0:
				list.insert(list.index(i),'-')
				list[list.index(i)] = list[list.index(i)].replace('-', '')
	
	calc_str = ''

	for calc in list:
		if len(calc_str) == 0:
			calc_str += calc
		else:
			calc_str += ' + ' + calc

	calc_str = calc_str.replace(' + - + ', ' - ')

	return calc_str

def generate_calc_string(list, x: int):

	string_parts = []

	def check(el: int, index: int):
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
	return calc_string
```
