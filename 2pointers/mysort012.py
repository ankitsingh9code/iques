'''
arrange 0s, 1s and 2s in acending order 
'''
# def mysort(arr):
#     print('mysort...')
#     print('que',arr)
#     count0, count1, count2 = 0, 0, 0
#     for num in arr:
#         if num == 0:
#             count0+=1
#         elif num == 1:
#             count1+=1
#         elif num == 2:
#             count2+=1
#     return [0]*count0 + [1]*count1 + [2]*count2

# def mysort(arr):
#     print('mysort...')
#     print('que', arr)
#     leftptr, rightptr = 0, len(arr)-1
#     for i in range(0,len(arr)):
#         if arr[i] == 0 and i>leftptr:
#             arr[i], arr[leftptr] = arr[leftptr], arr[i]
#             leftptr+=1
            
#         elif arr[i] == 2 and i<rightptr:
#             arr[i], arr[rightptr] = arr[rightptr], arr[i]
#             rightptr-=1
        
#     return arr
    
def mysort(arr):
    print('mysort...')
    print('que', arr)
    i, leftptr, rightptr = 0, 0, len(arr)-1
    # for i in range(0,len(arr)):
    while i <= rightptr:
        if arr[i] == 0:
            arr[i], arr[leftptr] = arr[leftptr], arr[i]
            leftptr+=1
            i+=1
        elif arr[i] == 2:
            arr[i], arr[rightptr] = arr[rightptr], arr[i]
            rightptr-=1
        else:
            i+=1
    return arr
    
s = mysort([2,1,0,1,1,2,2,0,0,1,2,0])
print('ans',s)
    
