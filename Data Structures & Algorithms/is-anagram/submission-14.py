class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Frequency Map
        if len(t)!= len(s):
            return False
        char_map: dict[str, int] = {};
        for ch in s:
            char_map[ch] = char_map.get(ch, 0) + 1;
        for ch in t:
            if ch not in char_map:
                return False
            char_map[ch] -= 1;
            if char_map[ch] == 0:
                del char_map[ch]
        return len(char_map) == 0
    
