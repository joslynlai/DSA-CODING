class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_set = set()

        for num in nums:
            if num not in number_set:
                number_set.add(num)
            else:
                return True

        return False


# note:
# set function: add
# return True/False in python
