class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        i = 0
        int_sum = 0

        while i < len(s):
            if i + 1 < len(s):
                if symbol_map[s[i]] < symbol_map[s[i + 1]]:
                    int_sum -= 2 * symbol_map[s[i]]
            int_sum += symbol_map[s[i]]
            i += 1

        return int_sum