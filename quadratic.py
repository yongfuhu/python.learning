a = int(input('请输入ax**2+bx+c=0中的a的值：'))
b = int(input('请输入ax**2+bx+c=0中的b的值：'))
c = int(input('请输入ax**2+bx+c=0中的c的值：'))
import math
def quadratic(a, b, c):
	for x in (a, b, c):
		if not isinstance(x, (int, float)):
			raise TypeError('bad operand type')
	n = b**2 - 4*a*c
	if a == 0:
		x = - b/c
		return x
	if n >= 0:
		x1 = (math.sqrt(b**2 - 4*a*c) - b) / (2*a)
		x2 = -(math.sqrt(b**2 - 4*a*c) + b) / (2*a)
		return x1, x2
	else:
		print ('无解')
print ('结果为：'+str(quadratic(a, b, c)))		