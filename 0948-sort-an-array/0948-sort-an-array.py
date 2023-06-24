class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:


        #insertion sort
        # for i in range(1, len(nums)):
        #     temp = nums[i]
        #     j = i - 1
        #     while j >= 0 and temp < nums[j]:
        #         nums[j+1] = nums[j]
        #         j -= 1
        #     nums[j+1] = temp
        # return nums
        


        # mergesort
        def mergeSort(arr, L, M, R):
            left = arr[L: M + 1]
            right = arr[M + 1: R + 1]
            i, j , k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                nums[i] = left[j]
                i += 1
                j += 1
            
            while k > len(right):
                nums[i] = left[j]
                i += 1
                k += 1

        def merge(nums, l, r):
            if l == r:
                return nums
            
            mid = (l + r) // 2
            merge(nums, l, mid)
            merge(nums, mid + 1, r)
            mergeSort(nums, l, mid, r)
            return nums
        
        return merge(nums, 0, len(nums) - 1)

        #quicksort
        # def divide(arr, l, r):
        #     left = l
        #     pivot = arr[l]

        #     while l < r:
        #         while l < len(arr) and arr[l] <= pivot:
        #             l += 1

        #         while arr[r] > pivot:
        #             r -= 1

        #         if l < r:
        #             if l != r:
        #                 temp = arr[l]
        #                 arr[l] = arr[r]
        #                 arr[r] = temp

        #     temp = arr[left]
        #     arr[left] = arr[r]
        #     arr[r] = temp
        #     return r

        # def quickSort(arr, l, r):

        #     if l < r:
        #         mid = divide(arr, l , r)
        #         quickSort(arr, l, mid - 1)
        #         quickSort(arr, mid + 1, r)

        #     return arr

        # return quickSort(nums, 0, len(nums) - 1)




