sumOfPowers :: Int -> Int -> Int
sumOfPowers x n = length $ filter (\s -> sum (map (^n) s) == x) $ subs [i,(i-1)..1]
  where i = floor (fromIntegral x ** (1/(fromIntegral n)))

subs :: [a] -> [[a]]
subs [] = [[]]
subs (x:xs) = yss ++ map (x:) yss
  where yss = subs xs

main :: IO ()
main = do
  x <- readLn :: IO Int
  n <- readLn :: IO Int
  putStrLn $ show $ sumOfPowers x n

