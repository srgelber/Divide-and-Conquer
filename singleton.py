##Simon Gelber - CSC359 Asgn 1
# Find the singleton

import sys

#function to find the number that occurs only once
def singleton(list, low, high):

    #single number does not occur
    if low > high:
        return None
    #single number is located
    if low == high:
        return list[low]

    #find the mid point
    mid = (low + high) // 2

    #if it is even, the next number must be the same or else we know the single is before mid
    if mid % 2 == 0:
        if list[mid] == list[mid + 1]:
            return singleton(list, mid + 2, high)
        else:
            return singleton(list, low, mid)
    #if it is odd, the previous number must be the same or else we know the single is before mid
    else:
        if list[mid] == list[mid - 1]:
            return singleton(list, mid + 1, high)
        else:
            return singleton(list, low, mid - 1)


def main(argv):
    file = open(argv[1],"r")
    numbers = file.read()
    numbers = numbers.strip()
    numberslist = numbers.split(", ")
    singleValue = singleton(numberslist, 0, len(numberslist) - 1)
    print(singleValue)


if __name__ == "__main__":
    main(sys.argv)