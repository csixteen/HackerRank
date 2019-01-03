import Control.Monad

evalex :: Double -> Double
evalex n = 1 + sum [n**i / product [1..i] | i <- [1..9]]

main :: IO ()
main = do
  n <- readLn :: IO Int
  forM_ [1..n] $ \n_itr -> do
    x <- readLn :: IO Double
    putStrLn $ show $ evalex x

