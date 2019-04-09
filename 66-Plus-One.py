class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # plus isn't a verb
        
        # okay so the point here is that if the last digit is a 9
        # you're supposed to like iterate through the list and increment everything
        # which gets annoying when it's like 999999999 or w/e and you have to also add an extra digit at the front
        # so i'm going to just do something clever and pythonic (or idk maybe not pythonic
        # but who am i that i gotta please the developers of a programming language's aesthetics)
        
        n = int("".join([str(i) for i in digits])) # this is how much i hate your stupid problem
        n += 1 # lmao
        return [int(i) for i in str(n)] # okay so maybe this is horribly ugly and unpythonic but um
        
        # fr i would do the actual problem if i didn't like changing python datatypes so much but <3
