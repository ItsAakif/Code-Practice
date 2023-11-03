class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        current = 1
        operations = []

        for num in target:
            while current != num:
                stack.append(current)
                operations.append("Push")
                operations.append("Pop")
                current += 1
            stack.append(current)
            operations.append("Push")
            current += 1

        return operations


solution = Solution()
result = solution.buildArray([1,3], 3)
print(result)  # Output: ["Push", "Push", "Pop", "Push"]
