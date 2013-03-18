import random
import copy

class World():

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.world = []

	def generate(self):
		self.world = []
		for i in range(self.height):
			self.world.append([random.choice([Cell(0), Cell(1)]) for j in range(self.width)])

	def set(self, world):
		self.world = world

	def show(self):
		for x in range(self.height):
			print ''.join([str(y.status) for y in self.world[x]])

	def evolve(self):
		evolvers = [
			Killer(),
			Killer(),
			Keeper(),
			LifeGiver(),
			Killer(),
			Killer(),
			Killer(),
			Killer(),
			Killer(),
		]

		evolution = copy.deepcopy(self.world)
		
		neighbours = self.get_neighbourhoods()

		for x in range(self.width):
			for y in range(self.height):
				evolver = evolvers[neighbours[y][x]]
				evolver.act(evolution[y][x])
		
		self.world = evolution

	def get_neighbourhoods(self):
		bordered_world = copy.deepcopy(self.world)
		
		#add borders
		bordered_world.insert(0, [Cell(0) for i in range(self.width)])
		bordered_world.append([Cell(0) for i in range(self.width)])

		for i in range(self.height+2):
			bordered_world[i].insert(0, Cell(0))
			bordered_world[i].append(Cell(0))

		neighbours = []

		for y in range(self.height):
			neighbours.append([])
			for x in range(self.width):
				neighbours[y].append(0)

		#count neighbours
		for x in range(self.width):
			for y in range(self.height):
				for i in range(-1, 2):
					for j in range(-1, 2):
						neighbours[y][x] += bordered_world[y+1+i][x+1+j].status
				neighbours[y][x] -= bordered_world[y+1][x+1].status

		return neighbours

class Cell():

	def __init__(self, status):
		self.status = status

	def show(self):
		print self.status

	def die(self):
		self.status = 0

	def live(self):
		self.status = 1

class Killer():
	def act(self, cell):
		cell.die()

class Keeper():
	def act(self, cell):
		pass

class LifeGiver():
	def act(self, cell):
		cell.live()