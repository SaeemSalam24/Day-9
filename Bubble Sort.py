def bubble_sort(list):
    n = len(list)
    
    for i in range(n):
    
        swapped = False
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
            if not swapped:
             break
    return list

list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", list)
sorted_arr = bubble_sort(list)
print("Sorted list:", list)
