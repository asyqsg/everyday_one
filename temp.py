n = int(input())
nums = list(map(int, input().split()))


def quick_sort(nums, l, r):
    if l >= r: return
    flag_num = nums[l]
    i, j = l - 1, r + 1
    while i < j:
        while True:
            i += 1
            if nums[i] >= flag_num:
                break
        while True:
            j -= 1
            if nums[j] <= flag_num:
                break
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    quick_sort(nums, l, j)
    quick_sort(nums,j + 1, r)
    return nums


print(quick_sort(nums, 0, len(nums)-1))