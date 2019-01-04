import Control.Monad

dist :: Double -> Double -> Double -> Double -> Double
dist x1 y1 x2 y2 = sqrt $ (x2-x1)**2 + (y2-y1)**2

perimeter :: [(Double,Double)] -> Double
perimeter ((x1,y1):(x2,y2):ps) = (dist x1 y1 x2 y2) + perimeter ((x2,y2):ps)
perimeter _ = 0

main :: IO ()
main = do
  n <- readLn :: IO Int
  points <- forM [1..n] (\_-> do fmap ((\[a,b]->(a,b)) . map (read :: String->Double) . words) getLine :: IO (Double,Double))
  putStrLn $ show $ perimeter (points ++ [(head points)])
