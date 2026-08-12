def partition(arr,start,end):
    pivot=arr[end]
    pindex=start
    for i in range(start,end):
        if (arr[i]<=pivot):
            arr[i],arr[pindex]=arr[pindex],arr[i]
            pindex+=1
    arr[pindex],arr[end]=arr[end],arr[pindex]
    return pindex

def quickSort(arr,start,end):
   if(start<end):
        pi=partition(arr,start,end)
        quickSort(arr,start,pi-1)
        quickSort(arr,pi+1,end)
        return arr

arr=[2,3,5,7,4,1,9,6]
print(quickSort(arr,0,len(arr)-1))  

