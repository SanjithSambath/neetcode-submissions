class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            # 1 Find the middle index and split the array
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            
            # 2 recursively sort both halves
            sorted_left = merge_sort(left_half)
            sorted_right = merge_sort(right_half)
            
            # 3 Merge the sorted halves
            return merge(sorted_left, sorted_right)




        def merge(left, right):
            result = []
            i = j = 0
            
            # Compare elements from both halves and build the sorted result
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
                    


            # Append any remaining elements left over in either array
            result.extend(left[i:])
            result.extend(right[j:])
            return result


        return(merge_sort(nums)) 