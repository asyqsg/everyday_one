def quick_sort(nums:list,l:int,r:int):
    if l >= r: return nums

    flag_num = nums[l]
    i = l-1
    j = r+1
    while i < j:
        while True:
            i+=1
            if nums[i] >= flag_num:
                break
        while True:
            j-=1
            if nums[j] <= flag_num:
                break
        if i < j:
            nums[i],nums[j] = nums[j],nums[i]

    quick_sort(nums,l,j)
    quick_sort(nums,j+1,r)
    return nums

if __name__ == '__main__':
    print(quick_sort([1,4,6,2,3],0,4))