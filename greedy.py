#DSA-Exer-24

def make_change(denomination_list, amount):
    '''Remove pass and implement the Greedy approach to make the change for the amount using the currencies in the denomination list.
    The function should return the total number of notes needed to make the change. If change cannot be obtained for the given amount, then return -1. Return 1 if the amount is equal to one of the currencies available in the denomination list.  '''
    denomination_list.sort(reverse = True)
    print(denomination_list)

    count = 0
    left_over = amount
    for i in range(len(denomination_list)):
        count = count + left_over//denomination_list[i]
        left_over = left_over%denomination_list[i]

    return count

#Pass different values to the function and test your program
amount= 20
denomination_list = [1,15,10]
make_change(denomination_list, amount)
