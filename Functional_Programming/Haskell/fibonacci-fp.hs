import Control.Monad
import Data.Array

fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

main :: IO ()
main = do
  let cache = array (0, 10000) [(i, j `mod` (10^8 + 7)) | (i, j) <- zip [0..] (take 10001 fibs)]
  t <- readLn :: IO Int
  forM_ [1..t] $ \_ -> do
    n <- readLn :: IO Int
    print $ cache ! n
    
