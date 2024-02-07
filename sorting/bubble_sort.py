def bubble_sort(arr):
    for i in range(0,len(arr)):
        print(f'==={i}===')
        for j in range(0,len(arr)-i-1):
            
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                print(j,arr)
    return arr
ans = bubble_sort([64, 34, 25, 12, 22, 11, 90])
print(ans)