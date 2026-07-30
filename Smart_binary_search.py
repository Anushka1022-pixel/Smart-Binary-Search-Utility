def binarysearch(array,start,end,target):
    if start>end:
        return -1
    if start<=end:
        mid=(start+end)//2
        if target==array[mid]:
            return mid
        elif target <array[mid]:
            return binarysearch(array,start,mid-1,target)
        else:
            return binarysearch(array,start,mid+1,target)
    else:
        print("Not Found")
        
def getarray(n):
    arr=[]
    for i in range(n):
        num=int(input("Enter you numbers"))
        arr.append(num)
    return arr

n=int(input("Enter the size of array"))
array=getarray(n)
target=int(input("Target"))
start=0
end=len(array)-1
result=binarysearch(array,start,end,target)
print(result)

        
