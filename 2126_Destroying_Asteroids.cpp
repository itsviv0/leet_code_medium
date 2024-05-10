class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        long long z = mass;
        sort(asteroids.begin(), asteroids.end());
        for(int i=0; i<asteroids.size(); i++)
        {
            if (z >= asteroids[i])
                z = z + asteroids[i];
            else 
                return false;  
        }
        return true;
    }
};

// beats 46.55% runtime and 41.60% memory
// https://leetcode.com/problems/destroying-asteroids/submissions/1223235587/
