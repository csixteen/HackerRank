module Main where


fibs :: [Int]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

fibonacci :: Int -> Int
fibonacci n = last . take (n+1) $ fibs

main = do
  input <- getLine
  print . fibonacci . (read :: String -> Int) $ input

