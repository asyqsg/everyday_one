class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        def find_target(ring:list,target:str):
            ring_reverse = list(ring)
            ring_reverse.reverse()
            index_positive = ring.index(target)
            index_negative = ring_reverse.index(target)
            step_positive = index_positive+1
            step_negative = index_negative+1+1
            if step_positive < step_negative:
                re_ring = ring[index_positive:] + ring[:index_positive]
                step = step_positive

            elif step_positive > step_negative:
                index_negative = len(ring)-1-index_negative
                re_ring = ring[index_negative:]+ring[:index_negative]
                step = step_negative


            return step,re_ring

        key = list(key)
        ring = list(ring)
        count = 0
        for i in key:
            step,ring = find_target(ring,i)
            count += step
            print(count)

        return count

if __name__ == '__main__':
    ring = 'iotfo'
    key = 'fioot'
    print(Solution().findRotateSteps(ring,key))