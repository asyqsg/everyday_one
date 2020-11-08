class Solution:
    def maxProfit(self, inventory, orders: int):
        if not inventory or not orders: return 0

        def get_val(val1,val2,count):
            return ((val1+val2)*count//2)

        val = 0
        if len(inventory) == 1:
            va11 = inventory[0]-orders+1
            val2 = inventory[0]
            val = get_val(va11,val2,orders)
            return val
        while orders > 0:
            inventory.sort()
            val1 = inventory[-2]
            val2 = inventory[-1]
            count = val2-val1+1
            if orders - count>=0:
                val+=get_val(val1,val2,count)
            else:
                count = orders
                val+= val2*count
            orders -= count
            inventory[-1] = val1-1
        return val%(10**9+7)

if __name__ == '__main__':
    print(Solution().maxProfit([2,8,4,10,6],20))