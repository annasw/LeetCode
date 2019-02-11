class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        
        for(int i=0; i<prices.size(); i++) {
            for(int j=i+1; j<prices.size(); j++) {
                profit = max(profit, prices[j]-prices[i]);
            }
        }
        
        return profit;
    }
};
/* Okay this is kinda funny.
   So I programmed the slow version in python and,
   predictably, it timed out.
   So instead of thinking of a good solution like a real programmer
   I just converted the program into C++
   (using my poor memory of C++ and my slightly better memory of Java,
   which is basically C++ but without garbage collection)
   just to see if the same program would run in time in a faster language.
   And it did, and I think that's funny, so I didn't write a faster version.
   So enjoy the O(n^2) solution.
  
  
  class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        profit = 0
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = max(profit, prices[j]-prices[i])
        
        return profit
  */
