//https://leetcode.com/problems/container-with-most-water

class Solution {
public:
    int maxArea(vector<int>& height) {
        int i, j;
        int n = height.size();
        i = 0;
        j = n-1;
        int maxWater = INT_MIN;
        while(i < j){
            maxWater = max(maxWater, (j-i)*min(height[i], height[j]));
            if(height[i] <= height[j]){
                i++;
            }
            else{
                j--;
            }
        }
        return maxWater;
    }
};