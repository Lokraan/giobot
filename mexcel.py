
from collections import deqeue
import priorityqueue

empty = -1
mountain = -2
fog = -3
obstacle = -4

obstacles = set([mountain, obstacle])

def distance(x1, y1, x2, y2):
	return abs(x1 - x2) + abs(y1 - y2)

def inBounds(grid, node):
	x, y = node
	return( 0 <= x < len(grid) and 0 <= y < len(grid[0]) )

def neighbors(grid, node):
	x, y = node
	neighbors = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
	neighbors = [item for item in neighbors if inBounds(grid, item)]
	return(neighbors)

def cost(grid, armies, tile, pi):
	x, y = tile
	if(grid[x][y] == empty or grid[x][y] == fog):
		return(-1)

	if(grid[x][y] == mountain or grid[x][y] == obstacle):
		return(-99999)

	if(grid[x][y] == pi):
		return(armies[x][y])

	if(0 < grid[x][y] != pi):
		return(-1 * armies[x][y])


def dijkstra(grid, start, goal, pi):
    frontier = priorityqueue.PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in neighbors(grid, current):
            new_cost = cost_so_far[current] + cost(grid, next)
            #print("current:", current, "next:", next, "cost", new_cost)
            if next not in cost_so_far or new_cost > cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from

def reconstructPath(cameFrom, start, goal):
	# deconstruct the path
	currentNode = goal 
	path = [currentNode]
	while currentNode != start:
		#print(currentNode)
		currentNode = cameFrom[currentNode]
		path.append(currentNode)
	path.reverse()

	return(path)


"""

	Returns an array consisting of:
		owned armies
		enemy armies
		strongest army
		strongest enemy army
		mountains/obstacles
		trapped tiles

"""
def findEverything(armies, tiles, pi):
	strongestEnemyArmy, strongestArmy = (-1, -1), (-1, -1)
	ownedArmies, enemyArmies = set(), set()
	lineTiles, edgetiles, connectingTiles, endingTiles, bodyTiles = set(), set(), set(), set(), set()
	trappedTiles = set()
	obstacles = set()
	visited = set()
	emptyTiles = set()

	frontier = deqeue((0, 0))

	while(len(frontier) > 0):
		currentNode = frontier.popleft()
		x, y = currentNode

		if currentNode in obstacles:
			obstacles.append(currentNode)
			continue

		elif tiles[x][y] == empty or tiles[x][y] == fog:
			emptyTiles.add(currentNode)
			continue

		elif 0 < tiles[x][y] != pi:
			enemyArmies.append(currentNode)
			continue	


		n = neighbors(grid, currentNode)

		yVals = []
		xVals = []

		if len(n == 1):
			endingTiles.append((x, y))
			continue


		elif len(n == 4):
			bodyTiles.append((x, y))
			continue

		for a in n:
			xVals.append(a[0])
			yVals.append(a[1])

		if len(n) == 2 and len(yVals) == len(set(yVals)) or len(xVals) == len(set(yVals)):
			lineTiles.add((x, y))

		elif len(n) == 2 and len(yVals) != len(set(yVals)) and len(xVals) != len(set(xVals)):
			edgeTiles.add((x, y))

		elif len(n) == 3 and len(yVals) - 1 == len(set(yVals)) or len(xVals) - 1 == len(set(yVals)):
			connectingTiles.add((x, y))


		for next in neighbors(grid, currentNode):
			trappedCount = 0
			if next not in visited:
				frontier.append(next)

			if(tiles[next[0]][next[1]] in obstacles):
				trappedCount += 1

		if(trappedCount > 2):
			trapped.add(currentNode)






