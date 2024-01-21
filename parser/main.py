############################################################
# Profit-Taker Analyzer by ReVoltage#3425                  #
# Rewritten by Iterniam#5829                               #
# Re-Rewritten by scamcat
# Original repo: https://github.com/revoltage34/ptanalyzer #
# Repo: https://github.com/Basiiii/Profit-Taker-Analytics  #
# Requires Python 3.10                                     #
############################################################

import traceback
from sty import fg
import colorama

from src.analyzer import Analyzer
from src.utils import color

VERSION = 'v1.0.0'


def error_msg():
    traceback.print_exc()
    print(color('\nAn unknown error occurred. Please screenshot this and report this along with your EE.log attached.',
                fg.li_red))
    input('Press ENTER to exit..')


def main():
    colorama.init()  # To make ansi colors work.
    print(f'{fg.cyan}Profit-Taker Analyzer {VERSION} by {fg.li_cyan}ReVoltage#3425{fg.cyan}, rewritten by '
          f'{fg.li_cyan}Iterniam#5829.')
    print(color("https://github.com/revoltage34/ptanalyzer \n", fg.li_grey))

    Analyzer().run()


if __name__ == "__main__":
    # noinspection PyBroadException
    try:
        main()
    except KeyboardInterrupt as e:  # To gracefully exit on ctrl + c
        pass
    except Exception:
        error_msg()
