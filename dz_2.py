#1

def max_in_range(arr, start: int, end: int):


    maximum = float('-inf')
    index = -1
    inde = -1

    for i in range(start, end + 1):
        if arr[i] > maximum:
            maximum = arr[i]
            index, inde = i - start , i

    return maximum, index, inde

print(max_in_range([2,7,1,8,2],1,3))


#2


def rotate_and_reverse(arr, k: int):

    listik = []

    k %= len(arr)

    for i in range(-k ,len(arr)-k):
        listik.insert( 0, arr[i])
    
    return listik


print(rotate_and_reverse([1,2,3,4],3))


#3


def reverse_even_elements(arr):

    indexs = [i for i in range(len(arr)) if arr[i] % 2 == 0]


    return [arr[i] if arr[i] % 2 != 0 else arr[indexs.pop()] for i in range(len(arr))]

print(reverse_even_elements([1,2,3,4,5]))


#4


#def number(arr):  я поняла, что нужно , но я не понимаю как это можно реализовать:(


#5

def bubble_sort(arr):

    for i in range(len(arr)):

        for j in range(len(arr)-1):

            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

    return arr

print(bubble_sort([1,3,4,6,2,8]))


#6

import random

def bogosort(arr):

    while not arr:

        for i in range(0, len(arr)):

            run =random.randint (0 , len(arr)-1)

            okeoke = arr[i]
            arr[i] = arr[run]
            arr[run] = okeoke

    #return, а дальше я не знаю что написать нужно:(
    
print(bogosort([1,3,5,2,8]))
        
#хорошего времени суток