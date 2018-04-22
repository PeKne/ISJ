#!/usr/bin/env python3

import math

class Polynomial:
	""" Class representing Polynomial as list of coeeficients"""




	def __init__(self, *args, **kwargs):
		""" Creates list of coeeficients of Polynomial in reverse order"""
		self.numbers = []
		if args:
			for num in args:
				if isinstance(num, list):
					self.numbers = num
					break
				else:
					self.numbers.append(num)
		if kwargs:
			i = 0
			for key, value in sorted(kwargs.items()):
				key = int(key[1:])
				while key != i:
					self.numbers.append(0)
					i = i + 1
				self.numbers.append(value)
				i = i + 1
		for num in self.numbers:
			if (self.numbers[-1] == 0) and (len(self.numbers) != 1):
				self.numbers.pop()
			else:
				break




	def __eq__(self, other):
		""" Returns statement about Polynomial's elements equality """
		return self.numbers == other.numbers




	def derivative(self):
		""" Derivates Polynomial and returns derivated one """
		derivated = []
		idx = 1;
		for num in self.numbers[1:]:
			derivated.append(num * idx)
			idx += 1
		return Polynomial(derivated)



	def at_value(self, *x):
		""" Quantify Polynomial by integer value  and returns integer as result"""
		x = list(x)
		if len(x) == 1:
			idx = 0
			final_numbers = 0
			for num in self.numbers:
				final_numbers += (x[0] ** idx) * num
				idx += 1
			return final_numbers
		elif len(x) == 2:
			if x[0] > x[1]:
				return self.at_value(x[0]) - self.at_value(x[1])
			else:
				return self.at_value(x[1]) - self.at_value(x[0])




	def __pow__(self, exp):
		""" Make power of Polynomial and returns new Polynomial """
		exponent = int(exp)
		final_numbers = []
		for k in range(0, exponent + 1):
			nCr = math.factorial(exponent) // math.factorial(k) // math.factorial(exponent - k)
			final_numbers.append(nCr * ((self.numbers[1]) ** (exponent - k)) * (self.numbers[0] ** k))
		return Polynomial(final_numbers[::-1])




	def __add__(self, other):
		""" Add two Polynomials into one and returns printable format """
		values1 = self.numbers
		values2 = other.numbers
		final_numbers = list()
		if len(values1) > len(values2):
			for i, val2 in enumerate(values2):
				final_numbers.append(values1[i] + val2)
			i += 1
			while i < len(values1):
				final_numbers.append(values1[i])
				i += 1
		else:
			for i, val1 in enumerate(values1):
				final_numbers.append(values2[i] + val1)
			i += 1
			while i < len(values2):
				final_numbers.append(values2[i])
				i += 1
		return str(Polynomial(final_numbers))




	def __str__(self):
		""" Creates printable form of Polynomial and returns it """
		string = ""
		counter = 0
		for num in self.numbers:
			if num == 0:
				counter = counter + 1
				continue
			elif (num == 1 or num == -1) and counter != 0:
				number = ""
			else:
				number = str(abs(num))
			if counter == len(self.numbers) - 1:
				if num < 0:
					oeprator = "- "
				else:
					oeprator = ""
			elif num < 0:
				oeprator = " - "
			else:
				oeprator = " + "
			if counter == 0:
				exponent = ""
			elif counter == 1:
				exponent = "x"
			else:
				exponent = "x^" + str(counter)
			string = oeprator + number + exponent + string
			counter = counter + 1

		if all(i == 0 for i in self.numbers):
			string = "0"
		return string




def test():
	assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
	assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
	assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
	assert str(Polynomial(x2=0)) == "0"
	assert str(Polynomial(x0=0)) == "0"
	assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
	assert Polynomial(x2=0) == Polynomial(x0=0)
	assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
	assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
	pol1 = Polynomial(x2=3, x0=1)
	pol2 = Polynomial(x1=1, x3=0)
	assert str(pol1+pol2) == "3x^2 + x + 1"
	assert str(pol1+pol2) == "3x^2 + x + 1"
	assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
	assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
	pol3 = Polynomial(x0=-1,x1=1)
	assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
	assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
	assert str(Polynomial(x0=2).derivative()) == "0"
	assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
	assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
	pol4 = Polynomial(x3=2,x1=3,x0=2)
	assert str(pol4.derivative()) == "6x^2 + 3"
	assert str(pol4.derivative()) == "6x^2 + 3"
	assert Polynomial(-2,3,4,-5).at_value(0) == -2
	assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
	assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
	pol5 = Polynomial([1,0,-2])
	assert pol5.at_value(-2.4) == -10.52
	assert pol5.at_value(-2.4) == -10.52
	assert pol5.at_value(-1,3.6) == -23.92
	assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
	test()
