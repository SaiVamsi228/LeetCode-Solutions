class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1  # Count frequency of each task

        freq.sort()  # Sort to find the task with highest frequency
        max_freq = freq[25]  # Most frequent task

        chunk = max_freq - 1  # Number of full gaps between most frequent tasks
        idle = chunk * n  # Initial idle slots

        # Fill idle slots with remaining tasks (other than the most frequent one)
        for i in range(24, -1, -1):  # From second most to least
            idle -= min(chunk, freq[i])  # Can’t place more than one per chunk

        # If idle is still > 0, we need to wait, else tasks fill all slots
        return len(tasks) + max(0, idle)
