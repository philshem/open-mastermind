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

import os
import random
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
		print('Invalid guess. Must include only letters rgyb.','\n')
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
	print('Color choices: '+' '.join([v+k+Style.RESET_ALL for k,v in params.color_dict.items()]))
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

def print_results(inp):
	
	grid = [Fore.WHITE + Style.BRIGHT + params.answer_dict.get(x) for x in inp]
	print(' '.join(grid))
	print(Style.RESET_ALL)
	return 

def get_results(guess, master):

	response = []

	for j, x in enumerate(list(master)):

		# scenario 1: color not in solution
		if master[j] not in guess:
			response += '9'

		# scenario 2: color in solution, but wrong position
		elif master[j] in guess and master[j] != guess[j]:
			response += '2'

		# scenario 3: color in solution, correct position
		elif master[j] == guess[j]:
			response += '1'

	# something went wrong
	if len(response) != params.count_boxes:
		print('🚀 Houston. We have a problem.')
		exit(0)

	# sort response array - comment out for debugging
	response = list(sorted(response))

	return response
	
def main():
	# clear terminal
	os.system('clear')

	# colorama initialization
	init() 

	# generate solution
	master = generate_board()
	
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
		results = get_results(guess, master)

		print_results(results)

		if ''.join(results) == '1'*params.count_boxes:
			print('🎉 Congrats! You found the solution:')
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
 