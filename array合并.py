#数组合并
arr1 = [1,3,4,6,10]
arr2 = [2,5,8,11]
arr3 = arr1.copy()
ind = 0 
for i in range(0,len(arr2)):
    while ind < len(arr1):
        if arr2[i] <= arr1[ind]:
            arr3.insert(ind + i,arr2[i])
            break
        else: ind += 1
    else:
        arr3 = arr3 + arr2[i:]
        break
print(arr1)
print(arr2)
print(arr3)
