import sys
import pygame
from maze_solver import *

#elementary box clss w draw method
class box():
	def __init__(self, x, y, width, height, text, color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text
		self.color = color

	def getPos(self):
		return (self.x, self.y)

	def getText(self):
		return self.text

	def setText(self, newText):
		self.text = newText

	def draw(self, canvas):
		pygame.draw.rect(canvas, self.color, (self.x, self.y, self.width, self.height))
		if not(self.text == " " or self.text == "#" or self.text == "S" or self.text == "E"):
			font = pygame.font.SysFont('comicsans', 25)
			text = font.render(str(self.text), 1, (0,0,0))
			canvas.blit(text, (self.x + int(self.width/2 - text.get_width()/2), self.y + int(self.height/2 - text.get_height()/2)))
		
	def hover(self, pos):
		if (pos[0] > self.x and pos[0] < self.x + self.width):
			if (pos[1] > self.y and pos[1] < self.y + self.height):
				return True
		return False

# create 7x7 grid of box class drawable objects
def setup():
	#grid = [[] for _ in range(22)]
	grid = [[] for _ in range(7)]
	for row in range(len(grid)):
		for col in range(len(grid)):
			gridBox = box(2 + (col * 20), 2 + (row * 20), 19, 19, " ", (255, 255, 255))
			grid[row].append(gridBox)
	return grid

def redraw(grid, canvas):
	for row in grid:
		for col in row:
			col.draw(canvas)

# grid to python nested lists
def getMazeArray(grid):
	mazeArray = []
	for i in grid:
		row = []
		for j in i:
			row.append(j.getText())
		mazeArray.append(row)
	return mazeArray


def paintPath(grid, startX, startY, path):
	currentCol = startX
	currentRow = startY
	pathArray = list(path)
	# -1 since last move is the end
	for direction in range(len(path)-1):
		if (pathArray[direction] == "U"):
			currentRow -= 1
		if (pathArray[direction] == "D"):
			currentRow += 1
		if (pathArray[direction] == "L"):
			currentCol -= 1
		if (pathArray[direction] == "R"):
			currentCol += 1
		grid[currentRow][currentCol].color = (0, 0, 255)
		

if __name__ == '__main__':
	pygame.init()

	# color, size parameters
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	WIDTH = 143
	HEIGHT = 197

	# flags if start and end exists. begins false, since empty grid
	START = None
	END = None

	# coordinates of START pos
	STARTROW = None
	STARTCOL = None

	CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('Maze')
	CANVAS.fill(BLACK)

	GRID = setup()
	SOLVEBUTTON = box(2, 143, 139, 25, 'Find', WHITE)
	RESETBUTTON = box(2, 170, 139, 25, 'Reset', WHITE)

	while True:
		redraw(GRID, CANVAS)
		SOLVEBUTTON.draw(CANVAS)
		RESETBUTTON.draw(CANVAS)

		# pos of mouse on pygame window
		pos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()
			# mousclick on:
			if (event.type == pygame.MOUSEBUTTONDOWN):
				# find
				if (SOLVEBUTTON.hover(pos)):
					if (START and END):
						print("finding")
						paintPath(GRID, STARTCOL, STARTROW, findShortestPath(getMazeArray(GRID)))
					else:
						print("missing start or end")
				# reset
				if (RESETBUTTON.hover(pos)):
					GRID = setup()
					print("resetting")
				# mazeblocks
				for row in GRID:
					for col in row:
						if (col.hover(pos)):
							if (col.getText() == " "):
								col.setText("#")
								col.color = BLACK
							else:
								col.setText(" ")
								col.color = WHITE
			# key presses
			if (event.type == pygame.KEYDOWN):
				if (event.key == pygame.K_s):
					for row in range(len(GRID)):
						for col in range(len(GRID[row])):
							if (GRID[row][col].hover(pos)):
								if (START == None):
									# flag current start block
									START = GRID[row][col]
									START.color = GREEN
									START.setText("S")
									STARTROW = row
									STARTCOL = col
								else:
									# unflag previous start block to default
									START.color = WHITE
									START.setText(" ")
									# flag new start block
									START = GRID[row][col]
									START.color = GREEN
									START.setText("S")
									STARTROW = row
									STARTCOL = col
				if (event.key == pygame.K_e):
					for row in range(len(GRID)):
						for col in range(len(GRID[row])):
							if (GRID[row][col].hover(pos)):
								if (END == None):
									# flag current end block
									END = GRID[row][col]
									END.color = RED
									END.setText("E")
								else:
									# unflag previous end block to default
									END.color = WHITE
									END.setText(" ")
									# flag new end block
									END = GRID[row][col]
									END.color = RED
									END.setText("E")
		pygame.display.update()