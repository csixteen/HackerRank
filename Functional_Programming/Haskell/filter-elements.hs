import Control.Monad
import Data.List
import Data.Maybe
import qualified Data.Map as M
import qualified Data.Set as S

freqs :: [Int] -> M.Map Int Int
freqs xs = f xs M.empty
  where
    f [] d = d
    f (x : xs) d | x `M.member` d = f xs (M.insert x ((fromJust (M.lookup x d))+1) d)
                 | otherwise = f xs (M.insert x 1 d)

valid :: Int -> Int -> M.Map Int Int -> S.Set Int -> Bool
valid x k d s = case M.lookup x d of
                  Nothing -> False
                  Just y  -> (y >= k) && not (x `S.member` s)

filterElements :: Int -> [Int] -> [Int]
filterElements k xs = f k xs (freqs xs) S.empty
  where
    f _ [] _ _ = []
    f i (x:xs) d s | (valid x i d s) = x : f i xs d (S.insert x s)
                   | otherwise = f i xs d s

main :: IO ()
main = do
  i <- readLn :: IO Int
  forM_ [1..i] $ \_ -> do
    l <- getLine
    let k = (map (read::String->Int) $ words l) !! 1
    e <- getLine
    let elems = map (read::String->Int) $ words e
        res = filterElements k elems
    putStrLn $ if length res == 0 then (show (-1)) else (intercalate " " (map show res))
    
