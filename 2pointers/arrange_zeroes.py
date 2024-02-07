'''
arrange all zeroes to last in an array without changing remaining elements
'''
# def arrange_zeros(arr):
#     non_zeros= [num for num in arr if num != 0]
#     zeros = [0] * (len(arr)-len(non_zeros))
#     print(non_zeros+zeros)
    
def arrange_zeros(arr):
    print('arrange_zeros...')
    print('que',arr)
    left = 0
    for i in range(0,len(arr)):
        if arr[i] != 0:
            arr[i], arr[left] = arr[left], arr[i]
            left+=1
    print('ans',arr)

arrange_zeros([1,3,4,5,2,0,9,0,8,0])
