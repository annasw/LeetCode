-- leetcode 561 array partition i in haskell
-- technically this can't be tested against leetcode's test cases, but it passed mine

partition :: (Integral a) => [a] -> a
partition [] = 0
partition [x] = x
partition (x:y:[]) = x
partition (x:y:xs) = x + partition xs

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort [x] = [x]
quicksort (x:xs) = (quicksort $ filter (<x) xs) ++ [x] ++ (filter (==x) xs) ++ (quicksort $ filter (>x) xs)

leet561 :: (Integral a) => [a] -> a
leet561 ls = partition $ quicksort ls
