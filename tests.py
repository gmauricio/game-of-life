import unittest 
from game import World, Cell

class WorldTest(unittest.TestCase):
	def test_counting_0_corner_cell_neighbours(self):
		world = World(2, 2)
		world.set([
			[Cell(0), Cell(0)],
			[Cell(0), Cell(0)]
		])
		self.assertEqual(0, world.get_neighbourhoods()[0][0])


	def test_counting_3_corner_cell_neighbours(self):
		world = World(2, 2)
		world.set([
			[Cell(0), Cell(1)],
			[Cell(1), Cell(1)]
		])
		self.assertEqual(3, world.get_neighbourhoods()[0][0])

	def test_counting_4_center_cell_4_neighbours(self):
		world = World(3, 2)
		world.set([
			[Cell(1), Cell(1), Cell(1)],
			[Cell(1), Cell(1), Cell(0)]
		])
		self.assertEqual(4, world.get_neighbourhoods()[0][1])


	def test_that_cell_dies_with_0_alive_neighbours(self):
		world = World(2, 2)
		world.set([
			[Cell(1), Cell(0)],
			[Cell(0), Cell(0)]
		])
		world.evolve()
		self.assertEqual(0, world.world[0][0].status)

	def test_that_cell_dies_with_1_alive_neighbours(self):
		world = World(2, 2)
		world.set([
			[Cell(1), Cell(1)],
			[Cell(0), Cell(0)]
		])
		world.evolve()
		self.assertEqual(0, world.world[0][0].status)

	def test_that_cell_lives_with_2_alive_neighbours(self):
		world = World(2, 2)
		world.set([
			[Cell(1), Cell(1)],
			[Cell(1), Cell(0)]
		])
		world.evolve()
		self.assertEqual(1, world.world[0][0].status)

	def test_that_cell_keeps_death_with_2_alive_neighbours(self):
		world = World(2, 2)
		world.set([
			[Cell(0), Cell(1)],
			[Cell(1), Cell(0)]
		])
		world.evolve()
		self.assertEqual(0, world.world[0][0].status)

	def test_that_cell_lives_with_3_alive_neighbours(self):
		world = World(2, 2)
		world.set([
			[Cell(1), Cell(1)],
			[Cell(1), Cell(1)]
		])
		world.evolve()
		self.assertEqual(1, world.world[0][0].status)

	def test_that_death_cell_lives_with_3_alive_neighbours(self):
		world = World(2, 2)
		world.set([
			[Cell(0), Cell(1)],
			[Cell(1), Cell(1)]
		])
		world.evolve()
		self.assertEqual(1, world.world[0][0].status)

	def test_that_cell_dies_with_4_alive_neighbours(self):
		world = World(3, 2)
		world.set([
			[Cell(1), Cell(1), Cell(1)],
			[Cell(1), Cell(1), Cell(0)]
		])
		world.evolve()
		self.assertEqual(0, world.world[0][1].status)

	def test_that_cell_keeps_death_4_alive_neighbours(self):
		world = World(3, 2)
		world.set([
			[Cell(1), Cell(0), Cell(1)],
			[Cell(1), Cell(1), Cell(0)]
		])
		world.evolve()
		self.assertEqual(0, world.world[0][1].status)


class WorldMakeTest(unittest.TestCase):

	def test_that_worlds_get_created_with_expected_size(self):
		world = World(10, 10)
		world.generate()
		self.assertEqual(10, len(world.world))
		self.assertEqual(10, len(world.world[0]))

