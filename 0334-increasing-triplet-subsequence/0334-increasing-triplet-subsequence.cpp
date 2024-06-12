class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if(nums.size()<3)
        {
            return 0;
        }
        float first = INFINITY;
        float second = INFINITY;

        for(int i:nums)
        {
            if(i<=first)
            {
                first=i;
            }
            else if(i<=second)
            {
                second =i;
            }
            else
            {
                return 1;
            }


        }
    return 0;
        
        
    }
};