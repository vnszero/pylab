def tf():
	pass

def plot():
	pass

class Axis():
	def __init__(begin, step, end):
		self.begin = begin
		self.step = step
		self.end = end
		self.axis = [begin:step:end]

	def __str__() -> str:
		return f'{} to {} by {}'.format(self.begin, self.end, self.step)

class polynomial():
	def __init__(coefficients:List, var:chr):
		self.coefficients = coefficients
		self.degree = len(coefficients)-1
		self.var = var

	def __str__():
		#warning: troubles to represent poly with 0 as coeff
		out = ''
		degree = self.degree
		for coefficient in self.coefficients:
			out += f'{}*{}^{} '.format(coefficient,var,degree)
			degree -= 1
		return out

class Freqs():
	def __init__(numerator, denominator, time:Axis)
