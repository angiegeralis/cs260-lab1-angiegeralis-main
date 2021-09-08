'''
Author      : Angie Geralis
Class       : CS260
Date        : 8/31/21
Description : This is the main driver program for the Introduction to Python
portion of Lab 1. This intro consists of a series of coding exercises that cover
some of the core syntax, data structures, and functionality of Python

'''

# TODO add imports here
import random

################################################################################
# MAIN
################################################################################

def main():
    '''
    For each function below, please write tests in main to confirm that it works
    correctly. Although the focus of this assignment is not on testing (so you
    don't necessarily need to check *every* case), it is good practice to
    consider both the standard and corner cases when writing your tests.
    '''
    print("movie")
    movie_ticket_cost()
    print("in place")
    shuffle_in_place([1,2,3,4])
    print("out of place")
    shuffle_out_of_place([1,2,3,4])
    print("fib")
    print(fib(3))
    print("binsrchr")
    print(binary_search_r(4,[1,2,3,4,5]))
    print("binsrchnr")
    binary_search_nr(4,[1,2,3,4,5])

    pass

################################################################################
# FUNCTIONS
################################################################################

def movie_ticket_cost():
    '''
    Calculates the price of movie tickets based on the user’s age.
    The method will prompt the user to enter their age, then print out the result.
    '''
    #take input of age and classify as $12 or $8 ticket
    age = int(input("Age of Ticket Holder: "))
    if (age > 12 and age < 65):
        print("$12")
    else:
        print("$8")

    pass


def shuffle_in_place(lst):
    '''
    Shuffles a given list in place by changing the order of the original
    list without returning anything.
    '''
    # find length of list
    length = len(lst)
    # start from highest increase and go down list, chosing a random index point to swap i with each time
    for i in (length-1,0,-1):
        rand_index = random.randint(0,i+1)
        lst[i],lst[rand_index] = lst[rand_index],lst[i]
    print(lst)

    pass

def shuffle_out_of_place(lst):
    '''
    Shuffles a given list out of place by leaving the original list intact
    and returning a new shuffled version of the list.
    '''
    newlst = lst[:]
    # find length of list
    length = len(newlst)
    # start from highest increase and go down list, chosing a random index point to swap i with each time
    for i in (length-1,0,-1):
        rand_index = random.randint(0,i+1)
        newlst[i],newlst[rand_index] = newlst[rand_index],newlst[i]
    print(lst)
    print(newlst)
    pass

def fib(n):
    '''
    Calculates the nth Fibonacci number, given a non-negative integer n.
    '''
    #start with 1,1...
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return fib(n-2) +fib(n-1)
    pass

def binary_search_r(query, lst): # recursive version
    '''
    Return the index of query, or -1 if it is not in the list. Recursive algorithm
    will take a middle element and check it against the target.If they are equal,
    it will return the index of the middle element. If the target is less than
    the middle element it calls binary search on the first half of the list.
    If the target is greater than the middle element it calls binary search on
    the second half of the list.
    '''
        mid = len(lst) // 2 #assigns mid
    if len(lst) == 1:
        if lst[mid]==query:
            return mid
        else:
            return -1
    elif lst[mid] == query:
        return mid
    else:
        if lst[mid] < query:
            #in order to keep track of the original index in my code, I had to create
            #a recurse variable that could be added to the mid
            recurse = binary_search_r(query, (lst[mid:]))
            if recurse != -1:
                return mid + recurse #adds segment of sliced lst if query is above the mid
            else:
                return -1
        else:
            return binary_search_r(query, (lst[:mid]))
    pass

def binary_search_nr(query, lst): # non-recursive version
    '''
    Return the index of query, or -1 if it is not in the list.
    Iterative algorithm will Compute the “low” index (usually begins at 0)
    and the “high” index. Then compute the index of the middle element and check
    it against the query. If the middle element is greater than the query, move
    the “high” down and repeat the process using a loop.
    '''
        low=0
    high = len(lst) - 1
    while low <= high:
        mid = int(low + high) // 2
        if query == lst[mid]:
            return mid
        if lst[mid] > query:  #decrease high index when mid is greater than query
            high -= 1
        if lst[mid] < query: #increase low when mid is less than query
            low += 1

    return -1


    pass

if __name__ == "__main__":
    main()
