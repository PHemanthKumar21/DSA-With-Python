#Pancakesort
def pancakesort(arr):
    n= len(arr)
    for size in range(n,1,-1):
        max_index = arr.index(max(arr[:size]))
        arr[:max_index+1] = arr[:max_index+1][::-1]
        arr[:size]=arr[:size][::-1]
    return arr
arr = list(map(int, input("Enter elements:").split()))
print("Sorted array:",pancakesort(arr))

                          
