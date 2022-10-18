"""
 *packageName    : 
 * fileName       : 3. Longest Substring Without Repeating Characters
 * author         : ipeac
 * date           : 2022-10-13
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-13        ipeac       최초 생성
 """

def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    left, right = 0, 0
    longest = 1
    while right < len(s):
        if s[right] in seen:
            left = seen[s[right]] + 1
        longest = max(longest, right - left + 1)
        seen[s[right]] = right
        right += 1
    return longest

# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
# print(lengthOfLongestSubstring("ca"))
# print(lengthOfLongestSubstring("dvdf"))
