# open-mastermind
Terminal-based python of classic board game [Mastermind®](https://en.wikipedia.org/wiki/Mastermind_(board_game))


![Mastermind board game](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Mastermind.jpg/137px-Mastermind.jpg)

## to get the game

Install with `pip` from the command line:

    pip install open-mastermind

Although written in Python3.7, it's compatible back to Python2.7.

## to get the code

Clone the repository, then install the requirements (currently only the non-standard python library [`colorama`](https://pypi.org/project/colorama/), which prints a colorful terminal.)

    git clone https://github.com/philshem/open-mastermind.git
    cd open-mastermind
    pip install -r requirements.txt

## to play

    cd open-mastermind
    python mastermind.py

## example game play

Each puzzle contains 4 boxes. Each turn you choose from 6 colors.

Can you guess the puzzle before your turns run out?

Color choices: r g y b m w

Example turn: rybg

Response:

◍  :  correct color in correct position

○  :  correct color in incorrect position

_  :  incorrect color

The order of the response tiles is sorted and does not necessarily match the position of the colored tiles.

Type !h during gameplay to read these instructions.

Type !q during gameplay to quit and show the solution.


## change the game parameters

Edit the file `params.py` to:

 + more pieces to guess

 + more/fewer turns per game

 + new colors

 + different emoji playing pieces

---

## screenshot of gameplay

![screenshot of gameplay](https://gist.githubusercontent.com/philshem/71507d4e8ecfabad252fbdf4d9f8bdd2/raw/e00c621f403520d3268f2a9ece176fb2f05f2185/mastermind.png)
