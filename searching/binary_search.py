def binarysearch(element, arr1):
    leftptr = 0
    rightptr = len(arr1)-1
    
    while leftptr <= rightptr:
        midptr = (leftptr+rightptr)//2
        
        if element == arr1[midptr]:
            return arr1[midptr]
        
        # If element is smaller, ignore right half
        elif element < arr1[midptr]:
            rightptr = midptr-1
        
        # If element is greater, ignore left half
        elif element > arr1[midptr]:
            leftptr = midptr+1

    # If we reach here, then the element was not present
    return -1

result = binarysearch(7, [1,2,3,4,5])
print(result)