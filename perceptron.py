import numpy as np

def activationFunction(number): #0.4 error and faster
	if number>0: return 1
	else: return -1

def sigmoid(x):
	return 1 / (1 + np.exp(-x)) #4.9% error

class Perceptron:
	def __init__(self, inputSize):
		self.weights = 2*np.random.random(inputSize) - 1
		self.bias = 2*np.random.random() - 1

	def feedForward(self, inputData):
		sum = np.sum(self.weights*inputData) + self.bias
		output = activationFunction(sum)
		return output

	def train(self, point, answer, guess = ""):
		if guess != "": pass
		else: guess = self.feedForward(point)
		error = answer - guess
		self.weights += error*point*Kp
		self.bias += error*Kp

percep = Perceptron(2)
Kp = 0.1

def findOutput(point, m, b):
	x = point[0]
	yPoint = point[1]
	yLine = m*x + b
	if(yPoint > yLine):
		return 1
	else:
		return -1

M = float(input("M: "))
B = float(input("B: "))
Km = 1000
for i in range(1000):
	point = Km*(2*np.random.random(2) - 1)
	answer = findOutput(point, M, B)
	percep.train(point, answer)


right = 0
wrong = 0
while True:
	point = Km*(2*np.random.random(2) - 1)
	realPoint = [point[0], point[0]*M + B]
	a = findOutput(point, M, B)
	b = percep.feedForward(point)
	if(a == round(b)):
		right+=1
	else:
		percep.train(point, a, b)
		wrong+=1
	print("Right: "+str(right)+" Wrong: "+str(wrong))

