# بسم الله الرحمن الرحيم
import os
from random import randint

db = {'name1': 1, 'name2': 2, 'name3': 3, 'name4': 4, 'name5': 5, 'name6': 6, 'name7': 7, 'name8': 8, 'name9': 9}


def print_board(name1, name2, name3, name4, name5, name6, name7, name8, name9):
	os.system('clear')
	print('  {name1} *  {name2}  * {name3} '.format(name1=name1, name2=name2, name3=name3))
	print('*** * *** * ***')
	print('  {name4} *  {name5}  * {name6} '.format(name4=name4, name5=name5, name6=name6))
	print('*** * *** * ***')
	print('  {name7} *  {name8}  * {name9} '.format(name7=name7, name8=name8, name9=name9))


def random_player():
	rand_player1 = 'x' if randint(1, 2) == 1 else 'o'
	player2 = 'o' if rand_player1 == 'x' else 'x'
	return rand_player1, player2


def move(s):
	while True:
		n = int(input("%s-Move:" % s.capitalize()))
		if place_check(n):
			if n == 1:
				db['name1'] = '%s' % s
				return
			if n == 2:
				db['name2'] = '%s' % s
				return
			if n == 3:
				db['name3'] = '%s' % s
				return
			if n == 4:
				db['name4'] = '%s' % s
				return
			if n == 5:
				db['name5'] = '%s' % s
				return
			if n == 6:
				db['name6'] = '%s' % s
				return
			if n == 7:
				db['name7'] = '%s' % s
				return
			if n == 8:
				db['name8'] = '%s' % s
				return
			if n == 9:
				db['name9'] = '%s' % s
				return


def win(db):
	if db['name1'] == db['name2'] == db['name3']:
		m = 'Congratulation X, You Won' if db['name1'] == 'x' else 'Congratulation O, You Won'
		return m
	if db['name4'] == db['name5'] == db['name6']:
		m = 'Congratulation X, You Won' if db['name4'] == 'x' else 'Congratulation O, You Won'
		return m
	if db['name7'] == db['name8'] == db['name9']:
		m = 'Congratulation X, You Won' if db['name7'] == 'x' else 'Congratulation O, You Won'
		return m
	if db['name1'] == db['name4'] == db['name7']:
		m = 'Congratulation X, You Won' if db['name4'] == 'x' else 'Congratulation O, You Won'
		return m
	if db['name2'] == db['name5'] == db['name8']:
		m = 'Congratulation X, You Won' if db['name5'] == 'x' else 'Congratulation O, You Won'
		return m
	if db['name3'] == db['name6'] == db['name9']:
		m = 'Congratulation X, You Won' if db['name3'] == 'x' else 'Congratulation O, You Won'
		return m
	if db['name1'] == db['name5'] == db['name9']:
		m = 'Congratulation X, You Won' if db['name5'] == 'x' else 'Congratulation O, You Won'
		return m
	if db['name3'] == db['name5'] == db['name7']:
		m = 'Congratulation X, You Won' if db['name7'] == 'x' else 'Congratulation O, You Won'
		return m


def place_check(n):
	if n in db.values():
		return True
	print("You can't make this move, try another one.")
	return False


def replayf():
	global moves
	moves = 0
	while True:
		global replay
		replay = input('Do you want to play again (y/n) ? :')
		if replay == 'y' or replay == 'n' or replay == 'Y' or replay == 'N':
			break

	replay = True if replay == 'y' or replay == 'Y' else False
	global db
	db = {'name1': 1, 'name2': 2, 'name3': 3, 'name4': 4, 'name5': 5, 'name6': 6, 'name7': 7, 'name8': 8, 'name9': 9}
	return replay


def full_board_check():
	global moves
	if moves >= 9:
		return True
	return False


replay = True
moves = 0


def play():
	while replay:
		global moves
		p1, p2 = random_player()
		while True:
			print_board(**db)
			move(p1)
			moves += 1
			if win(db) is not None:
				print(win(db))
				replayf()
			if full_board_check() is not False:
				print('Game over')
				replayf()
			print_board(**db)
			move(p2)
			moves += 1
			if win(db) is not None:
				print(win(db))
				replayf()
			if full_board_check() is not False:
				print('Game over')
				replayf()
			print_board(**db)


play()