def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1    
arry=[10,20,80,55,66,83]
target=83
result=(linear_search(arry,target))
if(result==-1):
    print("Element not found in the array")
else:
    print("Element found at :",result)
