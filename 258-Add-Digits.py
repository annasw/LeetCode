class Solution:
    def addDigits(self, num: 'int') -> 'int':

        '''
        okay so the only hard part here is the follow up: do it in o(1) w/out loop/recursion.
        um
        i'm certain there's a pattern here, but it's not immediately obvious what.
        let's look at a few examples and see if a pattern emerges.
        11 -> 2
        12 -> 3
        ...
        123 -> 6
        1234 -> 10
        
        2+2+2+2+2=1
        2+2+2+2+2+2=3
        2+2+2+2+2+2+2=5
        2+2+2+2+2+2+2+2=7
        
        3+3+3+3=3
        3+3+3+3+3=6
        1+2+3+4+5 = 6
        1+2+3+4+5+6 = 3
        
        okay i'm sure there's SOME pattern here but fuck if i can tell what it is.........
        i guess i could learn from the discussion panel but i doubt i'm gonna be able to figure it out here.
        meanwhile here's a bad solution that DOES loop and DOESN'T run in O(1) because
        '''
        
        while len(str(num)) > 1:
            num = sum([int(i) for i in str(num)])
        return num
    
        # okay so it turns out the trick is to mod by nine (iff the number is not divisible by nine, else 9)
        # clever digit tricks
        # whatever
