from queue import PriorityQueue

class Solution:
    def frequencySort2(self, s: str) -> str:
        h = {}

        i = 0
        l = len(s)
        while i < l:
            h[s[i]] = h.get(s[i], 0) + 1
            i = i + 1

        queue = PriorityQueue()
        for ch, count in h.items():
            queue.put((-count, ch))

        s = ""
        while not queue.empty():
            item = queue.get()
            count = item[0] * -1
            s = s + ''.join([item[1] for x in range(count)])
        return s

    def frequencySort(self, s: str) -> str:
        h = {}

        i = 0
        l = len(s)
        while i < l:
            h[s[i]] = h.get(s[i], 0) + 1
            i = i + 1

        count = [None for x in range(l + 1)]
        for k, v in h.items():
            if count[v] is None:
                count[v] = []
            count[v].append(k)

        s = ""
        i = l
        arr = []
        while i >= 1:
            if count[i] is None:
                i = i - 1
                continue
            charList = count[i]
            for ch in charList:
                s = s + ''.join([ch for x in range(i)])
            i = i - 1
        return s

print(Solution().frequencySort2("tree"))
print(Solution().frequencySort2("cceia09u3r333"))

