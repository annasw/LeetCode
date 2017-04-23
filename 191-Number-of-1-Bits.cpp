class Solution {
public:
    int hammingWeight(uint32_t n) {
        int oneCount = 0;
        while (n!=0) {
            if (n&1==1) {
                oneCount++;
            }
            n >>= 1;
        }
        return oneCount;
    }
};
