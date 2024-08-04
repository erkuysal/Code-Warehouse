
def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        print(arr)
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break


arr = [64, 34, 25, 12, 22, 11, 90]

print(f'unsorted array is : {arr}')
bubblesort(arr)
