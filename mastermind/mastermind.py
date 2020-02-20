#!/usr/bin/env python
# coding: utf-8

''' play mastermind '''

# python2 compatability
from __future__ import print_function
try:
	import __builtin__; input = getattr(__builtin__, 'raw_input', input)
except ImportError:
	pass

# internal parameters
from . import params
#import params

import os, sys
import random
import itertools
from collections import Counter, defaultdict
import binascii
from colorama import init, Style, Fore

def generate_board():

	# generates a random board based on params.py
	return [random.choice(list(params.color_dict.keys())) for x in range(params.count_boxes)]

def make_guess(msg, master):

	guess = input(msg).lower().strip()

	if guess.startswith('!h'):
		print_instructions()
		return
	elif guess.startswith('!q'):
		print ('You chose to quit. The solution is:')
		print_colors(master, params.guess_peg, True)
		exit(0)

	elif len(guess) != params.count_boxes:
		print('Invalid guess. Must be',str(params.count_boxes),'colors.','\n')
		return None
	elif not all([x in params.color_dict.keys() for x in list(guess)]):
		print('Invalid guess. Must include only letters: '+print_color_choices()+'\n')
		return None
	else:
		return guess

def print_colors(inp, guess_char, tf_master):

	# print colored characters, suppress new line

	print('  '.join([params.color_dict.get(x) + guess_char for x in inp]),end='\t')
	if tf_master:
		print(Style.RESET_ALL,end='\n')
	else:
		print(Style.RESET_ALL,end='\t')
	return

def print_instructions():
	print('Puzzle contains '+str(params.count_boxes)+' boxes. Each turn you choose from '+str(params.count_colors)+' colors.')
	print('Color choices: '+print_color_choices())
	print('Example turn: rybg')
	print('Response:')
	print(params.answer_dict.get('1')+'  :  correct color in correct position')
	print(params.answer_dict.get('2')+'  :  correct color in incorrect position')
	print(params.answer_dict.get('9')+'  :  incorrect color')
	print()
	print('The order of the response tiles does not necessarily match the colored characters.')
	print('Type !h to read these instructions again.')
	print('Type !q to quit and show solution.')
	print()

def print_color_choices():

	return ' '.join([v+k+Style.RESET_ALL for k,v in params.color_dict.items()])


def print_results(inp):

	grid = [Fore.WHITE + Style.BRIGHT + params.answer_dict.get(x) for x in inp]
	print(' '.join(grid))
	print(Style.RESET_ALL)
	return

def get_results(guess, master):

	response = []

	# much simpler logic
	# https://stackoverflow.com/a/45798078/2327328

	correct_colors = sum((Counter(guess) & Counter(master)).values())
	correct_locations = sum(g == m for g, m in zip(guess, master))

	correct_results = max(0,correct_colors - correct_locations)
	incorrect_results = max(0,params.count_boxes - correct_colors)

	result = '1' * correct_locations \
			 + '2' * correct_results \
			 + '9' * incorrect_results

	if params.debug: print(result)

	# something went wrong
	if len(result) != params.count_boxes:
		print('🚀 Houston. We have a problem.')
		exit(0)

	# sort response array - comment out for debugging
	#response = list(sorted(response))

	return result

def validate_puzzle(t):

	if len(t) != params.count_boxes:
		print ('Incorrect number of boxes. Needs to be {} boxes.'.format(params.count_boxes))
		exit(0)
	elif any([x for x in t if x not in params.color_dict.keys()]):
		print ('Incorrect color selected. Choose from {}.'.format(print_color_choices()))
		exit(0)
	else:
		#print(list(t))
		return True

def generate_code():

	xx = defaultdict(int)

	all_combos = [p for p in itertools.product(params.color_dict.keys(), repeat=params.count_boxes)]

	for aa in all_combos:
		t = ''.join(aa)
		z = binascii.crc_hqx(t.encode('ascii'), 0)
		#print(t,str(z).zfill(5))
		xx[str(z).zfill(5)] = t

	return xx

def main():

	# colorama initialization
	init()

	# generate code table (dict)
	dd = generate_code()

	# read system args, if any
	master = None
	# play random (normal) game if no input params are given
	if len(sys.argv) < 2:
		# generate solution
		master = generate_board()

	# check that not too many input params are given
	elif len(sys.argv) > 2:
		print('Incorrect number of system arguments.')
		exit(0)

	# check if puzzle is provided to generate code (no game is played in this case)
	elif sys.argv[1] in dd:
		#print(dd.get(sys.argv[1]))
		master = list(dd.get(sys.argv[1]))

	# generate puzzle based on code
	elif validate_puzzle(sys.argv[1]):
		rd = dict(map(reversed, dd.items()))
		if sys.argv[1] in rd:
			print('Your code to play {} is {}'.format(sys.argv[1],rd.get(sys.argv[1])))
			exit(0)

	# if you made it this far, there is no game to play
	else:
		#print('Invalid input parameters.')
		exit(0)

	# clear terminal
	os.system('clear')

	#cheat or debug mode
	if params.debug:
		print_colors(master, params.guess_peg, True)

	print_instructions()

	guess_list = []
	for i in range(params.count_turns):
		guess = None
		while not guess:

			# create message based on turn number
			if i + 1 < params.count_turns:
				msg = 'Turn '
			else:
				msg = 'Last turn! '
			msg += str(i+1)+' of '+str(params.count_turns)+'. Your guess: '

			# request guess from user
			guess = make_guess(msg, master)

		print_colors(guess, params.guess_peg, False)
		guess_list.append(guess)

		# check guess - if you made it this far,
		# the guess is valid and there are still more turns
		result = get_results(guess, master)

		print_results(result)

		if result == '1' * params.count_boxes:
			print('🎉 Congrats mastermind! You found the solution:')
			print_colors(master,params.guess_peg,True)
			print()
			exit(0)

		# game over... too many turns used
		if len(guess_list) >= params.count_turns:
			print ('Too many turns! The solution is:')
			print_colors(master,params.guess_peg,True)
			exit(0)

if __name__ == "__main__":

	main()
