import Control.Monad
import Data.List

rmdups :: Ord a => [a] -> [a]
rmdups = map head . group . sort

f_or_not :: [(Int,Int)] -> Bool
f_or_not pairs = let domain = map fst pairs
                 in length domain == length (rmdups domain)

main :: IO ()
main = do
  cases <- readLn :: IO Int
  forM_ [1..cases] $ \n_itr -> do
    pairs <- readLn :: IO Int
    func <- forM [1..pairs] (\_-> do fmap ((\[a,b]->(a,b)) . map (read :: String->Int) . words) getLine :: IO (Int,Int))
    putStrLn $ if (f_or_not func) then "YES" else "NO"
