class Solution:
    def countBits(self, n: int) -> List[int]:


        #O(N) time solution 

        ans = [0] * (n + 1) #desc says an arr is == to len of n + 1
                            #atleast one value will be zero so set all values to 0
        offset = 1 #to keep track of the powers of 2 since this is binary

        for i in range(1, n+1): #go up to including n but not n + 1
            if offset * 2. == i: #if the i is a power of 2 set offset = to i
                offset = i
            ans[i] = 1 + ans[i - offset] #our ith answer will be 1 + whatever i - offset
        return ans

        