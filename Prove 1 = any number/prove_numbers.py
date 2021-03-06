from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
#from pywebio.exceptions import SessionClosedException
import pickle
import warnings
import argparse
import time

warnings.filterwarnings("ignore")

def prove_numbers():
    solution_1 = "Let's take an equation \n" \
                 "X\u00b2 - Y\u00b2 = X\u00b2 - Y\u00b2 \n" \
                 "L.H.S = R.H.S \n" \
                 "So, Applying formula: (a\u00b2 - b\u00b2) = (a + b)(a - b) , we get\n" \
                 "L.H.S = (X + Y)(X - Y)\n" \
                 "Let's assume X = Y \n" \
                 "Since X is equal to Y, we can replace Y with X and we get, \n" \
                 "L.H.S = (X + X)(X - X) ----------------(1) \n" \
                 "and R.H.S = (X\u00b2 - Y\u00b2) = (X\u00b2 - X\u00b2) \n" \
                 "After taking X as common, we get\n" \
                 "R.H.S = (X\u00b2 - X\u00b2) = X(X - X) ----------(2) \n" \
                 "Now comparing L.H.S = R.H.S, we get \n" \
                 "(X + X)(X - X) = X(X - X) ---from (1) & (2) \n" \
                 "(X - X) gets cancel out from both the sides, so we are left with \n" \
                 "(X + X) = X \n" \
                 "2X = X \n" \
                 "X gets cancel out from both the sides, so we are left with \n" \
                 "2 = 1 which is also equal to \n" \
                 "1 = 2 ------(4)"
    solution_2 = "Adding '1' on both the sides of the above equation, we get \n" \
                 "1+1 = {}+1 \n" \
                 "2 = {} \n" \
                 "Since (1 = 2) & (2 = {}), so we get \n" \
                 "1 = {} ---------- ({})"
    put_text("Hey folks, Mathematically you can prove 1 to be equal to any number! \n"
             "Type any smaller number first to understand the mathematical twist!")
    user = int(input("Enter any number", placeholder='I want to prove 1 ='))
    put_text('Proving 1 = {}. Please wait.....'.format(user))
    put_processbar('bar1')
    for i in range(1, 11):
        set_processbar('bar1', i / 10)
        time.sleep(0.5)
    if user > 2:
        put_text(solution_1)
        for i in range(2, user):
            put_text(solution_2.format(i, i+1, i+1, i+1, i+3))
        put_text("Hurray! We have proved 1 = {} \U0001F609".format(user))
    elif user == 2:
        put_text(solution_1)
        put_text("Hurray! We have proved 1 = {} \U0001F609".format(user))
    elif user == 1:
        put_text("1 is already equal to 1 \U0001F606")
    else:
        put_text("Just reverse the process and start subtracting and you can prove 1 = {} \U0001F92F".format(user))


def main():
    return prove_numbers()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(main, port=args.port)
