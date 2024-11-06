def bubble_sort(list):
    steps = 0
    for n in range(len(list)-1, 0, -1):
        for i in range(n):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                steps +=1
    print(list)
    print("completed in " + str(steps)+ " steps")   
list = []

bubble_sort(list)
print(list)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)