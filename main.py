from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Rectangle

from game import World

class GameOfLife(Widget):
	
	def create_world(self):
		self.world = World(80, 60)
		self.world.generate()
		self.paint()

	def update(self, dt):
		self.world.evolve()
		self.paint()

	def paint(self):
		self.canvas.clear()
		with self.canvas:
			for x in range(self.world.width):
				for y in range(self.world.height):
					if self.world.world[y][x].status == 1:
						Rectangle(pos=(x*10, y*10), size=(10, 10))

class GameOfLifeApp(App):
    def build(self):
    	game = GameOfLife()
    	game.create_world()
    	Clock.schedule_interval(game.update, 0.15)
        return game

if __name__ == '__main__':
    GameOfLifeApp().run()