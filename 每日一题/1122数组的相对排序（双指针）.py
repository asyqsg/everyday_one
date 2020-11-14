class Solution:
    def relativeSortArray(self, arr1:list, arr2):
        size_1 = len(arr1)
        size_2 = len(arr2)

        def get_star():
            if not arr2:
                return None
            else:
                star = arr2[0]
                arr2.remove(star)
                return star

        i,j = 0,0
        star = get_star()
        while i < size_1:

            if arr1[i] == star:
                i += 1
            else:
                #需要判断j的位置，如果j在i到size-1之间，就按照j的位置，否则就i+1
                if j < i:
                    j = i
                while j < size_1:
                    if arr1[j] != star:
                        j+=1
                    else:
                        arr1[i],arr1[j] = arr1[j],arr1[i]
                        i+=1
                        break
                if j == size_1:
                    star = get_star()
                    if not star:
                        break
                    j = i
        if i != size_1:
            temp = arr1[i:]
            temp.sort()
            arr1 = arr1[:i] + temp
        return arr1
if __name__ == '__main__':
    print(Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))






