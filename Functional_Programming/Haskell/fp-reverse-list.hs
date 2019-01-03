rev :: [a] -> [a]
rev xs = foldl (\acc x -> x : acc) [] xs
