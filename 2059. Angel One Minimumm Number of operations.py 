class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        queue = deque([(start, 0)])  # (current_number, steps)
        visited = set([start])       # Set to track visited numbers

        while queue:
            current, steps = queue.popleft()

            # Try all operations with all numbers in nums
            for num in nums:
                for next_num in (current + num, current - num, current ^ num):
                    # If we reach the goal, return the number of steps
                    if next_num == goal:
                        return steps + 1

                    # Check bounds and avoid revisiting
                    if 0 <= next_num <= 1000 and next_num not in visited:
                        queue.append((next_num, steps + 1))
                        visited.add(next_num)

        # If we exhaust all possibilities and don't reach the goal
        return -1
