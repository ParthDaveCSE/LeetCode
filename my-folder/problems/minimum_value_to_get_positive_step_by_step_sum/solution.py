class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # Start with startValue = 1. 
        start_value = 1

        # While we haven't found the first valid startValue
        while True:
            # The step-by-step total "total" equals startValue at the beginning.
            # Use boolean parameter "isValid" to record whether the total 
            # is larger than or equal to 1.
            total = start_value
            is_valid = True

            # Iterate over the array "nums".
            for num in nums:
                # In each iteration, calculate "total" 
                # plus the element "num" in the array.
                total += num

                # If "total" is less than 1, we shall try a larger startValue,
                # we mark "isValid" as "false" and break the current iteration.
                if total < 1:
                    is_valid = False
                    break

            # If "isVaild" is true, meaning "total" is never less than 1 in the
            # iteration, therefore we return this "startValue". Otherwise, we 
            # go ahead and try "startValue" + 1 as the new "startValue". 
            if is_valid:
                return start_value
            else:
                start_value += 1
