from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers for the search range
        left = 0
        right = len(nums) - 1

        # Continue searching while the range is valid
        while left <= right:
            # Calculate the middle index safely to avoid overflow
            mid = left + (right - left) // 2

            # Target found, return its index
            if nums[mid] == target:
                return mid

            # If middle value is less than target,
            # discard the left half including mid
            elif nums[mid] < target:
                left = mid + 1

            # If middle value is greater than target,
            # discard the right half including mid
            else:
                right = mid - 1

        # Target was not found in the array
        return -1


if __name__ == "__main__":
    # Test cases
    sol = Solution()

    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
        ([], 1, -1),
    ]

    for nums, target, expected in test_cases:
        result = sol.search(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] search({nums}, {target}) = {result} (expected {expected})")