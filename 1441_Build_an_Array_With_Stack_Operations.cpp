class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> ans;
        int i, push_ele = 1;
        for (i=0; i<target.size(); i++)
        {
            while (target[i] != push_ele)
            {
                push_ele ++;
                ans.push_back("Push");
                ans.push_back("Pop");
            }
            if (target[i] == push_ele)
            {
                ans.push_back("Push");
                push_ele ++;
            }    
        }
        return ans;
    }
};

// beats 100% runtime and 100% memory
// https://leetcode.com/problems/build-an-array-with-stack-operations/submissions/1090636557/
