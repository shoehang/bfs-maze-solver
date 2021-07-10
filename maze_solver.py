import queue

def atFinish(maze, path, endCheck, moveCheck):
	startX = 0
	startY = 0
	# find beginning pos or start
	for row in maze:
		for pos in row:
			if pos == 'S':
				startX = row.index(pos)
				startY = maze.index(row)
	# finding end pos of path
	for move in path:
		if (move == "U"):
			startY -= 1
		elif (move == "D"):
			startY += 1
		elif (move == "L"):
			startX -= 1
		elif (move == "R"):
			startX += 1
	# check if end pos == maze end
	if (endCheck):
		if (maze[startY][startX] == "E"):
			return True
	# check if move is valid
	if (moveCheck):
		if (0 <= startX < len(maze[0]) and 0 <= startY < len(maze)):
			if (maze[startY][startX] != "#"):
				return True
	return False

def findShortestPath(grid):
	# new queue
	pathQueue = queue.Queue()
	# start at empty path
	pathQueue.put("")
	# placeholder
	currentPath = ""
	# check to see path leads to exit
	while not atFinish(grid, currentPath, True, False):
		# if not, grab from queue and add UDLR moves
		currentPath = pathQueue.get()
		for direction in ["U", "D", "L", "R"]:
			newPath = currentPath + direction
			# check validity of newPath, and add to queue
			if atFinish(grid, newPath, False, True):
				pathQueue.put(newPath)
	return currentPath