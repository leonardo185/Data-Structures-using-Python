def bubble_sort(arr):
    exchanges = True
    length = len(arr) - 1
    while(length > 0 and exchanges):
        exchanges = False
        for i in range(length):
            if(arr[i] > arr[i+1]):
                exchanges = True
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        length = length - 1

arr=[20,30,40,90,50,60,70,80,100,110]
bubble_sort(arr)
print(arr)
