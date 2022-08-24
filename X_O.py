def draw_grid(data):
	for row in data:
		print(f" {row[0]} | {row[1]} | {row[2]}")
		print("-----------")

def take_coordinates():
	global data
	while True:
		c = input("where do you want to put your mark?\n")
		if len(c.split(",")) != 2:
			print("Wrong input !!")
			continue
		row,column = int(c.split(",")[0]) , int(c.split(",")[1]) 
		if data[row-1][column-1] != " ":
			print("This cell is taken !!")
			continue
		if row not in [1,2,3] or column not in [1,2,3]:
			print("Out of grid !!")
			continue
		return row-1,column-1

def update_grid(row,column,turn):
	global data
	global players_mark
	key = f"player{turn}"
	data[row][column] = players_mark[key]

def check_winner():
	global data
	for row in data:
		if all([item=="X" for item in row]):
			return "X"
		if all([item=="O" for item in row]):
			return "O"
	for i in range(3):
		if data[i][0] == "X" and data[i][1] == "X" and data[i][2] == "X":
			return "X"
		if data[i][0] == "O" and data[i][1] == "O" and data[i][2] == "O":
			return "O"
	if data[0][0] == "X" and data[1][1] == "X" and data[2][2] == "X":
		return "X"
	if data[0][0] == "O" and data[1][1] == "O" and data[2][2] == "O":
		return "O"
	return None

def play_again():
	while True:
		play_again = input("Do you want to play again? [yes/no]\n")
		if play_again == "yes":
			return True
		elif play_again == "no":
			return False
		else: 
			print("Wrong input")
			continue

def check_tie():
	global data
	for row in data:
		for item in row:
			if item == " ": return False
	return True

data = [
	[" "," "," "],
	[" "," "," "],
	[" "," "," "]
]

players_mark = {
	"player1" : "",
	"player2" : ""
}

while True:
	mark = input("Player 1, Choose mark [X / O]\n")
	if mark == "X" or mark == "x":
		players_mark["player1"] = "X"
		players_mark["player2"] = "O"
	elif mark == "O" or mark == "o":
		players_mark["player1"] = "O"
		players_mark["player2"] = "X"
	else:
		print("Invalid input !!")
		continue
	print("player 1 mark: {}".format(players_mark["player1"]))
	print("player 2 mark: {}".format(players_mark["player2"]))
	turn = 1
	while True:
		draw_grid(data)
		print(f"player {turn} turn")
		row,column=take_coordinates()
		update_grid(row,column,turn)
		winner = check_winner()
		if winner is not None:
			won_player = [k for k,v in players_mark.items() if v.upper()==winner.upper()][0]
			print(f"{won_player} WON !!")
			break
		tie = check_tie()
		if tie:
			print("No One Wins, It's a TIE")
			break
		if turn == 1: turn = 2
		elif turn == 2: turn = 1 

	again = play_again()
	if again: continue
	else: print("Bye Bye !!"); break