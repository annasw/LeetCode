class Solution {
public:
    bool isPowerOfFour(int num) {
        if (num==1) {return true;}
        else if (num<=0) {return false;}
        else {return ((num%4)==0 && isPowerOfFour(num/4));}
    }
};
