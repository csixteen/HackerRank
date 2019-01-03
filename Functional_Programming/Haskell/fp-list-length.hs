len :: [a] -> Int
len = foldl (\acc _ -> acc+1) 0

