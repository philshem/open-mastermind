#!/usr/bin/env python
# coding: utf-8

''' params for mastermind '''

from colorama import Fore, Style

# how many turns to allow user to guess
count_turns = 10

# what unicode character to show guesses
# https://unicode-search.net/unicode-namesearch.pl?term=CIRCLE
guess_peg = '⬤'

# how many colors to guess (default = 6)
count_colors = 6
color_dict = {
            'r' : Fore.RED + Style.BRIGHT, 
            'g' : Fore.GREEN + Style.BRIGHT, 
            'y' : Fore.YELLOW, 
            'b' : Fore.BLUE, 
            'm': Fore.MAGENTA, 
            'w' : Fore.WHITE,
            }

# how many places to guess (default = 4)
count_boxes = 4

answer_dict = {'1' : '◍', '2' : '○', '9' : '_'}

# color options
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL


# cheat mode, prints master board before gameplay
debug = False