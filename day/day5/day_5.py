########################################################################################################################
### Advent Setup #######################################################################################################
########################################################################################################################

import os
from AdventBuilder import setupDayVariables, prettyInfo, prettyAnswers

__dir__ = os.path.dirname(__file__)
DAY_NUM, DAY_DESC, DAY_INPUT, DAY_INPUT_STR = setupDayVariables(__dir__)

########################################################################################################################
#### My Solution #######################################################################################################
########################################################################################################################

from hashlib import md5
from itertools import takewhile

def solution():
    salt = "abc"
    result = []
    count = 0
    find = "00000"
    while len(result) < 8:
        hash = md5(salt + str(count)).hexdigest()
        if not hash.startswith(find):
            pass
        else:
            result.append(hash[5])
            print result
        count += 1
    return result, None


########################################################################################################################
### Output #############################################################################################################
########################################################################################################################


def main():
    print prettyInfo(DAY_DESC, DAY_INPUT_STR)
    print prettyAnswers(*solution())


if __name__ == "__main__":
    main()