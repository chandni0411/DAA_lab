def bubblesort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-1):
            if(arr[j]>arr[j+1]):
                (arr[j],arr[j+1])=(arr[j+1],arr[j])

arr=[5,4,3,1,9,1,2]
bubblesort(arr)
print (arr)

