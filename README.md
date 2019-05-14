# open-mastermind
Terminal-based python of classic board game [Mastermind®](https://en.wikipedia.org/wiki/Mastermind_(board_game))


## to get the code

Clone the repository, then install the requirements (currently only the non-standary python3 library [`colorama`](https://pypi.org/project/colorama/), which prints a colorful terminal.)

    git clone https://github.com/philshem/open-mastermind.git
    cd open-mastermind
    pip install -r requirements.txt

    python3 mastermind.py

## game play

Each puzzle contains 4 boxes. Each turn you choose from 6 colors.

Can you guess the puzzle before your turns run out?

Color choices: r g y b m w

Example turn: rybg

Response:
◍  :  correct color in correct position
○  :  correct color in incorrect position
_  :  incorrect color

The order of the response tiles does not necessarily match the colored characters.

Type !h during gameplay to read these instructions.

## change the game parameters

Edit the file `params.py` to:

 + more pieces to guess

 + more/fewer turns per game

 + new colors

 + different emoji playing pieces


![Mastermind board game](https://upload.wikimedia.org/wikipedia/commons/2/2d/Mastermind.jpg)

