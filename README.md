# open-mastermind
Terminal-based python of classic board game [Mastermind®](https://en.wikipedia.org/wiki/Mastermind_(board_game))


![Mastermind board game](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Mastermind.jpg/137px-Mastermind.jpg)

![screenshot of gameplay](https://gist.githubusercontent.com/philshem/71507d4e8ecfabad252fbdf4d9f8bdd2/raw/e00c621f403520d3268f2a9ece176fb2f05f2185/mastermind.png)

## to get the game

Install with `pip` from the command line:

    pip install open-mastermind

And run with this command:

    mastermind

Although written in Python3.7, it's compatible back to Python2.7.

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

## 2-player mode

Solutions can be hashed and shared with other players. To generate a code for the solution `red-green-yellow-blue` (rgyb):

    mastermind rgyb

    > Your code to play rgyb is 20419

Then share the code `20419` with the other player, who plays the desired game like this:

    mastermind 20419

It's _serverless_ and also on the honor system. Codes are generated on the fly based on the [16-bit CRC value](https://docs.python.org/2/library/binascii.html#binascii.crc_hqx).

# to get the code

Clone the repository, then install the requirements (currently only the non-standard python library [`colorama`](https://pypi.org/project/colorama/), which prints a colorful terminal.)

    git clone https://github.com/philshem/open-mastermind.git
    cd open-mastermind
    pip install -r requirements.txt

And to play from your downloaded code:

    python mastermind.py


## change the game parameters

Edit the file `params.py` to:

 + more pieces to guess

 + more/fewer turns per game

 + new colors

 + different emoji playing pieces
