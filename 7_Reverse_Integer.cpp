class Solution {
public:
    int reverse(int x) {
        int revInt = 0;
        while (x) {
            if (revInt>INT_MAX/10 || revInt<INT_MIN/10)
                return 0;
            revInt = (revInt*10) + x%10;
            x = x/10;
        }
        return revInt;
    }
};

// beats 100% runtime and 61.24% memory
// O(n)
// https://leetcode.com/problems/reverse-integer/submissions/1242588990/
