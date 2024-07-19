class Solution:
    def compress(self, chars: List[str]) -> int:
        curChar = chars[0]
        ans = chars[0]
        counter = 1
        i = 1
        while i<len(chars):
            if curChar == chars[i]:
                counter += 1
            else:
                curChar = chars[i]
                if counter > 1:
                    ans += str(counter)
                ans += curChar
                counter = 1
            i += 1
        # adding the count of last occuring char
        if counter>1:
            ans += str(counter)
        # modifying the original list
        for i in range(len(ans)):
            chars[i] = ans[i]

        return len(ans)

  # beats 81.05% runtime and 13.77% memory
  # solved in O(n) time
  # https://leetcode.com/problems/string-compression/submissions/1259793132/
