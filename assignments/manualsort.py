def bubble_sort(list):
    for n in range(len(list)-1, 0, -1):
        for i in range(n):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
            
list = [5,3,4,7,1,2,6]

bubble_sort(list)
print(list)
