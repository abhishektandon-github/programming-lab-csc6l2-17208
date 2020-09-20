def binarySearch(arr, p, r, x):
    
    if(p <= r):
        q = (p+r)//2
        
        if arr[q] == x:
            return q
        
        if arr[q] < x:
            return binarySearch(arr, q+1, r, x)
            
        if arr[q] > x:
            return binarySearch(arr, p, q-1, x)
    return -1



if __name__ == "__main__":
    arr = list(map(int, input("Enter a sorted list of integers: \n").split(' ')))
    x = int(input("Enter number to search: \n"))
    val = binarySearch(arr, 0, len(arr)-1, x)
    if val != -1:
        print(x, "found at position:", val+1)
    else:
        print(x, "is not found")