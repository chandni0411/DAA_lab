#min-max approach

def min_max(arr):
    if(len(arr)==1):
        return (arr[0],arr[0] )
    mid=len(arr)//2
    min1,max1=min_max(arr[:mid])
    min2,max2=min_max(arr[mid:])
    if (min1<min2):
        final_min=min1
    else:
        final_min=min2
    if (max1>max2):
        final_max=max1

    else:
        final_max=max2
    return (final_min,final_max)
arr=[1,2,3,4,5,6,7,8,9]
print(min_max(arr)) 


    
