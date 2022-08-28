class Axis():
	'''
		defines an axis array between [begin, end] by step
		
		e.g.
		x = Axis(1, 0.1, 1.2)
		print(x.getAxis()) 
			out: [1, 1.1, 1,2]

		y = Axis(4, -1, 0)
		print(x.getAxis())
			out: [4, 3, 2, 1, 0]

		y = Axis(10, 3, 10)
		print(x.getAxis())
			out: [10]

		y = Axis(1, -1, 10)
		print(x.getAxis())
			out: []
	'''
	def __init__(self, begin, step, end):
		self.begin = begin
		self.step = step
		self.end = end
		self.axis = []

		# range function doesn't work for float numbers
		x = begin
		if step > 0 and begin < end:
			while(x < end):
				self.axis.append(x)
				x += step
		elif step < 0 and begin > end:
			while(x > end):
				self.axis.append(x)
				x += step
		elif begin == end:
			self.axis.append(begin)
		else:
			self.axis = []

	def __str__(self) -> str:
		return '{} to {} by step {}'.format(self.begin, self.end, self.step)

	def getAxis(self) -> list:
		return self.axis

class Polynomial():
	'''
		Defines a polynomial expression based on coefficients passed
		
		e.g.
		f = Polynomial([3,2,1], 'x')
		means: f(x) = 3x^2 + 2x + 1

		f = Polynomial([3,0,1], 't')
		means: f(t) = 3t^2 + 1
	'''
	def __init__(self, coefficients:list, var:chr):
		self.coefficients = coefficients
		self.degree = len(coefficients)-1
		self.var = var

	def __str__(self):
		# The final expression starts empty
		out = ''
		# Highest degree at beginning
		degree = self.degree
		for coefficient in self.coefficients:
			if coefficient != 0 and degree != 0:
				# To represent a*x^b
				out += '{}*{}^{} + '.format(coefficient, self.var, degree)
			elif coefficient != 0 and degree == 0:
				# To represent independent term c
				out += '{}'.format(coefficient)
			degree -= 1
		return out
	
	def getCoeff(self):
		return self.coefficients

class Tf():
	'''
		Defines a transfer function based in two arrays and a varible name char
		's' is defined by the default value for var
	'''
	def __init__(self, numerator_coeff:list, denominator_coeff:list, var='s'):
		self.numerator = Polynomial(numerator_coeff, var)
		self.denominator = Polynomial(denominator_coeff, var)
		self.var = var
	
	def __str__(self):
		out = '( {} ) / '.format(self.numerator)
		out += '( {} )'.format(self.denominator)
		return out