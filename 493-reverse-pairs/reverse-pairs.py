class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def getMeCnt(arr,low,high):

            if low >= high:

                return 0
            
            cnt = 0

            mid = (low + high)//2

            cnt += getMeCnt(arr,low,mid)

            cnt += getMeCnt(arr,mid+1, high)

            cnt += countPairs(arr, low, mid, high)

            merge(arr,low,high)

            return cnt

        def countPairs(arr, low, mid, high):
            right = mid + 1
            cnt = 0
            for i in range(low, mid + 1):
                while right <= high and arr[i] > 2 * arr[right]:
                    right += 1
                cnt += (right - (mid + 1))
            return cnt

        def merge(arr,low,high):

            mid = (low + high)//2

            left = low

            right = mid + 1

            cnt = 0

            temp = []

            while left <= mid and right <= high:

                if arr[left] <= arr[right]:

                    temp.append(arr[left])

                    left += 1
                
                else:

                    temp.append(arr[right])

                    if arr[left] > 2*arr[right]:

                        cnt += (mid - left + 1)

                    right += 1
            
            while left <= mid:

                temp.append(arr[left])

                left += 1
            
            while right <= high:

                temp.append(arr[right])
                
                right += 1
            
            for i in range(low,high + 1):

                arr[i] = temp[i - low]
            
            return cnt
        
        return getMeCnt(nums,0,len(nums)-1)