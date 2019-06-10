def selection(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if(list[min] > list[j]):
                min = j

        if(min != i):
            list[i],list[min] = list[min],list[i]

    return list

list = [9,8,7,6,5,4,3,2,1]

print(selection(list))
