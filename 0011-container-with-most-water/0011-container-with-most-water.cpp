class Solution {
public:
    int maxArea(std::vector<int>& height) {
        int res = 0;
        int l = 0;
        int r = height.size() - 1;

        while (l < r) {
            int area = std::min(height[l], height[r]) * (r - l);
            res = std::max(res, area);

            if (height[r] >= height[l]) {
                l++;
            } else {
                r--;
            }
        }
        
        return res;
    }
};