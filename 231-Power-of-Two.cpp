class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n<1) {return false;}
        // Bitshift right until bin. rep. ends in a 1
        while ((n&1)==0) {
            n >>= 1;
        }
        // Return true if there was only one 1
        return (n>>1 == 0);
    }
};
