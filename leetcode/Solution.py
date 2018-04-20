import random
import datetime
def uniq(arr):
    arr = sorted(arr)
    i = 0
    j = 1
    while True:
        if i >= len(arr):
            break
        while j < len(arr) and arr[i] == arr[j]:
            j += 1
        arr = arr[:i+1] + arr[j:]
        i += 1
        j = i+1

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    medium=1
    for i in range(1,len(nums)):
        for k in range(0,i):
            if nums[k]==nums[i]:
                nums[i]=-1
                break
            else:
                if nums[k]==-1 :
                    nums[medium]=nums[i]
                    if medium!=i : nums[i]=-1
                    medium+=1
                    break
                else:
                    if i == k+1:
                        medium+=1

    return nums[:medium]

def create_numbsers(n, m, count):
    i = 0
    arr = []
    while i < count:
        i += 1
        arr.append(str(random.randint(n, m)))
    return arr


arr = create_numbsers(1, 10000, 40000)
print "start"

s = datetime.datetime.now()
uniq(arr)
e = datetime.datetime.now()
print("Time cost(ms): ", (e-s).seconds)

s1 = datetime.datetime.now()
removeDuplicates(arr)
e1 = datetime.datetime.now()
print("Time cost(ms): ", (e1-s1).seconds)

