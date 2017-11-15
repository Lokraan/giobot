
import pathing
import generals
import time

# tile types
empty = -1
mountain = -2
fog = -3
obstacle = -4

# game settings
userId = "16141231"
name = "careNo"
gameType = 'private'
lobby = 'ihatebugs'

game = generals.Generals(userId, name, gameType, lobby)

updateTimes = []
longestUpdate = 0

for update in game.get_updates():

	complete = update['complete']

	if(complete):
		print("replay:", update['replay_url'])
		sum = 0
		for n in times:
			sum += n

		print("Avg Time:", round(sum/len(times), 6))
		continue

	pi = update['player_index']
	general = update['generals'][pi]
	terrain = update['tile_grid']
	armies = update['army_grid']
	cities = update['cities']
	turn = update['turn']

	landCount = update['lands'][pi]

	#print("landCount:", landCount)


	if(turn > 26):
		start = time.time()
		if(landCount < 35 or isEnemies(terrain, pi) == False):
			#print(isEnemies(terrain, pi))
			spread(armies, terrain, pi, general)

		else:
			attack(armies, terrain, general, pi)



		updateTime = round(time.time() - start, 6)
		print("updateTime:", updateTime)
		if(updateTime < longestUpdate):
			longestUpdate = updateTime
		updateTimes.append(updateTime)

