class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        del nums2[n:]
        for n2 in nums2:
            nums1.append(n2)
        nums1.sort()
        