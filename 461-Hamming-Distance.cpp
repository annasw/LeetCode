class Solution {
public:
    int hammingDistance(int x, int y) {
        int diff = x^y; // xor to get differences
        int count = 0; // number of differences
        while (diff != 0) {
            if ((diff&1) == 1) {
                count += 1;
            }
            diff >>= 1;
        }
        return count;
    }
};
