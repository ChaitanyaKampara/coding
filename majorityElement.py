def majorityElement(arr):
    cnt = 0
    ele = None
    n = len(arr)

    for i in range(n):
        if cnt == 0: 
            cnt = 1       
        elif ele == arr[i]:
             cnt += 1
        else:
            cnt -= 1
# until here we are fixing element ele

    cnt1 = 0

    for i in range(n):
        if arr[i] == ele:
            cnt1 += 1

    if cnt1 > (n/2):
        return ele
    return -1
# until here we are checking that ele element count by linear search

arr = [1,1,1,1,1,2,2]
ans = majorityElement(arr)
print("The majority element is:" , ans)   