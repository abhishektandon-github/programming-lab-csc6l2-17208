def insertionSort(arr): 
    for i in range(len(arr)):
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j]: 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
  
arr = list(map(int, input("Enter the array to sort: "). split(' ')))

insertionSort(arr) 
print("After Insertion Sort: ")
for a in arr: 
    print (a, end = " ") 