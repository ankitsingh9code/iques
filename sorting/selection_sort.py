# def selection_sort(arr):
#     for i in range(0,len(arr)):
#         min_idx = i
#         print(f'==={i}===')
        
#         # Find the minimum element's index in remaining unsorted array 
#         for j in range(i+1, len(arr)):
#             if arr[min_idx]>arr[j]:
#                 min_idx = j
                
#         arr[i],arr[min_idx],= arr[min_idx], arr[i] 
#         print(arr)
#     return arr

# ans = selection_sort([3,2,1,4,5,3,7,0])
# print(ans)

def selection_sort(arr):
    for i in range(0,len(arr)):
        print(f'==={i}===')
        
        # Find the minimum element's index in remaining unsorted array 
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j],= arr[j], arr[i] 
                print(j, arr)
        print(arr)
    return arr

ans = selection_sort([3,2,1,4,5,3,7,0])
print('ans', ans)