from typing import List

def read_integers() -> List[int]:
    # read line from stdin, not print
    # return list of integers
    user_list = [int(number) for number in input().split(",")]
    return user_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())