// Timed this one, too: 17 minutes
class Solution {
public:
    // There's a trivial O(n**2) implementation
    // But we can do it in O(n) without too much difficulty
    int totalHammingDistance(vector<int>& nums) {
        int vectorSize = nums.size();
        if (vectorSize == 0) {return 0;}
        
        int totDistance = 0;
        
        // get the largest number in the set, so we know when to stop
        int largestInSet = nums[0];
        for (int i=0; i<vectorSize; i++) {
            if (nums[i]>largestInSet) {largestInSet = nums[i];}
        }
        
        // iterate through each elt in vector.
        // count the number of elts with 1s at each given place,
        // then add to total distance that num times the num of 0s at that place
        // continue this, bitshifting right, until the largest elt is 0 (i.e. all elts are 0)
        while (largestInSet != 0) {
            int onesCountAtPlace = 0;
            for (int i=0; i<vectorSize; i++) {
                if ((nums[i]&1)==1) {onesCountAtPlace++;}
                nums[i] >>= 1;
            }
            // increment total distance with the distance at that place
            totDistance += onesCountAtPlace*(vectorSize-onesCountAtPlace);
            largestInSet >>= 1;
        }
        return totDistance;
    }
};
