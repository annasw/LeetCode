class Solution {
public:
    bool contains(vector<int>& nums, int val) {
        for (int i=0; i<nums.size(); i++) {
            if (nums[i]==val) {
                return true;
            }
        }
        return false;
    }
    
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> intersections;
        for (int i=0; i<nums1.size(); i++) {
            if (contains(nums2, nums1[i])) {
                if (!contains(intersections, nums1[i])) {
                    intersections.push_back(nums1[i]);
                }
            }
        }
        return intersections;
    }
};
