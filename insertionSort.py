def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key  ):
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=key
arr=[5,4,3,1,7,6,2]

insertionsort(arr)
print (arr)
