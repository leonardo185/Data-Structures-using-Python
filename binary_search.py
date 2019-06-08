def binarySearach(list, value):
    first = 0
    last = len(list) - 1
    found = False
    index = None

    while(first <= last and not found):
        midpoint = int((first + last)/2)
        if(list[midpoint] == value):
            found = True
            index = midpoint + 1
        else:
            if(value < list[midpoint]):
                last = midpoint - 1
            else:
                first = midpoint + 1

    return index

list = [1,2,3,4,5,6,7,8,9]

print(binarySearach(list, 8))
