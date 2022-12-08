# import test function
from evaluate_test import evaluate_test_cases
from test_zone import tests

# Linear search algorithm
def locate_card_linear(cards, query):

    # create a variable solution with value 0
    lo = 0

    # set up a loop for repetition
    while lo < len(cards):

        # check if element at the current position matches the query
        if cards[lo] == query:

            # answer found! return and exit ...
            return lo

        # if query not found at that position, increment the position
        lo += 1

    # number not found, return -1
    return -1

def test_location(cards, query, mid):
    """Helper function to deal with repetitive values"""
    mid_number = cards[mid]
    # print("mid: ", mid, "mid_number: ", mid_number)

    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return "left"
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


# Recursion
def locate_card_recursive(cards, query, start=0, end=None):
    if end is None:
        end = len(cards) - 1
    if start > end:
        return -1

    mid = (start + end) // 2
    if query == cards[mid]:
        return mid
    if query < cards[mid]:
        return locate_card_recursive(cards, query, start, mid - 1)
    # elem > arr[mid]
    return locate_card_recursive(cards, query, mid + 1, end)


# Binary Search Improved Algorithm
def locate_card_improved(cards, query):
    """Performs more efficiently a binary search."""
    lo, hi = 0, (len(cards) - 1)

    while lo <= hi:
        # find index of the middle card
        mid = (lo + hi) // 2
        # mid_number = cards[mid]

        result = test_location(cards, query, mid)

        # check if query is the middle card
        if result == 'found':

            # return position of middle card i.e mid
            return mid
        # else if mid number is greater than query
        # meaning query is on the left
        # discard all cards on the left
        elif result == 'left':
            hi = mid - 1

        # elif mid_number is less than query
        # meaning query is on the right
        # discard all cards on the right
        elif result == 'right':
            lo = mid + 1

    # if card not found return -1 as the loop exits
    return -1

evaluate_test_cases(locate_card_recursive, tests)


